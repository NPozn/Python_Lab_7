import re

def ContainSymbols(s):
    return re.findall(r"[wrtpsdfghjklzxcvbnmцкнтглдшщзхфвпртсчб]", s) != [] and re.findall(r"[-]", s) == []

a = re.split(r";|,|:|!",input("Введите предложение: "))
print("Слова с согласными буквами :")
for i in range(len(a)):
    if ContainSymbols(a[i]) == True:
        print(a[i])