from vehicle import Vehicle


class Bus(Vehicle):
    # Since we're only adding a single new prperty that needs to be initialized at instantiation (in the constructor)
    # We'll add only the bus specific constructor expression and call on the super-classes (the base Vehicle class) constructor for everything else.
    def __init__(self, top_speed, passengers) -> None:
        # You have to call the super class.. then call it's constructor (__init__).. otherwise this constructor would overwrite Vehicles
        super().__init__(top_speed)
        self.passengers = []

    # A bus class specific method... will not come from Vehicle base/super class

    def add_group(self, passengers):
        if len(passengers) > 0:
            self.passengers.extend(passengers)


bus = Bus(150, ['Mike', 'Johnny'])

bus.vehicle_print()     # Top Speed: 150  --  Warnings: []
