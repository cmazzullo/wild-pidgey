from Attack import Attack
from monster import Monster


def main():

    mud_blast = Attack(85.0, "earth", "intellectual", "", "")
    tornado_spin = Attack(70.0, "air", "physical", "", "")
    

    mazzullo = Monster("Mazzulo", ["air", "fire"], ["plasma", "solid"], [tornado_spin], 80.0, 50.0, 95.0, 75.0, 75.0, 70.0, 60.0, 60.0 )
    salim = Monster("Salim", ["earth", "water"], ["liquid", "gas", "solid"], [mud_blast], 75.0, 65.0, 75.0, 50.0, 95.0, 70.0, 30.0, 90.0 )

    print mazzullo.name + " hp = " + str(mazzullo.hp)
    print salim.name + " hp = " + str(salim.hp)

    player_1_attack_choice = mazzullo.moveset[0]
    player_2_attack_choice = salim.moveset[0]

    if mazzullo.speed > salim.speed:
        salim.recieve_attack(player_1_attack_choice, mazzullo)
        print salim.name + " hp = " + str(salim.hp)
        mazzullo.recieve_attack(player_2_attack_choice, salim)
        print mazzullo.name + " hp = " + str(mazzullo.hp)
    elif mazzullo.speed < salim.speed:
        mazzullo.recieve_attack(player_2_attack_choice, salim)
        print mazzullo.name + " hp = " + str(mazzullo.hp)
        salim.recieve_attack(player_1_attack_choice, mazzullo)
        print salim.name + " hp = " + str(salim.hp)
    #else
    #handle speed tie case via random 50% chance

if __name__ == '__main__': main()
