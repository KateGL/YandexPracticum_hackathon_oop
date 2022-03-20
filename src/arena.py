import random
from typing import List, Tuple

from character import Character


class Arena:
    """Базовый класс Арены."""
    def __init__(self, contenders: List[Character]):
        self.contenders = contenders

    def get_participants(self) -> Tuple[Character, Character]:
        """Выбор 2х бойцов случайным образом."""
        character_1 = random.choice(self.contenders)
        self.contenders.remove(character_1)
        character_2 = random.choice(self.contenders)
        self.contenders.remove(character_2)
        return character_1, character_2


def start_single_fight(character_1: Character, character_2: Character) -> None:
    """Начинает поединок между двумя бойцами и выводит победителя."""
    while character_1.is_alive() or character_2.is_alive():
        char_1_initiative, char_2_initiative = character_1.initiative(), character_2.initiative()
        if char_1_initiative > char_2_initiative:
            character_1.attack(character_2)
        else:
            character_1.recieve_damage(character_2)
        if character_1.is_alive() is False:
            return print(f'{character_2.character_name} победил!')
        elif character_2.is_alive() is False:
            return print(f'{character_1.character_name} победил!')
