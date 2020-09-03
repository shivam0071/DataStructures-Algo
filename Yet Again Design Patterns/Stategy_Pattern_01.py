from abc import ABC, abstractmethod


# BASE CLASSES
class Duck(ABC):

    def __init__(self):
        self.fly_behaviour = None
        self.quack_behavour = None

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self.fly_behaviour.fly()

    def perform_quack(self):
        self.quack_behavour.quack()

    def swim(self):
        print("Every Duck Floats, Even the Fake Ones")
    
    # Definning Setters for Dynamic Behavour change

    def set_fly_behaviour(self, fb):
        self.fly_behaviour = fb
    
    def set_quack_behviour(self, qb):
        self.quack_behavour = qb
    
class FlyBehavior(ABC):

    @abstractmethod
    def fly(self):
        pass

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


# CONCREATE CLASSES

# IMPLEMENTING THE BEHAVIOURS or HAS A properties of base class
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I can fly, i am flying!!!!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly man!!! NOPE not possible")


class Quack(QuackBehavior):
    def quack(self):
        print("Quack!!!")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeaak!!!")



# Actual Duck -- The client
class MallardDuck(Duck):
    
    def __init__(self):
        self.fly_behaviour = FlyWithWings()
        self.quack_behavour = Quack()        

    def display(self):
        print("I am a Mallard Duck")


# Finally
class MiniDuckSimulation():

    @classmethod
    def execute_simulation(cls):
        mallard = MallardDuck()
        mallard.perform_fly()
        mallard.perform_quack()
        mallard.display()

        # Dynamic Plug and Play
        mallard.set_quack_behviour(Squeak())
        mallard.perform_quack()


MiniDuckSimulation.execute_simulation()


# We can add as many as Fly and Quack behavours and assign them to our ducks dynamically 
# Similarly we can add new behavours without changing the Base Duck code
# That way we are not adding methods to all the classes, some minght not need them