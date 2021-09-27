from base64 import b64decode as b64d
with open('decoded.bin','rb') as f:
    PyKEvIqAmUkUVL0Anfn9FElFUN2dic3z = f.read()
    f.close()

GJrFu0fnwTxv2znmydOO5NG23UTO0MypKl = "b2JDN2luc2tiYXhLOFZaUWRRWTlSeXdJbk9lVWxLcHlrMXJsRnk5NjJaWkQ4SHdGVjhyOENQeFE5dGxUaEd1dGJ5ZDNOYTEzRmZRN1V1emxkZUJQNTN0Umt6WkxjbDdEaU1KVWF1M29LWURzOGxUWFR2YjJqQW1HUmNEU2RRcXdFSERzM0d3emhOaGVIYlE3dm9aeVJTMHdLY2Vhb3YyVGQ4UnQ2SXUwdm1ZbGlVYjA4YVRES2xESnlXU3NtZENMN0J4MnBYdlZET3RUSmlhY2V6Y3B6eUM2Mm4yOWs="

Ljasr99E9HLv1BBnSfEHYw = 64
npxuau2RsDO0L4hSVCBHx = bytearray(PyKEvIqAmUkUVL0Anfn9FElFUN2dic3z)

PeFEvMaDMvyrYg8UZgKKfVMBhak5 = len(npxuau2RsDO0L4hSVCBHx)

# likely an array of int/bytes
EuF8AepyhtkSXEWvNKIKZMaSHm4v = [i for i in b64d(GJrFu0fnwTxv2znmydOO5NG23UTO0MypKl)]

bNT5lGtaxYHeyHFeEdImdD12Csa7MlR=[i for i in 'gflsdgfdjgflkdsfjg4980utjkfdskfglsldfgjJLmSDA49sdfgjlfdsjjqdgjfj']

for i in range(len(EuF8AepyhtkSXEWvNKIKZMaSHm4v)):
    EuF8AepyhtkSXEWvNKIKZMaSHm4v[i] = ( EuF8AepyhtkSXEWvNKIKZMaSHm4v[i] + ord(bNT5lGtaxYHeyHFeEdImdD12Csa7MlR[i%64]) ) & 0xff

Oz9nOiwWfRL6yjIwvM4OgaZMIt0B = npxuau2RsDO0L4hSVCBHx

len_EuF8 = len(EuF8AepyhtkSXEWvNKIKZMaSHm4v)
for i in range(PeFEvMaDMvyrYg8UZgKKfVMBhak5):
    Oz9nOiwWfRL6yjIwvM4OgaZMIt0B[i] = ( Oz9nOiwWfRL6yjIwvM4OgaZMIt0B[i] - EuF8AepyhtkSXEWvNKIKZMaSHm4v[i%len_EuF8] ) & 0xff

sEjdWWMFU4wObKZap4WeMBgdfgIfTHCvS = ""

for i in range(len(npxuau2RsDO0L4hSVCBHx)):
    sEjdWWMFU4wObKZap4WeMBgdfgIfTHCvS += chr( Oz9nOiwWfRL6yjIwvM4OgaZMIt0B[i] )

print(sEjdWWMFU4wObKZap4WeMBgdfgIfTHCvS[:20])