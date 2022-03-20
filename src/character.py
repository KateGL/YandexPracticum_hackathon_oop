import random
from dataclasses import asdict, dataclass
from typing import ClassVar, List

from inventory import Inventory, generate_item


@dataclass()
class Character:  # Person
    """Базовый класс персонажа."""
    character_name: str
    health_points: int
    base_damage: int
    base_armor: int
    CHARACTER_INFO: ClassVar[str] = ('Character Name: {character_name}\n'
                                     'Armor: {base_armor} %\n'
                                     'Damage: {base_damage}\n'
                                     'Health: {health_points}'
                                     )

    def generate_inventory(self) -> Inventory:
        """Генерация инвентаря персонажа."""
        random_items = []
        for random_item in range(0, random.randint(1, 4)):
            item = generate_item()
            random_items.append(item)
        inventory_items = Inventory(random_items).items

        for item in inventory_items:
            self.health_points += item.health
            self.base_damage += item.damage
            self.base_armor += item.armor
        return Inventory(random_items)

    def initiative(self) -> int:
        """Расчёт инициативы бойцы, у кого выше, тот наносит удар."""
        return random.randint(1, 20)

    def is_alive(self) -> bool:
        """Проверка очков здоровья персонажа."""
        if self.health_points <= 0:
            return False
        else:
            return True

    def show_character_stats(self) -> None:
        """Печатает характеристики персонажа в консоль."""
        print(self.CHARACTER_INFO.format(**asdict(self)))

    def show_character_inventory(self, items: Inventory) -> None:
        """Печатает инвентарь персонажа в консоль."""
        items.show_inventory()

    def attack(self, opponent) -> None:
        """Рассчитывает нанесенный урон и отнимает очки здоровья у оппонента."""
        damage_dealt = (self.base_damage - (self.base_damage * opponent.base_armor / 100))
        opponent.health_points -= damage_dealt
        print(f'{self.character_name} наносит удар по {opponent.character_name} на {damage_dealt:.2f} урона')
        print(f'Очков здоровья осталось {opponent.character_name}: {opponent.health_points:.2f}')

    def recieve_damage(self, opponent) -> None:
        """Рассчитывает полученный урон и отнимает очки здоровья у персонажа."""
        damage_dealt = (opponent.base_damage - (opponent.base_damage * self.base_armor / 100))
        self.health_points -= damage_dealt
        print(f'{opponent.character_name} наносит удар по {self.character_name} на {damage_dealt:.2f} урона')
        print(f'Очков здоровья осталось {self.character_name}: {self.health_points:.2f}')


class Paladin(Character):
    def __init__(self, character_name: str, health_points: int, base_damage: int, base_armor: int) -> None:
        self.character_name = character_name
        self.health_points = health_points * 2
        self.base_damage = base_damage
        self.base_armor = base_armor * 2


class Warrior(Character):
    def __init__(self, character_name: str, health_points: int, base_damage: int, base_armor: int) -> None:
        self.character_name = character_name
        self.health_points = health_points
        self.base_damage = base_damage * 2
        self.base_armor = base_armor


def fantasy_name():
    """Генератор фентези имён для персонажей арены."""
    first = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
             'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
             'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
             'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam', 'She', 'Sheel',
             'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

    second = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
              'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
              'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
              'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
              'wain', 'wan', 'win', 'wise', 'ya']
    return random.choice(first) + random.choice(second)


def create_new_character() -> Character:
    """Генерация персонажа со случайным классом и предметами."""
    base_stats = [20, 5, 0]
    character_name = fantasy_name()
    character = random.choice([
        Character(character_name, *base_stats),
        Paladin(character_name, *base_stats),
        Warrior(character_name, *base_stats)]
    )
    return character


def generate_contenders() -> List[Character]:
    """Генерация списка участников арены."""
    contenders = []
    for contender in range(0, 10):
        contender = create_new_character()
        contenders.append(contender)
    return contenders
