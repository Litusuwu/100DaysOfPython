import menu
import random
import os

def report(valor):
    print(f"Water : {valor['water']} ml")
    print(f"Milk : {valor['milk']} ml")
    print(f"Coffee : {valor['coffee']} g")

def coffee(word, valor):
    if word=="espresso":
        if menu.MENU['espresso']['ingredients']['water'] > valor['water'] :
            print("Sorry, there is not enough water. ")
            return False
        elif menu.MENU['espresso']['ingredients']['coffee'] > valor['coffee'] :
            print("Sorry, there is not enough coffee. ")
            return False
         
    elif word=="latte":
        if menu.MENU['latte']['ingredients']['water'] > valor['water'] :
            print("Sorry, there is not enough water. ")
            return False
        elif menu.MENU['latte']['ingredients']['coffee'] > valor['coffee'] :
            print("Sorry, there is not enough coffee. ")
            return False
        elif menu.MENU['latte']['ingredients']['milk'] > valor['milk'] :
            print("Sorry, there is not enough milk. ")
            return False
    else:
        if menu.MENU['cappuccino']['ingredients']['water'] > valor['water'] :
            print("Sorry, there is not enough water. ")
            return False
        elif menu.MENU['cappuccino']['ingredients']['coffee'] > valor['coffee'] :
            print("Sorry, there is not enough coffee. ")
            return False
        elif menu.MENU['cappuccino']['ingredients']['milk'] > valor['milk'] :
            print("Sorry, there is not enough milk. ")
            return False
    return True
        
def func():
    valor = menu.resources
    os.system('clear')
    while True:
        
        word = input("What would you like? (espresso/latte/cappuccino): ")
        if word == "report":
            report(valor)
        elif word == "off":
            break
        else:
            flag = coffee(word, valor)
            if flag:
                costo = menu.MENU[word]['cost']
                print("Please insert coins.")
                quarters = int(input("How many quarters?:  "))
                dimes = int(input("How many dimes?:  "))
                nickles = int(input("How many nickles?:  "))
                pennies = int(input("How many pennies?:  "))
                
                presupuesto = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
                
                if costo > presupuesto : 
                    print("Sorry, that's not enough money. Money refunded.")
                else:
                    print(f"Here is ${round(presupuesto-costo, 2)} in change.")
                    print(f"Here is your {word}, ENJOY!!!")
                    valor['water'] = valor['water'] - menu.MENU[word]['ingredients']['water']
                    valor['coffee'] = valor['coffee'] - menu.MENU[word]['ingredients']['coffee']
                    if word != "espresso":
                        valor['milk'] = valor['milk'] - menu.MENU[word]['ingredients']['milk']
            
    
    
        
func()
        