from dataclasses import replace
from multiprocessing.sharedctypes import Value
from random import randint
from re import L
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
      self.show_score_card = dict()

    def create_hand(self): # Create hand if one does not already exist
      if self.hand != []:
        print("You've already got a hand!")
        return
      for i in range (1, 6, 1):
        i = randint(1, 6)
        self.hand.append(i)
      return self.hand.sort()
    
    def create_sh(self): # Sort and create show_hand
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
    
    def show_sc(self, player):
      print("              Score Card               ")
      print(" ------------------------------------- ") 
      for key, sub_dict in player.score_card.items():
        if key == "Upper":
          print("| Upper Secttion   |  Scores          |")
        elif key == "Lower":
          print(" ------------------------------------- ") 
          print("| Lower Secttion   |  Scores          |")
        for sub_dict, value in sub_dict.items():
          sub_dict_str = f" {sub_dict}: "
          while len(sub_dict_str) < 20:
            sub_dict_str = sub_dict_str + "."
          total_str = f"{sub_dict_str} {value}"
          while len(total_str) < 37:
            total_str = total_str + " "
          print(f"|{total_str}|")
      print(" ------------------------------------- ") 
      print(f" Your total score: {player.score}")

def start_game():   #  Inits game, asks how many players. 
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

def player_creation(players): # Recieve's players names, which will be used for rest of game
  if players == 1:
    print("Playing solo?")
    name = input("Player 1, enter your name: ")
    p1 = Player(name)
    p1 = [p1]
    return(p1)
  else:
    print("Two players? Great!\n")
    name = input("Player 1, enter your name: ")
    p1 = Player(name)
    print(f"Welcome, {p1.name}")
    sleep(.5)
    name = input("Player 2, enter your name: ")
    p2 = Player(name)
    print(f"Welcome, {p2.name}")
    sleep(.5)
    return p1, p2

def is_multiplayer(player_list): #  Checks if there are multiple players from player_creation
  if len(player_list) == 2:
    return True
  else: 
    return False

def single_player(player_list): # Single Player game will be played in this function
  p1 = player_list[0]
  p1.create_hand()
  p1.create_sh()
  dice_reroller(p1)
  rules.run_hand_check(p1)

def multiplayer(player_list): # Multiplayer game will be played in this function
  print("\nWhen prompted, enter the numbers corresponding to each dice you'd like to replace.")
  print("Whenever you want to hold instead of reroll, simply press ENTER.\n")
  sleep(.5)
  p1 = player_list[0]
  p1.create_hand()
  p1.create_sh()
  p2 = player_list[1]
  p2.create_hand()
  p2.create_sh()
  p1 = dice_reroller(p1)
  p2 = dice_reroller(p2)
  rules.run_hand_check(p1)
  rules.run_hand_check(p2)

def dice_reroller(player):
  sleep(.75)
  print("\n-- ROLL #1 --")
  input(f"**{player.name}**, Press ENTER to roll your starting hand.")
  print(f"Your starting hand: \n**{player.show_hand}**")
  sleep(.5)
  i = 1
  while i <= 3 and player.hold == False:
    if i == 2:
      print(f"-- ROLL #{i}--")  
      print(f"\n**{player.name}**, Your new hand: \n**{player.show_hand}**")
    elif i == 3:
      print(f"-- ROLL #{i}--")
      print(f"\n**{player.name}**, Your final hand: \n**{player.show_hand}**")
      return player
    i += 1
    replaced_dice = ""
    replace_list = []
    print("  ^ ^ ^ ^ ^")
    print("  1 2 3 4 5\n-------------\nReplace which dice? (ENTER to hold.)")
    print("> ", end='')
    replaced_dice = input("")
    if replaced_dice == "": # the 'break' for the reroller
      player.hold = True
      player.create_sh()
      print(f"{player.name} is holding with {player.show_hand}")
      return player
    for die in replaced_dice:
      die = int(die)
      die -= 1
      replace_list.append(die)
    player.replace_dice(replace_list)
    player.create_sh()
  return player



def yahtzee(): # Game runs in this function alone
  num_players = start_game()
  player_list = player_creation(num_players)
  if is_multiplayer(player_list):
    multiplayer(player_list)
  else:
    single_player(player_list)

#   


#  DC 5: Testing various checks
yahtzee()
# dyl = Player("Dyl")
# dyl.hand = [1, 1, 1, 1, 1] # Displayed Yahtzee, score 50
# dyl = rules.yahtzee_check(dyl)
# # dyl.show_sc(dyl)
# # dyl.hand = [2, 2, 2, 2, 2] 
# # dyl = rules.yahtzee_check(dyl)
# # dyl.show_sc(dyl)
 
# rules.catagory_taken(dyl)

# dyl.create_sc(dyl)




#  DC 4: Testing Yahtzee() with multiplayer and 
# yahtzee()

#  DC 3: Testing Reroller
# dyl = Player('dyl')
# dyl.create_hand()
# dyl.create_show_hand()
# dice_reroller(dyl)

#  DC 2: start_game() and player_creation() tests
# yahtzee()

#  DC 1: create_hand to create random hand
# dyl = Player(0, '')
# dyl.create_hand()


