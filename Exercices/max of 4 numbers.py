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