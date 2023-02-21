rows = int(input("Enter the Number of rows of matrix a : " ))
column = int(input("Enter the Number of Columns of matrix a : "))

print("Enter the elements of First Matrix:")
matrix_a= [[int(input()) for i in range(column)] for i in range(rows)]
print("First Matrix is: ")
for n in matrix_a:
    print(n)

rows1 = int(input("Enter the Number of rows of matrix b : " ))
column1 = int(input("Enter the Number of Columns of matrix b : "))
print("Enter the elements of Second Matrix:")
matrix_b= [[int(input()) for i in range(column1)] for i in range(rows1)]
for n in matrix_b:
    print(n)

if(rows != rows1 or column != column1):
    print("addition not possible")
else:
    result=[[0 for i in range(column)] for i in range(rows)]

    for i in range(rows):
        for j in range(column):
            result[i][j] = matrix_a[i][j]+matrix_b[i][j]

    print("The Sum of Above two Matrices is : ")
    for r in result:
        print(r)
