class Player:
    def __init__(self, location, disguise_level, inventory=None):
        if inventory is None:
            inventory = []
            self.location = location
            self.disguise_level = disguise_level
            self.inventory = inventory

