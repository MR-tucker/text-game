# Text based 10,000 dice game, where num of npc opponents can be chosen,
# rolls are random, and player can select die or dice to keep/ re-roll
import time, random

def show_title():
    # display a title/header
    # I noticed this lines up perfectly in my code editor but mis-aligned when viewed on gitHub
    print("""
    ---------------------------------------------------------------------------------------------------------------------------------------------------
    |           O                         OOO                             OOO                              OOO                             OOO           |
    |        OO                      O         O                       O         O                        O         O                       O         O        |
    |     O   O                   O               O                 O               O                  O               O                 O               O     |
    |           O                   O               O                 O               O                  O               O                 O               O     |
    |           O                   O               O                 O               O                  O               O                 O               O     |
    |           O                      O         O          /            O         O                        O         O                       O         O        |
    |     OOOOO                   OOO           /                 OOO                              OOO                             OOO           |
    ---------------------------------------------------------------------------------------------------------------------------------------------------
    """)
    time.sleep(2)
    print("""Welcome to a text based game of 10,000!
    Lets get started!""")


num_of_opponents = 0
opponent_names = []
def handle_player_and_opponent_assignment():
    #handles input to determine the amount of opponents
    global num_of_opponents
    opponent_name_choices = ["Alan", "Jack", "Jim", "Adam", "Rowan", "Roxy", "Alice", "Sarah", "Carol", "Beatrix"]
    try_again = True
    while try_again:
        num_of_opponents = input("Enter how many opponents you'd like to face. (1-5):")
        if num_of_opponents == "1" or num_of_opponents == "2" or num_of_opponents == "3"\
            or num_of_opponents == "4" or num_of_opponents == "5":
            num_of_opponents = int(num_of_opponents)
            time.sleep(1)
            try_again = False
        else:
            print("Only 1 - 5 is acceptable here! Try again!")
            try_again = True
            time.sleep(1)

        #assign opponent names
        for i in range(num_of_opponents):
            name = random.choice(opponent_name_choices)
            #prevents opponents from having the same name
            while name in opponent_names:
                name = random.choice(opponent_name_choices)
            opponent_names.append(name)
        print(opponent_names)


show_title()
handle_player_and_opponent_assignment()