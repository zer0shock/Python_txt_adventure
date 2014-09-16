from random import randint

def create_enemy():
	enemy_hp = randint(10, 30)
	enemy_att = randint(5, 15)
	enemy_desc = randint(1, 3)
	
	if enemy_desc == 1:
		enemy_type = "ogre"
	elif enemy_desc == 2:
		enemy_type = "troll"
	elif enemy_desc == 3:
		enemy_type = "goblin"
	else:
		print "Something fucked up :/"
	print enemy_hp 
	print enemy_att
	print enemy_desc
	print enemy_type

	
create_enemy()

