import random

names_string = input()
names = names_string.split(", ")
num = random.randint(0, len(names)-1)
print(names[num]+" is going to buy meal today!")
