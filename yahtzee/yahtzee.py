
from random import randint
from time import sleep
from yahtzee_pkg import rules

class Player:
    def __init__(self, name):
      self.name = name
      self.score = 0
      self.catagory = ""
      self.hand = []
      self.uniques = {}
      self.show_hand = []
      self.hold = False
      self.score_card = {
        "Upper": {
          "Aces": 0,
          "Twos": 0,
          "Threes": 0,
          "Fours": 0,
          "Fives": 0, 
          "Sixes": 0
        }, 
        "Lower": {
          "3 Kind": 0,
          "4 Kind": 0,
          "Full House": 0,
          "Small Straight": 0,
          "Large Straight": 0,
          "Yahtzee": 0,
          "Chance": 0
        }
      }

    def create_hand(self): # Create hand if one does not already exist
      if self.hand != []:
        print("You've already got a hand!")
        return
      for i in range (1, 6, 1):
        i = randint(1, 6)
        self.hand.append(i)
      return self.hand.sort()
    
    def create_show_hand(self): # Sort and create show_hand. Used in Reroll. 
      self.show_hand = []
      self.hand.sort()
      for dice in self.hand:
        self.show_hand.append(str(dice))
      self.show_hand = (' '.join(self.show_hand))
      return self.show_hand

    def replace_dice(self, dice): # Replace dice indicated by user
      for die in (dice):
        new_die = randint(1, 6)
        self.hand[die] = new_die
      return self.hand.sort
    
    def get_uniques(self, hand): # Get List of unique values
      self.uniques = set(hand)
      self.uniques = list(self.uniques)
      return self.uniques
    
    def show_score_card(self, player):
      print(f"        {player.name}'s Score Card         ")
      print(" ------------------------------------- ") 
      for key, sub_dict in player.score_card.items():
        if key == "Upper":
          print("| Upper Section    |  Scores          |")
        elif key == "Lower":
          print(" ------------------------------------- ") 
          print("| Lower Section    |  Scores          |")
        for sub_dict, value in sub_dict.items():
          sub_dict_str = f" {sub_dict}: "
          while len(sub_dict_str) < 20:
            sub_dict_str = sub_dict_str + "."
          total_str = f"{sub_dict_str} {value}"
          while len(total_str) < 37:
            total_str = total_str + " "
          print(f"|{total_str}|")
      print(" ------------------------------------- ") 
      print(f" Your total score: {player.score}\n")
      input("ENTER to continue.\n")

### Inits Game, asks how many palyers
def start_game(): 
  print("Welcome to Yahtzee!")
  print("How many people are playing?\n1. One Player       2. Two Players\n--> ", end='')
  while True:
    num_players = input("")
    if num_players.isnumeric() == False: ## Checks if num_players a number
      print("Sorry, please enter 1 or 2 only.\n")
      sleep(.5)
      print("1. One Player       2. Two Players\n--> ", end='')
    elif int(num_players) < 1 or int(num_players) > 2: ## Checks if num_players 1 or 2
      print("Sorry, you can only play with 1 or 2 players.\n")
      sleep(.5)
      print("1. One Player       2. Two Players\n--> ", end='')
    else:
      break
  num_players = int(num_players)
  return num_players

### Recieve's players names, which will be used for rest of game
def player_creation(players): 
  if players == 1:
    name = input("Player 1, enter your name: ")
    name_valid = False
    while name_valid != True:
      if len(name) <= 2:
        print("Name must at least be 3 characters long.")
        name = input("Enter your name")
      elif name.isalpha() != True:
        print("Name can not contain numbers or other characters.")
        name = input("Enter your name")
      else: 
        name_valid = True

    p1 = Player(name)
    p1 = [p1]
    return(p1)
  else:
    name = input("Player 1, enter your name: ")
    name_valid = False
    while name_valid != True:
      if len(name) <= 2:
        print("Name must at least be 3 characters long.")
        name = input("Enter your name: ")
      elif name.isalpha() != True:
        print("Name can not contain numbers or other characters.")
        name = input("Enter your name: ")
      else: 
        name_valid = True
    p1 = Player(name)
    print(f"Welcome, {p1.name}")
    sleep(.5)
    name = input("Player 2, enter your name: ")
    name_valid = False
    while name_valid != True:
      if len(name) <= 2:
        print("Name must at least be 3 characters long.")
        name = input("Enter your name: ")
      elif name.isalpha() != True:
        print("Name can not contain numbers or other characters.")
        name = input("Enter your name: ")
      else: 
        name_valid = True
    p2 = Player(name)
    print(f"Welcome, {p2.name}")
    sleep(.5)
    return p1, p2

###  Checks if there are multiple players from player_creation
def is_multiplayer(player_list): 
  if len(player_list) == 2:
    return True
  else: 
    return False

### Single Player game will be played in this function
def single_player(player_list): 
  p1 = player_list[0]
  round = 1
  print("ROUND 1")
  while round < 6:
    # p1.hand = [2, 2, 3, 3, 3]
    p1.create_hand()
    p1.create_show_hand()
    p1 = dice_reroller(p1)
    rules.hand_check(p1)
    sleep(.5)
    p1.show_score_card(p1)
    p1.hand = []
    round += 1
    input(f"\nPRESS ENTER TO START ROUND {round}")
    
### Multiplayer game will be played in this function
def multiplayer(player_list): 
  print("\nWhen prompted, enter the numbers corresponding to each dice you'd like to replace.")
  print("Whenever you want to hold instead of reroll, simply press ENTER.\n")
  sleep(.5)
  p1 = player_list[0]
  p2 = player_list[1]
  round = 1
  while round < 6:
    p1.create_hand()
    p1.create_show_hand()
    p2.create_hand()
    p2.create_show_hand()
    p1 = dice_reroller(p1)
    p2 = dice_reroller(p2)
    rules.hand_check(p1)
    rules.hand_check(p2)
    p1.show_score_card(p1)
    p2.show_score_card(p2)
    p1.hand = []
    p2.hand = []
    
### Gives user option to reroll dice
def dice_reroller(player): 
  print(f"\n\nSTART **{player.name.upper()}'S** TURN:\n")
  sleep(.75)
  i = 1
  while i <= 3 and player.hold == False:
    if i == 1:
      print(f"-- ROLL #{i} --\n")
      input(f"**{player.name}**, Press ENTER to roll your starting hand.\n")
      sleep(.5)
      print(f"Your starting hand: \n\n**{player.show_hand}**")
    elif i == 2:
      print(f"\n-- ROLL #{i}--\n")  
      print(f"**{player.name}**, Your new hand: \n\n**{player.show_hand}**")
      sleep(.5)
    elif i == 3:
      print(f"\n-- ROLL #{i}--\n")
      print(f"**{player.name}**, Your final hand: \n\n**{player.show_hand}**")
      sleep(1)
      return player
    i += 1
    replaced_dice = ""
    replace_list = []
    print("  ^ ^ ^ ^ ^")
    print("  1 2 3 4 5\n\n-------------\nReplace which dice? (ENTER to hold.)")
    print("> ", end='')
    replaced_dice = input("")
    if replaced_dice == "": # the 'break' for the reroller
      player.hold = True
      player.create_show_hand()
      print(f"{player.name} is holding with {player.show_hand}")
      return player
    for die in replaced_dice:
      die = int(die)
      die -= 1
      replace_list.append(die)
    player.replace_dice(replace_list)
    player.create_show_hand()
  return player

### Game runs in this function
def yahtzee(): 
  num_players = start_game()
  player_list = player_creation(num_players)
  if is_multiplayer(player_list):
    multiplayer(player_list)
  else:
    single_player(player_list)


yahtzee()
