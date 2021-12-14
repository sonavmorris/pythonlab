class student:
    "information about the class"
    studentcount=0
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
        student.studentcount=student.studentcount+1
    def displaycount():
        print("no: of student objects",student.studentcount)
    def display(self):
        print("ROLL NO:=",self.roll)
        print("name=",self.name)
        print("course name=",self.course)
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"destroyed")
        
s1=student(2008,"Reshma","MCA")
s2=student(2014,"Ananya","B.Tech")
print (getattr(s1,'name'))
s1.display()
s2.display()
student.displaycount()
del s1


