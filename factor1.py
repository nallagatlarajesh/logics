num1=int(input())
print(num1,"factors are:")
print(1,end=" ")
factor=2
while factor<=num/2:
    if num1%factor==0:
        print(factor,end=" ")
    factor+=1
print(num,end=" ")
