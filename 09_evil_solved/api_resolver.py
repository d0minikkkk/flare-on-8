import pefile

def create_hash(api_name):
    v18 = 64
    for i in api_name:
        v18 = (i - 0x45523f21 * v18) & 0xffffffff
    return hex(v18) 

DLL_MAPPING = {
    'kernel32':0x246132,
    'ntdll':0x176684,
    'ws2_32':0x52325,
    'user32':0x234324,
    'ole32':0x4258672,
    'gdi':0x43493856,
    'advapi':0x523422,
    'oleaut32':0x7468951
}

with open('lookup.txt','w') as f2:
    for dll in DLL_MAPPING.keys():
        path = 'C:\\Windows\\System32\\' + dll + '.dll'
        pe = pefile.PE(path,fast_load=True)
        pe.parse_data_directories()
        for entry in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            if entry.name is None:
                continue
            hash = create_hash(entry.name)
            f2.write(f'{entry.name.decode()} -> {hash}\n')
    
    f2.close()

print('Finished creating lookup file')
assert create_hash(b'A_SHAFinal') == '0xeead2108'