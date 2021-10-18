from base64 import b64decode as b64d
from string import printable

charset = printable[:-5]
# change here
count = 2
with open(f'b64text{count}.txt','r') as f:
    PyKEvIqAmUkUVL0Anfn9FElFUN2dic3z = f.read()
    f.close()

#stage1
#GJrFu0fnwTxv2znmydOO5NG23UTO0MypKl = "b2JDN2luc2tiYXhLOFZaUWRRWTlSeXdJbk9lVWxLcHlrMXJsRnk5NjJaWkQ4SHdGVjhyOENQeFE5dGxUaEd1dGJ5ZDNOYTEzRmZRN1V1emxkZUJQNTN0Umt6WkxjbDdEaU1KVWF1M29LWURzOGxUWFR2YjJqQW1HUmNEU2RRcXdFSERzM0d3emhOaGVIYlE3dm9aeVJTMHdLY2Vhb3YyVGQ4UnQ2SXUwdm1ZbGlVYjA4YVRES2xESnlXU3NtZENMN0J4MnBYdlZET3RUSmlhY2V6Y3B6eUM2Mm4yOWs="
#stage2
GJrFu0fnwTxv2znmydOO5NG23UTO0MypKl = "N0l2N2l2RTVDYlNUdk5UNGkxR0lCbTExZmI4YnZ4Z0FpeEpia2NGN0xGYUh2N0dubWl2ZFpOWm15c0JMVDFWeHV3ZFpsd2JvdTVSTW1vZndYRGpYdnhrcGJFS0taRnZOMnNJU1haRXlMM2lIWEZtN0RSQThoMG8yYUhjNFZLTGtmOXBDOFR3OUpyT2RwUmFOOUdFck12bXd2dnBzOUVMWVpxRmpnc0ZHTFFtMGV4WW11Wmc1bWRpZWZ6U3FoZUNaOEJiMURCRDJTS1o3SFpNRzcwRndMZ0RCNFFEZWZsSWE4Vg=="

Ljasr99E9HLv1BBnSfEHYw = 64
npxuau2RsDO0L4hSVCBHx = b64d(PyKEvIqAmUkUVL0Anfn9FElFUN2dic3z)


PeFEvMaDMvyrYg8UZgKKfVMBhak5 = len(npxuau2RsDO0L4hSVCBHx)


bNT5lGtaxYHeyHFeEdImdD12Csa7MlR=[i for i in 'gflsdgfdjgflkdsfjg4980utjkfdskfglsldfgjJLmSDA49sdfgjlfdsjjqdgjfj']
candidates = [[] for i in range(64)]
counts = [0 for i in range(64)]

for x in charset:
    EuF8AepyhtkSXEWvNKIKZMaSHm4v = [i for i in b64d(GJrFu0fnwTxv2znmydOO5NG23UTO0MypKl)]
    bNT5lGtaxYHeyHFeEdImdD12Csa7MlR = [x for i in range(64)]

    # 221
    for i in range(len(EuF8AepyhtkSXEWvNKIKZMaSHm4v)):
        EuF8AepyhtkSXEWvNKIKZMaSHm4v[i] = ( EuF8AepyhtkSXEWvNKIKZMaSHm4v[i] + ord(bNT5lGtaxYHeyHFeEdImdD12Csa7MlR[i%64]) ) & 0xff

    Oz9nOiwWfRL6yjIwvM4OgaZMIt0B = [k for k in npxuau2RsDO0L4hSVCBHx]

    len_EuF8 = len(EuF8AepyhtkSXEWvNKIKZMaSHm4v)
    for i in range(PeFEvMaDMvyrYg8UZgKKfVMBhak5):
        Oz9nOiwWfRL6yjIwvM4OgaZMIt0B[i] = ( Oz9nOiwWfRL6yjIwvM4OgaZMIt0B[i] - EuF8AepyhtkSXEWvNKIKZMaSHm4v[i%len_EuF8] ) & 0xff
    
    # analysis
    chunks = []
    for r in range(0,len(Oz9nOiwWfRL6yjIwvM4OgaZMIt0B),len_EuF8):
        chunks.append(Oz9nOiwWfRL6yjIwvM4OgaZMIt0B[r:r+len_EuF8])
    for g in range(64):
        tmp_array = []
        indexes = [y for y in range(g,len_EuF8,64)]
        for chunk in chunks:
            for index in indexes:
                try:
                    tmp_array.append(chunk[index])
                except IndexError:
                    continue
        checker = list(filter(lambda z: chr(z) in printable[:-2], tmp_array))
        if len(tmp_array) == len(checker):
            candidates[g].append(x)


print(counts)
print('Candidates:')
for i,a in enumerate(candidates):
    print(f'{i} -> {a}')
exit()