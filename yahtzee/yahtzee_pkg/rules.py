
from time import sleep

#              Score Card
#  ------------------------------------- 
# | Upper Sect     | Score              |
#  -------------------------------------
# | Aces           | Tot of Aces only   |
# | Twos           | Tot of Twos only   |
# | Threes         | Tot of Threes only |
# | Fours          | Tot of Fours only  |
# | Fives          | Tot of Fives only  |
# | Six            | Tot of Sixes only  |
#  ------------------------------------- 
# | Lower Sect     | Score              |
#  ------------------------------------- 
# | 3 Kind         | Tot of all 5 Dice  |
# | 4 Kind         | Tot of all 5 Dice  |
# | Full House     | 25 Points          |
# | Small Straight | 30 Points          |
# | Large Straight | 40 Points          |
# | YAHTZEE        | 50 Points          |
# | Chance         | Tot of all 5 Dice  |
#  ------------------------------------- 



def lower_check(player):
    player.hand.sort()
    player.get_uniques(player.hand)
    section = player.score_card["Lower"]
    if player.hand == [1, 2, 3, 4, 5] and section["Small Straight"] == 0:  # Sm Str Check
        section["Small Straight"] = 30
        player.score += 30
        player.catagory = "Small Straight"
        return player
    if player.hand == [2, 3, 4, 5, 6] and section["Large Straight"] == 0:  # Lg Str Check
        section["Large Straight"] = 40
        player.score += 40
        player.catagory = "Large Straight"
        return player
    if len(player.uniques) == 2:  # 4 Kind or FH Check
        for die in player.hand:
            if player.hand.count(die) == 4 and section["4 Kind"] == 0:  # 4 Kind
                section["4 Kind"] = sum(player.hand)
                player.score += sum(player.hand)
                player.catagory = "4 of a Kind"
                return player
            elif player.hand.count(die) == 3 or player.hand.count(die) == 2 and section["Full House"] == 0:  # Full House
                section["Full House"] = 25
                player.score += 25
                player.catagory = "Full House"
                return player
    if len(player.uniques) == 3 and section["3 Kind"] == 0:  # 3 Kind Check
        for die in player.hand:
            if player.hand.count(die) == 3:
                section["3 Kind"] = sum(player.hand)
                player.score += sum(player.hand)
                player.catagory = "3 of a Kind"
                return player
            else:
                pass
    if len(player.uniques) == 1 and section["Yahtzee"] == 0:
        section["Yahtzee"] = 50
        player.score += 50
        player.catagory = "Yahtzee"
        print("YAHZTEE!!!")
        return player
    if section["Chance"] == 0:
        section["Chance"] = sum(player.hand)
        player.score += sum(player.hand)
        player.catagory = "Chance"
        return player
    else:
        player.catagory = ""
        print("Sorry, your hand either doesn't fit into any catagory, or the catagory is filled.")
        return player

def upper_check(player):
    player.hand.sort()
    player.get_uniques(player.hand)
    player.create_show_hand()
    section = player.score_card["Upper"]
    print("Which catagory would you like to store in?")
    i = 0  # Used for 1-N Selection.
    display_cat_list = "" # Allows us to show the available list again if incorrect selection made 
    working_cat_dict = dict() # Stores avail list in dictionary for us to use in IF list later
    for cat, num in section.items():
        if num == 0:
            i += 1
            working_cat_dict[cat] = i
            display_cat_list += f"{i}. {cat}\n"
    print(f"{display_cat_list}\n")
    print(f"Your hand: **{player.show_hand}**")
    choice = input("")
    loop = True
    while loop: # Loops Choice if invalid
        if int(choice) > i or choice.isnumeric() != True:
            print("Invalid choice. Try again")
            print(display_cat_list)
            choice = input("")
        loop = False
    for key, num in working_cat_dict.items(): # Checks which key user chose
        if int(choice) == num:
            player.catagory = key
    temp_score = 0
    if player.catagory == "Aces" and section["Aces"] == 0:
        for die in player.hand:
            if die == 1:
                temp_score += die
        section["Aces"] = temp_score
        player.score += temp_score
        player.catagory = "Aces"
    if player.catagory == "Twos" and section["Twos"] == 0:
        for die in player.hand:
            if die == 2:
                temp_score += die
        section["Twos"] = temp_score
        player.score += temp_score
        player.catagory = "Twos"
        return player
    if player.catagory == "Threes" and section["Threes"] == 0:
        for die in player.hand:
            if die == 3:
                temp_score += die
        section["Threes"] = temp_score
        player.score += temp_score
        player.catagory = "Threes"
        return player
    if player.catagory == "Fours" and section["Fours"] == 0:
        for die in player.hand:
            if die == 4:
                temp_score += die
        section["Fours"] = temp_score
        player.score += temp_score
        player.catagory = "Fours"
        return player
    if player.catagory == "Fives" and section["Fives"] == 0:
        for die in player.hand:
            if die == 5:
                temp_score += die
        section["Fives"] = temp_score
        player.score += temp_score
        player.catagory = "Fives"
        return player
    if player.catagory == "Sixes" and section["Sixes"] == 0:
        for die in player.hand:
            if die == 6:
                temp_score += die
        section["Sixes"] = temp_score
        player.score += temp_score
        player.catagory = "Sixes"
        return player

def hand_check(player):
    print(f"\n**{player.name.upper()}'S** SCORING ROUND: \n\nWould you like to score the Upper or Lower section?\n")
    print(f"{player.name}'s hand: -- {player.show_hand} -- \n")
    print("1. Upper\n2. Lower\n3. Skip Scoring")
    choice = input("-> ")
    cont = False
    while cont != True: 
        if choice.isnumeric() != True:
            print("\nInvalid Choice. Please try again\n")
            sleep(.75)
            print("1. Upper\n2. Lower")
            choice = input("-> ")
        elif int(choice) < 1 or int(choice) > 3:
            print("\nInvalid Choice. Please try again\n")
            print("1. Upper\n2. Lower")
            choice = input("> ")
        else:
            break
    if choice == "1":
        upper_check(player)
        cont = True
        print(f"This hand was: {player.catagory}\n")
        sleep(.85)
        return player
    if choice == "2": 
        lower_check(player)
        cont = True
        print(f"This hand was: {player.catagory}\n")
        sleep(.85)
        return player
    if choice ==  "3":
        print(f"{player.name} skipped scoring this turn.")
        sleep(.85)
        return player

