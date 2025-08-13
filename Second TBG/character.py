class Character:
    def __init__(self, name, description):
            self.name = name
            self.description = description
            self.conversation = None
    def describe(self):
        print(self.name + " is nearby..")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self, player):
        if player.disguise_level >= 5:
            print(f"{self.name} looks at you suspiciously but lets you pass.")
        elif player.disguise_level >= 2:
            print(f"{self.name} narrows their eyes but says: '{self.conversation}'")
        else:
            print(f"{self.name} immediately notices you and raises the alarm!")

class Player(Character):
    def __init__(self, name, description, disguise_level = 0):
        super().__init__(name, description)
        self.disguise_level = disguise_level

    def describe(self):
        print(self.name + " is " + self.description)
        print("You must help him escape.")

    def increase_disguise(self, amount):
        self.disguise_level += amount
        print(f"Your disguise level is now {self.disguise_level}.")

    def decrease_disguise(self, amount):
        self.disguise_level = max(0, self.disguise_level - amount)
        print(f"Your disguise level is now {self.disguise_level}.")

class NPC(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.item = None