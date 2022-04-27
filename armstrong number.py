i=int(input("enter the number check for armstrong number"))
num=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if num==sum:
    print("armstrong number")
else:
    print("this is not armstrong number")





























