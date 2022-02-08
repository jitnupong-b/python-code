from vehicle import Automobile

class Car(Automobile):
# The _ _init_ _ method accepts arguments for the
# car's make, model, mileage, price, and doors.

    def __init__(self, make, model, mileage, price, doors):
        # Call the superclass's _ _init_ _ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)

        # Initialize the _ _doors attribute.
        self.__doors = doors

        # The set_doors method is the mutator for the
        # _ _doors attribute.

    def set_doors(self, doors):
        self.__doors = doors

    # The get_doors method is the accessor for the
    # _ _doors attribute.

    def get_doors(self):
        return self.__doors