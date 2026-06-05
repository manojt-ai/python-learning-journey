class teacher:
    
    def __init__(self,name,regno):
        self.name = name
        self.reg_no = regno

    def display(self):
        print("Name : ",self.name)
        print("Register Number : ",self.reg_no)

t1 = teacher("Manoj","1")
t2 = teacher("Aparna","2")

t1.display()
print()
t2.display()



  
