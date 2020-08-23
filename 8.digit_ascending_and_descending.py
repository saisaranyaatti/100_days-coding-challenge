n=int(input("enter a number"))
asc=des=nue=0
ele=n%10
n//=10
while n>0:
    if ele>n%10:
        asc+=1
    elif ele<n%10:
        des+=1
    elif ele==n%10:
        nue+=1
    ele=n%10
    n//=10
if des==0 and nue==0 and asc!=0:
    print("aescending")
elif asc==0 and nue==0 and des!=0:
    print("descending")
elif asc==0 and des==0 and nue!=0:
    print("neutral")
else:
    print("no order")



n=input("enter a number")
asc=des=nue=0
for i in range(len(n)-1):
    if n[i]<n[i+1]:
        asc+=1
    elif n[i]>n[i+1]:
        des+=1
    elif n[i]==n[i+1]:
        nue+=1
if asc==len(n)-1:
    print("aescending")
elif des==len(n)-1:
    print("descending")
elif nue==len(n)-1:
    print("nuetral")
else:
    print("no order")



n=input()
asc=n[0]<n[1]
des=n[0]>n[1]
neu=n[0]==n[1]
i=1
while i<len(n)-1:
    if asc:
        asc=n[i]<n[i+1]
    elif des:
        des=n[i]>n[i+1]
    elif neu:
        neu=n[i]==n[i+1]
    i+=1
if asc:
    print("ascending")
elif des:
    print("descending")
elif neu:
    print("neutral")
else:
    print("no order")      


               
    
