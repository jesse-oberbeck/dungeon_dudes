import random

def roll_dice(num_die):
    dice = []
    for die in range(num_die):
        dice.append(random.randrange(1,6))
    return dice

def initiative(hero, foe):
    hero_max = max(roll_dice(hero.die))
    foe_max = max(roll_dice(foe.die))
    if hero_max >= foe_max:
        return 1
    else:
        return 0

def combat(attacker, defender):
    attacker_max = max(roll_dice(attacker.die))
    defender_max = max(roll_dice(defender.die))
    if attacker_max > defender_max:
        defender.hp -= 1
        print("Attack hits!\n")
    elif attacker_max == defender_max and isinstance(attacker, Hero):
        defender.hp -= 1
        print("Attack hits! (Hero advantage)\n")
    else:
        print("Defended!\n")

    if defender.hp == 0 and isinstance(defender, Hero):
        print("You Died.\n")
        return 1

    elif defender.hp == 0:
        print("Victory Achieved.\n")
        return 2


class Hero():
    def __init__(self):
        self.die = 3
        self.hp = 10

class Monster():
    types = {"rat": 1, "bat": 1, "ghoul": 2, "zombie": 2, "bandit": 2, "golem": 3}
    def __init__(self):
        self.type = random.choice(   list(self.types.keys())   )
        self.hp = self.types[self.type]
        self.die = random.randrange(1, 3)
        
class Room():
    types = {"corridor": 1, "kitchen": 2, "dungeon": 5, "hold": 10}
    def __init__(self):
        self.type = random.choice(   list(self.types.keys())   )
        print(self.type)
        self.monsters = [Monster() for monster in range(random.randint(1, self.types[self.type]))]

class Dungeon():
    def __init__(self):
        num_rooms = random.randrange(6, 10)
        self.rooms = [Room() for room in range(num_rooms)]

def move(dungeon):
    dungeon.rooms.pop(0)

def printInventory(hero, ignore):
    pass

def heroHP(character, ignore):
    print(character.hp)

def foeHP(ignore, foe):
    print(foe.hp)

def menu(hero, foe, dungeon):
    options = dict([(str('1'), printInventory), (str('2'), move), (str('3'), heroHP), (str('4'), foeHP), (str('5'), combat)])
    print("1. Check inventory.")
    print("2. Next room.")
    print("3. Check HP.")
    print("4. Check enemy HP.")
    print("5. Attack.")
    selection = input(">>: ")
    if selection == str('2'):
        move(dungeon)
    else:
        options[selection](hero, foe)



def game(hero, dungeon):
    foe = dungeon.rooms[0].monsters[0]
    order = initiative(hero, foe)
    while(1):
        if not dungeon.rooms[0].monsters:
            print("Room is empty...")
            menu(hero, foe, dungeon)
        elif order == 0:
            print("FOE HP: ", foe.hp)
            print(foe.type, "attacks!")
            combat(foe, hero)
            menu(hero, foe, dungeon)
            if foe.hp == 0:
                dungeon.rooms[0].monsters.pop(0)
                if dungeon.rooms[0].monsters:
                    foe = dungeon.rooms[0].monsters[0]
            else:
                print(foe.type, "attacks!")
                combat(foe, hero)
#            if not dungeon.rooms[0].monsters:
#                print("pop room")
#                dungeon.rooms.pop(0)
            if not dungeon.rooms:
                print("YOU'VE WON!")
                return

        elif order == 1:
            print("FOE HP: ", foe.hp)
            menu(hero, foe, dungeon)
            if foe.hp == 0:
                dungeon.rooms[0].monsters.pop(0)
                if dungeon.rooms[0].monsters:
                    foe = dungeon.rooms[0].monsters[0]
            else:
                print(foe.type, "attacks!")
                combat(foe, hero)
#            if not dungeon.rooms[0].monsters:
#                print("pop room")
#                dungeon.rooms.pop(0)
            if not dungeon.rooms:
                print("YOU'VE WON!")
                return


#player = Hero()
#testMon = Monster()
#print(testMon.type, testMon.hp)
#check = combat(player, testMon)
#if check == 1:
#    return
#if check == 2:

#dungeon = Dungeon()
#room = dungeon.rooms[0]
#for monster in room.monsters:
#    print(monster.type)
#menu(player, room.monsters[0])

player = Hero()
dungeon = Dungeon()
game(player, dungeon)







