from random import choice
from random import randint

# Гра Монополія
print("Вас вітає гра 'Монополія' !!! Введіть імена гравців (2 гравці): ")
player_1_name = input("Перший гравець: ")
player_2_name = input("Другий гравець: ")
print()
print(player_1_name)
print(player_2_name)
steps_1 = 0
steps_2 = 0

# Опції, які випадають користувачу під час ходу, залежно від того,
# яке число випаде на кубику, '$$$' - можливість купити акції
main_game_options = ['STR', 'TER', 'LVI', 'KYV', 'ODS', '*?*',
                     '*#*', '$$$']
print(*main_game_options)

# Глобальна змінна History, в якій записуватиметься історія ходів
history = ''

# штраф
fines = [200, 500, 1000] 

# карточки  -  ШАНС
chance = ['move two spaces forward', 'move back one space', 'prize +1000', 'fine -500'] 


class Prison:
    def __init__(self):
        self.random_num_cube = randint(1, 6)
        
    def check_data_choice(self):
        if main_game_options[self.random_num_cube] != '*#Prison#*':
                print(f'You on: {main_game_options[self.random_num_cube]}')
        else:
            print(f'You on: {main_game_options[self.random_num_cube]}\n\tYour fine = {choice(fines)}')


class Surprise(Prison):
    def __init__(self):
         super().__init__()
        
    def check_data_choice(self):
        if main_game_options[self.random_num_cube] != '*?Surprise?*':
                print(f'You on: {main_game_options[self.random_num_cube]}')
        else:
            print(f'You on: {main_game_options[self.random_num_cube]}\n\tYour chance = {choice(chance)}')


lst_prison_surprise = [Prison(), Surprise()]
for data in lst_prison_surprise:
    data.check_data_choice()


class Territory:
    def __init__(self, factories, lands):
        self.factories = factories
        self.lands = lands

    def __str__(self):
        return f'Factories:\n{self.factories}\nLands:\n{self.lands}'

    def get_factory_price(self, factory):
        self.validation(factory, self.factories)
        return f'Price of factory {factory} is {self.factories.get(factory)}'

    def get_land_price(self, land):
        self.validation(land, self.lands)
        return f'This land {land} costs {self.lands.get(land)}'

    def set_factory(self, name_of_factory, price):
        self.factories[name_of_factory] = price
        return self.factories

    def set_land(self, name_of_land, land_price):
        self.lands[name_of_land] = land_price
        return self.lands

    @classmethod
    def validation(cls, key, dictionary):
        if key not in dictionary:
            raise KeyError('Wrong key!')

    def delete_factory(self, factory):
        self.validation(factory, self.factories)
        del self.factories[factory]

    def delete_land(self, land):
        self.validation(land, self.lands)
        del self.lands[land]


terra = Territory({}, {})
terra.set_factory('МоторСіч', 500)
terra.set_factory('НВК Іскра', 450)
terra.set_factory('Електроважмаш', 300)
terra.set_factory('Ворскла Сталь', 350)
terra.set_factory('Стальканат-Сілур', 200)
terra.set_factory('Дніпрометиз', 400)

terra.set_land('50 соток', 100)
terra.set_land('1 гектар', 200)
terra.set_land('40 соток', 80)
terra.set_land('30 соток', 60)
terra.set_land('20 соток', 50)
terra.set_land('10 соток', 25)

# print(terra)


# Дескрипротр для класу City, в якому можна видаляти , отримувати чи присвоювати значення
# певного параметру. Також цей дескриптор використовується і в класі Stocks(див. нижче)
class CityDescriptor:

    def __set_name__(self, owner, var):
        self.var = '_' + var

    def __get__(self, instance, owner):
        return getattr(instance, self.var)

    def __set__(self, instance, value):
        setattr(instance, self.var, value)


class City:
    streets = CityDescriptor()
    real_estate = CityDescriptor()
    parking_areas = CityDescriptor()

    def __init__(self, streets, real_estate, parking_areas):
        self.streets = streets
        self.real_estate = real_estate
        self.parking_areas = parking_areas


class Lviv(City):
    coffee_shops = CityDescriptor()

    def __init__(self, streets, real_estate, parking_areas, coffee_shops):
        super().__init__(streets, real_estate, parking_areas)
        self.coffee_shops = coffee_shops

    def __str__(self):
        return f'Для міста Львів:\n'\
               f'Вулиці, доступні для продажу:\n{self.streets}\n' \
               f'Автостоянки:\n{self.parking_areas}\n' \
               f'Житлові комплекси(нерухомість):\n{self.real_estate}\n' \
               f'Доступні кавярні для покупки:\n{self.coffee_shops}'


lviv = Lviv({}, {}, {}, {})
lviv.streets['Вулиця Хімічна'] = 140
lviv.streets['Проспект Шевченка'] = 200
lviv.streets['Краківська вулиця'] = 170
lviv.streets['Проспект Свободи'] = 185
lviv.streets['Вулиця Генерала Чупринки'] = 220
lviv.streets['Підвальна вулиця'] = 210


lviv.parking_areas['КООПЕРАТИВ АВТОГАРАЖІВ №1'] = 90
lviv.parking_areas['АВТОГАРАЖ №6'] = 75
lviv.parking_areas['АВТОГАРАЖНИЙ КООПЕРАТИВ №15'] = 80
lviv.parking_areas['Автостоянка № 1'] = 100
lviv.parking_areas['ГАРАЖНИЙ КООПЕРАТИВ "ПАСІЧНИК"'] = 95
lviv.parking_areas['АВТОГАРАЖІВ №2'] = 65


lviv.coffee_shops['Старий Львів'] = 110
lviv.coffee_shops["Кав'ярня-галерея 'Штука'"] = 115
lviv.coffee_shops['Kredens Cafe'] = 120
lviv.coffee_shops['Про100 КАВА'] = 105
lviv.coffee_shops['Dominicanes/Домініканес'] = 95
lviv.coffee_shops['SDV Coffee'] = 90


lviv.real_estate['ЖК Екодім'] = 380
lviv.real_estate['ЖК HELGA'] = 365
lviv.real_estate['ЖК Tiffany apartments'] = 390
lviv.real_estate['ЖК AUROOM SOLAR'] = 370
lviv.real_estate['ЖК Avalon Holiday'] = 350
lviv.real_estate['ЖК Вікінг Парк'] = 375

#print(lviv)


class Kyiv(City):
    restaurants = CityDescriptor()

    def __init__(self, streets, real_estate, parking_areas, restaurants):
        super().__init__(streets, real_estate, parking_areas)
        self.restaurants = restaurants

    def __str__(self):
        return f'Для міста Київ:\n'\
               f'Вулиці, доступні для продажу:\n{self.streets}\n' \
               f'Автостоянки:\n{self.parking_areas}\n' \
               f'Житлові комплекси(нерухомість):\n{self.real_estate}\n' \
               f'Доступні ресторани для покупки:\n{self.restaurants}'


kyiv = Kyiv({}, {}, {}, {},)
kyiv.restaurants['Porto Maltese'] = 130
kyiv.restaurants['Philadelphia Roll&Bowl'] = 110
kyiv.restaurants['Promenade'] = 100
kyiv.restaurants['Велюр'] = 150
kyiv.restaurants['Musafir'] = 125
kyiv.restaurants['Пузата Хата'] = 105

kyiv.parking_areas['Паркінг на Лісовій'] = 90
kyiv.parking_areas['Автостоянка "Престиж"'] = 95
kyiv.parking_areas['Платна парковка на Хрещатику'] = 80
kyiv.parking_areas['Мережа автогаражів "Святошин"'] = 85
kyiv.parking_areas['Автостоянка №1'] = 60
kyiv.parking_areas['Паркінг біля метро "Вокзальна"'] = 70

kyiv.streets['Хрещатик'] = 250
kyiv.streets['Борщагівська'] = 170
kyiv.streets['Андріївський узвів'] = 200
kyiv.streets['Труханівська вулиця'] = 180
kyiv.streets['вулиця Петра Сагайдачного'] = 185
kyiv.streets['вулиця Металістів'] = 130

kyiv.real_estate['Клубний будинок "OLEGIVSKIY"'] = 420
kyiv.real_estate['ЖК LUCKY LAND'] = 330
kyiv.real_estate['Русанівська Гавань'] = 340
kyiv.real_estate['ЖК Eco Dream'] = 380
kyiv.real_estate['ЖК Illinsky House'] = 470
kyiv.real_estate['ЖК Метрополіс'] = 310
kyiv.real_estate['ЖК 4 сезони'] = 270

#print('\n')
#print(kyiv)


class Odessa(City):
    # Бази відпочинку
    camp_bases = CityDescriptor()

    def __init__(self, streets, real_estate, parking_areas, camp_bases):
        super().__init__(streets, real_estate, parking_areas)
        self.camp_bases = camp_bases

    def __str__(self):
        return f'Для міста Одеса:\n'\
               f'Вулиці, доступні для продажу:\n{self.streets}\n' \
               f'Автостоянки:\n{self.parking_areas}\n' \
               f'Житлові комплекси(нерухомість):\n{self.real_estate}\n' \
               f'Туристичні бази відпочинку для покупки:\n{self.camp_bases}'


odessa = Odessa({}, {}, {}, {})
odessa.camp_bases['Приватний сектор «Райський куточок»'] = 130
odessa.camp_bases['Пансіонат «Совіньйон»'] = 150
odessa.camp_bases['База відпочинку «Вулик»'] = 145
odessa.camp_bases['Дача міні-готель «Wood Village»'] = 125
odessa.camp_bases['Приватний будинок «Затишний дворик»'] = 140
odessa.camp_bases['Турбаза "Веселка"'] = 120

odessa.streets['Дерибасівська вулиця'] = 240
odessa.streets['Приморський бульвар'] = 200
odessa.streets['вулиця Рішельєвська'] = 210
odessa.streets['Магістральна вулиця'] = 130
odessa.streets['вулиця Польська'] = 120
odessa.streets['вулиця Героїв Маріуполя'] = 180

odessa.parking_areas['Австостоянка на вул. Шклярука'] = 80
odessa.parking_areas['Аркадіївська австостоянка'] = 85
odessa.parking_areas['Австостоянка №1'] = 70
odessa.parking_areas['Південна автостоянка'] = 65
odessa.parking_areas['Автостоянка "Фенікс-92"'] = 75
odessa.parking_areas['Австостоянка "Супутник"'] = 60

odessa.real_estate['ЖК Золота Ера'] = 370
odessa.real_estate['ЖК Еллада'] = 290
odessa.real_estate['ЖК Атмосфера'] = 310
odessa.real_estate['ЖК Modern'] = 330
odessa.real_estate['ЖК Приморські Сади'] = 240
odessa.real_estate['ЖК Сьоме Небо'] = 260

#print('\n')
#print(odessa)


# Також потрібен клас BankAccount, де будуть зберігатись гроші гравців
# та реалізовано методи для зняття та нарахування коштів

class BankAccount:
    def __init__(self, money):
        self.money = money

    def withdraw_money(self, suma):
        if not self.valid_money(self.money, suma):
            return 'You do not have enough money for this operation'

        self.money -= suma

    def add_money(self, suma):
        self.money += suma

    def __str__(self):
        return f'Money = {self.money}'

    # Валідатор, щоб можна було знімати кошти лише тоді, коли сума для зняття не перевищує суму на рахунку
    @classmethod
    def valid_money(cls, money, suma):
        if money < suma:
            return False
        return True


player1_bank = BankAccount(5000)
player2_bank = BankAccount(5000)

# Клас Stocks, де гравець може придбати акції тої чи іншої компанії


class Stocks:
    companies = CityDescriptor()

    def __init__(self, companies):
        self.companies = companies

    def __str__(self):
        return f'Available stocks of different companies:\n{self.companies}'


stocks = Stocks({})
stocks.companies['Tesla'] = 500
stocks.companies['Space X'] = 600
stocks.companies['Google'] = 700
stocks.companies['Microsoft'] = 750
stocks.companies['Apple'] = 800
stocks.companies['Thermotransit'] = 400

print(stocks)


while True:
    print(f'{player_1_name} кидає гральний кубик...')
    probils_1 = ''
    rand1 = randint(1, 6)
    steps_1 += rand1
    print(f'Випало {rand1} очок')
    print(f'{player_2_name} кидає гральний кубик...')
    probils_2 = ''
    rand2 = randint(1, 6)
    steps_2 += rand2
    print(f'Випало {rand2} очок')
    if steps_1 % 8 == 0:
        player1_bank.add_money(400)
        print(f'Вітаємо, гравець {player_1_name}!\nВи пройшли повне коло і потрапили рівно на клітинку STR!\n'
              f'За це вам буде нараховано 400 одиниць валюти на ваш банківський рахунок')

    if steps_2 % 8 == 0:
        player2_bank.add_money(400)
        print(f'Вітаємо, гравець {player_2_name}!\nВи пройшли повне коло і потрапили рівно на клітинку STR!\n'
              f'За це вам буде нараховано 400 одиниць валюти на ваш банківський рахунок')
    steps_1 -= 8 if steps_1 >= 8 else 0
    steps_2 -= 8 if steps_2 >= 8 else 0
    probils_1 += steps_1 * '    '
    probils_2 += steps_2 * '    '
    print(probils_1 + player_1_name)
    print(probils_2 + player_2_name)
    print(*main_game_options)

    contin = input("Do you want to continue or stop?: ")
    if contin == 'stop':
        break
