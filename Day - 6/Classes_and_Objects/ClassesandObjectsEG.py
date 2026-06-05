class goa():
    Name = "Enter the name"
    Drink = "Yes or no"

    def party(self):
        print("Lets Party......")
    def beach(self):
        print("Enjoy the beach")

Manoj = goa()
Aparna = goa()

Manoj.Name = "Manoj"
Aparna.Name = "Aparna"

Manoj.Drink = "Yes"
Aparna.Drink = "No"

print("Tourist 1 Name : ",Manoj.Name)
print("Drinks : ",Manoj.Drink)
Manoj.party()
print()
print("Tourist 2 Name : ",Aparna.Name)
print("Drinks : ",Aparna.Drink)
Aparna.beach()




