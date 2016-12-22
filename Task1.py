def MaxMinElement (a = []):
    if len(a) != 0:
        max = a[0]
        min = a[0]
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
        if a[i] < min:
            min = a[i]
    return max,min
a = [12,-786,43,755,-345,-2321,11111]
x, y = MaxMinElement(a)
print("max = {0}, min = {1}".format(x,y))