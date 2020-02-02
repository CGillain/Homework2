
##################### INTRODUCTION TO PYTHON ##########################
## Student name: Céline Gillain

##### Homework 1 ######

### First Question ###

# 1. Write a program that asks for your name and prints: “Hello <name>!”.

# Entering your name as an input
yourname = input("Please enter your name: ")

# Printing out Output
print("Hello", yourname,"!")


### Second Question ###

# 2. Write a program that takes 2 numbers as input and prints the rounded up division.

# Inputting 2 numbers
x, y = [float(x) for x in input("Enter two numbers here (separated by a space): ").split()]

### Could have used int ((x/y) + 0.5)

# Dividing these 2 numbers
division = x/y

# Outputting the rounded up result
import math  # to use the rounding up function "math.ceil" and the number pi.
print("The result is: ", math.ceil(division))


### Third Question ###

# 3. Write a program that takes the radius of circle as input and prints the surface of the circle.

# The Surface of a circle is calculated as follows:
# Surface = pi * (radius**2)

# Inputting radius of a circle
radius = float(input("Please enter the radius of the circle to find the surface: "))

# Outputting Surface area of the circle
Surface = math.pi * (radius**2)
print("The surface of the circle is: ", Surface)

### Fourth Question ###
# 4. Write a program that behaves like a pocket calculator that can do: (+,-,*,/) of 2 numbers.

# Creating the pocket calculator based on user input as would be entered in a calculator
operation_result = eval(input('''
Please enter the mathematical operation you would like to complete
 by entering 2 numbers separated by any of these operators,
+ for additions
- for subtractions
* for multiplications or
/ for divisions: 
'''))

# Printing output
print("The result of the typed in operation is: ", operation_result)







