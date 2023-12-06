start=int(input("enetr the starting value :"))
end=int(input("enter the ending value:"))
print("prime numbers between ",start,"and",end,"is")
for i in range(start,end):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
