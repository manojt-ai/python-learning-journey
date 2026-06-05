class laptop:
    def __init__(self):
        self.ram = ""
        self.processor = ""

    def display(self):
        print("Ram : ",self.ram)
        print("Processor : ",self.processor)

hp = laptop()
dell = laptop()

hp.ram = "8gb"
hp.processor = "i5"

dell.ram = "16gb"
dell.processor = "i7"

hp.display()
print()
dell.display()

