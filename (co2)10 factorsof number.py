num=int(input("enter the number"))
print("factors of",num,"are:")
for i in range(1,num+1):
    if num%i==0:
        print(i)
        
