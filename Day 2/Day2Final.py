print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentaje = int(input("What percentaje tip would you like to give? 10, 12, or 15? "))
many = int(input("How many people to split the bill? "))
ans = round(((100+percentaje)/100)*bill/many,2)
print(f"Each person should pay: ${ans}")