class Employee:
    __empName = None
    __empID = None
    def __init__(self):
        self.__empName = None
        self.__empID = None
    def inputData(self):
        self.__empName = input("Enter the Name: ")
        self.__empID = int(input("Enter the Employee ID:"))
    def displayMembers(self):
        print("Name: ", self.__empName)
        print("Employee ID: ", self.__empID)
class Manager(Employee):
    __basicSalary = None
    __DA = None
    __HRA = None
    def __init__(self):
        super().__init__()
        self.__basicSalary  = None
        self.__DA = None
        self.__HRA= None
    def getINFO(self):
        super().inputData()
        self.__basicSalary= float(input("Input the Basic Salary: "))
        self.__DA = float(input("Enter DA : "))
        self.__HRA = float(input("Enter HRA : "))
    def calSal(self):
        return (self.__basicSalary + self.__DA + self.__HRA)
    def printInfo(self):
        self.displayMembers()
        print("Salary: " , self.calSal())
obj = Manager()
obj.getINFO()
obj.printInfo()