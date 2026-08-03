# DEMONSTRATION OF IF ELSE STATEMENTS :

age = int(input("please tell your age - "))

print("vote") if age >= 18 else print("not vote")

# DEMONSTRATION OF IF , ELIF ,ELSE STATEMENTS :

money = int(input("please give me 10,20 or 30 rs or above "))

if money == 10:
     print("I will have a choco bar")

elif money == 20:
     print("I will have a mango dolly")

elif money == 30:
    print("I will have a cone")

else:
    print("I will have full course meal")

# if else statement with logical operators

a = 10
b = 40
c = 30

if a > b and a > c:
    print("A is the Largest number")
elif b > a and b > c:
    print("b is the Largest number")
else:
    print("C is the largest number")

# IF STATEMENT WITH PASS STATEMENT:

A=10
B=20
C=30

if A > B and A > C:
    pass
elif B > A and B > C:
    pass
else:
    print("C is the largest number")    