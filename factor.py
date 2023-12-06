num=int(input("enetr the number:"))
print(num,"factors are")
for i in range(1,num+1):
    if num%i==0:
        print(i)
