import random
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
    def __init__(self, name, description, disguise_level = 0, money = 10):
        super().__init__(name, description)
        self.disguise_level = disguise_level
        self.money = money
        self.inventory = []

    def describe(self):
        print(self.name + " is " + self.description)
        print("You must help him escape.")

    def increase_disguise(self, amount):
        self.disguise_level += amount
        print(f"Your disguise level is now {self.disguise_level}.")

    def decrease_disguise(self, amount):
        self.disguise_level = max(0, self.disguise_level - amount)
        print(f"Your disguise level is now {self.disguise_level}.")

    def pick_up(self, item):
        self.inventory.append(item)
        self.disguise_level += item.disguise_bonus
        print(f"You picked up {item.name}. Disguise level is now {self.disguise_level}.")

    def show_inventory(self):
        if not self.inventory:
            print("You have no items.")
        else:
            for item in self.inventory:
                item.describe()

    def change_money(self, amount):
        self.money += amount
        print(f"You now have {self.money} credits.")


class NPC(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.shop_items = []
        self.stealable_item = None

    def steal_from(self, player):
        if not self.stealable_item:
            print(f"{self.name} has nothing worth stealing.")
            return
            
        if random.random() < 0.5:
            print(f"As you try to grab it, {self.name} notices!")    
            loss = 2
            player.money = max(0, player.money - loss)
            print(f"You lose {loss} credits running away. You now have {player.money} credits.")
        else:
            print(f"You snatch the {self.stealable_item.name} from {self.name}!")
            player.inventory.append(self.stealable_item)
            player.disguise_level += self.stealable_item.disguise_bonus
            print(f"Disguise level is now {player.disguise_level}.")
            self.stealable_item = None
    
    def set_shop_items(self, items):
        self.shop_items = items

    def talk(self, player):
        if self.shop_items:
            print(f"{self.name}: Interested in buying something>")
            for idx, item in enumerate(self.shop_items, start = 1):
                print(f"{idx}. {item.name} - {item.disguise_bonus} disguise bonus - {item.price} credits")

        else:
            print(f"{self.name} says: '{self.conversation}'")

    def sell_item(self, player, item_number):
        if 1 <= item_number <= len(self.shop_items):
            item = self.shop_items[item_number - 1]
            if player.money >= item.price:
                player.money -= item.price
                player.inventory.append(item)
                player.disguise_level += item.disguise_bonus
                print(f"You bought {item.name}! Disguise level is now {player.disguise_level}")
            else:
                print("You don't have enough credits for that.")
        else:
            print("That item doesn't exist.")