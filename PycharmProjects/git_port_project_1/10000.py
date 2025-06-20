# Text based 10,000 dice game, where num of npc opponents can be chosen,
# rolls are random, and player can select die or dice to keep/ re-roll
import time

def show_title():
    #display a title/header
    #i noticed this lines up perfectly in my code editor but mis-aligned when viewed on github
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


show_title()