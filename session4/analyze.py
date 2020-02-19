word = "magic"
nr_found = 0

with open("") as f:
    for line in f:
        line= line.lower()
        start=0
        while True:
            start = line.find(word,start)
            if start == -1:
                break
            nr_found=nr_found+1
            start=start+len(word)

print("In the book harry potter the word |{}| appears {}  times.".format(word,nr_found))

sum=0
import random
for i in range(10):
    number = random.randint(1,20)
    print(number)
    sum += number
print(sum)



# Functions

# alwaxs use "def" followed by a name of functionality
