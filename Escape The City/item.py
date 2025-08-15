class Item:
    def __init__ (self, name, description, disguise_bonus = 0, price = 0):
        self.name = name
        self.description = description
        self.disguise_bonus = disguise_bonus
        self.price = price

    def describe(self):
        print(f"{self.name}: {self.description}")
        print(f"Adds {self.disguise_bonus} disguise points.")