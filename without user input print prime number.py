i=1
while i<=100:
    n=1
    count=0
    while n<=i:
        if i%n==0:
            count=count+1
        n=n+1
    if count==2:
        print(i)
    i=i+1
    


