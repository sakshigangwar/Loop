num=int(input("enter the number:"))
nir=0
sum=1
while num>0:
    nir=num%10
    sum=sum*nir
    num=num//10
print(sum)