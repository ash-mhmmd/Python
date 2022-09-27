############### Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
###########################################################
import random
from replit import clear
from logo import logo

def deal_cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calc_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 21

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(player_score, comp_score):
  if player_score > 21 and comp_score > 21:
    return "You went over 21. You lose 😤\n"
  if player_score == comp_score:
    return "Draw 🙃\n"
  elif comp_score == 0:
    return "You lose, opponent has Blackjack 😱\n"
  elif player_score == 0:
    return "You win with a Blackjack 😎\n"
  elif player_score > 21:
    return "You went over 21. You lose 😭\n"
  elif comp_score > 21:
    return "Opponent went over. You win 😁\n"
  elif player_score > comp_score:
    return "You win 😃\n"
  else:
    return "You lose 😤\n"

def play_game():
  print(logo)
  game_over = False

  player_hand = []
  comp_hand = []

  for _ in range(2):
    player_hand.append(deal_cards())
    comp_hand.append(deal_cards())

  while not game_over:
    player_score = calc_score(player_hand)
    comp_score = calc_score(comp_hand)
    print("\n")
    print(f"Your hand: {player_hand}")
    print(f"Your score: {player_score}")
    print(f"Computer's first card: {comp_hand[0]}\n")
    print("----------------------------------------")

    if player_score == 0 or comp_score == 0 or player_score > 21:
      game_over = True
    else:
      player_hit = input("Type 'h' to hit or type 's' to stand: ")
      if player_hit == "h":
        player_hand.append(deal_cards())
      elif player_hit == "s":
        game_over = True
  while comp_score != 0 and comp_score < 18:
    comp_hand.append(deal_cards())
    comp_score = calc_score(comp_hand)

  print("\n")
  print(f"Your final hand: {player_hand}")
  print(f"Your final score: {player_score}")
  print("\n")
  print(f"Computer's final hand: {comp_hand}")
  print(f"Computer's final score: {comp_score}")
  print("\n")
  print(compare(player_score, comp_score))

while input(
    "Would you like to play a game of blackjack? Please answer 'y' or 'n':\n"
) == 'y':
  clear()
  play_game()
