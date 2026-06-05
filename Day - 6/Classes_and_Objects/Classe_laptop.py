class laptop:
    Price = "Price"
    Processor = "Processor"
    Ram = "Ram"

HP = laptop()
DELL = laptop()
LENOVO = laptop()

HP.Price =  50000
HP.Processor = "Happo"
HP.Ram = "16GM Ram"

DELL.Price = 65000
DELL.Processor = "Deava"
DELL.Ram = "32GB Ram"

LENOVO.Price = 75000
LENOVO.Processor = "Lavdo"
LENOVO.Ram = "64GB Ram"

print("HP Price : ",HP.Price)
print("Processor : ",HP.Processor)
print("Ram : ",HP.Ram)
print()
print("DELL Price : ",DELL.Price)
print("Processor : ",DELL.Processor)
print("Ram : ",DELL.Ram)
print()
print("LENOVO Price : ",LENOVO.Price)
print("Processor : ",LENOVO.Processor)
print("Ram : ",LENOVO.Ram)
