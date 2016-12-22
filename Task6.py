import re

def ContainSymbols(s):
    return re.findall(r"[wrtpsdfghjklzxcvbnmцкнтглдшщзхфвпртсчб]", s) != [] and re.findall(r"[-]", s) == []

input_data = re.split(r";|,|:|!|\s+",input("Введите предложение: "))
print(input_data)
dic = {}
for x in input_data:
    if ContainSymbols(x):
        dic[x] = dic.get(x, 0) + 1
print(dic)