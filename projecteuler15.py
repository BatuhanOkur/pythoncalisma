def latticePaths(n):
    list1 = []
    for i in range(1, n+2):
        list1.append(i)
    list2 = []
    for i in range(1, n+2):
        list2.append(list1)
    for i in range(0, n+1):
        for j in range(0, n+1):
            if j == 0 or i == 0:
                list2[i][j] = 1
            else:
                list2[i][j] = list2[i-1][j] + list2[i][j-1]
    return list2[n][n]

print(latticePaths(20))
