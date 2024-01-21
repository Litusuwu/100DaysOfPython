import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def extract(Sum, Cards):
    value = random.randint(1, 13)
    Sum+= value
    Cards.append(value)
    return Sum
    

def verify(mySum, opSum, MyCards, OpCards):
    print(f"Your final hand: {MyCards}")
    print(f"Computer's final hand: {OpCards}")
    
    if opSum > 21:
        print("You Win.")
        return
    elif mySum > 21:
        print("You Lose.")
        return
        
    if opSum < mySum :
        print("You Win.")
    elif opSum > mySum :
        print("You Lose.")
    else:
        print("Draw.")

def recursionBlackJack():
    os.system('clear')
    print(logo)
    
    MyCards =[]
    OpCards =[]
    MySum = 0

    MyCards.append(random.randint(1, 14))  
    MyCards.append(random.randint(1, 14))
    OpCards.append(random.randint(1, 14))
    OpCards.append(random.randint(1, 14))
    MySum = MyCards[0]+MyCards[1]
    OpSum = OpCards[0]+OpCards[1]
    while True:
        print(f"Your cards : {MyCards}, current score : {MySum}")
        print(f"Computer's first card : {OpCards[0]}")
        val = input("Type 'y' to get another card, type 'n' to pass : ")
        if MySum >= 21 or OpSum >=21 :
            verify(MySum, OpSum, MyCards, OpCards)
            break
        elif val == "y":
            MySum = extract(MySum, MyCards)
            OpSum = extract(OpSum, OpCards)
        elif val== "n":
            break
        if MySum >= 21 or OpSum >=21 :
            verify(MySum, OpSum, MyCards, OpCards)
            break
        
    val = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if val=="y":
        recursionBlackJack()    

recursionBlackJack()
