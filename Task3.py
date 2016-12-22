def Plus(first, second):
    res = []
    for i in range(len(first)):
        temp = []
        for j in range(len(first[i])):
            temp.append(first[i][j] + second[i][j])
        res.append(temp)
    return res

def PrintMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{0} ".format(matrix[i][j]), end="")
        print("\n")
    print()

matrix = [[1, 2, 5 ,6], [4, 6, 9 ,2]]
PrintMatrix(matrix)
