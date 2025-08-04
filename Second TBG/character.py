class Character:
    def __init__(self, name, description):
            self.name = name
            self.description = description

    def describe(self):
        print(self.name + " is nearby..")
        print(self.description)

class Player(Character):
    def __init__(self, name, description, disguise_level):
        super().__init__(name, description)
        self.disguise_level = disguise_level

class NPC(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.item = None