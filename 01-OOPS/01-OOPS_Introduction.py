class Emp():

    id = None
    name = None
    sal = None

emp_1 = Emp()
emp_1.id = 101
emp_1.name = "Ram"
emp_1.sal = 32000
print(emp_1.__dict__)

emp_2 = Emp()
emp_2.id = 101
emp_2.name = "Ram"
emp_2.sal = 32000
print(emp_2.__dict__)

