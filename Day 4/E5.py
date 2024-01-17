line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
if position[0] == "A":
    po1 = 0
elif position[0]=="B":
    po1 = 1
elif position[0]=="C":
    po1 = 2
    
    
if position[1] == "1":
    po2 = 0
elif position[1]=="2":
    po2 = 1
elif position[1]=="3":
    po2 = 2
    
map[po2][po1] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")