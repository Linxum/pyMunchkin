import random

debug = int(input("0 - debug; 1 - basic: "))
if debug == 0:
	user = ["Алишер", "Тима"]
	count_card = 6
else:
	count_user = int(input("Скока игроков?: "))
	user = []
	for i in range(count_user):
		user.append(input("Имя?:"))
	count_card = int(input("Кол-во карт: "))

count_user = len(user)

bool = True
card_user = [[], [], [], []]

door = [["навальный", "лукашенко", "медведев", "путин", "бэтмен"], ["пожилая чокопайка", "каво-2", "олежа навальный", "карнавальный", "”], [“поцелуй Брежнева”, “”, “”, “”, “”], [“плоти нологи”, “денег нет, но вы держитесь”, “”, “”, “”, “”], ]
riches = [[“бротофан”, “wargaming”, “любэ”, “”], [“коммандирово4ка Ельцина”, “”, “”, “”, “”], [“маска для сна”, “брови Брежнева”, “”, “”, “”], [“зубр”, “мишка”, “”, “”, “”, “”], [“палёная б/ушная колонка JBL”, “бэтаранг”]]

def cardsbegin(x):
	for i in range(x):
		c = random.randint(0, 8)
		for it in range(0, count_user):
			n = random.randint(0, 4)
			if c == 0:
				card_user[it].append(a[n])
			elif c == 1:
				card_user[it].append(b[n])
			elif c == 2:
				card_user[it].append(c[n])
			elif c == 3:
				card_user[it].append(d[n])
			elif c == 4:
				card_user[it].append(e[n])
			elif c == 5:
				card_user[it].append(g[n])
			elif c == 6:
				card_user[it].append(f[n])
			elif c == 7:
				card_user[it].append(h[n])
			elif c == 8:
				card_user[it].append(i[n])

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

def door():
	print("Check")
	open_door = a[random.randint(0, 4)]
	print("Ты открыл дверь. Тебе выпало: " + open_door)

begin()
chkcnt()
door()
