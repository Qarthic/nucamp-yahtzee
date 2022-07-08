# Making a handful of changes to commit

hand = [1, 2, 3, 4, 5]
hand_score = 0

# Beautify Score and print


def show_score(hand, hand_score):
    hand = (', '.join(hand))
    print(f"Your hand was: {hand}\nYour score was: {hand_score}")

# Check if Yahtzee


def yahtzee_check(hand):
    global hand_score
    if len(set(hand)) == 1:
        print("YAHTZEE!!!")
        print(f"{hand}")

# Check if 4 of a Kind or Full House


def four_house_check(hand):
    global hand_score
    hand.sort()
    if len(set(hand)) == 2:
        if hand.count(hand[0]) == 4:
            print("Four of a kind! That's great!")
            hand_score = 40 + sum(hand)
            print(f"{hand} {hand_score}")
        elif hand.count(hand[0]) == 3 or hand.count(hand[0]) == 2:
            hand_score = 40 + sum(hand)
            print("Full House!")
            print(f"{hand} {hand_score}")

# Check if Straight


def straight_check(hand):
    global hand_score
    hand.sort()
    if sorted(hand) == list(range(min(hand), max(hand)+1)):
        if sum(hand) == 15:
            print("Small Straight")
            return
        elif sum(hand) == 20:
            print("Big Straight!")
            return

# Check if 3 of a Kind


def three_kind_check(hand):
    global hand_score
    hand.sort()
    if len(set(hand)) == 3:
        if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
            print("Three of a kind!")
            hand_score = sum(hand)
            show_score(hand, hand_score)
            return

# Check if Two Pairs

# Check if One Pair


for i in ("Git commit"):
    print(i)
