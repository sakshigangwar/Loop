a=input("enter the alphabate ") 
i=0
count=0
count_1=0
while i<len(a):
    if (a[i]=="a"or a[i]=="e"or a[i]=="i" or a[i]=="o" or a[i]=="u"):
        count=count+1
        # print(a[i],"vovel")
    else:
        count_1=count_1+1
        # print(a[i],"consonant")
    i=i+1
print(count,"Vovel")
print(count_1,"Consonant")








 
