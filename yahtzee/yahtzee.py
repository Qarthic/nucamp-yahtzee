from random import randint
from time import sleep

class Player:
    def __init__(self, name):
      self.name = name
      self.score = 0
      self.catagory = ""
      self.hand = []
      self.player = 0
      self.uniques = set(self.hand)

    def create_hand(self):
      if self.hand != []:
        print("You've already got a hand!")
        return
      for i in range (1, 6, 1):
        i = randint(1, 6)
        self.hand.append(i)
      return self.hand.sort()

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

def player_creation(players):
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
    name = input("Player 2, enter your name: ")
    p2 = Player(name)
    print(f"Welcome, {p2.name}")
    return p1, p2

def is_multiplayer(player_list):
  if len(player_list) == 2:
    return True
  else: 
    return False

def single_player(player_list):
  p1 = player_list[0]
  p1.create_hand()
  

def multiplayer(player_list):
  p1 = player_list[0]
  p1.create_hand()
  print(p1.hand)
  p2 = player_list[1]
  p2.create_hand()
  print(p2.hand)

# ""
def yahtzee():
  num_players = start_game()
  player_list = player_creation(num_players)
  if is_multiplayer:
    multiplayer(player_list)
  else:
    single_player(player_list)
  

#  DC 2: start_game() and player_creation() tests
# yahtzee()

#  DC 1: create_hand to create random hand
"""
dyl = Player(0, '')
dyl.create_hand()
dylsethand
"""
