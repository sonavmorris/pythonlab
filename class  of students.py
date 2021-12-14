class student:
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
l=[]
n=int(input("enter the no: of students"))
for i in range(0,n):
    name=input("enter name")
    roll=int(input("enter roll No:"))
    course=input("enter course")
    l.append(student(roll,name,course))
for obj in l:
    print(obj.name,obj.roll,obj.course)
        
        
