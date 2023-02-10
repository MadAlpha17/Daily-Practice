class Queue:
    def __init__(self):
        self.queue=[]
    def insert(self):
        p=input("Enter the element to be insert:")
        self.queue.append(p)
        print(p,"has been inserted into the stack.")
    def delete(self):
        x = self.queue.pop(0)
        print(x, "has been deleted from the stack.")
    def display(self):
        print("{}".format( self.queue))
           
 
queue=Queue()
c="y"
while(c=="y"):
    print("Choices:")
    print("1.Insert")
    print("2.Delete")
    print("3.Display")
    print("4.Exit")
    choice=int(input("Please in enter a choice(1,2,3,4):"))
    if(choice==1):
        queue.insert()
    elif(choice==2):
        queue.delete()
    elif(choice==3):
        queue.display()
    elif(choice==4):
        c="n"
        print("Bye have a Nice Day!!")
    else:
        print("Wrong choice try again!!") 