from warriors import *
from random import choice


swadian_spearman_1 = Spearman('Swadian spearman 1')
swadian_spearman_2 = Spearman('Swadian spearman 2')
swadian_spearman_3 = Spearman('Swadian spearman 3')
swadian_spearman_4 = Spearman('Swadian spearman 4')
swadian_infantryman_1 = Infantryman('Swadian infantryman 1')
swadian_infantryman_2 = Infantryman('Swadian infantryman 2')
swadian_infantryman_3 = Infantryman('Swadian infantryman 3')
swadian_infantryman_4 = Infantryman('Swadian infantryman 4')
swadian_knight_1 = Knight('Swadian knight 1')
swadian_knight_2 = Knight('Swadian knight 2')

kingdom_of_swadia = [swadian_spearman_1,
                     swadian_spearman_2,
                     swadian_spearman_3,
                     swadian_spearman_4,
                     swadian_infantryman_1,
                     swadian_infantryman_2,
                     swadian_infantryman_3,
                     swadian_infantryman_4,
                     swadian_knight_1,
                     swadian_knight_2]

vaegir_spearman_1 = Spearman('Vaegir spearman 1')
vaegir_spearman_2 = Spearman('Vaegir spearman 2')
vaegir_spearman_3 = Spearman('Vaegir spearman 3')
vaegir_spearman_4 = Spearman('Vaegir spearman 4')
vaegir_infantryman_1 = Infantryman('Vaegir infantryman 1')
vaegir_infantryman_2 = Infantryman('Vaegir infantryman 2')
vaegir_infantryman_3 = Infantryman('Vaegir infantryman 3')
vaegir_infantryman_4 = Infantryman('Vaegir infantryman 4')
vaegir_knight_1 = Knight('Vaegir knight 1')
vaegir_knight_2 = Knight('Vaegir knight 2')

kingdom_of_vaegirs = [vaegir_spearman_1,
                      vaegir_spearman_2,
                      vaegir_spearman_3,
                      vaegir_spearman_4,
                      vaegir_infantryman_1,
                      vaegir_infantryman_2,
                      vaegir_infantryman_3,
                      vaegir_infantryman_4,
                      vaegir_knight_1,
                      vaegir_knight_2]


def battle():
    fight = 0
    print('The battle begins!')
    while len(kingdom_of_swadia) > 0 and len(kingdom_of_vaegirs) > 0:
        swadian = choice(kingdom_of_swadia)
        vaegir = choice(kingdom_of_vaegirs)
        fight += 1
        if fight % 2 == 1:
            swadian.go_fight(vaegir)
        else:
            vaegir.go_fight(swadian)
        if swadian.get_health() <= 0:
            kingdom_of_swadia.remove(swadian)
        elif vaegir.get_health() <= 0:
            kingdom_of_vaegirs.remove(vaegir)
    if len(kingdom_of_vaegirs) == 0:
        print('Kingdom of Swadia wins the battle!')
        print('Remaining warriors:')
        for warrior in kingdom_of_swadia:
            print(warrior.name, 'with', warrior.health, 'health left.')
    else:
        print('Kingdom of Vaegirs wins the battle!')
        print('Remaining warriors:')
        for warrior in kingdom_of_vaegirs:
            print(warrior.name, 'with', warrior.health, 'health left.')


battle()
