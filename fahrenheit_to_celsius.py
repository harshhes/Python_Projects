import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def convert(a):
    f = float(a)
    ans= (f-32)* 5/9
    return Fore.BLACK+Back.RED+f'{ans}°C'  # to display answer in Red colour 

print(convert(int(input("Enter temperature in fahrenheit which you want to convert to celsius: "))))
