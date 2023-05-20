#CREATING METHODS
class item:
    #A FUNCTION INSIDE A CLASS IS CALLED METHODS
    def calculate_total_price(self, x, y):
        return x * y

#Assigning Attributes to Instances
item1 = item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5 
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3 
print(item2.calculate_total_price(item2.price, item2.quantity))

#CREATE A METHOD WITH A UNIQUE NAME <__init__> TO ACCESS PARAMETERS
class item:
    def __init__(self):
        print("I AM CREATED LIKE THAT")

item1 = item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5 

item2 = item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3 

# ANOTHER EXAMPLE WITH AN ADDITIONAL PARAMETER
class item:
    def __init__(self, name):
        print(f"An instance created: {name}")
        
item1 = item("Phone")
item1.name = "Phone"
item1.price = 100
item1.quantity = 5 

item2 = item("Laptop")
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3 

# WE CAN AS WELL PASS THE PARAMETER NAME IN WITHIN THE METHOD
class item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
item1 = item("Phone", 100, 5) 
item2 = item("Laptop", 1000, 3)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)