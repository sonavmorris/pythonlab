class employee:
    "INFORMATION ABOUT EMPLOYEES"
    def __init__(self,empid,name,salary,department):
        self.empid=empid
        self.name=name
        self.salary=salary
        self.department=department
l=[]
n=int(input("enter the no: of Employees"))
for i in range(0,n):
    empid=int(input("enter Employee ID:"))
    name=input("enter name:")
    salary=int(input("ENTER SALARY :"))
    department=input("enter Department:")
    l.append(employee(empid,name,salary,department))
for obj in l:
    if obj.salary>=15000:
        print(obj.empid,obj.name,obj.salary,obj.department)
    
