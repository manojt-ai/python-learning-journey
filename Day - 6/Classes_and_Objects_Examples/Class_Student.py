class student:
    
    def __init__(self):
        name = ""
        register_number = ""
        
    def display(self):
        print("Name : ",self.name)
        print("Register number : ",self.register_number)

s1 = student()
s2 = student()

s1.name = "Manoj"
s1.register_number = "721423244303"

s2.name = "Aparna"
s2.register_number = "721423244304"

s1.display()
print()
s2.display()

