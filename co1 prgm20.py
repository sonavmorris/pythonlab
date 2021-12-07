l1=[]
l2=[]
n=int(input("enter no:"))
for x in range(0,n):
    y=int(input("enter integer:"))
    l1.append(y)
    if(y%2!=0):
        l2.append(y)
print(l1)
print("without even no:",l2)
