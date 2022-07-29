from vehicle import Vehicle


class Car(Vehicle):

    # We will be inheriting all of Vehicles props and methods

    # Create a Car object specific method (which Vehicle will not have)
    def rev_engine(self):
        print('Vroom-Vroom .. Im a loud dumbass on peachtree in a CAR')


car1 = Car(200)
car1.add_warning('HOLY SHIT!!!')

car1.vehicle_print()    # Top Speed: 200  --  Warnings: ['HOLY SHIT!!!]
