import glob

def genv4v8(index):
    new_num = list(num_arr)
    v8 = 0    
    v9 = 0
    v11 = 0
    v4 = None
    for i in range(index+1):
        v9 = (v9 + 1) % 256
        v11 = (v11 + new_num[v9]) % 256
        v5 = new_num[v9]
        new_num[v9] = new_num[v11]
        new_num[v11] = v5
        v4 = new_num[(new_num[v11] + new_num[v9]) % 256]
        v8 = v4
        
    return v4, v8

key_arr = "A secret is no longer a secret once someone knows it"

num_arr = [i for i in range(256)]

v11 = 0
for i in range(256):
    v11 = (num_arr[i] + v11 + ord(key_arr[i% 52])) % 256
    v6 = num_arr[i]
    num_arr[i] = num_arr[v11]
    num_arr[v11] = v6

print(num_arr)


path = "C:\\Users\\alloysius.goh.yc\\Desktop\\documents\\Documents"

for filepath in glob.glob("**/*.broken", recursive=True):
    new_num = list(num_arr)
    v8 = 0    
    v9 = 0
    v11 = 0
    v4 = None
    pt_full = b""
    with open(filepath, "rb") as f:
        data = f.read()
        f.close()
    for i in range(len(data)):
        v9 = (v9 + 1) % 256
        v11 = (v11 + new_num[v9]) % 256
        v5 = new_num[v9]
        new_num[v9] = new_num[v11]
        new_num[v11] = v5
        v4 = new_num[(new_num[v11] + new_num[v9]) % 256]
        pt = data[i] ^ v4 ^ v8
        v8 = v4
        pt_full += (pt).to_bytes(1,byteorder='little')
    with open(filepath + '.new','wb') as f2:
        f2.write(pt_full)
        f2.close()

with open(path + '\\.daiquiris.txt.broken','rb') as f:
    data = f.read()

new_num = list(num_arr)
v8 = 0    
v9 = 0
v11 = 0
v4 = None
pt_full = b""
for i in range(1024):
    v9 = (v9 + 1) % 256
    v11 = (v11 + new_num[v9]) % 256
    v5 = new_num[v9]
    new_num[v9] = new_num[v11]
    new_num[v11] = v5
    v4 = new_num[(new_num[v11] + new_num[v9]) % 256]
    pt = data[i] ^ v4 ^ v8
    v8 = v4
    pt_full += (pt).to_bytes(1,byteorder='little')
with open(path + '\\daiquiris.txt.new','wb') as f2:
    input(pt_full)
    f2.write(pt_full)
    f2.close()
# password[0] = E, [1] = 0x34, [3] = 0x35, [2]=0x51, [6] = 0x66 [7] = 0x60. [12] = 0x35
