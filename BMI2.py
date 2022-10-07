height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
b = float (weight/(height*height))
b1 = round (b)
if b1 <= 18.5:
    print ( f"Your BMI is {b1}, You are underweight")
elif b1 <= 25:
    print( f"Your BMI is {b1}, You have a normal weight")
elif b1  <=30:
    print ( f"Your BMI is {b1}, you are slightly overweight") 
elif b1 <=35:
    print ( f"Your BMI is {b1}, you are obese")
else:
    print ( f"Your BMI is {b1}, you are clinically obese")