import itertools
from hashlib import md5
import binascii

jetsam = ['newaui\x00', 'HwdwAZ\x00', 'SLdkv\x00']

floatsam = ['DFWEyEW','PXopvM', 'BGgsuhn']
b = '00A8A3FCD1A79DD2BA8F8F87A4E4CBF9'
a = '169E81F938E5AF9F909A96A3A9A42596'
control1 = ''.join(reversed([a[i:i+2] for i in range(0, len(a), 2)]))
control2 = ''.join(reversed([b[i:i+2] for i in range(0, len(b), 2)]))
control = bytearray.fromhex(control1+control2)

def transform_input(orig,permu_jet, permu_float):
	new_str = b''
	for i in range(31):
		temp = orig[i]
		#input(f'[+] {i}')
		temp ^= ord(permu_float[i%len(permu_float)])
		#input(f'[-]{hex(ord(permu_float[i%len(permu_float)]))}')
		#input(hex(temp & 0xff))
		if i%0x11 > (len(permu_jet) - 1):
			if i == 0xf:
				temp -= 0xfe
			elif i == 0x10:
				temp -= 0x0 
			else:
				temp -= 0xab
		else:
			temp -= ord(permu_jet[i%0x11])
		new_str += (temp & 0xff).to_bytes(1,byteorder='little')
		#input(hex(temp & 0xff))
	#new_str += (orig[-1]).to_bytes(1,byteorder='little')
	#new_str += (0x0 & 0xff).to_bytes(1,byteorder='little')
	new_str = bytearray(new_str)
	#new_str.reverse()
	#new_str = new_str[int(len(new_str)/2):] + new_str[:int(len(new_str)/2)]
	#input(binascii.hexlify(new_str[int(len(new_str)/2):]))
	#print(f'{permu_jet}:{permu_float}')
	#print(binascii.hexlify(new_str))
	print(md5(bytes(new_str)).hexdigest())
# build arrays
iter_js = []
iter_fs = []
for i in range(1,4):
	iter_js.extend(list(itertools.combinations_with_replacement(jetsam,i)))
	iter_fs.extend(list(itertools.combinations_with_replacement(floatsam,i)))
input(list(itertools.product(iter_js,iter_fs)))
for i_set in itertools.product(iter_js, iter_fs):
	transform_input(control,''.join(i_set[0]),''.join(i_set[1]))

