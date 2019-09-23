class Bank:

    def __init__(self,name,accType,occ,address):
        self.name = name
        self.accType = accType
        self.occ = occ
        self.address = address

    def showCustomer(self):
        print("Default Details of Customer : ")
        print("Name : {}".format(self.name))
        print("Account Type : {}".format(self.accType))
        print("Occupation : {}".format(self.occ))
        print("Address : {}".format(self.address))

class Person(Bank):

    def __init__(self,name,accType,occ,address):
        # super - call the parent class constructor
        super().__init__(name,accType,occ,address)

    def personDetails(self):
        if self.occ == "Student":
            print("Account Open for student with 0 balance")
        else:
            print("Account Open for employeed with 1000 balance")

class Student(Person):
    students = []
    def __init__(self,name,accType,occ,address):
        super().__init__(name,accType,occ,address)

    def studentDetails(self):
        age = int(input("Enter age : "))
        college = input("Enter college : ")
        education = input("Enter education : ")
        s = {"name":self.name,"age":age,"college":college,"edu":education}
        self.students.append(s)
        print(s)

class Employee(Person):
    emp = []
    def __init__(self,name,accType,occ,address):
        super().__init__(name,accType,occ,address)

    def empDetails(self):
        age = int(input("Enter age : "))
        company = input("Enter company : ")
        sal = input("Enter salary : ")
        e = {"name":self.name,"age":age,"company":company,"sal":sal}
        self.emp.append(e)
        print(e)

emp = Employee('Ram','Current','Private Job','Delhi')
# emp.showCustomer()
# emp.personDetails()
emp.empDetails()