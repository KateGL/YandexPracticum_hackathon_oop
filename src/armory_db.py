import random
"""Оружейная."""

weapon_material = {'Iron': 1, 'Steel': 2, 'Ebony': 4}
weapon_type = {
    'Axe': 3,
    'Club': 3,
    'Sword': 3,
    'Rapier': 2,
    'Dagger': 2,
    'Spear': 3,
}

armor_type = {
    'Light Armor': 4,
    'Medium Armor': 7,
    'Heavy Armor': 10
}

shield_type = {
    'Small Shield': 2,
    'Medium Shield': 3,
    'Greatshield': 5
}

trinket = {
    'Talisman': random.randint(1, 5),
    'Ring': random.randint(1, 5)
}

armory = {
    'weapons': {
        'weapon_type': weapon_type,
        'weapon_material': weapon_material
    },
    'armor': armor_type,
    'shield': shield_type,
    'trinket': trinket,
}
