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
The_Wall = Room("The Wall")
The_Wall.set_description("The barrier keeping citizens in and dangers out.")

sleeping_quarters.link_room(markets, "west")
markets.link_room(slums, "west")
