import math
t_area=lambda b,h:1/2*(b*h)
r_area=lambda l,b:l*b
c_area=lambda r:math.pi*r*r
s=int(input("enter breadth of triangle:"))
t=int(input("enter height of triangle:"))
print("area of triangle:",t_area(s,t))
u=int(input("enter length of rectangle:"))
v=int(input("enter breadth of rectangle:"))
print("area of rectangle=",r_area(u,v))
w=int(input("enter radius of circle:"))
print("area of circle=",c_area(w))

