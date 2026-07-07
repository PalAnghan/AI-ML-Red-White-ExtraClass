print("------------------------")
# Print “Hello, World!

print("Hello World!")


print("------------------------")
# Take user input and display it

name = input("Write Your Name : ")
print(f"Yor Name : {name}")


print("------------------------")
# Swap two variables

a = 10
b = 5
print(f"Before Swap - First Number : {a}, Second Number : {b}")
a, b = b, a
print(f"After Swap - First Number : {a}, Second Number : {b}")


print("------------------------")
# Find square and cube of a number

n = int(input("Enter a Number to find Square :"))

print(f"Square Number is : {n*n}")


print("------------------------")
# Convert Celsius to Fahrenheit

c = 15

f = c * 1.8 + 32

print(f"Celsius : {c} to Fahrenheit : {f}")

print("------------------------")
# Check if a number is even or odd

num = int(input("Enter a Number : "))

if num%2==0:
    print(f"The Number is EVEN Number : {num} ")
elif num%2!=0:
    print(f"The Number is ODD Number : {num} ")
else :
    print("INVALID NUMBER !")

print("------------------------")
# Find the largest of three numbers

a = 5
b = 15
c = 5

if a>=b :
    if a>=c:
        print("First Number is Large!")
    else:
        print("Third Number is Large!")
elif b>=a :
    if b>=c:
        print("Second Number is Large!")
    else:
        print("Third Number is Large!")


print("------------------------")
# Create a simple grading system

number = float(input("Enter Your Marks : "))

match number:
    case number if 85 <= number <= 100:
        print("You Receive Grade A , Congratulaition!")
    case number if 75 <= number <= 84:
        print("You Receive Grade B , Congratulaition!")
    case number if 60 <= number <= 74:
        print("You Receive Grade C , Congratulaition!")
    case number if 34 <= number <= 59:
        print("You Receive Grade D , Congratulaition!")
    case number if 0 <= number <= 33:
        print("YOU ARE FAIL......")
    case _:
        print("INVALID NUMBER.....")


print("------------------------")
# Check if a year is a leap year

year = int(input("Enter Current Year :"))

if year%4==0:
    print(f"This Year is LeapYear {year}")
elif year%4!=0:
    print(f"This is Not LeapYear {year}")
else :
    print("INVALID NUMBER!")
