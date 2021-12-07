n=int(input("enter value of n"))
a=0
b=1
sum=0
count=1
while(count<=n):
     print(sum,"\n")
     a=b
     b=sum
     sum=a+b
     count+=1
     
