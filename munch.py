import random, time
import sqlite3 as sql

names =['Алишер', 'Тима', 'Акакий', 'Тофик', 'Никита']

debug = int(input("0 - debug; 1 - basic: "))
mode = int(input("0 - игра с ботом; 1 - игра вдвоем: "))
if debug == 0:
	user = ["Алишер", "Тима"]
	user_items = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]
	count_card = 6
else:
	count_user = int(input("Скока игроков (до 4-х)?: "))
	user = []

	user.append(input("Имя?: "))
	for i in range(0, count_user - 1):
		user.append(names[random.randint(0,4)])
	count_card = int(input("Кол-во карт: "))
	print("Ваши соперники: " + str(', '.join(user[1:])))
count_user = len(user)

bool = True
card_user = [[], [], [], []]

libcards = sql.connect('cards.sqlite')
cursor = libcards.cursor()

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
	if mode == 1:
		for i in range(0, count_user):
			print("Карты " + user[i] + " : " + str(', '.join(card_user[i])))
	else :
		print("Твои карты: " + str(', '.join(card_user[0])))
	time.sleep(2)

def chkcnt():
	if mode == 1:
		for i in range(0, count_user):
			while len(card_user[i]) > 5:
				d = int(input(user[i] + ", введи номер карты, которую не жалко: ")) - 1
				del card_user[i][d]
				print("Теперь у тебя: " + str(', '.join(card_user[i])))
	else:
		while len(card_user[0]) > 5:
				d = int(input(user[0] + ", введи номер карты, которую не жалко: ")) - 1
				del card_user[0][d]
				print("Теперь у тебя: " + str(', '.join(card_user[0])))
	time.sleep(3)

def door():
	print("Check-check")
	time.sleep(1)
	open_door = doors[random.randint(0, 3)][random.randint(0, 4)]
	print("Ты открыл дверь. Тебе выпало: " + str(open_door))
	actions()

def actions():
	action = input("Твои действия: (С)мывка; (П)омощь друга; (К)арты: ")
	if action == "С" or action == "с" or action == "c" or action == "C":
		square = random.randint(1, 6)
		print("Тебе выпало: " + str(square))
		if square > 4 :
			print("А тебе везет!")
		else:
			print("Не повезло")
	elif action == "К" or action == "к" or action == "K" or action == "k":
		print("Твои карты: " + str(', '.join(card_user[0])))
		chosen_card = input("Выбери карту действия: ")
	elif action == "П" or action == "п" or action == "h" or action == "H" or action == "p"  or action == "P" or action == "g" or action == "G":
		print("Список твоих немногочисленных друзей: " + str(', '.join(user)))
		time.sleep(1)
		fri = input("А теперь выбери одного из них: ")
begin()
chkcnt()
door()
