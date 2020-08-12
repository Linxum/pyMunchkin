import random

debug = int(input("0 - debug; 1 - basic: "))
if debug == 0:
	user = ["Алишер", "Тима"]
	count_card = 10
else:
	count_user = int(input("Скока игроков?: "))
	user = []
	for i in range(count_user):
		user.append(input("Имя?:"))
	count_card = int(input("Кол-во карт: "))

count_user = len(user)

bool = True
card_user = [[], [], [], []]
a = ["thief", "wizard", "warrior", "elf", "ogr"]
b = ["dragons", "evil org", "witch", "witcher", "tank"]

def cardsbegin(x):
	for i in range(x):
		c = random.randint(0, 1)
		for it in range(0, count_user):
			n = random.randint(0, 4)
			if c == 0:
				card_user[it].append(a[n])
			else:
				card_user[it].append(b[n])

def begin():
	cardsbegin(count_card)
	for i in range(0, count_user):
		print("Карты " + user[i] + " : " + str(card_user[i]))

def chkcnt():
	for i in range(0, count_user):
		while len(card_user[i]) > 5:
			d = int(input(user[i] + ", введи номер карты, которую не жалко: ")) - 1
			del card_user[i][d]
			print("Теперь у тебя: " + str(card_user[i]))

def game():
	while bool == True:
		chkcnt()

begin()
game()
