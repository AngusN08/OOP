import random

from character import Character, Player, Suspect

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