def armstrong(n):

    sum=0
    num=n
    while(num>0):
        n1=num%10
        sum+=n1*n1*n1
        num=num//10
    return sum
n=int(input("enter a number:"))
result=armstrong(n)
print(result)
if n==result:
      print(result,"is armstrong")
else:
      print(result,"not armstrong")
