from hashlib import sha256
from string import printable

target = 'b3c20caa9a1a82add9503e0eac43f741793d2031eb1c6e830274ed5ea36238bf'

charset = printable[:-6]

for i in charset:
	password = 'E4Q5' + i + '6f`s4l'
	for x in charset:
		password2 = password + x
		password2 += '5I'
		if sha256(password2.encode()).hexdigest() == target:
			print(password2)
			exit()
print('Not Found')
