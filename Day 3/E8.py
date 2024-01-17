print("THe Love Calculator is calculating your score")
name1 = input()
name2 = input()
name1 = name1.upper()
name2 = name2.upper()
var1 = 0
var2 = 0
var1 += name1.count("T") + name2.count("T")
var1 += name1.count("R") + name2.count("R")
var1 += name1.count("U") + name2.count("U")
var1 += name1.count("E") + name2.count("E")
var2 += name1.count("L") + name2.count("L")
var2 += name1.count("O") + name2.count("O")
var2 += name1.count("V") + name2.count("V")
var2 += name1.count("E") + name2.count("E")

if var1+var2 < 10 or var1+var2 > 90 :
    print(f"Your score is {var1*10+var2}, you go togheter like coke and ment.")
elif 50 >= var1+var2 >= 40 :
    print(f"Your score is {var1*10+var2}, your are alright together.")
else:
    print(f"Your score is {var1*10+var2}")