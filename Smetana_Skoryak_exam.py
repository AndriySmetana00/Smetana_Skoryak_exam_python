import time
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

# Список для класу сюрприз - може випасти як бонусні гроші, так і штраф
surp_lst = [500, 1000, 2000, -1500, -750, -1200]


class Surprise:

    def __init__(self):
        self.chance = choice(surp_lst)

    def get_chance(self):
        return self.chance


class Territory:
    def __init__(self, factories, lands):
        self.factories = factories
        self.lands = lands

    def __str__(self):
        return f'Factories:\n{self.factories}\nLands:\n{self.lands}'

    def get_factory_price(self, factory):
        self.validation(factory, self.factories)
        return self.factories.get(factory)

    def get_land_price(self, land):
        self.validation(land, self.lands)
        return self.lands.get(land)

    def set_factory(self, name_of_factory, price):
        self.factories[name_of_factory] = price
        return self.factories

    def set_land(self, name_of_land, land_price):
        self.lands[name_of_land] = land_price
        return self.lands

    @classmethod
    def validation(cls, key, dictionary):
        if key not in dictionary.keys():
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

# print(lviv)


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
kyiv.streets['Андріївський узвіз'] = 200
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

# print('\n')
# print(kyiv)


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

# print('\n')
# print(odessa)


# Також потрібен клас BankAccount, де будуть зберігатись гроші гравців
# та реалізовано методи для зняття та нарахування коштів

class BankAccount:
    def __init__(self, money: int):
        self.money = money

    def withdraw_money(self, suma):
        self.money -= suma

    def add_money(self, suma):
        self.money += suma

    def __str__(self):
        return f'Money = {self.money}'


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


# print(stocks)


def game_func(index, bank, name):
    global history
    if main_game_options[index] == 'LVI':
        print(lviv)
        print('Виберіть операцію для міста Львів:\n'
              '1 - купити вулицю\n'
              '2 - купити нерухомість\n'
              '3 - купити автостоянку\n'
              '4 - купити кавярню\n')
        choice = int(input())
        lst_choice = [1, 2, 3, 4]
        if choice in lst_choice:
            if choice == 1:
                choice_2 = input('Введіть назву вулиці, яку хочете придбати: ')
                if choice_2 in lviv.streets:
                    history += f'\nПридбано вулицю {choice_2} гравцем {name} ціною {lviv.streets[choice_2]} у місті Львів'
                    bank.withdraw_money(lviv.streets[choice_2])
                    del lviv.streets[choice_2]
            elif choice == 2:
                choice_2 = input('Введіть назву нерухомості, яку хочете придбати: ')
                if choice_2 in lviv.real_estate:
                    history += f'\nПридбано нерухомість {choice_2} гравцем {name} ціною {lviv.real_estate[choice_2]} у місті Львів'
                    bank.withdraw_money(lviv.real_estate[choice_2])
                    del lviv.real_estate[choice_2]
            elif choice == 3:
                choice_2 = input('Введіть назву автостоянки, яку хочете придбати: ')
                if choice_2 in lviv.parking_areas:
                    history += f'\nПридбано автостоянку {choice_2} гравцем {name} ціною {lviv.parking_areas[choice_2]} у місті Львів'
                    bank.withdraw_money(lviv.parking_areas[choice_2])
                    del lviv.parking_areas[choice_2]
            else:
                choice_2 = input('Введіть назву кавярні, яку хочете придбати: ')
                if choice_2 in lviv.coffee_shops:
                    history += f'\nПридбано кавярню {choice_2} гравцем {name} ціною {lviv.coffee_shops[choice_2]} у місті Львів'
                    bank.withdraw_money(lviv.coffee_shops[choice_2])
                    del lviv.coffee_shops[choice_2]
    elif main_game_options[index] == 'KYV':
        print(kyiv)
        print('Виберіть операцію для міста Київ:\n'
              '1 - купити вулицю\n'
              '2 - купити нерухомість\n'
              '3 - купити автостоянку\n'
              '4 - купити ресторан\n')
        choice = int(input())
        lst_choice = [1, 2, 3, 4]
        if choice in lst_choice:
            if choice == 1:
                choice_2 = input('Введіть назву вулиці, яку хочете придбати: ')
                if choice_2 in kyiv.streets:
                    history += f'\nПридбано вулицю {choice_2} гравцем {name} ціною {kyiv.streets[choice_2]} у місті Київ'
                    bank.withdraw_money(kyiv.streets[choice_2])
                    del kyiv.streets[choice_2]
            elif choice == 2:
                choice_2 = input('Введіть назву нерухомості, яку хочете придбати: ')
                if choice_2 in kyiv.real_estate:
                    history += f'\nПридбано нерухомість {choice_2} гравцем {name} ціною {kyiv.real_estate[choice_2]} у місті Київ'
                    bank.withdraw_money(kyiv.real_estate[choice_2])
                    del kyiv.real_estate[choice_2]
            elif choice == 3:
                choice_2 = input('Введіть назву автостоянки, яку хочете придбати: ')
                if choice_2 in kyiv.parking_areas:
                    history += f'\nПридбано автостоянку {choice_2} гравцем {name} ціною {kyiv.parking_areas[choice_2]} у місті Київ'
                    bank.withdraw_money(kyiv.parking_areas[choice_2])
                    del kyiv.parking_areas[choice_2]
            else:
                choice_2 = input('Введіть назву ресторану, який хочете придбати: ')
                if choice_2 in kyiv.restaurants:
                    history += f'\nПридбано ресторан {choice_2} гравцем {name} ціною {kyiv.restaurants[choice_2]} у місті Київ'
                    bank.withdraw_money(kyiv.restaurants[choice_2])
                    del kyiv.restaurants[choice_2]
    elif main_game_options[index] == 'ODS':
        print(odessa)
        print('Виберіть операцію для міста Одеса:\n'
              '1 - купити вулицю\n'
              '2 - купити нерухомість\n'
              '3 - купити автостоянку\n'
              '4 - купити базу відпочинку\n')
        choice = int(input())
        lst_choice = [1, 2, 3, 4]
        if choice in lst_choice:
            if choice == 1:
                choice_2 = input('Введіть назву вулиці, яку хочете придбати: ')
                if choice_2 in odessa.streets:
                    history += f'\nПридбано вулицю {choice_2} гравцем {name} ціною {odessa.streets[choice_2]} у місті Одеса'
                    bank.withdraw_money(odessa.streets[choice_2])
                    del odessa.streets[choice_2]
            elif choice == 2:
                choice_2 = input('Введіть назву нерухомості, яку хочете придбати: ')
                if choice_2 in odessa.real_estate:
                    history += f'\nПридбано нерухомість {choice_2} гравцем {name} ціною {odessa.real_estate[choice_2]} у місті Одеса'
                    bank.withdraw_money(odessa.real_estate[choice_2])
                    del odessa.real_estate[choice_2]
            elif choice == 3:
                choice_2 = input('Введіть назву автостоянки, яку хочете придбати: ')
                if choice_2 in odessa.parking_areas:
                    history += f'\nПридбано нерухомість {choice_2} гравцем {name} ціною {odessa.parking_areas[choice_2]} у місті Одеса'
                    bank.withdraw_money(odessa.parking_areas[choice_2])
                    del odessa.parking_areas[choice_2]
            else:
                choice_2 = input('Введіть назву бази відпочинку, яку хочете придбати: ')
                if choice_2 in odessa.camp_bases:
                    history += f'\nПридбано базу відпочинку {choice_2} гравцем {name} ціною {odessa.camp_bases[choice_2]} у місті Одеса'
                    bank.withdraw_money(odessa.camp_bases[choice_2])
                    del odessa.camp_bases[choice_2]
    elif main_game_options[index] == 'TER':
        print(terra)
        print('Виберіть операцію для території:\n'
              '1 - купити завод\n'
              '2 - купити земельну ділянку\n')
        choice = int(input())
        lst_choice = [1, 2]
        if choice in lst_choice:
            if choice == 1:
                choice_2 = input("Введіть назву заводу, який хочете придбати: ")
                if choice_2 in terra.factories:
                    history += f'\nПридбано завод {choice_2} гравцем {name} ціною {terra.get_factory_price(choice_2)}'
                    bank.withdraw_money(terra.get_factory_price(choice_2))
                    terra.delete_factory(choice_2)
            elif choice == 2:
                choice_2 = input("Введіть назву земельної ділянки, який хочете придбати: ")
                if choice_2 in terra.lands:
                    history += f'\nПридбано емельну ділянку {choice_2} гравцем {name} ціною {terra.get_land_price(choice_2)}'
                    bank.withdraw_money(terra.get_land_price(choice_2))
                    terra.delete_land(choice_2)
    elif main_game_options[index] == '$$$':
        print(stocks)
        print('Виберіть акції для покупки:\n')
        choice = input()
        if choice in stocks.companies:
            history += f'\nПридбано акції компанії {choice} гравцем {name} ціною {stocks.companies[choice]} '
            bank.withdraw_money(stocks.companies[choice])
            del stocks.companies[choice]
    elif main_game_options[index] == '*?*':
        surprise = Surprise()
        surp_res = surprise.get_chance()
        if surp_res > 0:
            print(f'Вітаю {name}, вам пощастило!\n'
                  f'Ви щойно виграли {surp_res}!')
            history += f'\nВітаю {name}, вам пощастило!\n' \
                       f'Ви щойно виграли {surp_res}!'
            bank.add_money(surp_res)
        else:
            print(f'\nНа жаль {name}, вам не пощастило(((\n'
                  f'Ви щойно отримали штраф у розмірі {surp_res}!')
            history += f'\nНа жаль {name}, вам не пощастило(((\n' \
                       f'Ви щойно отримали штраф у розмірі {surp_res}!'
            bank.add_money(surp_res)
    elif main_game_options[index] == '*#*':
        print(f'\n{name}, ви потрапили до тюрми, тож протягом даного ходу не зможете робити ніяких покупок')
        history += f'\n{name}, ви потрапили до тюрми, тож протягом даного ходу не зможете робити ніяких покупок'


def who_win():
    flag = False
    if player1_bank.money <= 0:
        print(f'{player_2_name}, вітаю, ви перемогли!'
              f'{player_1_name}, на жаль, ви програли(((')
        flag = True
    elif player2_bank.money <=0:
        print(f'{player_1_name}, вітаю, ви перемогли!'
              f'{player_2_name}, на жаль, ви програли(((')
        flag = True
    return flag


question = input("\nВи вже грали в цю гру раніше?: ")
if question == 'yes':
    with open('Smetana_Skoryak_exam.txt', encoding='utf-8') as file:
        print('\n')
        print(file.read())
        print('\n')


while True:
    print(f'\n{player_1_name} кидає гральний кубик...')
    time.sleep(3)
    probils_1 = ''
    rand1 = randint(1, 6)
    steps_1 += rand1
    print(f'Випало {rand1} очок')
    time.sleep(1)
    if steps_1 % 8 == 0:
        player1_bank.add_money(400)
        print(f'\nВітаємо, гравець {player_1_name}!\nВи пройшли повне коло і потрапили рівно на клітинку STR!\n'
              f'За це вам буде нараховано 400 одиниць валюти на ваш банківський рахунок')
        history += f'\nВітаємо, гравець {player_1_name}!\nВи пройшли повне коло і потрапили рівно на клітинку STR!' \
                    f'\nЗа це вам буде нараховано 400 одиниць валюти на ваш банківський рахунок'

    steps_1 -= 8 if steps_1 >= 8 else 0
    probils_1 += steps_1 * '    '

    print(f'\n{player_2_name} кидає гральний кубик...')
    time.sleep(3)
    probils_2 = ''
    rand2 = randint(1, 6)
    steps_2 += rand2
    print(f'Випало {rand2} очок')
    time.sleep(1)

    if steps_2 % 8 == 0:
        player2_bank.add_money(400)
        print(f'\nВітаємо, гравець {player_2_name}!\nВи пройшли повне коло і потрапили рівно на клітинку STR!\n'
                f'За це вам буде нараховано 400 одиниць валюти на ваш банківський рахунок')
        history += f'\nВітаємо, гравець {player_2_name}!\nВи пройшли повне коло і потрапили рівно на клітинку STR!' \
                    f'\nЗа це вам буде нараховано 400 одиниць валюти на ваш банківський рахунок'

    steps_2 -= 8 if steps_2 >= 8 else 0
    probils_2 += steps_2 * '    '

    print(probils_1 + player_1_name)
    print(probils_2 + player_2_name)
    print(*main_game_options)
    print(f'\nГравець {player_1_name}, ваші дії:\n')
    game_func(steps_1, player1_bank, player_1_name)

    print(f'\nГравець {player_2_name}, ваші дії:\n')
    game_func(steps_2, player2_bank, player_2_name)

    print('\n')
    print(f'Баланс гравця {player_1_name} = {player1_bank.money}')
    print(f'Баланс гравця {player_2_name} = {player2_bank.money}')

    round_result = who_win()
    if round_result:
        print('\nІсторія гри:\n')
        print(history)
        break

    contin = input("Do you want to continue or stop?: ")
    if contin == 'stop':
        print('\nІсторія гри:\n')
        print(history)
        break

with open('Smetana_Skoryak_exam.txt', 'w', encoding='utf-8') as file:
    file.write(history)