class q:
    def __init__(self):
        self.a=[]
    def insert(self,k):
        if len(self.a)>=n:
            print("queue overfolw ")
            print(self.a)
        else:
            self.a.append(k)
            print(self.a)
    def delet(self):
        if len(self.a)<=0:
            print("queue is empty ")
        else:
            self.a.pop(0)
            print(self.a)
    def dis(self):
        print(self.a)        
q=q()  
          
n = int(input("Enter the no of elements : "))
c=1
while(c>0 and c<5):
    c=int(input("Enter the choice 1 insert 2 delete 3 show 4 exit "))
    if (c==1):
        k=int(input("Enter the element : "))
        q.insert(k)
    elif (c==2):
        q.delet()
    elif (c==3):
        q.dis()
    elif (c==4):
        break
    else:
        print("Invalid choice")