a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [5, 6, 7, 8, 9, 29, 44, 16]
print("Первое множ-во: {0}".format(a))
print("Второе множ-во: {0}".format(b),end="\n\n")

print("Разность:{0} ".format(set(a)-set(b)))
print("Объедение:{0} ".format(set(a) | set(b)))
print("Пересечение:{0}".format(set(a) & set(b)))
print("Симметрическая разность: {0}".format((set(a) | set(b)) - (set(a) & set(b))))