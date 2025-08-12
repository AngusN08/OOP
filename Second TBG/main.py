from character import *
from room import Room

#Center of city
sleeping_quarters = Room("Sleeping Quarters")
sleeping_quarters.set_description("A boring grey room where you sleep at night.")

#Just outside city center
markets = Room("Markets")
markets.set_description("A crowded plaza filled with stalls.")

#On the outer rim of the city
slums = Room("Slums")
slums.set_description("The dirtiest and poorest zone in the city. Very dangerous if unprepared.")

#The last step for escape
Wall = Room("The Wall")
Wall.set_description("The barrier keeping citizens in and dangers out.")

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


Markus.describe()
current_room = sleeping_quarters
discovered = False
while discovered == False:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    # item = current_room.get_item()
    # if item is not None:
    #     item.describe()
    command = input("> ")
    if command in ["east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()