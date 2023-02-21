books = dict()
n = int(input("Enter the number of books :"))
for i in range(n):
    b = input("Enter name of book :")
    num = input("Enter no of books available :")
    books[b] = num
print("Dictionary is created :",books)
while(1):
    c=int(input("Enter your choice :\n1: update \n2: add \n3: delete \n4: exit \n"))
    if(c==1):
        t = input("Enter the name book to update stock :")
        num = int(input("Enter no of books available :"))
        books[t] = num
        print("Dictionary is :",books)
    if(c==2):
        t = input("Enter the name book to add :")
        num = int(input("Enter no of books available :"))
        books[t] = num
        print("Dictionary is :",books)
    if(c==3):
        t = input("Enter the name book to delete :")
        books.pop(t)
        print("Dictionary is :",books)
    if(c==4):
        print("exit")
        break
