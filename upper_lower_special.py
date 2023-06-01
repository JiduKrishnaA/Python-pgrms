f=open("f2.txt","r")
data=f.read()
words=data.split()
print("number of words = ",len(words))
f=open("f2.txt","r")
c=0
count=f.read()
cl=count.split("\n")
for i in cl:
    if i:
        c=c+1
print("no of lines = ",c)
def num(d):
    upper, lower, special = 0, 0, 0
    for i in range(len(d)):
        if d[i].isupper():
            upper += 1
        elif d[i].islower():
            lower += 1
        else:
            if(d[i]!=' '):
                if(d[i]!='\n'):
                    special += 1
    print('Upper case letters:', upper)
    print('Lower case letters:', lower)
    print('Special characters:', special)
f=open("f2.txt","r")
d=f.read()
num(d)
