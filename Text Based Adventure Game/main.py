from character import Character
from character import Enemy, Friend
from cave import Cave

cavern = Cave("cavern")
cavern.set_description("a dank and dirty cave")

dungeon = Cave("dungeon")
dungeon.set_description("a large cave with a crack")

grotto = Cave("grotto")
grotto.set_description("a small cave with ancient graffiti")

dungeon.link_cave(grotto, "west")
dungeon.link_cave(cavern, "north")
cavern.link_cave(dungeon, "south")
grotto.link_cave(dungeon, "east")

harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry...Hanggrry")
harry.set_weakness("vegemite")
dungeon.set_character(harry)
josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday.")
grotto.set_character(josephine)

current_cave = cavern
dead = False
while dead == False:
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Bravo, hero you won the fight!")
                current_cave.set_character(None)
            else:
                print("Scurry home, you lost the fight.")
                print("That's the end of the game")
                dead = True
        else:
            print("There is no one here to fight with")

    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if i were you...")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat:(")

    elif command == "shake":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.shake()
        else:
            print("There is no one here to shake hands with:(")