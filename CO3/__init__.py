from graphics1.graphics3D1 import cuboid
from graphics1 import circle
from graphics1 import rectangle
from graphics1.graphics3D1 import sphere
r=int(input("enter the radius of a circle"))
l=int(input("enter the length of the rectangle"))
w=int(input("enter the breadth of the rectangle"))
a=int(input("enter the length of the cuboid"))
b=int(input("enter the breadth of the cuboid"))
c=int(input("enter the height of the cuboid"))
radius=int(input("enter the radius of a sphere"))
print("Area of Circle : ",circle.area(r))
print("Perimeter of Circle : ",circle.perimeter(r))
print("Area of Rectangle : ",rectangle.area(l,w))
print("Perimeter of Rectangle : ",rectangle.perimeter(l,w))
print("Area of Cuboid : ",cuboid1.area(a,b,c))
print("Perimeter of Cuboid : ",cuboid.perimeter(a,b,c))
print("Area of sphere : ",sphere.area(radius))
print("Perimeter of sphere : ",sphere.perimetr(radius))


