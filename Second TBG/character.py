import random

class Character:
    def __init__ (self, name, is_alive):
        self.name = name
        self.is_alive = True

    def speak(self):
        return f"{self.name} has nothing to say."

class Player(Character):
    def __init__ (self, name):
        super().__init__(name)
        self.notes = {}

    def interview(self, suspect):
        print(f"You approach {suspect.name}...")
        print(suspect.speak())

class Suspect(Character):
    def __init__ (self, name, dialogue_lines, is_killer=False):
        super().__init__(name)
        self.dialogue_lines = dialogue_lines
        self.is_killer = is_killer

    def speak(self):
        if self.is_killer:
            return random.choice([
                "I was outta town that night.",
                "I think you're out of line.",
                "Maybe YOU'RE the killer"
            ])
        else:
            return random.choice(self.dialogue_lines)