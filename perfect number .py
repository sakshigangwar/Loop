num=int(input("enter the number"))
sum=0
i=1
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print(num,"is perfect")
else:
    print(num,"is not perfect number")

    

