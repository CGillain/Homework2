try:
    gross = int(input("Gross:"))
    child = int( input("Child:"))

except:
    print("Enter a proper number")
    exit()

if gross < 1000 :
    tax = 0.1 -(child*0.01)

elif gross < 2000 :
    tax = 0.12 - (child * 0.01)

elif gross < 4000 :
    tax = 0.14 - (child*0.005)

else:
    tax = 0.18 - (child*0.005)

print(gross-(gross*tax), 'is the net salary')



divisor = 3
for num in range (0,12,3):
    print(num/divisor)


for letter in 'Ahola':
    print(letter)


a=5
b=3
result=1
for i in range(b):
    current= result
    result = 0
    for j in range(a):
        result += current

print(result)


for i in range(1,11):
    for j in range (i, 11):
        print(i, "x", j, "=", i*j)