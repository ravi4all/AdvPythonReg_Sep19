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
        elif self.occ == "Employeed":
            print("Account Open for employeed with 1000 balance")

    # Overriding
    def showCustomer(self):
        print("Default Details of Customer : ")
        print("Name : {}".format(self.name))
        print("Account Type : {}".format(self.accType))
        print("Occupation : {}".format(self.occ))
        print("Address : {}".format(self.address))

obj_1 = Person('Ram','Saving','Student','Delhi')
obj_1.showCustomer()
obj_1.personDetails()