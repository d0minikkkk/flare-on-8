from base64 import b64decode as b64d
from string import printable
charset = printable[:-5]

count = 1

with open(f'b64text{count}.txt','r') as f:
    PyKEvIqAmUkUVL0Anfn9FElFUN2dic3z = f.read()
    f.close()

#stage1
GJrFu0fnwTxv2znmydOO5NG23UTO0MypKl = "b2JDN2luc2tiYXhLOFZaUWRRWTlSeXdJbk9lVWxLcHlrMXJsRnk5NjJaWkQ4SHdGVjhyOENQeFE5dGxUaEd1dGJ5ZDNOYTEzRmZRN1V1emxkZUJQNTN0Umt6WkxjbDdEaU1KVWF1M29LWURzOGxUWFR2YjJqQW1HUmNEU2RRcXdFSERzM0d3emhOaGVIYlE3dm9aeVJTMHdLY2Vhb3YyVGQ4UnQ2SXUwdm1ZbGlVYjA4YVRES2xESnlXU3NtZENMN0J4MnBYdlZET3RUSmlhY2V6Y3B6eUM2Mm4yOWs="
#stage2
# GJrFu0fnwTxv2znmydOO5NG23UTO0MypKl = "N0l2N2l2RTVDYlNUdk5UNGkxR0lCbTExZmI4YnZ4Z0FpeEpia2NGN0xGYUh2N0dubWl2ZFpOWm15c0JMVDFWeHV3ZFpsd2JvdTVSTW1vZndYRGpYdnhrcGJFS0taRnZOMnNJU1haRXlMM2lIWEZtN0RSQThoMG8yYUhjNFZLTGtmOXBDOFR3OUpyT2RwUmFOOUdFck12bXd2dnBzOUVMWVpxRmpnc0ZHTFFtMGV4WW11Wmc1bWRpZWZ6U3FoZUNaOEJiMURCRDJTS1o3SFpNRzcwRndMZ0RCNFFEZWZsSWE4Vg=="

Ljasr99E9HLv1BBnSfEHYw = 64
npxuau2RsDO0L4hSVCBHx = b64d(PyKEvIqAmUkUVL0Anfn9FElFUN2dic3z)

PeFEvMaDMvyrYg8UZgKKfVMBhak5 = len(npxuau2RsDO0L4hSVCBHx)

# likely an array of int/bytes
EuF8AepyhtkSXEWvNKIKZMaSHm4v = [i for i in b64d(GJrFu0fnwTxv2znmydOO5NG23UTO0MypKl)]

#stage1 key
bNT5lGtaxYHeyHFeEdImdD12Csa7MlR = 'ChVCVYzI1dU9cVg1ukBqO2u4UGr9aVCNWHpMUuYDLmDO22cdhXq3oqp8jmKBHUWI'
#stage2 key
# bNT5lGtaxYHeyHFeEdImdD12Csa7MlR = 'UQ8yjqwAkoVGm7VDdhLoDk0Q75eKKhTfXXke36UFdtKAi0etRZ3DoHPz7NxJPgHl'
assert len(bNT5lGtaxYHeyHFeEdImdD12Csa7MlR) == 64
sEjdWWMFU4wObKZap4WeMBgdfgIfTHCvS = ""

EuF8AepyhtkSXEWvNKIKZMaSHm4v = [i for i in b64d(GJrFu0fnwTxv2znmydOO5NG23UTO0MypKl)]
for i in range(len(EuF8AepyhtkSXEWvNKIKZMaSHm4v)):
    EuF8AepyhtkSXEWvNKIKZMaSHm4v[i] = ( EuF8AepyhtkSXEWvNKIKZMaSHm4v[i] + ord(bNT5lGtaxYHeyHFeEdImdD12Csa7MlR[i%64]) ) & 0xff

Oz9nOiwWfRL6yjIwvM4OgaZMIt0B = [k for k in npxuau2RsDO0L4hSVCBHx]

len_EuF8 = len(EuF8AepyhtkSXEWvNKIKZMaSHm4v)
for i in range(PeFEvMaDMvyrYg8UZgKKfVMBhak5):
    Oz9nOiwWfRL6yjIwvM4OgaZMIt0B[i] = ( Oz9nOiwWfRL6yjIwvM4OgaZMIt0B[i] - EuF8AepyhtkSXEWvNKIKZMaSHm4v[i%len_EuF8] ) & 0xff

for i in range(len(npxuau2RsDO0L4hSVCBHx)):
    sEjdWWMFU4wObKZap4WeMBgdfgIfTHCvS += chr( Oz9nOiwWfRL6yjIwvM4OgaZMIt0B[i] )
print(sEjdWWMFU4wObKZap4WeMBgdfgIfTHCvS[:100].encode())
with open('decrypted.txt','w') as f2:
    f2.write(sEjdWWMFU4wObKZap4WeMBgdfgIfTHCvS)