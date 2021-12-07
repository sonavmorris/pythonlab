l1=['6','7','2','9','4','55','14','100']
l2=['0','2','66','3','6']
sum1=str(0)
sum2=str(0)
if len(l1)==len(l2):
    print("both list are of the same length")
else:
    print("both list are of different length")
for x in l1:
    sum1=sum1+x
for x in l2:
    sum2=sum2+x
if sum1==sum2:
    a="equal"
else:
    a="not equal"
print("sum of two lists are:",a)
for x in l1:
    for y in l2:
        if x==y:
            print(y,"occurs in both lists")
