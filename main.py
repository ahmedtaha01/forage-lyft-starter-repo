from car_factory import CarFactory
from datetime import datetime


car = CarFactory.create_calliope(datetime.today().date(),
                                 datetime.today().date().replace(year=datetime.today().date().year - 3)
                                 ,40000,20000,[0.1,0.3,0.5,0.6])

print(car.needs_service())
