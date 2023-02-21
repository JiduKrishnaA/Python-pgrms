def prime(i):
    if i==1:
        return False
    for j in range (2,int(i/2)+1):
        if i%j==0:
            return False
    return True
f=open("f2.txt",'r')
for i in [int(x) for x in f.readlines()]:
    if prime(i):
        print (i)
