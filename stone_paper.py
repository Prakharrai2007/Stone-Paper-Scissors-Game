# Stone paper scissor game

import random 

cscore = 0             # Computer score
hscore = 0             # Human score

while True:
    print(f"Current Scores You - {hscore} Computer - {cscore}\n")
    user = int(input("1 for Stone , 2 for Paper , 3 for Scissors choose :- "))

    com = random.randint(1,3)

    if user == 1 and com == 3:
        hscore+=1 
        print("You won the Round \n")

    elif user == 2 and com == 1:
        hscore+=1 

        print("You won the Round \n")

    elif user == 3 and com == 2:
        hscore+=1 

        print("You won the Round \n")

    elif user == com:
        print("It was a draw")

    else:
        cscore+=1 
        print("Computer won this Round ")
    

    if cscore == 5:
        print("Computer won this Game 👿")
        break
    elif hscore == 5:
        print("Congratulations You Won 🏅")
        break


    