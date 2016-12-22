def Plus(first, second):
    res = []
    for i in range(len(first)):
        temp = []
        for j in range(len(first[i])):
            temp.append(first[i][j] + second[i][j])
        res.append(temp)
    return res


def Multip(first, second):
    res = []
    temp = []
    for i in range(len(first)):
        sum = 0
        temp =[]
        for j in range(len(first[i])):
            for k in range(len(second[j])):
                sum = sum +(first[i][j] * second[k][i])
            temp.append(sum)
        res.append(temp)
        #print(temp)
    return res

def PrintMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{0} ".format(matrix[i][j]),end="")
        print("\n")
    print()

matrix1 = [[1, 2, 5 , 6], [4, 6, 9 ,2],[4,1,2,3],[8,7,6,4]]
matrix2 = [[3, 4, 8, 12],[7, 10 ,11 ,23],[8,7,6,4],[4,1,2,3]]
#PrintMatrix(Plus(matrix1,matrix2))
PrintMatrix(Multip(matrix1,matrix2))
