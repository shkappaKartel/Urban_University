class BMW_X3:

    def __init__(self):
        self.model = 'BMW X3'
        self.color = 'Black'
        self.price = '9500$'
        self.max_velocity = '307 km/h'
        self.current_velocity = '0 km/h'
        self.engine_rpm = 0
        self.lights = 'OFF'
        self.is_in = False
        self.is_seatbelt = False

    def sit_in(self):
        self.is_in = True
        print("You have sit in ", self.model)

    def lights_on(self):
        self.lights = "ON"
        print("You have turn on the lights")

    def seatbelt(self):
        self.is_seatbelt = True
        print("Seatbelt is done!")

    def start_engine(self):
        print('Engine started.')
        self.engine_rpm = 900

    def drive(self):
        print("Let's go!")
        self.engine_rpm = 2000
        self.current_velocity = '20 km/h'


my_car = BMW_X3()
print('---------------------------------------')
print('Color: ', my_car.color)
print('Price: ', my_car.price)
print('Max velocity: ', my_car.max_velocity)
print('RPM: ', my_car.engine_rpm)
print('Current velocity: ', my_car.current_velocity)
print('---------------------------------------')
my_car.sit_in()
print('---------------------------------------')
my_car.seatbelt()
print('---------------------------------------')
my_car.start_engine()
print('RPM: ', my_car.engine_rpm)
print('Current velocity: ', my_car.current_velocity)
print('---------------------------------------')
my_car.lights_on()
print('---------------------------------------')
my_car.drive()
print('RPM: ', my_car.engine_rpm)
print('Current velocity: ', my_car.current_velocity)
print('---------------------------------------')