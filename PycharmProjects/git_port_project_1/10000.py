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


players_name = ""
num_of_opponents = 0
opponent_names = []
all_players_names = []
all_players = []
def handle_player_and_opponent_assignment():
    #handles input to determine the amount of opponents
    global num_of_opponents, players_name
    opponent_name_choices = ["Alan", "Jack", "Jim", "Adam", "Rowan", "Roxy", "Alice", "Sarah", "Carol", "Beatrix"]
    try_again = True
    valid_player_name = False
    while try_again:
        num_of_opponents = input("Enter how many opponents you'd like to face. (1-5): ")
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
        if not try_again:
            for i in range(num_of_opponents):
                name = random.choice(opponent_name_choices)
                #prevents opponents from having the same name
                while name in opponent_names:
                    name = random.choice(opponent_name_choices)
                opponent_names.append(name)

            time.sleep(1)
            print(f"You will face {num_of_opponents} opponents and their names are:")
            time.sleep(1)
            for name in opponent_names:
                print(name)
                time.sleep(.5)
            time.sleep(1)

            #get the players desired name
            while not valid_player_name:
                players_name = input("Now enter your name: ")
                if players_name == "":
                    print("At least enter something here to continue!")
                    time.sleep(1)
                    valid_player_name = False
                else:
                    valid_player_name = True
                    all_players_names.append(players_name)
                    for name in opponent_names:
                        all_players_names.append(name)

                    #after a valid name is selected create a class of every player
                    for player in all_players_names:
                        player_class = Player(player)
                        all_players.append(player_class)

rolls_first = ""

dice = [[
    ".==========.",
    "|                      |",
    "|          O         |",
    "|                      |",
    "°==========°"],
[
    ".==========.",
    "|      O             |",
    "|                      |",
    "|              O     |",
    "°==========°"],
[
    ".==========.",
    "|      O             |",
    "|          O         |",
    "|              O     |",
    "°==========°"],
[
    ".==========.",
    "|      O     O     |",
    "|                      |",
    "|      O     O     |",
    "°==========°"],
[
    ".==========.",
    "|      O     O     |",
    "|          O         |",
    "|      O     O     |",
    "°==========°"],
[
    ".==========.",
    "|      O     O     |",
    "|      O     O     |",
    "|      O     O     |",
    "°==========°"]
]


def turn_deciding_roll():
    # this section handles assigning who will play first
    print("Alright! Lets roll to see who goes first!")
    time.sleep(1)
    roll = []
    players_to_reroll = []
    first_roll = True
    tied = True
    for player in all_players_names:
        players_to_reroll.append(player)

    while tied:
        roll = []
        for i in range(len(players_to_reroll)):
            die_num = random.randint(1, 6)
            roll.append(die_num)

        for lines in zip(*[dice[r - 1] for r in roll]):
            print("          ".join(lines))

        # displays a number identifier underneath each die
        num_display = "           "
        for i in range(len(players_to_reroll)):
            #conditional here to fix an offset issue with dice 3-6's display numbers
            if i <= 2:
                num_display += str(i + 1) + "                                "
            else:
                num_display += str(i + 1) + "                                 "
        print(num_display)
        time.sleep(1)

        # prints who is associated to each die
        for i in range(len(players_to_reroll)):
            print(f"Die {i + 1} : {players_to_reroll[i]}")
            time.sleep(.5)
    #
        # check to see if there were any ties in the starting roll
        highest_roll = max(roll)
        highest_roll_index = roll.index(highest_roll)
        if roll.count(max(roll)) == 1:
            print(f"Highest roller is Die {highest_roll_index + 1} : {players_to_reroll[highest_roll_index]}")

            #set play order according to who won
            starting_index = all_players_names.index(players_to_reroll[highest_roll_index])
            turn_order = 1
            for i in range(len(all_players)):
                all_players[starting_index].turn_order = turn_order
                turn_order += 1
                starting_index += 1
                if starting_index > len(all_players) - 1:
                    starting_index = 0
            tied = False
            time.sleep(.5)
        else:
            # get high roller indexes to roll again
            #make a secondary llst so i can clear the original one to loop through  easier?
            time.sleep(.5)
            print("Tie-Breaker!")
            players_to_reroll_2 = []
            index = 0
            for num in roll:
                if num == highest_roll:
                    players_to_reroll_2.append(players_to_reroll[index])
                index += 1
            players_to_reroll = players_to_reroll_2



class Player():
    def __init__(self, name):
        self.name = name
        self.roll = []
        self.score = 0
        self.on_board = False
        self.turn_order = 0

    def roll_dice(self, num_of_dice):
        # this section handles normal rolls
        for i in range(int(num_of_dice)):
            die_num = random.randint(1, 6)
            self.roll.append(die_num)

        if len(self.roll) == 1:
            for num in self.roll:
                for line in dice[num - 1]:
                    print(line)
        if len(self.roll) == 2:
            for line1, line2 in zip(dice[self.roll[0] - 1], dice[self.roll[1] - 1]):
                print(line1 + "        " + line2)
        if len(self.roll) == 3:
            for line1, line2, line3 in zip(dice[self.roll[0] - 1], dice[self.roll[1] - 1], dice[self.roll[2] - 1]):
                print("        " + line1 + "        " + line2 + "        " + line3)
        if len(self.roll) == 4:
            for line1, line2, line3, line4 in zip(dice[self.roll[0] - 1], dice[self.roll[1] - 1], dice[self.roll[2] - 1],
                                                  dice[self.roll[3] - 1]):
                print("        " + line1 + "        " + line2 + "        " + line3 + "        " + line4)
        if len(self.roll) == 5:
            for line1, line2, line3, line4, line5 in zip(dice[self.roll[0] - 1], dice[self.roll[1] - 1], dice[self.roll[2] - 1],
                                                         dice[self.roll[3] - 1], dice[self.roll[4] - 1]):
                print(
                    "        " + line1 + "        " + line2 + "        " + line3 + "        " + line4 + "        " + line5)
        if len(self.roll) == 6:
            for line1, line2, line3, line4, line5, line6 in zip(dice[self.roll[0] - 1], dice[self.roll[1] - 1],
                                                                dice[self.roll[2] - 1], dice[self.roll[3] - 1],
                                                                dice[self.roll[4] - 1], dice[self.roll[5] - 1]):
                print(
                    "        " + line1 + "        " + line2 + "        " + line3 + "        " + line4 + "        " + line5 + "        " + line6)


show_title()
handle_player_and_opponent_assignment()
turn_deciding_roll()