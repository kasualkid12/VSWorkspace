import random

def dice_size(size):
  rng = random.randint(1, size)
  print("With your", size, "sided die, you rolled a", rng)
  return 0

print("Would you like to roll a dice?")
user_answer = input()
player_dice_size = 0
rng = 0

while (not user_answer == "no") and (not user_answer == "No") and (not user_answer == "NO") and (not user_answer == "yes") and (not user_answer == "Yes") and (not user_answer == "YES"):
  print("I need a yes or no answer!")
  user_answer = input()

if (user_answer == "no") or (user_answer == "No") or (user_answer == "NO"):
  print("Well why'd you wake me up then?")

while (user_answer == "yes") or (user_answer == "Yes") or (user_answer == "YES"):
  print("How many sides to your dice?")
  player_dice_size = input()
  player_dice_size = int(player_dice_size)

  if player_dice_size == 2:
    dice_size(player_dice_size)
  elif player_dice_size == 4:
    dice_size(player_dice_size)
  elif player_dice_size == 6:
    dice_size(player_dice_size)
  elif player_dice_size == 8:
    dice_size(player_dice_size)
  elif player_dice_size == 10:
    dice_size(player_dice_size)
  elif player_dice_size == 12:
    dice_size(player_dice_size)
  elif player_dice_size == 20:
    dice_size(player_dice_size)
  elif player_dice_size == 50:
    dice_size(player_dice_size)
  elif player_dice_size == 100:
    dice_size(player_dice_size)
  else:
    print("That is not a valid dice size, try again?")
    user_answer = input()

  if (user_answer == "no") or (user_answer == "No") or (user_answer == "NO"):
    print("Back to sleep I go then.")
    
print("Would you like to roll again?")
user_answer = input()