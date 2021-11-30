import math
list=[]
start=int(input("enter start"))
end=int(input("enter end"))
for a in range(start,end+1):
    for b in str(a):
        if int(b)%2!=0:
            break
    else:
      root=math.sqrt(a)
      if root%1==0:
          list.append(a)
print(list)
