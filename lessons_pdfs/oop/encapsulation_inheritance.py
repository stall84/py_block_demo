# Encapsulation is the term used to generally describe the concept of utilizing private and public accessors (properties and methods)
# to hide the detail from end-user. https://medium.com/@cancerian0684/what-are-four-basic-principles-of-object-oriented-programming-645af8b43727#:~:text=Encapsulation%20is%20the%20mechanism%20of%20hiding%20of%20data%20implementation%20by%20restricting%20access%20to%20public%20methods.%20Instance%20variables%20are%20kept%20private%20and%20accessor%20methods%20are%20made%20public%20to%20achieve%20this.

class Car:
    def __init__(self, top_speed) -> None:
        self.top_speed = top_speed
        # self.warnings = []      # These are both public props/atts as written .. it is the default.
        # You can make a prop-attr private by dundering the side after the dot (i.e. self.__my_priv_method():)
        self.__warnings = []

    def __repr__(self):
        return f'Top Speed: {self.top_speed}  --  Warnings: {self.__warnings}'

    # Let's create our first 'setter-type' method add_warning() which could easily be named set_warning()
    def add_warning(self, warning_text):
        # your first thought should usually be 'can i guard against something ?
        if len(self.__warnings > 0):
            self.__warnings.append(warning_text)

    def get_warnings(self):
        print('warnings: ', self.__warnings)

    def vehicle_print(self):
        print(repr(self))


car1 = Car(150)
car2 = Car(189)

# car2.__warnings.append('LOOKOUT JEZUS!')          # This won't work once we've privatized our warnings prop .. use the proper getter and setters

car_list = [car1, car2]

for car in car_list:
    car.vehicle_print()
    car.get_warnings()


# INHERITANCE
# In order to keep code DRY .. We can extend from a base class, just like in any other OOP language.
