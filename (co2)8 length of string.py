s=input("enter string:")
s=s.split(" ")
a=[]
for i in s:
    a.append(i)
max=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max):
        max=len(i)
        temp=i
print("the word with the largest length is:",temp,"and length is:",max)
