import itertools
from hashlib import md5

jetsam = ['newaui', 'HwdwAZ', 'SLdkv']
floatsam = ['DFWEyEW','PXopvM', 'BGgsuhn']

# form bytes used in binary to transform input
b = '00A8A3FCD1A79DD2BA8F8F87A4E4CBF9'
a = '169E81F938E5AF9F909A96A3A9A42596'
control1 = ''.join(reversed([a[i:i+2] for i in range(0, len(a), 2)]))
control2 = ''.join(reversed([b[i:i+2] for i in range(0, len(b), 2)]))
control = bytearray.fromhex(control1+control2)

def transform_input(orig,permu_jet, permu_float):
	current_input = b''
	for i in range(31):
		temp = orig[i]
		temp ^= ord(permu_float[i%len(permu_float)])
		if i%0x11 > (len(permu_jet) - 1):
			if i == 0xf:
				temp -= 0xfe
			elif i == 0x10:
				temp -= 0x0 
			else:
				temp -= 0xab
		else:
			temp -= ord(permu_jet[i%0x11])
		current_input += (temp & 0xff).to_bytes(1,byteorder='little')
	current_input = bytearray(current_input)
	current_hash = md5(bytes(current_input)).hexdigest()
	if current_hash == '6c5215b12a10e936f8de1e42083ba184':
		print('[+] FOUND')
		print(f'jetsam input: {permu_jet}')
		print(f'flotsam input: {permu_float}')
		print(f'MD5: {current_hash}')
		exit()

# form permutations of inputs
iter_js = []
iter_fs = []
for i in range(1,4):
	iter_js.extend(list(itertools.product(jetsam,repeat=i)))
	iter_fs.extend(list(itertools.product(floatsam,repeat=i)))

# run each set of inputs against algo, to determine if match
for i_set in itertools.product(iter_js, iter_fs):
	transform_input(control,''.join(i_set[0]) + '\x00',''.join(i_set[1]))

