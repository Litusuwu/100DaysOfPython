import random
print("Welcome to the PyPassword Generator!\nHow many letters would you like in your password?")
tot = int(input())
symb = int(input("How many symbols would you like?\n"))
num = int(input("How many numbers would you like?\n"))
ans = ""
symbols=["*", "%", "&", ")", ")", "=", "+", "-", "$","!"]
letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
lista = [symbols, letters, numbers]

for i in range(1, (tot+1)):
    ans+=random.choice(letters)
for i in range(1, (symb+1)):
    ans+=random.choice(symbols)
for i in range(1, (num+1)):
    ans+=random.choice(numbers)
ans2 = "".join(random.sample(ans, len(ans)))
print(f"Your password is: {ans2}")
    
    