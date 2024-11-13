import os
import time
import random
import sys

pet_art = '''
     ⢀⡀         
    ⢰⣿⡿⠗ ⠠⠄⡀    
    ⡜⢁⣀⡀   ⠈⠑⢶⣶⡄
⢀⣶⣦⣸⠈⢿⣟⡇  ⣀⣀ ⠘⡿⠃
 ⢿⣿⣿⣄⠒ ⠠⢶⡂⢫⣿⢇⢀⠃ 
 ⠈⢿⡿⣿⣿⣶⣤⣀⣄⣀⣂⡠⠊  
   ⡇  ⠉⠙⠛⠿⣿⣿⣧   
   ⣿      ⠘⣿⣿⡇  
   ⣿⣧⡤⠄⣀⣀⣀⣴⡟⠿⠃  
   ⢻⣿⣿⠉⠉⢹⣿⣿⠁    
    ⠉⠁   ⠉⠁     
'''


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def make_pet_talk(last_message=None):
    responses = [
        "Hello there! 🐾",
        "I love snacks! 🍪",
        "Did you hear that? 🐱",
        "I’m a cute pet! 😺",
        "Play with me! 🎮"
    ]

    message = random.choice(responses)
    while message == last_message:
        message = random.choice(responses)

    return message


def interact_with_pet():
    options = {
        "1": "Feed the pet 🍲",
        "2": "Play with the pet 🎾",
        "3": "Pet the pet 🐾",
        "4": "Let it sleep 😴",
        "5": "Exit 🛑"
    }
    print("Choose an action:")
    for key, action in options.items():
        print(f"{key}. {action}")
    return options.get(input("Enter a choice: "), "Invalid")


pet_name = "Cinnamon"
pet_mood = "happy"

def adjust_mood(action):
    global pet_mood

    if action == "Feed the pet 🍲":
        pet_mood =  "More! 😡"
    elif action == "Play with the pet 🎾":
        pet_mood = "You're so slow! 😬"
    elif action == "Pet the pet 🐾":
        pet_mood = "Bad"
    elif action == "Let it sleep 😴":
        pet_mood = "I'm not tired 🥱"
    else:
        sys.exit()


    return (f"{pet_name}: {pet_mood}")


def main():
    clear_screen()
    print(pet_art)

    last_message = None

    while True:
        print(f"Current mood: {pet_mood}")

        message = make_pet_talk(last_message)
        print(message)
        last_message = message

        action = interact_with_pet()
        if action == "Invalid":
            print("Please choose a valid option.")
        elif action == "5":
            print("Goodbye! 🐾")
            break  # Exit the loop and end the program
        else:
            new_mood = adjust_mood(action)
            print(f"{new_mood}")

        time.sleep(2)
        clear_screen()
        print(pet_art)


if __name__ == "__main__":
    main()
