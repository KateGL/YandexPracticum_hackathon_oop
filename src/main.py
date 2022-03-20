from arena import Arena, start_single_fight
from character import generate_contenders


def announce_fighter(color, participant, inventory):
    """Анонс участников битвы. Печатает информация о персонажах в консоль."""
    print('---------------------------------------')
    print(f"{color} fighter:")
    participant.show_character_stats()
    participant.show_character_inventory(inventory)
    print('---------------------------------------')


def main(arena: Arena) -> None:
    participant_1, participant_2 = arena.get_participants()

    participant_1_inv, participant_2_inv = participant_1.generate_inventory(), participant_2.generate_inventory()
    announce_fighter('Blue', participant_1, participant_1_inv)
    announce_fighter('Red', participant_2, participant_2_inv)

    start_single_fight(participant_1, participant_2)


if __name__ == '__main__':
    contenders = generate_contenders()
    arena = Arena(contenders)
    main(arena)
