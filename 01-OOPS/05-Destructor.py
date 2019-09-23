class Emp():

    # Constructor
    def __init__(self,id,name,sal):
        print("Constructor called..")
        self.id = id
        self.name = name
        self.sal = sal
        self.user = []

    def register(self):
        self.user.append([self.id,self.name,self.sal])
        print(self.user)

    def __del__(self):
        print("Destructor Called...")

emp_1 = Emp(101,'Ram',32000)
emp_1.register()

del emp_1

emp_2 = Emp(102,'Shyam',21000)
emp_2.register()

