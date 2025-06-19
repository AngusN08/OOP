class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickup(self):
        return f"You picked up {self.name}."

    def give(self):
        return f"You gave {self.name}."

    