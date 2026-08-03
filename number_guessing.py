# Number guessing game and this is my 2nd code

import random 

num = random.randint(1,100)

tries = 0 
while True:
    guessed = int(input("guess the number between 1 - 100 : "))
    tries += 1 
    if guessed == num:
        print(f"Congratulations you found your number in {tries} tries")
        break
    elif guessed > num:
        print("Sorry you need to go lower\n")
    elif guessed < num:
        print("Sorry you have to go a little upper\n")