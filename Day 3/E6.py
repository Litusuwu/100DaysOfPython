print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age?"))
    
    if age < 12 :
        print("Please pay 5$. ")
        prize = 5
    elif age <=18:
        print("Please pay 7$. ")
        prize = 7
    else:
        print("Please pay 12$. ")
        prize = 12
        
    wants = input("Do you want a photo taken? Y or N. ")
    
    if wants == "Y" :
        prize+=3
    print(f"Your final bill is {prize} $. ")
else:
    print("Sorry, you have to grow taller before you can ride.")