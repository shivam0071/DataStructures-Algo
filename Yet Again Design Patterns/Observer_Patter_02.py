# The Observer Pattern defines a one-to-many dependency between objects so that when one
# object changes state, all of its dependents are notified and updated automatically.

from abc import ABC, abstractmethod

# THE SUBJECT or THE OBSERVABLE
class Subject(ABC):

    def register_observer(self):
        pass

    def remove_observer(self):
        pass

    def notify_observer(self):
        pass

class Observer(ABC):
    def update(self, temp, humidity, pressure):
        pass

# To  display the data, encapsulating the changing code
class DisplayElement(ABC):

    def display(self):
        pass





# CONCREATE CLASSES

# THE STATE
class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self. temp = None
        self.humid = None
        self.pressure = None

    def register_observer(self, observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
        else:
            print("Exception with removing observers")
        
    def notify_observer(self):
        for obs in self.observers:
            obs.update(self.temp, self.humid, self.pressure)
    
    def measurements_changed(self):
        self.notify_observer()

    def set_measurements(self, temp, humid, pressure):
        self.temp = temp
        self.humid = humid
        self.pressure = pressure
        self.measurements_changed()
        
    
class CurrentConditionDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.temperature = None
        self.humidity = None
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp, humid, pressure):
        self.temperature = temp
        self.humidity = humid
        self.display()

    def display(self):
        print(f"CURRENT CONDITIONS: TEMP - {self.temperature}, Humidity  - {self.humidity}")

class FutureConditionDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.temperature = None
        self.humidity = None
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp, humid, pressure):
        self.temperature = temp + 5
        self.humidity = humid + 5
        self.display()

    def display(self):
        print(f"FUTURE CONDITIONS: TEMP - {self.temperature}, Humidity  - {self.humidity}")

# Finally Run this
class WeatherStation:

    @classmethod
    def execute(cls):
        weather_data = WeatherData()
        current_condition = CurrentConditionDisplay(weather_data)
        future_cond = FutureConditionDisplay(weather_data)
        weather_data.set_measurements(80, 65, "38.5f")


WeatherStation.execute()