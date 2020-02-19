### Introduction to Python ###
######## Homework 4 ##########

# In the triangle problem: calculate and print the area of the triangle

####---------- Code as done in class ------------####
numbers=[]
count=0
while True:
    if count >= 3:
        break
    number= input("Enter a number: ")
    try:
        number= int(number)
    except:
        print("That was not a number")
        continue
    #We have a proper number
    numbers.append(number)
    count += 1
numbers.sort()
# check if not triangle
if numbers[0]+numbers[1]<numbers[2]:
    print("it's not a triangle")
    exit()
# check if equilateral
if numbers[0]==numbers[1] and numbers [1]== numbers[2]:
    print(" it is an equilateral triangle")
#check if isosels
if numbers [0]==numbers[1] or numbers[1]== numbers[2]:
    print("isosceles")
#check if right angle
if numbers[2]**2== numbers[0]**2+numbers[1]**2:
    print("right angle")
#check if obtue
if numbers[2]**2> numbers[0]**2+numbers[1]**2:
    print("obtuse angle")
if numbers[2]**2< numbers[0]**2+numbers[1]**2:
    print("acute angle")



####---------- New piece of code ------------####

# Heron's Formula

# Calculating semi perimeter:

semi_perimeter = (numbers[0]+numbers[1]+numbers[2])/2

# print("The semi-perimeter of the triangle is:", semi_perimeter)

# Calculating the Area of the triangle if it is a triangle
import math

area = math.sqrt(semi_perimeter*(semi_perimeter-numbers[0])*(semi_perimeter-numbers[1])*(semi_perimeter-numbers[2]))
print("The area of the triangle is: ", area)
