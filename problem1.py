import time
import random
print()
print('-' * 60)
print('A Super Randopuff appears!')
time.sleep(0.4)
print('You only have one Pokémon.')
time.sleep(0.4)
print()
print('I chose you, Roarlax!')
time.sleep(0.4)
print()
time.sleep(0.4)

#Starting HPs
roarlax_hp = 200
rando_hp = 125

print('Orignial HP')
print('- Roarlax HP: ' + str(roarlax_hp))
time.sleep(0.3)
print('-Randopuff HP: ' + str(rando_hp))
time.sleep(0.3)
print()
time.sleep(0.3)

while roarlax_hp > 0 and rando_hp > 0:
	print('Battle options:')
	time.sleep(0.3)
	print('- [1] Sleep')
	time.sleep(0.3)
	print('- [2] slick kick')
	time.sleep(0.3)
	print('- [3] waterblast')
	time.sleep(0.3)
	print('- [4] turbo bomb')
	time.sleep(0.3)
	print('- [5] Capture')
	time.sleep(0.3)
	your_move = input('Chose a move using the corresponding number: ')
	print()

	if your_move == '1':
		roarlax_hp = roarlax_hp + 50
		print('roarlax uses Sleep, his HP increases to ' + str(roarlax_hp))
		time.sleep(0.3)
	elif your_move == '2':
		rando_hp = rando_hp - 10
		print('roarlax uses slick kick and deals 10 damage to Randopuff')
		time.sleeRando
	elif your_move == '3':
		rando_hp = rando_hp - 30
		print('Roarlax uses waterblast and deals 30 damage to Randopuff')
		time.sleep(0.3)
	elif your_move == '4':
		rando_hp = rando_hp - 40
		print ('Roarlax uses turbo bomb and deals 40 damage to Randopuff')
		time.sleep(0.3)
	elif your_move == '5':
		capture_roll = random.randint(0,125)
		if capture_roll > rando_hp:
			print('You have caught Randopuff')
			break
		else:
			print('You tried to capture Randopuff, but it escaped')
	print()

	#Randopuff attacks
	enemy_move = random.randint(1,2)
	enemy_move = str(enemy_move)

	if enemy_move == '1':
		roarlax_hp = roarlax_hp - 30
		rando_hp = rando_hp + 30
		print('Randpuff uses trunk smash and deals 30 damage while recovering 30 HP')
		time.sleep(0.3)
	elif enemy_move == '2':
		roarlax_hp = roarlax_hp - 50
		print('Randopuff uses knight slash and deals 50 damage')
		time.sleep(0.3)
print()
 
 # check for overkill
if roarlax_hp < 0:
	roarlax_hp = 0 
if rando_hp < 0:
	rando_hp = 0
	print('Updated HP')
	print('- Roarlax HP: ' + str(roarlax_hp))
	time.sleep(0.3)
	print('-Randopuff HP: ' + str(rando_hp))
	time.sleep(0.3)
	print()
	time.sleep(0.3)
if roarlax_hp == 0:
	print('Roarlax has lost the battle the winner is Randopuff')
elif rando_hp == 0:
	print('Randopuff has lost the battle the winner is Roarlax')