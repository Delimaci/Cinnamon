# main.py

import os
import time
from ai_response import generate_response  # Import AI response function

# ASCII Art for Cinnamon
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

pet_name = "Cinnamon"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print(pet_art)
    print(f"{pet_name}: Hello! Type something to talk to me.")
    print()

    while True:
        # Get user input
        user_input = input("You: ")

        # Check if the user wants to exit
        if user_input.lower() == "exit":
            print(f"{pet_name}: Goodbye! 🐾")
            break
        
        # Generate AI response based on the user's input
        response = generate_response(user_input)  # Call the AI response function

        print(f"{pet_name}: {response}")
        time.sleep(1)  # Pause briefly between messages

if __name__ == "__main__":
    main()
