from base64 import b64encode as b64e
from base64 import b64decode as b64d

flag = ''
password = b64e(b'goldenticket')
key = b64d('P1xNFigYIh0BGAofD1o5RSlXeRU2JiQQSSgCRAJdOw==')

for i in range(len(key)):
    flag += chr(key[i] ^ password[i%len(password)])

print(flag)