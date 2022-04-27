num=int(input("enter the number"))
a=65
i=1
while i<=num:
    j=1
    while j<=num:
       print(chr(a),end=" ")
       a=a+1
       j=j+1
    print()
    i=i+1