###############################################################################
# DONE: 1. (4 pts)
#
#   For this _todo_, create a parent class called Vehicle. It should have an
#   __init__() function that sets two properties:
#       - year      <- int
#       - make      <- int
#       - model     <- int
#
#   It should have two methods:
#       - horn
#       - vehicle_info
#
#   This Shape class should assume that the vehicle is a car, so these
#   functions should behave as follows.
#
#       horn() -> should print the sound of a car horn
#               "BEEP BEEP"
#
#       vehicle_info() -> should print the vehicle's information
#                       Year: 2012
#                       Make: Chevrolet
#                       Model: Colorado
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
# Creates a parent class the init method initalizes the object with keys of year, make, and model. horn method is a behavior that is associated with vehicle class. vehicle_info displays information. 
class Vehicle: 
    def __init__(self, year, make, model):
        self.year = year
        self.make = make 
        self.model = model 
    def horn(self):
        print("BEEP BEEP")
    def vehicle_info(self):
         print("Year:", self.year)
         print("Make:", self.make)
         print("Model:", self.model)

       

###############################################################################
# DONE: 2. (2 pts)
#
#   For this _todo_, create a child class called Car that inherits its
#   class from Vehicle. Since Vehicle already assumes the vehicle is a car, we
#   don't really need to modify anything. Remember that you can create an empty
#   class by using the pass keyword.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
# Car is a child class of Vehicle thus inherits from Vehicle and the pass statement is a placeholder indicating that Car doesn't add/have any modifications from parent class
class Car(Vehicle): 
    pass
###############################################################################
# DONE: 2. (4 pts)
#
#   For this _todo_, create a child class called Boat that inherits its class
#   from Vehicle.
#
#   Now, a boat is a little bit different because we don't really need a
#   make and model. We will simply give the boat a name and a year. So, it's
#   __init__() method should only have two parameters:
#       - year
#       - name
#
#   A Boat's methods should work as follows.
#
#       horn() -> should print the sound of a boat horn
#               "TOOT TOOT"
#
#       vehicle_info() -> should print the vehicle's information
#                       Year: 2010
#                       Name: Seas the Day
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
#child class of Vehicle but overrides parent class thus use super(). 
class Boat(Vehicle):
    def __init__(self, year, name): 
        super().__init__(year,"", "")
        self.name = name 

    def horn(self):
        print("TOOT TOOT")

    def vehicle_info(self): 
        print("Year:" , self.year)
        print("Name: ", self.name)
###############################################################################
# DONE: 3. (4 pts)
#
#   For this _todo_, create a child class called Train that inherits its class
#   from Vehicle. A Train has only two parameter:
#       - number    <- a number that identifies a train
#       - length    <- which is just a number of train cars
#
#   A Train's methods should work as follows.
#
#       horn() -> should print the sound of a train horn
#               "CHOO CHOO"
#
#       vehicle_info() -> should print the vehicle's information
#                         Number: 74
#                         Length: 20
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
#Same as above
class Train(Vehicle): 
    def __init__(self,  number, length): 
        super(). __init__(0, "", "")
        self.number = number 
        self.length = length 

    def horn(self): 
        print("CHOO CHOO")

    def vehicle_info(self):
        print("Number:", self.number)
        print("Length: ", self.length)
###############################################################################
# DONE: 4. (3 pts)
#
#   For this _todo_, create three different objects and save each to a
#   variable. Create a Car, Boat, and Train.
#
#   You should also call each one's horn() and vehicle_info() methods.
#   (Remember that each method already does the printing for you, so you don't
#   need to use print here.)
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
#Creates 3 objects and gives variable with values thus calls the functions made above

car = Car(2012, "Toyota", "Tundra")
boat = Boat(2011, "Carpe Diem")
train = Train(75,24)

car.horn()
car.vehicle_info() 

boat.horn()
boat.vehicle_info()

train.horn()
train.vehicle_info()