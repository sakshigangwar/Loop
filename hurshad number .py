num=int(input("enter the number :"))
i=num
sum=0
while (i>0):
    k=i%10
    i=i//10
    sum+=k
if num%sum==0:
    print(num,"harshad number")
else:
    print(num,"not harshad number") 


# a=int(input("enter the number"))
# dec=0
# i=0
# while a>0:
#     rem=a%10
#     dec=dec+rem*2**i
#     a=a//10
#     i=i+1
# print(dec)



