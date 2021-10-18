import zlib
from Crypto.Cipher import ARC4

enc1 = 'c9fa83ebe8'
enc2 = '033553264e393a'
enc3 = '08403b38'
enc4 = '63503734'
def decrypt_part(hexstr):
    arr1 = bytearray.fromhex(hexstr)
    for i in range(len(arr1)-1,0,-1):
        byte1 = arr1[i-1]
        lside = byte1 | (~arr1[i] & 0xff)
        rside = arr1[i] | (~byte1 & 0xff)
        tmp = ~(lside & rside)
        final = (tmp - 3) & 0xff
        arr1[i] = final
    return arr1

arr1 = decrypt_part(enc1)

b1l = ~((arr1[0] | 0x79) & (~arr1[0] | 0x86))
b1r = ~((arr1[0]| 0xfb) & (~arr1[0] | 0x4)) | 0xf3
f1 = (b1l & b1r) -3
arr1[0] = f1 & 0xff
print(f'string 1: {arr1.decode()}')

arr2 = decrypt_part(enc2)
b1l = ~((arr2[0] | 0x8a) & (~arr2[0] | 0x75))
b1r = ~((arr2[0]| 0xfb) & (~arr2[0] | 0x4)) | 0xf3
f1 = (b1l & b1r) -3
arr2[0] = f1 & 0xff
print(f'string 2: {arr2.decode()}')

arr3 = decrypt_part(enc3)
b1l = (arr3[0] | 0xf3)
b1r = ~((arr3[0]| 0xcf) & (~arr3[0] | 0x30)) 
f1 = (b1l & b1r) -3
arr3[0] = f1 & 0xff
print(f'string 3: {arr3.decode()}')

arr4 = decrypt_part(enc4)
b1l = ~((arr4[0] | 0xf6) & (~arr4[0] | 0x09))
b1r = ~((arr4[0]| 0x04) & (~arr4[0] | 0xfb)) | 0xf3
f1 = (b1l & b1r) -3
arr4[0] = f1 & 0xff
print(f'string 4: {arr4.decode()}\n')

byte_arr = [arr1,arr2,arr3,arr4]
key = ''

for x in byte_arr:
    crc = hex(zlib.crc32(x))[2:].zfill(8)
    print(f'CRC32 of {x.decode()}: {crc}')
    key += crc

flag_enc = bytearray.fromhex('3238A70270DFE72BF77A77F576291BA287E4C2F953CC3F6EE89AA6820CBDA4D196E87A8900C5F5')

print('\nciphertext: 3238A70270DFE72BF77A77F576291BA287E4C2F953CC3F6EE89AA6820CBDA4D196E87A8900C5F5')
print(f'key: {key}')

key = bytearray.fromhex(key)
rc4 = ARC4.new(key)

print(f'plaintext: {rc4.decrypt(flag_enc).decode()}')