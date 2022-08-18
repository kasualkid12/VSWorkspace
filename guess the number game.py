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
print("Pick a random number between 1 and 100")
player_number = input()

int_between_1_100(player_number)

if player_number <= answer - 25:
    print("you are way low, guess higher")
