import os
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print("Welcome to the secret auction program")
bidders = {}
old = 0
while True:
    name = input("What is your name? : ")
    money = int(input("What is your bid? : $"))
    bidders[name] = money
    print("Are there any other bidders? Type 'yes' or 'no'.")
    bulean = input()
    if money > old :
        key = name
        old = money
    if bulean == "yes":
        os.system('clear')
    elif bulean == "no":
        os.system('clear')
        print(f"The winner is {key} with a bid of ${old}.")
        break
    