import random
from dataclasses import asdict, dataclass
from typing import ClassVar, List

import pandas as pd

from armory_db import armory


@dataclass()
class Item:  # Things
    name: str
    armor: int
    damage: int
    health: int
    ITEM_INFO: ClassVar[str] = ('Item Name: {name}\n'
                                'Bonus Armor: {armor} %\n'
                                'Bonus Damage: {damage}\n'
                                'Health Bonus: {health}'
                                )

    def show_thing_info(self) -> str:
        """Форматирует информационное сообщение."""
        return self.ITEM_INFO.format(**asdict(self))


class Inventory:
    def __init__(self, items: List[Item]):
        self.items = items

    def show_inventory(self):
        """Форматирует информационное сообщение."""
        item_names = [item.name for item in self.items]
        item_damage = [item.damage for item in self.items]
        item_armor = [item.armor for item in self.items]
        item_health = [item.health for item in self.items]

        data = {
            'Item Name': item_names,
            'Damage': item_damage,
            'Armor': item_armor,
            'Health': item_health
        }
        inventory_info = pd.DataFrame(data=data)
        inventory_info.index += 1
        print(f'Inventory:')
        print(inventory_info)


def generate_item():
    item_name = None
    item_armor = 0
    item_damage = 0
    item_health = 0

    item_type = random.choice(list(armory.keys()))
    if item_type == 'weapons':
        weapon_material, weapon_bonus_dmg = random.choice(
            list(armory[item_type]['weapon_material'].keys())), random.choice(
            list(armory[item_type]['weapon_material'].values()))
        weapon_type, weapon_base_dmg = random.choice(list(armory[item_type]['weapon_type'].keys())), random.choice(
            list(armory[item_type]['weapon_type'].values()))
        item_name = f'{weapon_material} {weapon_type}'
        item_damage = weapon_base_dmg + weapon_bonus_dmg
    elif item_type == 'armor' or item_type == 'shield':
        item_name, item_armor = random.choice(
            list(armory[item_type].keys())), random.choice(
            list(armory[item_type].values()))
    elif item_type == 'trinket':
        item_name, item_armor = random.choice(
            list(armory[item_type].keys())), random.choice(
            list(armory[item_type].values()))
    return Item(name=item_name, armor=item_armor, damage=item_damage, health=item_health)


# @TODO: trinket randomise bonus
