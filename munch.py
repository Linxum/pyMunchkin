import random

debug = int(input("0 - debug; 1 - basic: "))
if debug == 0:
	users = ["Алишер", "Тима"]
	count = 6
else:
	users = []
	for i in range(2):
		users.append(input("Имя?:"))
	count = int(input("Кол-во карт: "))

bool = True
mu1 = []
mu2 = []
a = ["thief", "wizard", "warrior", "elf", "ogr"]
b = ["dragons", "evil org", "witch", "witcher", "tank"]

def cardsbegin1(x):
	for i in range(x):
		c = random.randint(0, 1)
		n = random.randint(0, 4)
		if c == 0:
			mu1.append(a[n])
		else:
			mu1.append(b[n])

def cardsbegin2(x):
	for i in range(x):
		c = random.randint(0, 1)
		n = random.randint(0, 4)
		if c == 0:
			mu2.append(a[n])
		else:
			mu2.append(b[n])

def begin():
	cardsbegin1(count)
	cardsbegin2(count)
	print("Карты " + users[0] + " : " + str(mu1))
	print("Карты " + users[1] + " : " + str(mu2))

def chkcnt():
	while len(mu1) > 5:
		d = int(input(users[0] + ", введи номер карты, которую не жалко: ")) - 2
		del mu1[d]
		print("Ты теряешь: " + mu1[d])
	while len(mu2) > 5:
		d = int(input(users[1] + ", введи номер карты, которую не жалко: ")) - 2
		del mu2[d]
		print("Ты теряешь: " + mu2[d])

def game():
	while bool == True:
		chkcnt()

def getcard():
		n = random.randint(0, 4)
		mu1.append(a[n])
		n = random.randint(0, 4)
		mu2.append(a[n])

begin()
game()
