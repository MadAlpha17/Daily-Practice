from abc import ABC , abstractmethod
class Polygon(ABC):
    def area(self):
        pass
class Triangle(Polygon):
    def area(self):
        base = int(input("Enter the Base: "))
        height = int(input("Enter the Height: "))
        print("The Area of the Triangle is" , base*height)
class Square(Polygon):
    def area(self):
        side = int(input("Enter the Side"))
        print("The Area of the Sqaure is" , side*side)
class Circle(Polygon):
    def area(self):
        radius = int(input("Enter the Radius"))
        print("The Area of the Circle is" , 3.14*radius*radius)
       
print("Hello!!! Welcome to the Area Calculator")
while(1):
    print("1.Triangle \n2.Circle \n3.Square \n4.Exit")
    x=int(input("Enter the Choice:(1,2,3,4)"))
    if(x==1):
        R.area()
    elif(x==2):
        k.area()
    elif(x==3):
        R.area()