import random

def if_integer(string):
  
    if string[0] == ('-', '+'):
        return string[1:].isdigit()

    else:
        return string.isdigit()

def int_between_1_100(num):
    while (not if_integer(num)):
        print("I needed a number between 1 and 100")
        num = input()

    num = int(num)

    while (not num >= 1) or (not num <= 100):
        print("I needed a number between 1 and 100")
        num = input()

        while (not if_integer(num)):
            print("I needed a number between 1 and 100")
            num = input()

        num = int(num)
    return num

answer = random.randint(1, 100)
print("Guess the number between 1 and 100, you have 6 guesses.")
player_number = input()

int_between_1_100(player_number)
player_number = int(player_number)

for i in range(6):
    if player_number <= answer - 25:
        print("You are way low, guess higher")
        player_number = input()
        int_between_1_100(player_number)
        player_number = int(player_number)
    elif player_number >= answer + 25:
        print("You are way high, guess lower")
        player_number = input()
        int_between_1_100(player_number)
        player_number = int(player_number)
    elif (player_number > answer - 25) and (player_number <= answer - 6):
        print("You are a bit off, guess higher")
        player_number = input()
        int_between_1_100(player_number)
        player_number = int(player_number)
    elif (player_number < answer + 25) and (player_number >= answer + 6):
        print("You are a bit off, guess lower")
        player_number = input()
        int_between_1_100(player_number)
        player_number = int(player_number)
    elif (player_number >= answer - 5) and (player_number <= answer - 1):
        print("You are so close, guess higher")
        player_number = input()
        int_between_1_100(player_number)
        player_number = int(player_number)
    elif (player_number <= answer + 5) and (player_number >= answer + 1):
        print("You are so close, guess lower")
        player_number = input()
        int_between_1_100(player_number)
        player_number = int(player_number)
    elif player_number == answer:
        print("Congrats, you guessed the number correct")
        break
    
    if i == 4:
        print("That was guess number", i + 1, "one more guess")
    if i == 5:
        print("That was your last guess")
if player_number <= answer - 25:
    print("you are way low, guess higher")
