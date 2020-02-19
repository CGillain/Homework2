### triangle with 3 numbers ###

# condition 1 : max < min 1 + max 2
# condition 2 : max = min1 = max 2 --> equilateral

numbers = []
count=0

while True:
    if count >= 3:
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


# Check if not triangle
if numbers [0] + numbers[1]<numbers[2]:
    print("This is not a triangle")
    exit()

# Check if equilateral
if numbers[0] == numbers[1] and numbers[1] == numbers[2]:
    print("it is an equilateral triangle")

# Check if isoscel
if numbers[0] == numbers[1] or numbers[1]==numbers[2]:
    print("This is a isoscel triangle")

# Check if rigth angel
if numbers[2]**2 == numbers[0]**2 + numbers[1]**2:
    print("right angle")

# Check if obtuse
if numbers[2]**2 > numbers[0]**2 + numbers[1]**2:
    print("obtuse")

# Check if acute
if numbers[2]**2 < numbers[0]**2 + numbers[1]**2:
    print("acute")




