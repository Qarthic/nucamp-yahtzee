
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

# Beautify Score and print


# Check if already stored 

def catagory_taken(player):
    for key, sub_dict in player.score_card.items():
        for sub_dict, value in sub_dict.items():
            if sub_dict == player.catagory:
                if value != 0:
                    return True

# Check if Yahtzee

def yahtzee_check(player):
    player.get_uniques(player.hand)
    section = player.score_card["Lower"]
    if len(player.uniques) == 1:
        player.catagory = "Yahtzee"
        if player.catagory in section.keys() and catagory_taken(player) != True:
            player.score += 50
            section[player.catagory] = 50 
            return player
        else:
            player.catagory = ""
            return player

# Check if 4 of a Kind or Full House

def four_house_check(player):
    player.get_uniques(player.hand)
    section = player.score_card["Lower"]
    if len(player.uniques) == 2:
        for die in player.hand:
            if player.hand.count(die) == 4:
                player.catagory = "4 Kind"
                if player.catagory in section.keys() and catagory_taken(player) != True:
                    player.score += sum(player.hand)
                    section[player.catagory] = sum(player.hand) 
                    return player   
                else:
                    player.catagory = ""
                    return player
            else:
                player.catagory = "Full House"
                if player.catagory in section.keys() and catagory_taken(player) != True:
                    player.score += 25
                    section[player.catagory] = 25 
                    return player   
                else:
                    player.catagory = ""
                    return player

# Check if Straight

def straight_check(player):
    section = player.score_card["Lower"]
    if player.hand == [1, 2, 3, 4, 5]:
        player.catagory = "Small Straight"
        if player.catagory in section.keys() and catagory_taken(player) != True:
            player.score += 30
            section[player.catagory] = 30
            return player   
        else:
            player.catagory = ""
            return player
    elif player.hand == [2, 3, 4, 5, 6]:
        player.catagory = "Large Straight"
        if player.catagory in section.keys() and catagory_taken(player) != True:
            player.score += 40
            section[player.catagory] = 30
            return player   
        else:
            player.catagory = ""
            return player

# Check if 3 of a Kind

def three_kind_check(player):
    player.get_uniques(player.hand)
    section = player.score_card["Lower"]
    if len(player.uniques) == 3:
        for die in player.hand:
            if player.hand.count(die) == 3:
                player.catagory = "3 Kind"
                if player.catagory in section.keys() and catagory_taken(player) != True:
                    player.score += sum(player.hand)
                    section[player.catagory] = sum(player.hand) 
                    return player   
                else:
                    player.catagory = ""
                    return player

def upper_check(player):
    print("It doesn't look like your hand matches any available Lower Section hands.")
    if player.score_card["Lower"]["Chance"] == 0:
        print("Would you like to score Chance, or choose from the Upper options remaining?")
        choice = input("1. Chance\n2. Uppers remaining\n>> ")
        if choice == "1":
            player.score_card["Lower"]["Chance"] = sum(player.hand)
            player.catagory = "Chance"
        

# Global check

def run_hand_check(player):
    player.catagory = ""
    while player.catagory == "":
        yahtzee_check(player)
        four_house_check(player)
        three_kind_check(player)
        straight_check(player)
        if player.catagory == "":
            upper_check()
        print(f"You had a {player.catagory}")
        return player


