import Engine

# prompts for action choice
# returns the name of the choice
def choose_action(player):
    print str.format("{}'s turn:",player.name)
    s = raw_input('Do you want to:\n1. Attack\n2. Switch\n3. Change State\n')
    if s == '1':
        return 'attack'
    elif s == '2':
        return 'switch'
    elif s == '3':
        return 'state'

# prompts for attack choice
# returns attack
def choose_attack(player, attacks):
    c = 1
    print 'Which attack:\n'
    for a in attacks:
        print (str(c) + '. ' + a.name)
        c += 1
    s = raw_input()
    if s == '1':
        return attacks[0]
    elif s == '2':
        return attacks[1]
    elif s == '3':
        return attacks[2]
    elif s == '4':
        return attacks[3]

# prompts for lead choice
# returns lead
def choose_lead(player, monsters):
    c = 1
    print 'Which lead:\n'
    for m in monsters:
        print (str(c) + '. ' + m.name)
        c += 1
    s = raw_input()
    if s == '1':
        return monsters[0]
    elif s == '2':
        return monsters[1]
    elif s == '3':
        return monsters[2]
    elif s == '4':
        return monsters[3]

# prompts for state choice
# returns state
def choose_state(player):
    print 'Which state:\n1. Solid\n2. Liquid\n3. Gas\n4. Plasma\n'
    s = raw_input()
    if s == '1':
        return 'solid'
    elif s == '2':
        return 'liquid'
    elif s == '3':
        return 'gas'
    elif s == '4':
        return 'plasma'
