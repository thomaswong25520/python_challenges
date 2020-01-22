c = 50
h = 30

d = str(input("Enter comma separated values: "))

d_list = d.split(',')

val = [str(round(((2 * c * int(i)) / h) ** (1/2), 0)) for i in d_list]

print(','.join(val))


