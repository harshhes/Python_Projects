import colorama #adding colour text feature
from colorama import Fore, Back
colorama.init(autoreset=True)

print("------Welcome to the BMI Calculator------")
height = (input("Enter you height in metres:"))
if "." in height:
    height= float(height)
else:
    height= int(height)
weight = (input("Enter your weight in Kgs: "))
if "." in weight:
    weight= float(weight)
else:
    weight= int(weight)

# bmi calculation and correcting the answer to two decimal places.
bmi = (weight/(height*height))

if bmi>0:
    if bmi < 18.5:
        print(bmi, " You are Underweight. Gain some weight. Starting exercising. Eat nutritious diet")
    elif bmi > 18.5 and bmi < 25.0:
        print(bmi, " Your BMI is healthy")
    elif bmi > 25.0 and bmi < 30.0:
        print (bmi," You are Overweight. Lose some weight. Starting exercising. Eat balanced diet")
    else:
        print(bmi,"Your BMI says you are Obese.")
else:
    print(Fore.BLACK+Back.RED+"Invalid credentials!!!") # to printout the message in Red colour.

