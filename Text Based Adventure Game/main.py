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

current_cave = cavern
while True:
    print("\n")
    current_cave.get_details()
    command = input("> ")
    current_cave = current_cave.move(command)