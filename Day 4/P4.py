import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

listGame = [ rock, paper, scissors]
dec = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(listGame[dec])
decPC = random.randint(0, 2)
print(f"Computer chose : \n {listGame[decPC]}")

if listGame.index(listGame[dec-1]) == listGame.index(listGame[decPC]) :
    print("You Win.")
elif listGame.index(listGame[dec]) == listGame.index(listGame[decPC-1]):
    print("You lose.")
else:
    print("Draw.")