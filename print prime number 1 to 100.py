num=int(input("enter the number"))
num_1=int(input("enter the number"))
a=1
while a<=num_1:
    i=1
    count=0
    while (i<=a):
        if a%i==0:
            count+=1
        i=i+1
    if count==2:
        print(a)
    a=a+1




# n=int(input("enter the number:"))
# count=0
# i=1
# while (i<=n):
#     if n%i==0 :
#         count=count+1
#     i=i+1
# if (count==2):
#     print("prime number")
# else:
#     print("prime number ni hai")




