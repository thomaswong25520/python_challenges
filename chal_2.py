def factoriall(n):
    if n == 0:
        return 1
    else:
        return(n*factoriall(n-1))

print(factoriall(8))
