# To illustrate Inheritance in OOP (in python) we'll have this vehicle class serve as our base class from which Bus and Car will inherit from.

class Vehicle:
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
        # Here lets make sure the add_warning method receives a non-null number (length greater than zero) so we don't attempt to append 'null' to the array
        if len(warning_text) > 0:
            self.__warnings.append(warning_text)

    def get_warnings(self):
        print('warnings: ', self.__warnings)

    def drive(self):
        print(f'I am driving at a maximum of {self.top_speed} km/h')

    def vehicle_print(self):
        print(repr(self))
