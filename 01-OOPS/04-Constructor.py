class Emp():

    # Constructor
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal
        self.user = []

    def register(self):
        self.user.append([self.id,self.name,self.sal])
        print(self.user)

emp_1 = Emp(101,'Ram',32000)
emp_1.register()

emp_2 = Emp(102,'Shyam',21000)
emp_2.register()

