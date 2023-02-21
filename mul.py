n=int(input("Enter the number you need to find the multiplication table : "))
x=int(input("\nEnter the limit upto which the table should be created : "))
for i in range(1,x+1):
    print(n,"x",i,"=",n*i)
