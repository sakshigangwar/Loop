num=int(input("enter number"))
a=num
i=0
while(num>0):
    c=num%10
    i=i*10+c
    num=num//10
if(a==i):
    print("palindrome number")
else:
    print("this is not palindrome number")







num=int(input("enter the numbr:"))
a=num
i=0
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
if a==rev:
    print("palindrome",rev)
else:
    print("not palindrome",rev)
