
number=int(input("enter the number :"))
sum=0
i=1
while i<=number:
    num=int(input("enter the number"))
    sum=sum+num
    i+=1
print("sum",sum)
print("avg",sum/number)
if (sum/number)%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")

