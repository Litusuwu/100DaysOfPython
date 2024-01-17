height = float(input())
weight = int(input())

BMI = (weight / height**2)

if BMI < 18.5 : 
    sti = "you are underweight."
elif 18.5 <= BMI < 25:
    sti = "you have normal weight."
elif 25 <= BMI < 30:
    sti = "you are slightly overweight."
elif 30 <= BMI < 35:
    sti = "you are obese."
elif 35 <= BMI :
    sti = "you are clinically obese."
    
print(f"Your BMI is {BMI}, {sti}\n since {weight} / ({height} x {height}) = {int(BMI)}")