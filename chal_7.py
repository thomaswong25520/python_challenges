l = str(input("Enter row,col : ")).split(',')

row, col = int(l[0]), int(l[1])

l2 = []

for i in range(row):
    l3 = []
    for j in range(col):
        l3.append(i*j)
    l2.append(l3)

print(l2)
