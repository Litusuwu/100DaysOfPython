logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def addition(num1, num2):
    return num1 + num2 
def substraction(num1 , num2):
    return num1 - num2 
def multiply(num1, num2):
    return num1*num2 
def divide(num1, num2):
    return num1/num2

diction = {
    "+":addition,
    "-":substraction,
    "/":divide,
    "*":multiply
}
flag = "n"

while True:
    
    if flag =="n":
        value = float(input("What's the first number?: "))
        print("+ \n -\n *\n / \n")
    else:
        value = key(value, value2)
    operation = input("Pick an operation: ")
    value2 = float(input("What's the next number?: "))

    key = diction[operation]
    print(f"{value} + {value2} = {key(value, value2)}")

    flag = input(f"Type 'y' to continue calculating with {key(value, value2)} or type 'n' to start a new calculation: ")
