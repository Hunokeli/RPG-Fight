import random

ice_cost = 2
fire_cost = 5
heal_cost = 5
lightning_cost = 7

class Wizard:
	def __init__(self,name):
		self.name = name
		self.maxhealth = 20
		self.health = self.maxhealth
		self.maxmana = 50
		self.mana = self.maxmana
		self.fist = 2

	def attack(self):
		attack = self.fist
		print(f"Hit!\n{attack} Damage!")
		return attack

	def heal(self):
		heal_amount = random.randint(10,20)
		self.health += heal_amount
		self.mana -= 5
		print(f'Healed for {heal_amount}')
		if self.health > self.maxhealth:
			self.health = self.maxhealth

	def fire(self):
		dmg = random.randint(8,13)
		hit = random.randint(1,10)
		if hit != 1:
			self.mana -= 5
			print(f'Hit!\n{dmg} Damage!')
			return dmg

		else:
			self.mana -= 5
			print('Miss!')
			return 0

	def ice(self):
		dmg = random.randint(3,6)
		self.mana -= 2
		print(f'Hit!\n{dmg} Damage!')
		return dmg
	
	def lightning(self):
		dmg = random.randint(15,20)
		hit = random.randint(1,3)
		if hit != 1:
			self.mana -= 7
			print(f'Hit!\n{dmg} Damage!')
			return dmg
		else:
			self.mana -= 7
			print('Miss!')
			return 0


	def __str__(self):
		return f'Name: {self.name}\nHealth: {self.health}\nMana: {self.mana}'


class Goblin:
	def __init__(self, name):
		self.name = name
		self.maxhealth = 15
		self.health = self.maxhealth

	def attack(self):
		print('\nThe Goblin Attacks!')
		attack = random.randint(1,5)
		hit = random.randint(1,15)
		if hit != 1:
			print(f'Hit!!\n{attack} Damage!\n')
			return attack
		else:
			print('It Missed!\n')
			return 0

	def __str__(self):
		return f'Name: {self.name}\nHealth: {self.health}'

def player_turn():
	print('Player Turn')
	choice = ''
	target = ''
	while choice not in [1,2,3,4,5]:
		try:
			choice = int(input('What will you do? \n1: Ice MP-2\n2: Fire MP-5\n3: Lightning MP-7 \n4: Heal MP-5\n5: Attack\n'))
			print(choice)
			if choice not in [1,2,3,4,5]:
				print('Choose between 1 and 5')			
		except:
			print("Choose a number")
	if choice == 4:
		jace.heal()
	else:
		bads = []
		position = 0
		for i in enemies:
			bads.append(position)
			print(f'{position}: ',i.name,'\n')
			position += 1

		while target not in bads:
			try:
				target = int(input('Choose a target:'))
				
				if target not in bads:
					print('Make a valid selection')
			except:
				print("Choose a number")

		if choice == 1:
			enemies[target].health -= jace.ice()
		elif choice == 2:
			enemies[target].health -= jace.fire()
		elif choice == 3:
			enemies[target].health -= jace.lightning()
		elif choice == 5:
			enemies[target].health -= jace.attack()

def enemy_turn():
	for i in enemies:
		jace.health -= i.attack()


def remove_dead():
	for i in enemies:
		position = 0
		if i.health <1:
			enemies.pop(position)
		position += 1

def dis_enemies():
	for i in enemies:
		print(i)
	print('\n')



play = True

while play:
	print('Welcome to the fight. Good luck')
	jace = Wizard('Jace')
	garbonzo = Goblin('Garbonzo')
	garbonzo2 = Goblin('Garbonzo2')
	enemies = [garbonzo, garbonzo2]

	while jace.health>0 and len(enemies)>0:
		print(jace,'\n')
		dis_enemies()

		player_turn()
		remove_dead()
		if len(enemies)<1:
			choice = "fool"
			while choice not in ['Y','y','N','n']:
				choice = input("The enemies are defeated! would you like to fight again? (Y/N)")
				if choice == 'Y' or choice == 'y':
					continue
				elif choice == 'N' or choice == 'n':
					play = False
				else:
					print('Enter a valid selction')
			break
		enemy_turn()
		if jace.health<1:
			choice = "fool"
			while choice not in ['Y','y','N','n']:
				choice = input("You Lost! would you like to fight again? (Y/N)")
				if choice == 'Y' or choice == 'y':
					continue
				elif choice == 'N' or choice == 'n':
					play = False
				else:
					print('Enter a valid selction')
			break
