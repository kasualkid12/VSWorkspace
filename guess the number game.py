import random

def if_integer(string):
  
    if string[0] == ('-', '+'):
        return string[1:].isdigit()

    else:
        return string.isdigit()

answer = random.randint(1, 100)
print("Pick a random number between 1 and 100")
player_number = input()

print(type(if_integer(player_number)))
while (not if_integer(player_number)):
    print("I needed a number between 1 and 100")
    player_number = input()

player_number = int(player_number)

while (not player_number >= 1) or (not player_number <= 100):
    print("I needed a number between 1 and 100")
    player_number = input()
    player_number = int(player_number)