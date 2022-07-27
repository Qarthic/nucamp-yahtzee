





# Beautify Score and print


def show_score(hand, hand_score):
    hand = (', '.join(hand))
    print(f"Your hand was: {hand}\nYour score was: {hand_score}")

# Check if Yahtzee


def yahtzee_check(hand):
    global hand_score, final_hand
    if len(set(hand)) == 1:
        final_hand = "Yahtzee!"
        return final_hand

# Check if 4 of a Kind or Full House


def four_house_check(hand):
    global hand_score, final_hand
    if len(set(hand)) == 2:
        for di in hand:
            if hand.count(di) == 4:
                final_hand = "Four of a kind"
                return final_hand
            else:
                final_hand = "Full House"
                return final_hand

# Check if Straight


def straight_check(hand):
    global hand_score, final_hand
    hand.sort()
    if sorted(hand) == list(range(min(hand), max(hand)+1)):
        if sum(hand) == 15:
            final_hand = "Small Straight"
            return final_hand
        elif sum(hand) == 20:
            final_hand = "Big Straight!"
            return final_hand

# Check if 3 of a Kind


def three_kind_check(hand):
    global hand_score, final_hand
    if len(set(hand)) == 3:
        for di in hand:
            if hand.count(di) == 3:
                final_hand = "Three of a kind"
                return final_hand

# Check if Two Pairs


def two_pairs_check(hand):
    global hand_score, final_hand
    hand.sort()
    if len(set(hand)) == 3:
        if (hand.count(hand[0]) == 2 and hand.count(hand[2]) == 3) or (hand.count(hand[1]) == 2 and hand.count(hand[3])) or (hand.count(hand[0]) == 2 and hand.count(hand[3])):
            final_hand = "Two of a kind"
            return final_hand

# Check if One Pair


def one_pair_check(hand):
    global hand_score, final_hand
    hand.sort()
    if len(set(hand)) == 4:
        for di in hand:
            if hand.count(di) == 2:
                final_hand = "One pair"
                return final_hand


def run_hand_check(hand):
    global final_hand
    while final_hand == "":
        yahtzee_check(hand)
        four_house_check(hand)
        three_kind_check(hand)
        two_pairs_check(hand)
        one_pair_check(hand)
        straight_check(hand)
    print(final_hand)


