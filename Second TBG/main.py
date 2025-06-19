import random

from character import Character, Player, Suspect
# class Character:
#     def __init__ (self, name):
#         self.name = name
#         self.is_alive = True

#     def speak(self):
#         return f"{self.name} has nothing to say."

# class Player(Character):
#     def __init__ (self, name):
#         super().__init__(name)
#         self.notes = {}

#     def interview(self, suspect):
#         print(f"You approach {suspect.name}...")
#         print(suspect.speak())

# class Suspect(Character):
#     def __init__ (self, name, dialogue_lines, is_killer=False):
#         super().__init__(name)
#         self.dialogue_lines = dialogue_lines
#         self.is_killer = is_killer

#     def speak(self):
#         if self.is_killer:
#             return random.choice([
#                 "I was outta town that night.",
#                 "I think you're out of line.",
#                 "Maybe YOU'RE the killer"
#             ])
#         else:
#             return random.choice(self.dialogue_lines)

def main():
    player = Player("Detective")

    suspects = [
        Suspect("Joseph", ["I been down the pub all day.", "You should ask Dianne, she seemed off today.", "Are you accusing me of murder?!"]),
        Suspect("Dianne", ["I was sleeping Sir, okay?", "Your son Flynn was acting weird.", "Why does nobody trust me."]),
        Suspect("Flynn", ["I swear Dad I didn't see or hear anything!", "Joseph was downing drinks faster than you'll ever see."])
    ]

    killer_index = random.randint(0, len(suspects) - 1)
    suspects[killer_index].is_killer = True
    print(f"[DEBUG] The killer is {suspects[killer_index].name}")

    print("Midnight Murder begins.")
    print("You can talk to any of the suspects.\n")

    while True:
        print("\n Who do you want to interview?")
        for i, suspect in enumerate(suspects):
            print(f"{i + 1}. {suspects[i].name}")
        
        choice = input("> ")

        if choice.isdigit():
            choice_num = int(choice)
            if choice_num == 0:
                print("\nExiting the game. Goodbye.")
                break
            elif 1 <= choice_num <= len(suspects):
                player.interview(suspects[choice_num - 1])
            else:
                print("Please choose a number from the list.")
        else:
            print("Please enter a number only.")

if __name__ == "__main__":
    main()