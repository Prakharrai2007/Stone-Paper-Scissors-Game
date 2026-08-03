# To print the string according to the user input we can use for loop and range function

#n = int(input("Please tell me how many times you wan to print : - "))

#for i in range(n):
#     print(f"{i+1} : hello world")
#   print("hello world")

# To print the numbers in order

# n = int(input("Till where you want your numbers :- "))

# for i in range(1,n+1):
#     print(i)

# Print numbers in reverse order 

# n = int(input("Till where you want your numbers :- "))

# for i in range(n,0,-1):
#     print(i)

# To print the sum of numbers given by user

# n = int(input("till where you want your sum :- "))

# s = 0 

# for i in range(1,n+1):
#     s = s + i


# print(f"your sum is {s}")

# To print the factorial of a number given by user

# n = int(input("which number factorial you want :- "))

# fact = 1

# for i in range(1,n+1):
#     fact = fact * i 

# print(f"your factorial is {fact}")

# Print the sum of even and odd numbers given by user

# n = int(input("Tell your range:- "))

# even_sum = 0
# odd_sum = 0 

# for i in range(1,n+1):
#     if i%2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i 
    
# print(f"Hello your even sum is {even_sum} and your odd sum is {odd_sum}")


# Print the factors of a number given by user

# n = int(input("what number factors I want to find:-  "))

# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)

# To print the sum of factors of a number given by user

# n = int(input("what number factors sum you want:- "))
# s = 0

# for i in range(1, n+1):
#     if n%i ==0:
#         s = s + i

# print(f"your factors sum is {s}")

# Print the power of a number given by user

# a = int(input("tell your value :- "))
# b = int(input("tell your exponent :- "))
# power = a
# for i in range(b-1):
#     power = power * a

# print(f"After power your answer is {power}")

# To check Number is prime or not (1st method)

# n = int(input("give your number (prime check):- "))
# count = 0 

# for i in range(1,n+1):
#     if n % i == 0:
#         count = count + 1

# if count == 1:
#     print("your number is a unity number")
# elif count == 2:
#     print("your number is prime")
# else:
#     print("your number is composite")

# To check Number is prime or not  (2nd method) 

# n = int(input("give your number (prime check):- "))


# for i in range(2,n):
#     if n % i == 0:
#         print("sorry your number is composite")
#         break

# else:
#     print("your number is prime")

