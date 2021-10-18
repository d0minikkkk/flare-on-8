# credits to https://wumb0.in/extracting-and-diffing-ms-patches-in-2020.html
from ctypes import (windll, wintypes, c_uint64, cast, POINTER, Union, c_ubyte,
                    LittleEndianStructure, byref, c_size_t)
import zlib
from glob import glob
import sys

# types and flags
DELTA_FLAG_TYPE             = c_uint64
DELTA_FLAG_NONE             = 0x00000000
DELTA_APPLY_FLAG_ALLOW_PA19 = 0x00000001


# structures
class DELTA_INPUT(LittleEndianStructure):
    class U1(Union):
        _fields_ = [('lpcStart', wintypes.LPVOID),
                    ('lpStart', wintypes.LPVOID)]
    _anonymous_ = ('u1',)
    _fields_ = [('u1', U1),
                ('uSize', c_size_t),
                ('Editable', wintypes.BOOL)]


class DELTA_OUTPUT(LittleEndianStructure):
    _fields_ = [('lpStart', wintypes.LPVOID),
                ('uSize', c_size_t)]


# functions
ApplyDeltaB = windll.msdelta.ApplyDeltaB
ApplyDeltaB.argtypes = [DELTA_FLAG_TYPE, DELTA_INPUT, DELTA_INPUT,
                        POINTER(DELTA_OUTPUT)]
ApplyDeltaB.rettype = wintypes.BOOL
DeltaFree = windll.msdelta.DeltaFree
DeltaFree.argtypes = [wintypes.LPVOID]
DeltaFree.rettype = wintypes.BOOL
gle = windll.kernel32.GetLastError


def apply_patchfile_to_buffer(buf, buflen, patchpath, legacy):
    with open(patchpath, 'rb') as patch:
        patch_contents = patch.read()

    # some patches (Windows Update MSU) come with a CRC32 prepended to the file
    # if the file doesn't start with the signature (PA) then check it
    if patch_contents[:2] != b"PA":
        paoff = patch_contents.find(b"PA")
        if paoff != 4:
            raise Exception("Patch is invalid")
        crc = int.from_bytes(patch_contents[:4], 'little')
        patch_contents = patch_contents[4:]
        if zlib.crc32(patch_contents) != crc:
            raise Exception("CRC32 check failed. Patch corrupted or invalid")

    applyflags = DELTA_APPLY_FLAG_ALLOW_PA19 if legacy else DELTA_FLAG_NONE

    dd = DELTA_INPUT()
    ds = DELTA_INPUT()
    dout = DELTA_OUTPUT()

    ds.lpcStart = buf
    ds.uSize = buflen
    ds.Editable = False

    dd.lpcStart = cast(patch_contents, wintypes.LPVOID)
    dd.uSize = len(patch_contents)
    dd.Editable = False

    status = ApplyDeltaB(applyflags, ds, dd, byref(dout))
    if status == 0:
        raise Exception("Patch {} failed with error {}".format(patchpath, gle()))

    return (dout.lpStart, dout.uSize)

def xorbytes(var, key, byteorder=sys.byteorder):
        key, var = key[:len(var)], var[:len(key)]
        int_var = int.from_bytes(var, byteorder)
        int_key = int.from_bytes(key, byteorder)
        int_enc = int_var ^ int_key
        return int_enc.to_bytes(len(var), byteorder)


with open('output.dll','rb') as f:
    inbuf = f.read()

buf = cast(inbuf, wintypes.LPVOID)
n = len(inbuf)
to_free = []
with open('hex_data.txt','r') as f2:
    hex_data = f2.read()
patches = hex_data.split()
for i,p in enumerate(patches):
    tempbuf = bytearray.fromhex(p)
    with open(f'{i}.patch', 'wb') as f3:
        f3.write(tempbuf)
        f3.close()

outbuf_xor = b''
try:
    to_patch = sorted(glob('*.patch'),key=lambda x:int(x.split('.')[0]))
    for index,patch in enumerate(to_patch):
        print(patch)
        buf, n = apply_patchfile_to_buffer(buf, n, patch, False)
        to_free.append(buf)
    
        outbuf = bytes((c_ubyte*n).from_address(buf))
        key = b'meoow' * (len(outbuf)//5 + 1)
        temp = xorbytes(outbuf,key)
        outbuf_xor += temp
    with open('transcript.txt','wb') as final:
        final.write(outbuf_xor)
finally:
    for buf in to_free:
        DeltaFree(buf)
