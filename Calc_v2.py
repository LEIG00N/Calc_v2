#Calc v2
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.BLUE)

mypass = input("Пароль: ")
if mypass == "108":
    print(Fore.GREEN)
    b = input("Действие(+, -):")
    s = int(input("Число: "))
    a = int(input("Число: "))

    if b == "+":
        c = s + a
        print(Fore.YELLOW)
        str(print(s,"+", a, "=", c))

    if b == "-":
        c = s - a
        print(Fore.YELLOW)
        str(print(s,"-", a, "=", c))

else:
    print(Fore.RED)
    print("Неверный пароль")

input()
