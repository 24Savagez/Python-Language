class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn on : Air")

class Car(Vehicle):
    def sayHi(self):
        print("Hello Bro! Where are you?")

class Van:
    pass

car1 = Car()
car1.turnOnAirConditioner()
car1.sayHi()

#van1 = Van()
#van1.turnOnAirConditioner()
