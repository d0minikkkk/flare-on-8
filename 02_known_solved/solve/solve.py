ror = lambda val, r_bits, max_bits:((val & (2**max_bits-1)) >> r_bits%max_bits) | (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def get_key():
    with open('challenge\\Files\\capa.png.encrypted','rb') as f:
        data = f.read()
    header = [0x89,0x50,0x4E,0x47,0x0D,0x0A,0x1A,0x0A]
    key = ""
    for i in range(8):
        enc = ror(header[i]+i,i,8)
        key += chr(enc ^ data[i])
    return key
        
print(get_key())