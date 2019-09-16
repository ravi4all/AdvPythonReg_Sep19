class Emp():
    users = []
    emp_id = 0
    def __init__(self):
        self.user = {}

    def menu(self):
        print("""
        1. Register
        2. Login
        3. Salary
        4. View Employee
        """)
        ch = input("Enter your choice : ")
        opr = {
            "1" : self.registerEmp,
            "2" : self.loginEmp,
            "3" : self.salary,
            "4" : self.viewEmp
        }
        opr.get(ch)()

    def registerEmp(self):
        name = input("Enter name : ")
        dept = input("Enter dept : ")
        desig = input("Enter designation : ")
        exp = input("Enter experience : ")
        Emp.emp_id += 1
        self.user['emp_id'] = self.emp_id
        self.user['name'] = name
        self.user['dept'] = dept
        self.user['desig'] = desig
        self.user['exp'] = exp
        self.users.append(self.user)
        print(self.users)

    def loginEmp(self):
        emp_id = int(input("Enter Emp Id : "))
        emp_name = input("Enter Emp Name : ")
        for i in range(len(self.users)):
            if emp_id == self.users[i]['emp_id'] and emp_name == self.users[i]['name']:
                print("Login Success")
                break
        else:
            print("Login Failed")

    def salary(self):
        pass

    def viewEmp(self):
        pass

while True:
    emp = Emp()
    emp.menu()