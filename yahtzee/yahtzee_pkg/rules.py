
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
    if len(set(hand)) == 2:
        for di in hand:
            if hand.count(di) == 4:
                return "four of a kind"
            else:
                return "Full House"

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
    if len(set(hand)) == 3:
        for di in hand:
            if hand.count(di) == 3:
                return "Three of a kind"

# Check if Two Pairs


def two_pairs_check(hand):
    global hand_score
    hand.sort()
    if len(set(hand)) == 3:
        if (hand.count(hand[0]) == 2 and hand.count(hand[2]) == 3) or (hand.count(hand[1]) == 2 and hand.count(hand[3])) or (hand.count(hand[0]) == 2 and hand.count(hand[3])):
            print("Two pairs!")
            hand_score = sum(hand)
            show_score(hand, hand_score)
            return

# Check if One Pair


def one_pair_check(hand):
    global hand_score
    hand.sort()
    if len(set(hand)) == 4:
        for di in hand:
            if hand.count(di) == 2:
                return "One pair"
