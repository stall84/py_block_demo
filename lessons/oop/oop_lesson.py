# Trivial example showing the python syntax for writing classes

class Car:
    # Property / Field NOTE: Like js .. this is a class attibute.. we're not assigining it in the constructor so it's not an instance attribute..
    top_speed = 100
    # This can clearly lead to unexpected behavior when directly accessing or changing these class-level attributes.
    warnings = []

    # Method NOTE: the 'self' keyword is not reserved, but is the standard convention.
    def drive(self):
        # self gives access to the classes properties/attributes (similar to the way this is used in js, but NOT at all the same)
        # Mind that python passes this 'self' object in as the first argument to EVERY method on a class/object .. it's up to you to
        # name it ('self' is convention) and place it first so that any other arguments you want for your methods will come after 'self'
        print(f'I am driving under speed: {self.top_speed}')


car1 = Car()            # Constructor call version of object instantiation in python.. no 'new' keyword needed like in js or other langs

# Execute the drive method on our instantiated Car object.
car1.drive()

car2 = Car()
car2.drive()

# This is done to show that we are modifying a class-level attibute.. so we might naively think this will only be adding
car2.warnings.append('New Warning FOR CAR 2 ONLY...')
# this warning to the car2 object, but you'll see that it actually modifies every instance of the Car class

car3 = Car()
print('Car3 warnings .. we assume its still empty.. : ', car3.warnings)


# Of course the constructor will avoid the above issues with class attributes
# (btw theres nothing wrong with using class attibutes,
# just be aware they are not scoped to the instance object, but instead to every instance object from that class )

class InstanceCar:
    # Python uses a dunder (double underscored) 'special' method __init__ specifically for the constructor function.
    # We set a default value for the speed parameter.. Thus making speed an optional argument
    def __init__(self, speed=100):
        self.top_speed = speed
        # Just like originally (in Car class above) we create a 'warnings' attribute.. However this time in the constructor, it is scoped to the instance object
        self.warnings = []
        # Also note we do not accept any arguments for this list at object construction/creation


# Create instance object passing speed in constructor
new_car1 = InstanceCar(120)
# Create a new instance object with no speed passed in constructor
new_car2 = InstanceCar()

print('new_car1 (instance car) speed: ', new_car1.top_speed)

# Attempt exact same operation as before except this time it won't modify/act on the class attibute and won't affect every single object created from the class
new_car1.top_speed = 115.11111

print('new_car2 top speed: ', new_car2.top_speed)
print('new_car1 top speed after direct modify: ', new_car1.top_speed)
