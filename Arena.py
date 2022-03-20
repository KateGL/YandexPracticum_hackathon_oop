import random

possible_paladin_names = ['Ярза', 'Виллирал', 'Фарельльт', 'Утер',
                          'Тэйфест', 'Болвар', 'Арбнэнам', 'Кейсэна',
                          'Гегель', 'Довастин', 'Берлен', 'Лисорба',
                          'Грелек', 'Гуон', 'Семкиль', 'Сайданлия',
                          'Тариса', 'Джелейса', 'Ломанир', 'Гайя']
possible_warrior_names = ['Хольгор', 'Гаррош', 'Кайру', 'Тройлин',
                          'Винелен', 'Расельмир', 'Лирозаэль', 'Удлан',
                          'Лоти', 'Завак', 'Делрани', 'Гритейр', 'Рикхэйл',
                          'Скузза', 'Мар', 'Хасижоу', 'Варриан', 'Магни',
                          'Меветал', 'Виллорн', 'Холекта']


class Thing:
    def __init__(self, name, hit_points, attack_rate, defence):
        self.name = name
        self.hit_points = hit_points
        self.attack_rate = attack_rate
        self.defence = defence


wooden_sword = Thing('деревянный меч', 0, 3, 0)
legendary_sword = Thing('легендарный меч', 20, 30, 10)
straw_hat = Thing('соломенная шляпа', 0, 0, 2)
all_thing_list = [wooden_sword, legendary_sword, straw_hat]


class Person:
    def __init__(self, name,
                 hit_points=100,
                 attack_rate=20,
                 defence=10,
                 inventory=0):
        self.name = name
        self.hit_points = hit_points
        self.attack_rate = attack_rate
        self.defence = defence
        self.inventory = inventory


class Warrior(Person):
    WARRIOR_ATTACK_MULTIPLIER = 2

    def __init__(self,
                 name,
                 hit_points=100,
                 attack_rate=20 * WARRIOR_ATTACK_MULTIPLIER,
                 defence=10,
                 inventory=0):
        self.name = name
        self.hit_points = hit_points
        self.attack_rate = attack_rate
        self.defence = defence
        self.inventory = inventory
        super().__init__(name, hit_points, attack_rate, defence, inventory)


class Paladin(Person):
    PALADIN_HIT_POINTS_MULTIPLIER = 2
    PALADIN_DEFENCE_MULTIPLIER = 2

    def __init__(self,
                 name,
                 hit_points=100 * PALADIN_HIT_POINTS_MULTIPLIER,
                 attack_rate=20,
                 defence=10 * PALADIN_DEFENCE_MULTIPLIER,
                 inventory=0):
        self.name = name
        self.hit_points = hit_points
        self.attack_rate = attack_rate
        self.defence = defence
        self.inventory = inventory
        super().__init__(name, hit_points, attack_rate, defence, inventory)


def create_things():
    created_thing_list = []
    for i in range(random.randint(10, 40)):
        new_thing = random.choice(all_thing_list)
        created_thing_list.append(new_thing)
    return created_thing_list


def create_characters():
    created_characters_list = []
    for i in range(10):
        random_class = random.choice([Paladin, Warrior])
        new_character = random_class(random.choice(possible_paladin_names))
        # print(new_character.name, new_character.__class__.__name__)
        created_characters_list.append(new_character)
    return created_characters_list


def things_distribution(characters_list, thing_list):
    for i in range(len(thing_list)):
        random_character = random.choice(characters_list)
        if random_character.inventory == 4:
            continue
        setattr(random_character, 'hit_points', random_character.hit_points
                + thing_list[i].hit_points)
        setattr(random_character, 'attack_rate', random_character.attack_rate
                + thing_list[i].attack_rate)
        setattr(random_character, 'defence', random_character.defence
                + thing_list[i].defence)
        setattr(random_character, 'inventory', random_character.inventory + 1)

    return characters_list


ready_for_battle_characters = things_distribution(create_characters(),
                                                  create_things())
while len(ready_for_battle_characters) != 1:
    attacking_character = random.choice(ready_for_battle_characters)
    defending_character = random.choice(ready_for_battle_characters)
    if attacking_character == defending_character:
        continue
    print(f'{attacking_character.name} наносит '
          f'{(attacking_character.attack_rate - attacking_character.attack_rate * (defending_character.defence/100)):.0f} урона по '
          f'{defending_character.name}')
    setattr(defending_character, 'hit_points', defending_character.hit_points
            - (attacking_character.attack_rate
               - attacking_character.attack_rate
               * (defending_character.defence/100)))
    print(f'теперь у него {defending_character.hit_points:.0f} здоровья')
    print('-------------------------------------------------')
    if defending_character.hit_points < 0:
        ready_for_battle_characters.remove(defending_character)
    if len(ready_for_battle_characters) == 1:
        print(ready_for_battle_characters[0].name, 'победил')