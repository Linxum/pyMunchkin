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

door = [[a], [b], [d],[e], []]
riches = [[c], [g], [f], [h], [i]]

a = ["навальный", "лукашенко", "медведев", "путин", "бэтмен"]#классы
b = ["пожилая чокопайка", "каво-2", "олежа навальный", "карнавальный"]#монстры   
c = [“бротофан”, “wargaming”, “любэ”, “”]#бонус 
d = [“поцелуй Брежнева”, “”, “”, “”, “”]#карты действия
e = [“плоти нологи”, “денег нет, но вы держитесь”, “”, “”, “”, “”]#проклятья  
g = [“коммандирово4ка Ельцина”, “”, “”, “”, “”]#разовые шмотки
f = [“маска для сна”, “брови Брежнева”, “”, “”, “”]#шмотки
h = [“зубр”, “мишка”, “”, “”, “”, “”]#скакуны
i = [“палёная б/ушная колонка JBL”, “бэтаранг”]#шмотки в руки

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

def door():
	print("Check")
	open_door = a[random.randint(0, 4)]
	print("Ты открыл дверь. Тебе выпало: " + open_door)

begin()
chkcnt()
door()
