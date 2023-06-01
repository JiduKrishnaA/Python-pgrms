n=int(input("enter no of elements : "))
c=1
k=0
class demo:
    def __init__(self):
        self.a=[]
    def insert(self,k):
        if(len(self.a)>=n):
            print("stack overflow : ")
            print(self.a)
        else:
            self.a.append(k)
            print(self.a)
            
    def delete(self,k):
        if len(self.a)<=0:
            print("stack underflow :")
            print(self.a)
        else:
            self.a.pop()
            print(self.a)
    def display(self):
        print(self.a)
        
d= demo()
while(c>0 and c<5):
    c=int(input("Enter 1 for insert 2 for delete and 3 for display 4 exit : "))
    if(c==1):
        k=int(input("Enter the element : "))
        d.insert(k)
    elif(c==2):
        d.delete(k)
    elif(c==3):
        print("The stack is : \n")
        d.display()
    elif(c==4):
        print("exit")
        break
    else:
        print("try again :  Enter 1 for insert 2 for delete and 3 for display 4 exit : ")
    
