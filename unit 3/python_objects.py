# python objects are digital representations of things

# objects are collection of data that we use to 
# characterize things

# example - A car is a object/"Thing"
# chaeacteristics of a car: engine, tires battery, seating,
# color, model, doors

# when we want to make an object, we need to use a class
# class keyword = object maker

# the class name always is capitalized / pascal case
class Car:
    # we always start with this code below
    # this function is used to describe the characteristics of 
    # the object ex. self
    def _init_(self, color, year, model, engine, pushtostart):
        # attributes
        self.color = "red",
        self.year = 2027,
        self.model = "enzo",
        self.engine = "v12",
        self.pushtostart = True
    

        # methods - functions (*that exist inside of a object)
        # these are functions that exclusively work within the object
        # things the car acually does!

        def start():
            # if key is present when push to is clicked/ pressed,
            # start the engine and vehicle
            if self.pushtostart == True:
                # start car

        def accelerate():
            # when gas pedal is pressed, move vehiclw.

        def brake():
            # when brake pedal is pressed, trigger braking pads and lock    


class character_GTA:
    def _init_(self):
        # attributes - characteristics
        self. movementspeed = 5

        # methods - what it does/ its actions
        def run():
            # when x button is clicked, increase movement by 5
                movementspeed +=5 

        def addItemToIventory():
             # when right trigger is pressed and nearby another object
             self.inventory.append("sword")                    
