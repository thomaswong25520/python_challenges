nums = "0100,0011,1010,1001"

l = nums.split(",")
l2 = [i for i in l if int(i,2)%5==0]

for i in l2:
    print(i)

