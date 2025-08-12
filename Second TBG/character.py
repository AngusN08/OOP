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

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)

class Player(Character):
    def __init__(self, name, description, disguise_level):
        super().__init__(name, description)
        self.disguise_level = int(disguise_level)

    def describe(self):
        print(self.name + " is " + self.description)
        print("You must help him escape.")

class NPC(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.item = None