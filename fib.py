i=0
j=1
s=0
n=int(input("Enter the limit : "))
if(n<0):
    print("Invalid input...")
if(n==1):
    print(i)
if(n>1):
    for k in range(1,n+1):
        print(i)
        s=i+j
        i=j
        j=s
        s=s+1
