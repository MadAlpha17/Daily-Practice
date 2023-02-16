class Student:
    student_name = 'Terrance Morales'
    marks = 93  
print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")
x=str(input("Enter the Name: "))
y=int(input("Enter the Mark: "))
setattr(Student, 'student_name',x)
setattr(Student, 'marks', y)
print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")