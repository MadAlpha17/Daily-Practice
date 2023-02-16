class Employee:
     def __init__(self , ids , name):
        self.ids = ids
        self.name = name
emp1 = Employee(2e45 , "dikshya")
attributes_to_add = ['department']
for x in range(len(attributes_to_add)):
    setattr(emp1, attributes_to_add[x], x)
print(emp1.__dict__)
delattr(emp1 , "name")
print(emp1.__dict__)