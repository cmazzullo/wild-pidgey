from random import randint
from Attack import Attack

class Monster:
    """A framework for the monsters in States of Matter"""

    # creates a monster with certain stats
    # eventually, stats should be stored in a database rather than passed by parameter
    # would look like: def __init__(self, KEY) where key is the name of the monster
    def __init__(self, name, types, elements, moveset,vitality, speed, phys_strength, spirit_strength, int_strength, phys_endur, spirit_endur, int_endur):
        self.name               = name
        self.types              = types
        self.elements           = elements
        self.moveset            = moveset

        #used to save base stats
        self.vitality 		= vitality
        self.speed 		= speed 
        self.phys_strength 	= phys_strength 
        self.spirit_strength	= spirit_strength
        self.int_strength 	= int_strength
        self.phys_endur 	= phys_endur
        self.spirit_endur 	= spirit_endur
        self.int_endur 		= int_endur

        #used to save temporary stats per battle
        self.hp = vitality
        self.current_state = elements[0]

    # returns total outgoing damage for a given attack - not implemented
    #	Physical Strength ===> Spiritual Endurance
    #	Spritual Strength ===> Intellectual Endurance
    #	Intellectual Strength ===> Physical Endurance
    #
    #	damage =  health - ((strength-endurance)*element*state*) 
    #	.05% chance of critical hit which will double damage
    #
    #	---> beats
    #	~~~> doesnt affect
    #	///> resisted by
    #
    #	Water ---> Fire ---> Air ---> Earth ---> Water
    #	Light <---> Dark
    #	Fire ---> Dark
    #	Fire ~~~> Light
    #	Dark ///> Fire
    #	Fire ///> Water
    #	Air ///> Earth
    #	Earth ///> Water
    #
    #	Plasma <---> Liquid
    #	Plasma ///> Gas
    #	Liquid ///> Solid
    #
    def recieve_attack(self, attack, enemy_monster):
        if attack.attack_attribute == "physical":
            attribute_damage = (enemy_monster.phys_strength - self.spirit_endur)/enemy_monster.phys_strength
        elif attack.attack_attribute == "spritual":
            attribute_damage = (enemy_monster.spirit_strength - self.int_endur)/enemy_monster.spirit_strength
        elif attack.attack_attribute == "intellectual":
            attribute_damage = (enemy_monster.int_strength - self.phys_endur)/enemy_monster.int_strength

        #avoid negatives
        if attribute_damage < 0.0:
            attribute_damage = 0.0
        else:
            attribute_damage = attack.base_damage*attribute_damage
        
        type_damage_0 = 1.0
        if (attack.attack_type == "fire" and self.types[0] == "light"):
            type_damage_0 = 0.0
        elif (attack.attack_type == "dark" and self.types[0] == "fire") or (attack.attack_type == "fire" and self.types[0] == "water") or (attack.attack_type == "air" and self.types[0] == "earth") or (attack.attack_type == "earth" and self.types[0] == "water"):
            type_damage_0 = 0.5
        elif (attack.attack_type == "water" and self.types[0] == "fire") or (attack.attack_type == "fire" and self.types[0] == "air") or (attack.attack_type == "air" and self.types[0] == "earth") or (attack.attack_type == "earth" and self.types[0] == "water") or (attack.attack_type == "light" and self.types[0] == "dark") or (attack.attack_type == "dark" and self.types[0] == "light") or (attack.attack_type == "fire" and self.types[0] == "dark"):
            type_damage_0 = 2.0



        type_damage_1 = 1.0
        #check to see if Monster has a second type
        if self.types[1]:
            if (attack.attack_type == "fire" and self.types[1] == "light"):
                type_damage_1 = 0.0
            elif (attack.attack_type == "dark" and self.types[1] == "fire") or (attack.attack_type == "fire" and self.types[1] == "water") or (attack.attack_type == "air" and self.types[1] == "earth") or (attack.attack_type == "earth" and self.types[1] == "water"):
                type_damage_1 = 0.5
            elif (attack.attack_type == "water" and self.types[1] == "fire") or (attack.attack_type == "fire" and self.types[1] == "air") or (attack.attack_type == "air" and self.types[1] == "earth") or (attack.attack_type == "earth" and self.types[1] == "water") or (attack.attack_type == "light" and self.types[1] == "dark") or (attack.attack_type == "dark" and self.types[1] == "light") or (attack.attack_type == "fire" and self.types[1] == "dark"):
                type_damage_1 = 2.0

        state_damage = 1.0
        enemy_state = enemy_monster.current_state
        if (enemy_state == "plasma" and self.current_state == "liquid") or (enemy_state == "liquid" and self.current_state == "plasma"):
            state_damage = 2.0
        elif (enemy_state == "plasma" and self.current_state == "gas") or (enemy_state == "liquid" and self.current_state == "solid"):
            state_damage = 0.5

        crit = randint(0,100)
        crit_damage = 1.0
        if(crit <= 4):
            crit_damage = 2.0
                
        total_damage = attribute_damage*type_damage_0*type_damage_1*state_damage*crit_damage
        #print "total damage = " + str(total_damage)
        self.hp = self.hp - total_damage


    def str(self):
        print 'Name:', self.name, 'Types:', self.types, 'Vitality:', self.vitality,'Speed:', self.speed, 'Physical strength:', self.phys_strength,'Spirit Strength:', self.spirit_strength, 'Intellectual Strength:',self.int_strength, 'Pysical endurance:', self.phys_endur, 'Spiritual Endurance:', self.spirit_endur, 'Intellectual Endurance:',self.int_endur

