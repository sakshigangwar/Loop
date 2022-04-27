num=int(input("enter the number"))
i=1
while i<=num:
    j=0
    while j<i:
        if j==0 or j==i-1:
            print("*",end=" ")
        else:
            if i!=num:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        j=j+1
    print()
    i=i+1




string="python"
i=0
while i<=5:
    j=0
    while j<=i:
        print(string[j],end=" ")
        j=j+1
    print()
    i=i+1



k=1
i=1
while i<=5:
    b=1
    while b<=5-i:
        print(" ",end=" ")
        b=b+1
    j=1
    while j<=k:
        print("*",end=" ")
        j=j+1
    k=k+1
    print()
    i=i+1



a=int(input("enter the number"))
i=1
while i<=a:
    print("q",i,"z",i)
    i=i+1

