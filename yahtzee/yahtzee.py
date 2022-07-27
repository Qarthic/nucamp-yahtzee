from dataclasses import replace
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
      self.uniques = set(self.hand)
      self.show_hand = []
      self.hold = False

    def create_hand(self):
      if self.hand != []:
        print("You've already got a hand!")
        return
      for i in range (1, 6, 1):
        i = randint(1, 6)
        self.hand.append(i)
      return self.hand.sort()
    
    def create_show_hand(self):
      self.show_hand = []
      self.hand.sort()
      for dice in self.hand:
        self.show_hand.append(str(dice))
      self.show_hand = (' '.join(self.show_hand))
      return self.show_hand

    def replace_dice(self, dice):
      i = 0
      for die in (dice):
        i += 1
        new_die = randint(1, 6)
        print(f"#{i}) {self.hand} soon to add {new_die}")
        self.hand[die] = new_die
        print(f"#{i}) {self.hand}")
        # temp = self.hand.pop(die)
        # print(f"#{i}) {self.hand}")
        # new_die = randint(1,6)
        # print(f"#{i}) {self.hand} soon to be added die {new_die}")
        # self.hand.append(new_die)
        # print(f"#{i}) {self.hand}")
      return self.hand.sort

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
  p1.create_show_hand()
  dice_reroller(p1)

def multiplayer(player_list): # Multiplayer game will be played in this function
  print("\nWhen prompted, enter the numbers corresponding to each dice you'd like to replace.")
  print("Whenever you want to hold instead of reroll, simply press ENTER.\n")
  sleep(.5)
  p1 = player_list[0]
  p1.create_hand()
  p1.create_show_hand()
  p2 = player_list[1]
  p2.create_hand()
  p2.create_show_hand()
  p1 = dice_reroller(p1)
  p2 = dice_reroller(p2)
  rules.run_hand_check(p1.hand)
  rules.run_hand_check(p2.hand)
  


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
      player.create_show_hand()
      print(f"{player.name} is holding with {player.show_hand}")
      return player
    for die in replaced_dice:
      die = int(die)
      die -= 1
      replace_list.append(die)
      print(replace_list)
    player.replace_dice(replace_list)
    player.create_show_hand()
  return player

def yahtzee(): # Game runs in this function alone
  num_players = start_game()
  player_list = player_creation(num_players)
  if is_multiplayer:
    multiplayer(player_list)
  else:
    single_player(player_list)
#   


#  DC 4: Testing Yahtzee() with multiplayer and 
yahtzee()

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


