from character import *
from room import *
from item import *

#Center of city
sleeping_quarters = Room("Sleeping Quarters")
sleeping_quarters.set_description("a boring grey room where you sleep at night.")

#Just outside city center
markets = Room("Markets")
markets.set_description("a crowded plaza filled with stalls.")

#On the outer rim of the city
slums = Room("Slums")
slums.set_description("the dirtiest and poorest zone in the city. Very dangerous if unprepared.")

#The last step for escape
Wall = Room("The Wall")
Wall.set_description("the barrier keeping citizens in and dangers out.")

sleeping_quarters.link_room(markets, "west")
markets.link_room(slums, "west")
slums.link_room(Wall, "west")
Wall.link_room(slums, "east")
slums.link_room(markets, "east")
markets.link_room(sleeping_quarters, "east")

Markus = Player("Markus", "a civilian who wants to escape the city.", 0)

SleepingQuartersGuard = NPC("Sleeping Quarters Guard", "An observant guard standing at the entrance to your dorm.")
SleepingQuartersGuard.set_conversation("Move along, citizen — no loitering near the entrance.")
sleeping_quarters.set_character(SleepingQuartersGuard)

Jericho = NPC("Jericho", "A wise and mysterious man who dwells in the shadows.")
Jericho.set_conversation("The market thrives on what’s seen—and on what’s hidden in plain sight")
markets.set_character(Jericho)

Clara = NPC("Clara", "The elder in the slums, overflowing with useful knowledge")
Clara.set_conversation("The slums will eat you alive if you don't know where to step.")
slums.set_character(Clara)

The_Gatekeeper = NPC("The Gatekeeper", "An unblinking sentinel, recording your every move.")
The_Gatekeeper.set_conversation("Every step you take is logged; don't think the gate will forget you.")
Wall.set_character(The_Gatekeeper)

fake_id = Item("Fake ID", "A forged identification card.", disguise_bonus = 2, price = 5)
stolen_uniform = Item("Stolen Guard Uniform", "A guard's uniform taken from the slums.", disguise_bonus = 4, price = 10)
old_watch = Item("Old Watch", "A rusty old watch, could hold some value.", price = 10)
sleeping_quarters.set_item(old_watch)

scrap_metal = Item("Scrap Metal", "A piece of scrap metal, you might be able to pawn it.", price = 5)
slums.set_item(scrap_metal)


Jericho.set_shop_items([fake_id])
Clara.stealable_item = stolen_uniform

Markus.describe()
current_room = sleeping_quarters
game_over = False


while not game_over:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command in ["east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            result = inhabitant.talk(Markus)
            
            if inhabitant == The_Gatekeeper and Markus.disguise_level >= 6:
                print("The Gatekeeper scans you... and lets you through the gate.")
                print("You slip past the Wall into freedom.")
                print("YOU WIN!")
                game_over = True
                break
            
            elif inhabitant == The_Gatekeeper and Markus.money >= 15:
                print("The Gatekeeper eyes your credits and silently accepts your bribe.")
                print("He steps aside, and you pass through the gate into freedom.")
                print("YOU WIN (but at a price)!")
                Markus.money -= 15
                game_over = True
                break
            
            if result == "discovered":
                print("You've been caught! Guards swarm in and drag you away.")
                print("Game Over.")
                game_over = True
                break

    elif command.startswith("buy "):
        if inhabitant and inhabitant.shop_items:
            parts = command.split(" ")
            if len(parts) > 1 and parts[1].isdigit():
                choice = int(parts[1])
                inhabitant.sell_item(Markus, choice)
            else:
                print("Please enter the number of the item you want to buy")
        else:
            print("There's nothing to buy here.")

    elif command == "sell":
        if Markus.inventory:
            print("\n Your inventory:")
            for idx, item in enumerate(Markus.inventory, start=1):
                print(f"{idx}. {item.name} - {item.price} credits")
            choice = input("Enter the number of the item you want to sell: ")
            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= len(Markus.inventory):
                    item_name = Markus.inventory[choice_num - 1].name
                    Jericho.buy_from_player(Markus, item_name)
                else:
                    print("Invalid choice.")
            else:
                print("Please enter a valid number.")
        else:
            print("You have nothing to sell.")

    elif command == "steal":
        if inhabitant and inhabitant.stealable_item:
            inhabitant.steal_from(Markus)
        else:
            print("There's nothing to steal here.")

    elif command == "take":
        item = current_room.get_item()
        if item is not None:
            Markus.pick_up(item)
            current_room.set_item(None)
            print(f"You pick up the {item.name}.")
        else:
            print("There's nothing to take here.")


    elif command == "status":
        print(f"Disguise Level: {Markus.disguise_level}")
        print(f"Money: {Markus.money} credits")
        if Markus.inventory:
            print("Inventory:")
            for item in Markus.inventory:
                print(f"- {item.name}: {item.description} (Disguise +{item.disguise_bonus}, {item.price} credits)")
        else:
            print("Inventory is empty.")

    elif command == "help":
        print("Available commands:")
        print("- east / west: Move between rooms")
        print("- talk: Talk to the character in the room")
        print("- buy <number>: Buy an item from a shopkeeper")
        print("- sell: Sell an item to Jericho")
        print("- steal: Attempt to steal from the NPC")
        print("- take: Pick up an item in the room")
        print("- status: View disguise level, money, and inventory")
        print("- help: Show this help message")