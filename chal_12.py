l = [str(i) for i in range(1000,3001) if int(str(i)[0])%2==0 and int(str(i)[1])%2==0 and int(str(i)[2])%2==0 and int(str(i)[3])%2==0]

print(','.join(l))
