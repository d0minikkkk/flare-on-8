import binascii

with open('unfound','r') as f:
	data = f.read()
data = [i.lower() for i in data.split()]

with open('colors2','r') as f:
	colors = f.read()

colors = [i.title() for i in colors.split('\n')]
for i in colors:
	temp = i + '\n'
	try:
		crc = hex(binascii.crc32(temp.encode('ascii')))[2:]
		if crc in data:
			print(f'[!] FOUND {crc}->{temp}')
	except UnicodeEncodeError:
		continue
