print("===== Q.1 =====")


import math
'''
def calculate(number):
    print("square root of", number, "is", math.sqrt(number))
    print("factorial of", number, "is", math.factorial(number))
    print("power of", number, "is", math.pow(number, 2))

number = int(input("Enter a number: "))
calculate(number)
'''

print("===== Q.2 =====")
'''
def calculate(number):
    print("Area of circle with radius", number, "is", math.pi * number * number)
    if number > 0:
        print("Logarithm of", number, "is", math.log(number))
    else:
        print("Logarithm is not defined for non-positive numbers.")
        

number = int(input("Enter a number: "))
calculate(number)
'''

print("===== Q.3 =====")
'''
def Trigonomtry(number):
    print("Sine of", number, "is", math.sin(math.radians(number)))
    print("Cosine of", number, "is", math.cos(math.radians(number)))
    print("Tangent of", number, "is", math.tan(math.radians(number)))


number = int(input("Enter a number: "))
Trigonomtry(number)
'''

print("===== Q.4 =====")
'''
def calculate(value):
    print("Ceiling of", value, "is", math.ceil(value))
    print("Floor of", value, "is", math.floor(value))
    print("Absolute value of", value, "is", math.fabs(value))

Value = int(input("Enter a number: "))
calculate(Value)
'''

print("===== Q.5 =====")
'''
import random
numbers = []

for i in range(10):
    number = random.randint(1, 10)
    numbers.append(number)

print("Random numbers:", numbers)   
'''

print("===== Q.6 =====")
'''
import random

dice = random.randint(1, 6)
print("Random number between 1 and 6:", dice)

players = ["Rohit" , "Sachin" , "Rahul" , "Mahendra" , "Virat" , "Samson"]

print(players)

random.shuffle(players)

print("Shuffle Players : " , players)

'''
print("===== Q.7 =====")
'''
import random

students = ["Rahul" , "Vivek" , "Pal" , "Bahubali" , "Nikunj",  "Shreya" , "Rohit" , "Sakshi" , "Riya" , "Anjali"]

student = random.choice(students)

print(student)
'''

print("===== Q.8 =====")

import random
# rock paper scissor

p1 = ["Rock" , "Paper" , "Scissor"]
p2 = ["Rock" , "Paper" , "Scissor"]

p1_choice = random.choice(p1)
p2_choice = random.choice(p2)

print("Player 1 choice: ", p1_choice)
print("Player 2 choice: ", p2_choice)
print("Winner is: ", end = "")
print("Player 1" if (p1_choice == "Rock" and p2_choice == "Scissor") or (p1_choice == "Paper" and p2_choice == "Rock") or (p1_choice == "Scissor" and p2_choice == "Paper") else ("Player 2" if (p2_choice == "Rock" and p1_choice == "Scissor") or (p2_choice == "Paper" and p1_choice == "Rock") or (p2_choice == "Scissor" and p1_choice == "Paper") else "Draw"))
