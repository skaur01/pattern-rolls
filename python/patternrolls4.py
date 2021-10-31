"""
For n=5, Output:

*********
 *******
  *****
   ***
    *
"""
n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,2*(n+1)-2*i):
        print("*",end="")
    print()
