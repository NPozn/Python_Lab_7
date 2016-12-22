import re

def ContainSymbols(s):
    return re.findall(r"[wrtpsdfghjklzxcvbnmцкнтглдшщзхфвпртсчб]", s) != []

exist = ContainSymbols(input("Введите слово"))
if exist == True :
    print("Есть согласная буква")
else:
    print("Согласной буквы нет")