import re

def ContainSymbols(s):
    return re.findall(r"[wrtpsdfghjklzxcvbnmцкнтглдшщзхфвпртсчб]", s) != [] and re.findall(r"[-]", s) == []

input_data=input("Введите предложение: ").split(",",maxsplit=-1)

for i in range(len(input_data)):
    if(ContainSymbols(input_data[i])==True):
        print(input_data)

