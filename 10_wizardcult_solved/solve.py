import re

# t = '''PRIVMSG #dungeon :I cast Moonbeam on the Goblin for 205d205 damage!
# PRIVMSG #dungeon :I cast Reverse Gravity on the Goblin for 253d213 damage!
# PRIVMSG #dungeon :I cast Water Walk on the Goblin for 216d195 damage!
# PRIVMSG #dungeon :I cast Mass Suggestion on the Goblin for 198d253 damage!
# PRIVMSG #dungeon :I cast Planar Ally on the Goblin for 199d207 damage!
# PRIVMSG #dungeon :I cast Water Breathing on the Goblin for 140d210 damage!
# PRIVMSG #dungeon :I cast Conjure Barrage on the Goblin for 197d168 damage!
# PRIVMSG #dungeon :I cast Water Walk on the Goblin for 204d198 damage!
# PRIVMSG #dungeon :I cast Call Lightning on the Goblin for 193d214 damage!
# PRIVMSG #dungeon :I cast Branding Smite on the Goblin!'''

with open('Wyvern.txt','r') as f0:
    data = f0.read()

encrypted = data.split('\n')

spell_lookup = []

for i in range(1,9):
    with open(f'water_spell_lookup{i}.txt','r') as f1:
        data = f1.read()
        f1.close()
    spell_array = data.split('\n')
    assert len(spell_array) == 256
    spell_lookup.append(spell_array)

damage_lookup1 = []
for i in range(1,9):
    with open(f'water_dam_{i}-1.txt','r') as f2:
        data = f2.read()
        f2.close()
    damage_array = data.split('\n')
    assert len(damage_array) == 256
    damage_lookup1.append(damage_array)

damage_lookup2 = []
for i in range(1,9):
    with open(f'water_dam_{i}-2.txt','r') as f3:
        data = f3.read()
        f3.close()
    damage_array = data.split('\n')
    assert len(damage_array) == 256
    damage_lookup2.append(damage_array)
message = b''

# for line in t.split('\n'):
for index,line in enumerate(encrypted):
    
    # match = re.search(r'.*cast (.+) on the Goblin(?: for (.*) damage)?',line)
    match = re.search(r'.*cast (.+) on the Wyvern(?: for (.*) damage)?',line)
    spell = match.group(1)
    damage = match.group(2)
    # print(damage.split('d'))
    chosen_spell = spell_lookup[index%8]
    byte1 = chosen_spell.index(spell)
    # if damage is None:
    #     byte_2_and_3 = 0
    # else:
    #     byte_2_and_3 = damage_array.index(damage)
    chosen_damage1 = damage_lookup1[index%8]
    byte2 = chosen_damage1.index(damage.split('d')[0])

    chosen_damage2 = damage_lookup2[index%8]
    byte3 = chosen_damage2.index(damage.split('d')[1])

    message += byte1.to_bytes(1,byteorder='big')
    message += byte2.to_bytes(1,byteorder='big')
    message += byte3.to_bytes(1,byteorder='big')
# print(message[:6])
with open('cool_wizard_meme.png','wb') as f3:
    f3.write(message)