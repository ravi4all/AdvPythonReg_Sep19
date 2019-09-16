class Emp():

    id = None
    name = None
    sal = None

    def register(this):
        print(this.id,this.name,this.sal)

emp_1 = Emp()
emp_1.id = 101
emp_1.name = "Ram"
emp_1.sal = 32000
emp_1.register()

emp_2 = Emp()
emp_2.id = 102
emp_2.name = "Raman"
emp_2.sal = 21000
emp_2.register()

