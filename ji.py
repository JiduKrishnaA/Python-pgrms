table=[[0,10,5],[10,20,10],[20,30,20],[30,40,40],[40,50,30],[50,60,20],[60,70,10],[70,80,5]]
print("Table: ")
print("Class frequency")
print(f"{table[0][0]}-{table[0][1]} {table[0][2]}")
for i in range(1,8):
    print(f"{table[i][0]}-{table[i][1]} {table[i][2]}")
mean=0
fsum=0
mid=0
prod=0
for i in range(8):
    x=(table[i][0]+table[i][1])/2
    mid.append(x)
    x=x*table[i][2]
    prod.append(x)
    mean=mean+x
    fsum+=table[i][2]
mean=mean/fsum
var=0
for i in range(8):
    x=0
    x=((mid[i]-mean)**2)
    var+=(x*table[i][2])
var=var/fsum
sd=var**0.5
cov=sd/mean
