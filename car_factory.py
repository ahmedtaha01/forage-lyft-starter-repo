from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from car import Car
from datetime import datetime

class CarFactory:

    def create_calliope(current_date ,last_service_date,current_mileage,last_service_mileage,sensors):
        return Car(CapuletEngine(current_mileage,last_service_mileage),
                   SpindlerBattery(last_service_date,current_date),
                   CarriganTire(sensors))
    
    def create_glissade(current_date,last_service_date,current_mileage,last_service_mileage,sensors):
        return Car(WilloughbyEngine(current_mileage,last_service_mileage),
                    SpindlerBattery(last_service_date,current_date),
                    CarriganTire(sensors))
    
    def create_palindrome(current_date,last_service_date,warning_light_on,sensors):
        return Car(SternmanEngine(warning_light_on),
                   SpindlerBattery(last_service_date,current_date),
                   OctoprimeTire(sensors))
    
    def create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage,sensors):
        return Car(WilloughbyEngine(current_mileage,last_service_mileage),
                    NubbinBattery(last_service_date,current_date),
                    OctoprimeTire(sensors))
    
    def create_thovex(current_date,last_service_date,current_mileage,last_service_mileage,sensors):
        return Car(CapuletEngine(current_mileage,last_service_mileage),
                   NubbinBattery(last_service_date,current_date),
                   CarriganTire(sensors))

