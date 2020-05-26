import random

debug = int(input("0 - debug; 1 - basic: "))
if debug == 0:
	user1 = "Алишер"
	user2 = "Тима"
	co = 6
else:
	user1 = input("Введи свое имя, User1: ")
	user2 = input("Введи свое имя, User2: ")
	co = int(input("Кол-во карт: "))

bool = True
counts = [0, 0]
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
		counts[0] = counts[0] + 1

def cardsbegin2(x):
	for i in range(x):
		c = random.randint(0, 1)
		n = random.randint(0, 4)
		if c == 0:
			mu2.append(a[n])
		else:
			mu2.append(b[n])
		counts[1] = counts[1] + 1

def begin():
	cardsbegin1(co)
	cardsbegin2(co)
	print("Карты " + user1 + " : " + str(mu1))
	print("Карты " + user2 + " : " + str(mu2))

def chkcnt():
	while counts[0] > 5:
		d = int(input(user1 + ", введи номер карты, которую не жалко: ")) - 2
		del mu1[d]
		counts[0] = counts[0] - 1
		print("Ты теряешь: " + mu1[d])
	while counts[1] > 5:
		d = int(input(user2 + ", введи номер карты, которую не жалко: ")) - 2
		del mu2[d]
		counts[1] = counts[1] - 1
		print("Ты теряешь: " + mu2[d])

def game():
	while bool == True:
		chkcnt()
def getcard():
	

begin()
game()
