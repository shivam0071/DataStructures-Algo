        
        # Definition:
        # The Decorator Pattern attaches additional
        # responsibilities to an object dynamically.
        # Decorators provide a flexible alternative to
        # subclassing for extending functionality.

from abc import ABC, abstractmethod

# A normal bevrage, it can be coffee, it can be ice tead, lemonade etc. Design Principle 1
class Beverage(ABC):

    def __init__(self):
        self.description = None

    def get_description(self):
        return self.description
    
    @abstractmethod
    def cost(self):
        pass




# The decorator class
class CondimentDecorator(Beverage):

    @abstractmethod
    def get_description():
        """So that we can name each of them, mocha, soy milk, chocolate etc"""
        pass



# Concreate class, the base beverage...ESPRESSO, Lemonade etc

class Espresso(Beverage):

    def __init__(self, description):
        self.description = description
    
    def cost(self):
        return 1.99

# Condiment, extra things that people add to coffee or lemonade
class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        # A beverage is the base here, we decorate on top of the existing beverage

        self.beverage = beverage    # DESIGN PRINCIPLE-  using composition over inheritance

    
    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + .20




# Finally the simulator

class StarDonaldsCafe:

    @classmethod
    def run(cls):
        beverage = Espresso("Espresso")
        beverage2 = Mocha(beverage)
        print(beverage2.cost())    
        print(beverage2.get_description())    


StarDonaldsCafe.run()
        # This pattern is generally used with Factory Pattern and Builder Pattern 
        # as object creation is nested and prone to bugs and kinda complex
