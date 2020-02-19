### Exercices ###

numbers = []
count=0

while True:
    if count >= 4:
        break
    number=input("Enter a number: ")
    try:
        number= int(number)
    except:
        print("That was not a number")
        continue
     #We have a proper number
    numbers.append(number)
    count += 1

numbers.sort()
print("The maximum is {}".format(numbers[3]))



# Another way

my_numbers= input("Please give me 4 numbers, seperated by, ")

list_numbers= my_numbers.split(", ")

#print(list_numbers)

numbers= []
for i in list_numbers:
    try:
        numbers.append(int(i))
        continue
    except:
        print("that was not a number")
numbers.sort()
print(numbers)

### Average of 4 random numbers ###

import random

numbers = []
sum = 0
for i in range(1000):
    number.append(random.randint(0, 100))
    sum += number[-1]  # the new number is the last one in the list

print("The average of {} is {}".format(numbers, sum / 1000))

a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)
d = random.randint(0, 100)

print("The Average is {}".format((a + b + c + d) / 4))
