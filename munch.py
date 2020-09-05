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

doors = [["навальный", "лукашенко", "медведев", "путин", "бэтмен"], ["пожилая чокопайка", "каво-2", "олежа навальный", "карнавальный", "q"], ["поцелуй Брежнева", "q", "q", "q", "q"], ["плоти нологи", "денег нет, но вы держитесь", "q", "q", "q"]]
riches = [["бротофан", "wargaming", "любэ", "q", "q"], ["коммандирово4ка Ельцина", "q", "q", "q", "q"], ["маска для сна", "брови Брежнева", "q", "q", "q"], ["зубр", "мишка", "q", "q", "q"], ["палёная б/ушная колонка JBL", "бэтаранг", "q", "q", "q"]] 

def cardsbegin(x):
	for i in range(x):
		c = random.randint(0, 1)
		for it in range(0, count_user):
			n = random.randint(0, 4)
			doo = int(random.randint(0, 3))
			rich = int(random.randint(0, 4))
			if c == 0:
				chosen_card = doors[doo][n]
				card_user[it].append(chosen_card)
			else:
				chosen_card = riches[rich][n]
				card_user[it].append(chosen_card)
			
def begin():
	cardsbegin(count_card)
	for i in range(0, count_user):
		print("Карты " + user[i] + " : " + str(', '.join(card_user[i])))

def chkcnt():
	for i in range(0, count_user):
		while len(card_user[i]) > 5:
			d = int(input(user[i] + ", введи номер карты, которую не жалко: ")) - 1
			del card_user[i][d]
			print("Теперь у тебя: " + str(', '.join(card_user[i])))

def door():
	print("Check")
	open_door = doors[random.randint(0, 3)][random.randint(0, 4)]
	print("Ты открыл дверь. Тебе выпало: " + str(open_door))
	actions()

def actions():
	action = input("Твои действия: (С)мывка; (П)омощь друга; (К)арты: ")
	if action == "С" or action == "с" or action == "c" or action == "C":
		square = random.randint(1, 6)
		print("Тебе выпало: " + str(square))
		if square > 4 :
			print("Тебе везет сегодня!")
		else:
			print("Не повезло")
	elif action == "К" or action == "к" or action == "K" or action == "k":
		print("Твои карты: " + str(', '.join(card_user[0])))
		chosen_card = input("Выбери карту действия: ")

begin()
chkcnt()
door()
