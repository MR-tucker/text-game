# Text based 10,000 dice game, where num of npc opponents can be chosen,
# rolls are random, and player can select die or dice to keep/ re-roll
import time, random

def show_title():
    # display a title/header
    # I noticed this lines up perfectly in my code editor but mis-aligned when viewed on gitHub or ran on bash. tried very hard to fix this issue
    print("""\
---------------------------------------------------------------------------------------------------------------------------------------------------
|          O                          OOO                             OOO                              OOO                             OOO           |
|        OO                      O         O                       O         O                        O         O                       O         O        |
|     O   O                   O               O                 O               O                  O               O                 O               O     |
|           O                   O               O                 O               O                  O               O                 O               O     |
|           O                   O               O                 O               O                  O               O                 O               O     |
|           O                      O         O          /            O         O                        O         O                       O         O        |
|     OOOOO                   OOO           /                 OOO                              OOO                             OOO           |
---------------------------------------------------------------------------------------------------------------------------------------------------\
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
        time.sleep(2)
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

player_order = []
def turn_deciding_roll():
    # this section handles assigning who will play first
    print("Alright! Lets roll to see who goes first!")
    time.sleep(2)
    players_to_reroll = []
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
        time.sleep(2)

        # prints who is associated to each die
        for i in range(len(players_to_reroll)):
            print(f"Die {i + 1} : {players_to_reroll[i]}")
            time.sleep(.8)
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
                player_order.append(all_players[starting_index])
                turn_order += 1
                starting_index += 1
                if starting_index > len(all_players) - 1:
                    starting_index = 0
            tied = False
            time.sleep(.5)
        else:
            # get high roller indexes to roll again
            #make a secondary llst so i can clear the original one to loop through  easier?
            time.sleep(1)
            print("Tie-Breaker!")
            players_to_reroll_2 = []
            index = 0
            for num in roll:
                if num == highest_roll:
                    players_to_reroll_2.append(players_to_reroll[index])
                index += 1
            players_to_reroll = players_to_reroll_2

run_game = True
def game():
    #prints a message showing the play order
    order_message = f"{player_order[0].name} rolls First, followed by "
    for player in player_order:
        if player_order.index(player) > 0 and player_order.index(player) < len(player_order) - 1:
            order_message += player.name + ", "
        if player_order.index(player) != 0 and player_order.index(player) == len(player_order) - 1:
            order_message += "then " + player.name
    print(order_message)
    input("Press enter to begin!")
    time.sleep(1)

    while run_game:
        for i in range(len(all_players)):
            if player_turn == i + 1:
                player_order[i].roll_dice()



player_turn = 1
class Player():
    def __init__(self, name):
        self.name = name
        self.roll = []
        self.current_score = 0
        self.total_score = 0
        self.on_board = False
        self.turn_order = 0
        self.dice_to_roll = 6
        self.combo_options = []
        self.used_dice = []
        self.unused_dice = []
        self.can_stay = False
        self.turn_just_changed = True

    def roll_dice(self):
        # this section handles normal rolls
        self.roll = []
        self.combo_options = []
        self.used_dice = []
        self.unused_dice = []

        #display the players turn their total score and  how much they need to win
        if player_turn == self.turn_order and self.turn_just_changed:
            print(f"It's {self.name}'s turn, they currently have {self.total_score} Points and need {10000 - self.total_score} Points to win")
            self.turn_just_changed = False
            time.sleep(1)

        #rolls the dice for normal gameplay
        for i in range(self.dice_to_roll):
            die_num = random.randint(1, 6)
            self.roll.append(die_num)
        #draws the dice on screen for each roll
        for lines in zip(*[dice[r - 1] for r in self.roll]):
            print("          ".join(lines))

        time.sleep(1)

        self.score_combos()
        time.sleep(1)
        self.take_roll_score()
        if self.name != players_name:
            self.stay()

    def score_combos(self):
        #straight (1-6)
        if sorted(self.roll) == [1, 2, 3, 4, 5, 6]:
            self.combo_options.append(("Straight", 1500, 6))
            return self.combo_options

        #3 pairs
        doubles_count = []
        for num in self.roll:
            count =self.roll.count(num)
            if count == 2 and not num in doubles_count:
                doubles_count.append(num)
        if len(doubles_count) ==  3:
            self.combo_options.append(("3 Pairs", 1000, 6))
            return self.combo_options

        #check for double triples
        triples_count = []
        placeholder_score = 0
        #counts the triples and appends to a temp list
        for num in self.roll:
            count = self.roll.count(num)
            if count == 3 and not num in triples_count:
                triples_count.append(num)
        if len(triples_count) == 2:
            for num in triples_count:
                if num == 1:
                    placeholder_score += 1000
                else:
                    placeholder_score += num * 100
            self.combo_options.append(("Double Triple", placeholder_score, 6))
            return self.combo_options

        #check for 3+ of a kind
        for num in self.roll:
            count = self.roll.count(num)
            if count >= 3 and not num in self.used_dice:
                base_score = 1000 if num == 1 else num * 100
                if count == 3:
                    self.combo_options.append(("Combo", base_score, 3))
                elif count == 4:
                    self.combo_options.append(("Combo", base_score * 2, 4))
                elif count == 5:
                    self.combo_options.append(("Combo", base_score * 3, 5))
                elif count == 6:
                    self.combo_options.append(("Combo", base_score * 4, 6))
            if count >= 3:
                self.used_dice.append(num)
            else:
                self.unused_dice.append(num)

        #get remaining usable options
        if 1 in self.unused_dice or 5 in self.unused_dice or len(self.combo_options) < 1:
            ones = 0
            fives = 0
            for num in self.unused_dice:
                if num == 1:
                    ones += 1
                if num == 5:
                    fives += 1
            #check if player can take all remaining dice
            if len(self.unused_dice) == ones + fives:
                self.combo_options.append(("Take all remaining", (ones * 100) + (fives * 50), len(self.unused_dice)))
                return self.combo_options
            if ones > 0:
                self.combo_options.append(("Take ones", ones * 100, ones))
            if fives > 0:
                self.combo_options.append(("Take fives", fives * 50, fives))
        return self.combo_options

    def take_roll_score(self):
        global player_turn, run_game
        #checks for a bust
        if not self.combo_options:
            print(f"{self.name} Busted!\n")
            self.dice_to_roll = 6
            self.current_score = 0
            self.turn_just_changed = True
            player_turn += 1
            if player_turn > len(all_players):
                player_turn = 1
            return

        # handle user input
        if self.name == players_name:
            already_taken = set()
            while True:
                print("\nAvailable options:")
                for i, option in enumerate(self.combo_options):
                    print(f"{i + 1}: {option[0]} for {option[1]} points (uses {option[2]} dice)")

                try:
                    choice = input("Choose option(s) to keep (enter number(s), separated by comma): ").strip()
                    indices = [int(x.strip()) - 1 for x in choice.split(',')]

                    valid = all(0 <= idx < len(self.combo_options) for idx in indices)
                    if not valid:
                        print("One or more choices are invalid. Try again.")
                        continue

                    total_dice_used = 0
                    for idx in indices:
                        if idx in already_taken:
                            print(f"Option {idx + 1} already used. Skipping.")
                            continue
                        selected = self.combo_options[idx]
                        print(f"You chose to take: {selected[0]} for {selected[1]} points!")
                        self.current_score += selected[1]
                        self.dice_to_roll -= selected[2]
                        total_dice_used += selected[2]
                        already_taken.add(idx)

                    break  # Exit combo selection loop

                except ValueError:
                    print("Please enter valid numbers separated by commas.")

            # Ask if they want to stay or roll again
            # Ask if they want to stay or roll again
            while True:
                print(f"\nYour current roll score: {self.current_score}")
                print(f"You have {self.dice_to_roll} dice left.")
                choice = input("Would you like to stay or roll again? (stay/roll or s/r): ").lower()

                if choice in ("stay", "s"):
                    # if player is not on the board yet
                    if not self.on_board:
                        if self.current_score >= 1000:
                            print("You can now get on the board!")
                            self.can_stay = True
                            self.stay()
                            return
                        else:
                            print("You need at least 1000 points in one turn to get on the board. Keep rolling!")
                            continue  # don't exit the loop — re-prompt
                    else:
                        # player is already on board and chose to stay
                        self.can_stay = True
                        self.stay()
                        return

                elif choice in ("roll", "r"):
                    if self.dice_to_roll == 0:
                        print("All dice used — rolling 6 fresh dice.")
                        self.dice_to_roll = 6
                    self.roll_dice()
                    return

                else:
                    print("Please type 'stay', 's', 'roll', or 'r'.")



        #handles ai decisions
        else:
            #if opponent has a good combo that uses all 6 dice
            #they will take this option
            for option in self.combo_options:
                if option[2] == 6:
                    self.current_score += option[1]
                    self.dice_to_roll -= option[2]
                    print(f"{self.name} is going to take a {self.combo_options[0][0]} for {self.combo_options[0][1]} Points")
                    break

                #if the opponent has a combo for the highest roll that doesn't use all 6 dice but uses 3 or more
                if option[0] == "Combo" and option[2] != 6:
                    #checks 1-6 to see what combo exists
                    for i in range(6):
                        if self.used_dice[0] == i + 1:
                            #if a combo isn't the only option there is a small chance that they won't take it
                            if len(self.combo_options) > 1:
                                if random.randint(1, 10) <= 2 and self.used_dice[0] != 1:
                                    pass
                                else:
                                    self.current_score += option[1]
                                    self.dice_to_roll -= option[2]
                                    print(f"{self.name} is going to take a {option[0]} for {option[1]} Points")
                                    if len(self.used_dice) == 3 and random.randint(1, 10) <= 8:
                                        break
                            #if a combo is the only option they will take it
                            else:
                                self.current_score += option[1]
                                self.dice_to_roll -= option[2]
                                print(f"{self.name} is going to take a {option[0]} for {option[1]} Points")

                #if the player can take all remaining dice to keep rolling then they will
                if "Take all remaining" in option[0]:
                    self.current_score += option[1]
                    self.dice_to_roll -= option[2]
                    print(f"{self.name} is going to {option[0]} for {option[1]} Points")
                    break
                #if the player cant take all remaining then they will take ones if available
                elif "Take ones" in option[0]:
                    self.current_score += option[1]
                    self.dice_to_roll -= option[2]
                    print(f"{self.name} is going to {option[0]} for {option[1]} Points")
                    break
                #if no ones are available then they will take fives
                elif "Take fives" in option[0]:
                    self.current_score += option[1]
                    self.dice_to_roll -= option[2]
                    print(f"{self.name} is going to {option[0]} for {option[1]} Points")
                    break

        #player must have the exact points available to take to reach 10000 without going over
        if self.current_score + self.total_score == 10000:
            print(f"{self.name} Wins!!")
            run_game = False
            return
        elif self.current_score + self.total_score > 10000:
            print(f"{self.name} Busted!\n")
            self.dice_to_roll = 6
            self.current_score = 0
            self.turn_just_changed = True
            player_turn += 1
            if player_turn > len(all_players):
                player_turn = 1
            return

        time.sleep(.5)
        print(f"\n{self.name} is currently holding {self.current_score} Points and has a total of {self.total_score}\n")
        time.sleep(1)

    def stay(self):
        global player_turn
        #if someone has won the game, this prevents the rest of the stay method from execution
        if run_game == False:
            return
        self.can_stay = False
        #checks if the player has enough points to get on the board, if they do then they will stay
        if not self.on_board and self.name != players_name:
            if self.current_score >= 1000:
                self.can_stay = True
            else:
                self.can_stay = False
        elif not self.on_board and self.name == players_name:
            if self.current_score >= 1000:
                self.can_stay = True
            else:
                self.can_stay = False
                print("You need 1000 points minimum to get on the board!")

        #if play is on the board and is not the user, there is an increasing chance they will stay based on how big their holding score is
        elif self.on_board and self.name != players_name:
            if self.current_score >= 500 and self.current_score < 600:
                if random.randint(1, 10) <= 5:
                    self.can_stay = True
            if self.current_score >= 600 and self.current_score < 700:
                if random.randint(1, 10) <=6:
                    self.can_stay = True
            if self.current_score >= 700 and self.current_score < 800:
                if random.randint(1, 10) <= 7:
                    self.can_stay = True
            if self.current_score >= 1000 and self.current_score < 2000:
                if random.randint(1, 10) <= 8:
                    self.can_stay = True
            if self.current_score >= 2000:
                if random.randint(1, 10) <= 9:
                    self.can_stay = True

        #if the player has taken their score, handles adding that score to the total, resetting a few variables and changing the players turn
        if self.can_stay:
            self.total_score += self.current_score
            print(f"{self.name} is going to stay with {self.current_score} and now has {self.total_score} Points\n")
            self.dice_to_roll = 6
            self.current_score = 0
            self.turn_just_changed = True
            player_turn += 1
            if player_turn > len(all_players):
                player_turn = 1
            if not self.on_board:
                self.on_board = True
            time.sleep(1)
            return

        #handles resetting available dice count if user has 0 dice left to roll
        if self.dice_to_roll == 0:
            print(f"{self.name} is still rolling!\n")
            self.dice_to_roll = 6

show_title()
handle_player_and_opponent_assignment()
turn_deciding_roll()
game()