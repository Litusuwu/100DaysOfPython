year = int(input())

if year % 400 == 0 :
    print("Is leap!")
elif year % 100 == 0 :
    print("Is not leap.")
elif year % 4 == 0:
    print("Is leap!")
else:
    print("Is not leap.")