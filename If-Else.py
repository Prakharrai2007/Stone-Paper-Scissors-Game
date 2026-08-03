
# Number comparison 

#def new_func():
    #if a >b:
        #print(f"{a} is greater than {b}")
    #elif b> a:
       #print(f"{b} is greater than {a}")
    #else:
       #print(f"{a} is equal to {b}")

#new_func()

# Finding the gender of the user

#gen = input("Please tell your gender in Character(m,f) : - ")

# if gen == 'm' or gen == "M":
#     print("hello sir how are you")
# elif gen == "F" or gen == "f":
#     print("hello mam how are you ")
#else:
#print("wrong input only provide m or f")


# Check the number is even or odd

# a = int(input("please tell your number:- "))

# if a % 2 == 0:
#     print("your number is even")
# else:
#     print("your number is odd ")

# Eligibility of voting

# name = input("please tell your name:- ")
# age = int(input("please tell your age:- "))

# if age >= 18:
#     print(f"Hello {name} you can vote")
# else:
#     print(f"Hello {name} sorry you can vote after {18 - age} years")


# Finding the week day from the number given by user

# a = int(input("please tell your day(1-7):- "))

# if a == 1:
#     print("Monday it is")
# elif a == 2:
#     print("Tuesday it is")
# elif a == 3:
#     print("Wednesday it is")
# elif a == 4:
#     print("Thursday it is")
# elif a == 5:
#     print("Friday it is")
# elif a == 6:
#     print("Saturday it is")
# elif a == 7:
#     print("Sunday it is")
# else:
#     print("sorry your input is wrong")

# Comparison of three numbers

# a = int(input("Please tell your 1st numbers : - "))
# b = int(input("Please tell your 2nd numbers : - "))
# c = int(input("Please tell your 3rd numbers : - "))

# if a== b and b == c:
#     print("All the numbers are equal ")
# elif a == b or b == c or c ==a:
#     print("Any two numbers are equal")
# elif a > b and a > c:
#     print(f"{a} is the greatest number")
# elif b > a and b> c:
#     print(f"{b} is the greatest number")
# else:
#     print(f"{c} is the greatest number")


# Check the year is leap year or not
 
# year = int(input("please tell your year :- "))

# if year % 100 == 0 and year %400 == 0:
#     print("its a leap year")
# elif year %100 != 0 and year % 4 == 0:
#     print("its a leap year ")
# else:
#     print("sorry its not a leap year")

#Discount on the bill amount

bill = int(input("please tell your total amount : - "))

if bill >= 1000 and bill <= 4999:
    print(f"you got a discount of 10% your final amount is {(bill *90)/100}")

elif bill >= 5000:
    print(f"you got a discount of 20% your final amount is {(bill *80)/100}")

else:
    print("sorry no discount for you")


# Alphabet check for vowel or consonent

# char = input("please tell your Alphabet :- ")

# if char in "aeiouAEIOU":
#     print("its a vowel")
# else:
#     print("its a consonent")
