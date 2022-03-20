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
    """Класс вещей"""
    def __init__(self, name, hit_points, attack_rate, defence, slot):
        self.name = name
        self.hit_points = hit_points
        self.attack_rate = attack_rate
        self.defence = defence
        self.slot = slot


wooden_sword = Thing('деревянный меч', 0, 3, 0, 'weapon')
legendary_sword = Thing('легендарный меч', 20, 30, 5, 'weapon')
steel_sword = Thing('стальной меч', 0, 8, 0, 'weapon')
war_hammer = Thing('боевой молот', 0, 15, 0, 'weapon')
straw_hat = Thing('соломенная шляпа', 0, 0, 2, 'helm')
mail_hood = Thing('кольчужный капюшон', 8, 0, 5, 'helm')
bascinet = Thing('бацинет', 12, 0, 8, 'helm')
legendary_helm = Thing('легендарный шлем', 20, 0, 10, 'helm')
rabbit_foot = Thing('кроличья лапка', 1, 1, 1, 'accessory')
magic_ring = Thing('волшебное кольцо', 3, 3, 3, 'accessory')
amulet_of_strength = Thing('амулет силы', 0, 12, 0, 'accessory')
ring_of_omnipotence = Thing('кольцо всевластия', 10, 10, 5, 'accessory')
home_bathrobe = Thing('домашний халат', 0, 0, 2, 'armor')
chain_mail = Thing('кольчуга', 10, 0, 5, 'armor')
full_armor = Thing('полные латы', 15, 0, 8, 'armor')
legendary_armor = Thing('легендарная броня', 20, 0, 10, 'armor')

all_thing_list = [wooden_sword, steel_sword, war_hammer, legendary_sword,
                  straw_hat, mail_hood, bascinet, legendary_helm,
                  rabbit_foot, magic_ring, amulet_of_strength,
                  ring_of_omnipotence, home_bathrobe, chain_mail, full_armor,
                  legendary_armor]


class Person:
    """Базовый класс персонажей"""
    def __init__(self, name, hit_points=100, attack_rate=20, defence=10):
        self.name = name
        self.hit_points = hit_points
        self.attack_rate = attack_rate
        self.defence = defence

    def get_damage(self, attacker):
        """Получить количество урона"""
        return (attacker.attack_rate - attacker.attack_rate
                * (self.defence/100))

    def get_hitpoints(self, attacker):
        """Получить количество хп оставшихся после удара"""
        return (self.hit_points - (attacker.attack_rate - attacker.attack_rate
                * (self.defence/100)))


class Warrior(Person):
    """Класс воина"""

    WARRIOR_ATTACK_MULTIPLIER = 2

    def __init__(self, name, hit_points=100,
                 attack_rate=20 * WARRIOR_ATTACK_MULTIPLIER, defence=10,
                 weapon='ничего нет(!)', helm='повязка',
                 accessory='серьга в носу', armor='рубаха'):
        """Добавлены слоты для вещей, чтобы они не дублировались,
        и значения по умолчанию, чтобы бойцы не выступали голыми"""
        self.name = name
        self.hit_points = hit_points
        self.attack_rate = attack_rate
        self.defence = defence
        self.weapon = weapon
        self.helm = helm
        self.accessory = accessory
        self.armor = armor
        super().__init__(name, hit_points, attack_rate, defence)


class Paladin(Person):
    """Класс паладина"""

    PALADIN_HIT_POINTS_MULTIPLIER = 2
    PALADIN_DEFENCE_MULTIPLIER = 2

    def __init__(self, name, hit_points=100 * PALADIN_HIT_POINTS_MULTIPLIER,
                 attack_rate=20, defence=10 * PALADIN_DEFENCE_MULTIPLIER,
                 weapon='ничего нет(!)', helm='повязка',
                 accessory='священный символ', armor='ряса'):
        """Добавлены слоты для вещей, чтобы они не дублировались,
        и значения по умолчанию, чтобы бойцы не выступали голыми"""
        self.name = name
        self.hit_points = hit_points
        self.attack_rate = attack_rate
        self.defence = defence
        self.weapon = weapon
        self.helm = helm
        self.accessory = accessory
        self.armor = armor
        super().__init__(name, hit_points, attack_rate, defence)


def create_things():
    """Создаем случайное количество вещей из списка доступных"""
    created_thing_list = []
    for i in range(random.randint(10, 40)):
        new_thing = random.choice(all_thing_list)
        created_thing_list.append(new_thing)
    return created_thing_list


def create_characters():
    """Создаем 10 бойцов"""
    created_characters_list = []
    for i in range(10):
        random_class = random.choice([Paladin, Warrior])
        new_character = random_class(random.choice(possible_paladin_names))
        created_characters_list.append(new_character)
    return created_characters_list


def things_distribution(characters_list, thing_list):
    """Раздаем вещи бойцам"""
    for i in range(len(thing_list)):
        random_character = random.choice(characters_list)
        slot = thing_list[i].slot
        setattr(random_character, 'hit_points', random_character.hit_points
                + thing_list[i].hit_points)
        setattr(random_character, 'attack_rate', random_character.attack_rate
                + thing_list[i].attack_rate)
        setattr(random_character, 'defence', random_character.defence
                + thing_list[i].defence)
        setattr(random_character, slot, thing_list[i].name)
    return characters_list


def info_message():
    """Сообщение с информацией о бойцах"""
    print('На арену выходят!')
    for i in range(len(ready_for_battle_characters)):
        print(f'{ready_for_battle_characters[i].__class__.__name__} '
              f'{ready_for_battle_characters[i].name} у него в руках '
              f'{ready_for_battle_characters[i].weapon}, на голове '
              f'{ready_for_battle_characters[i].helm}, на теле '
              f'{ready_for_battle_characters[i].armor}, его аксессуар '
              f'{ready_for_battle_characters[i].accessory} ХАРАКТЕРИСТИКИ: '
              f'Здоровье - {ready_for_battle_characters[i].hit_points}, '
              f'Сила удара - {ready_for_battle_characters[i].attack_rate}, '
              f'Защита - {ready_for_battle_characters[i].defence}%')


ready_for_battle_characters = things_distribution(create_characters(),
                                                  create_things())
info_message()
while len(ready_for_battle_characters) != 1:  # Главный цикл
    attacking_character = random.choice(ready_for_battle_characters)
    defending_character = random.choice(ready_for_battle_characters)
    if attacking_character == defending_character:
        continue
    print(f'{attacking_character.name} наносит '
          f'{Person.get_damage(defending_character, attacking_character):.0f} '
          f'урона по '
          f'{defending_character.name}')
    setattr(defending_character, 'hit_points',
            Person.get_hitpoints(defending_character, attacking_character))
    print(f'теперь у него {defending_character.hit_points:.0f} здоровья')
    if defending_character.hit_points < 0:
        ready_for_battle_characters.remove(defending_character)
        print(f'{defending_character.name} погибает')
    print('-------------------------------------------------')
    if len(ready_for_battle_characters) == 1:
        print(ready_for_battle_characters[0].name, 'побеждает!')
