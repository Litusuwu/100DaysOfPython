print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

w1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ")

if w1.lower() == "right":
    print("FAll into a hole. GAME OVER.")
else:
    w2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across." )
    if w2.lower() == "swim":
        print("Attacked by trout. GAME OVER.")
    else:
        w3 = input("You arrive at the island unharmed. There is a house with 3 doors. ONe red, one yellow and one blue. Which colour do you choose? ")
        
        if w3.lower()=="red":
            print("Burned by fire. GAME OVER.")
        elif w3.lower()=="blue":
            print("Eaten by beasts. GAME OVER. ")
        elif w3.lower() == "yellow":
            print("YOU WIN.")
        else:
            print("GAME OVER.")
        