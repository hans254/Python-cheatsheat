name = input("What is your name? ")
color = input(" What's your favourite color? ")
print(name + " likes " + color)

year = input("Enter year of birth: ")
current_year = 2022
print(current_year - int(year))


# PYTHON STRINGS
course = "Python for beginners"
print(course[0:6])
print(course[6:])
print(course.find("for"))
print(course.replace("beginners", "developers"))
print(len(course))
print(course.upper())
print(course.lower())
print("for" in course)
print(course.title())

# ARITHMETIC OPERAIONS
print(10 + 3)
print(10 - 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)  # modulus
print(10 ** 3)  # Exponential

# OPERATOR PRECEDENCE
x = 10 + 3 * 4
y = 10 - 3 + 15 / 3
print(x)
print(y)

# MATH FUNCTIONS
x = 2.9
print(round(2.9))
print(abs(-2.9))
from importlib.resources import path
import math

print(math.ceil(2.9))

# IF STATEMENTS
is_hot = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

# IF ELSE EXERCISE
price = 1000000
good_credit = True
if good_credit:
    print("Put down 10% $", price * 0.1)
else:
    print("Put down 20% $", price * 0.2)

# ELIF EXERCISE
price = 1000000
good_credit = False
no_good_credit = True
if good_credit:
    print("Put down 10% $", price * 0.1)
elif no_good_credit:
    print("Put down 20% $", price * 0.2)
else:
    print("Does not qualify for the loan")

# ELIF STATEMENT WHERE NO SITUATION IS TRUE
price = 1000000
good_credit = False
no_good_credit = False
if good_credit:
    print("Put down 10% $", price * 0.1)
elif no_good_credit:
    print("Put down 20% $", price * 0.2)
else:
    print("Does not qualify for the loan")

# LOGICAL OPERATORS AND, OR, NOT
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")

has_high_income = False
has_good_credit = True
if has_high_income or has_good_credit:
    print("Eligible for loan")

# IF APPLICANT HAS GOOD CREDIT AND DOESN'T HAVE A CRIMINAL OFFENCE
# THEN THEY ARE ELIGIBLE FOR A LOAN
has_high_income = True
has_criminal_record = False
if has_high_income and not has_criminal_record:
    print("Not eligible to vie for Gubernatorial seat")

has_high_income = True
has_criminal_record = True
if has_high_income and not has_criminal_record:
    print("Eligible to vie for Gubernatorial seat")

# COMPARISON OPERATORS
temperature = 30
if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

temperature = 30
if temperature < 30:
    print("It's not a hot day")
else:
    print("It's a hot day") 

name = input("Enter your name: ")
if len(name) < 3:
    print("Name must be atleast 3 characters")
elif len(name) > 50:
    print("Maximum name of of character should be 50")
else:
    print("Name looks good!")

# CREATE A WIEGHT CONVERTER FROM LBS TO KG OR KG TO LBS
weight = int(input("Enter your weight: "))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

# WHILE LOOPS
i = 1
while i <= 5:
    print(i)
    i += 1
print("Done")

i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("Done")

# GUESS GAME
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed!!!")
    print("Please Try Again")

# CAR GAME
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print('''
        Start - to start the car
        Stop - to stop the car
        Quit - to quit
        ''')
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that command!!!")

# FOR LOOP
for item in 'Python':
    print(item)

for item in ["Hansel", "Tony", "Brian", "Matelong", "Meshack", "Ken"]:
    print(item)

for x in range(11):
    print(x)
for x in range(1, 11, 2):
    print(x)

# CALCULATE TOTAL PRICE
prices = [10, 20, 30, 40]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# NESTED LOOPS
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

# CHALLENGE
# 1
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)

    # 2
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
        print(output)

#   LIST
names = ["Hansel", "Tony", "Brian", "Matelong", "Meshack"]
print(names)
print(names[2])
names.append("Oluoch")
print(names)
names.insert(3, "Phidence")
print(names)
print(names.pop(-1))
names.remove("Tony")
names.clear()
print(names)
# print(names.index("Hansel"))
print("Hansel" in names)

# WRITE A PROGRAM TO FIND THE LARGEST NUMBER IN A LIST
num = [23, 10, 20, 70, 65]
max = num[0]
for number in num:
    if number > max:
        max = number
print(max)

# 2D LIST IN PYTHON

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])
matrix[0][1] = 20
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

# WRITE A PROGRAM TO REMOVE THE DUPLICATES IN A LIST
hans = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
unique = []
for x in hans:
    if x not in unique:
        unique.append(x)
        print(unique)

# TUPLES "THEY ARE IMMUTABLE" THEY ARE USED WHEN ON THINGS YOU WON'T WANT TO INTERFERE WITH
numbers = (1, 2, 3)
print(numbers[0])

# UNPACKING
coordinates = (1, 2, 3)
x, y, z = coordinates
print(y)

# DICTIONARIES IN PYTHON
customer = {
    "name": "Hansel Fidel",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("name"))
print(customer.get("birth date", "Feb 1 2003"))

# EXERCISE
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!")
print(output)


# EMOJI CONVERTER
# message = input(">")
# word = message.split(" ")
# emoji = {
#    ":)": ""
# }
##print

# FUNCTIONS
def greet_user():
    print("Hi there")
    print("Welcome abroad")
print("Start")
greet_user()
print("Finish")

# PARAMETERS
def greet_user(name):
    print(f"Hi {name}")
    print("Welcome abroad")
print("Start")
greet_user("Hansel")
greet_user("Mary")
print("Finish")

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome abroad")
print("Start")
greet_user("Hansel", "Ndemange")
greet_user("Tony", "Toroitich")
print("Finish")

# KEY ARGUMENTS
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome abroad")
print("Start")
greet_user( last_name="Ndemange", first_name="Hansel")
print("Finish")

# RETURN STATEMENTS
def square(number):
    return number * number
result = square(3)
print(result)

#   OR
def square(number):
    return number * number

print(square(3))

# EXCEPTIONS "HOW TO HANDLE ERRORS IN PYTHON PROGRAMME"
try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid Value")

  # ANOTHER EXAMPLE
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0!!!")
except ValueError:
    print("Invalid Value")

# COMMENTS
print("Programmed by Dr. Hansel .F. Ndemange")

# CLASSES
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("Draw")

point1  = Point()
point1.x = 10
point1.y = 20
point1.draw()

point2 = Point()

# CONSTRUCTOR
#class Person:
#    def __int__(self, name):
 #       self.name = name
#    def talk(self):
 #       print(f"Hi, I am {self.name}")


#John = Person()
#John.talk()
#bob = Person()
#bob.talk()

#  INHERITANCE
class mammal:
    def walk(self):
        print("Walk")

class Dog(mammal):
   def bark(self):
       print("Bark")


class cat (mammal):
    def be_annoying(self):
        print("Annoying")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = cat()
cat1.be_annoying()

# PACKAGES

# GENERATING RANDOM VALUES
import random
for i in range(3):
    print(random.randint(1,50))
import random
members = ['Hansel','Tony','Brian','Matelong','Meshack','Ken','Tiffany']
leader = random.choice(members)
print(leader)

#    DICE
import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second  = random.randint(1,6)
        return (first,second)


dice = Dice()
print(dice.roll())

# FILE DIRECTORIES (Mosh,3.45.00)
from pathlib import Path

path = Path("Guess")
print(path.exists())

# Pypi and Pip(Huh?)

