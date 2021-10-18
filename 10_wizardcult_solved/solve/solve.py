import re

with open('..\\extracted\\pcap_artifacts\\Wyvern.txt','r') as f0:
    data = f0.read()

encrypted = data.split('\n')

spell_lookup = []

for i in range(1,9):
    with open(f'lookups\\water_spell_lookup{i}.txt','r') as f1:
        data = f1.read()
        f1.close()
    spell_array = data.split('\n')
    assert len(spell_array) == 256
    spell_lookup.append(spell_array)

damage_lookup1 = []
for i in range(1,9):
    with open(f'lookups\\water_dam_{i}-1.txt','r') as f2:
        data = f2.read()
        f2.close()
    damage_array = data.split('\n')
    assert len(damage_array) == 256
    damage_lookup1.append(damage_array)

damage_lookup2 = []
for i in range(1,9):
    with open(f'lookups\\water_dam_{i}-2.txt','r') as f3:
        data = f3.read()
        f3.close()
    damage_array = data.split('\n')
    assert len(damage_array) == 256
    damage_lookup2.append(damage_array)
message = b''

for index,line in enumerate(encrypted):
    
    match = re.search(r'.*cast (.+) on the Wyvern(?: for (.*) damage)?',line)
    spell = match.group(1)
    damage = match.group(2)
    
    chosen_spell = spell_lookup[index%8]
    byte1 = chosen_spell.index(spell)
    chosen_damage1 = damage_lookup1[index%8]
    byte2 = chosen_damage1.index(damage.split('d')[0])

    chosen_damage2 = damage_lookup2[index%8]
    byte3 = chosen_damage2.index(damage.split('d')[1])

    message += byte1.to_bytes(1,byteorder='big')
    message += byte2.to_bytes(1,byteorder='big')
    message += byte3.to_bytes(1,byteorder='big')

with open('cool_wizard_meme.png','wb') as f3:
    f3.write(message)