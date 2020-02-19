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