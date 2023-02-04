X = [[10, 20],
    [50, 30]]

Y = [[20, 30],
    [40, 10]]

result = [[0, 0],
         [0, 0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
