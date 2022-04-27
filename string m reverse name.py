user=input("enter the string")
i=len(user)
string=""
while i>0:
    string+=user[i-1]
    i-=1
print(string)