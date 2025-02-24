import time

from boots import Boots
from levels import *

dev_commands = {"1": level_one, "2": level_two, "3": level_three}

def dev_mode(b):
    print("Dev mode activated")
    time.sleep(1.5)
    print("You can now test any level by typing the level number")
    time.sleep(1.5)
    print("Type 'exit' to leave dev mode")

    while True:
        user_input = input("Enter level number: ")
        if user_input == "exit":
            break
        elif user_input in dev_commands:
            dev_commands[user_input](b)
        else:
            print("Invalid input. Please enter a valid level number or exit.")
            time.sleep(1.5)

def main():
    b = Boots()
    flag = level_tutorial(b)
    if flag:
        dev_mode(b)
        
    level_one(b)
    level_two(b)
    level_three(b)

if __name__ == "__main__":
    main()
