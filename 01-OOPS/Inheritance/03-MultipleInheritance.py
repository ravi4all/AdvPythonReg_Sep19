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

class Loan:

    def __init__(self,age,bal,occ):
        self.age = age
        self.bal = bal
        self.occ = occ

    def approveLoan(self):
        if self.occ == "student":
            print("Limit for loan is upto 1 Lac only")
        elif self.occ == "employee":
            if self.bal < 25000 and self.bal > 20000:
                print("Limit for loan according to your balance is 10 lac only")
            elif self.bal > 25000 and self.bal < 50000:
                print("Limit for loan according to your balance is 40 lac only")
            elif self.bal < 20000:
                print("Loan not permitted...")

class Student(Bank,Loan):
    students = []
    def __init__(self,name,accType,occ,address,age,bal):
        super().__init__(name,accType,occ,address)
        Loan.__init__(self,age,bal,occ)

    def studentDetails(self,college,education):
        # age = int(input("Enter age : "))
        # college = input("Enter college : ")
        # education = input("Enter education : ")
        s = {"name":self.name,"age":self.age,"college":college,"edu":education}
        self.students.append(s)
        print(s)

class Employee(Bank,Loan):
    emp = []
    def __init__(self,name,accType,occ,address,age,bal):
        super().__init__(name,accType,occ,address)
        Loan.__init__(self,age,bal,occ)

    def empDetails(self,company,sal):
        # age = int(input("Enter age : "))
        # company = input("Enter company : ")
        # sal = input("Enter salary : ")
        e = {"name":self.name,"age":self.age,"company":company,"sal":sal}
        self.emp.append(e)
        print(e)

emp = Employee('Ram','Current','employee','Delhi',34,32000)
emp.showCustomer()
emp.empDetails('TCS',31000)
emp.approveLoan()