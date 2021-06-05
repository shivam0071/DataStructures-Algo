from abc import ABC, abstractmethod

# BASE CLASSES
class Duck(ABC):


    @abstractmethod
    def display(self):
        pass

    def fly(self):
        print("I believe i can fly")

    def quack(self):
        print("QUACK QUACK!!!!")

    def swim(self):
        print("Every Duck Floats, Even the Fake Ones")



class Normal_Duck(Duck):

    def display(self):
        print("I am an ordinary duck")


class Rubber_Duck(Duck):

    def display(self):
        print("I am an ordinary duck")

    def fly(self):
        print("Rubber duck can't fly!!!")

    def quack(self):
        print("Squak Squak!!!")



# Behaviours
class Flyable(ABC):

    @abstractmethod
    def fly(self):
        pass

class Quackable(ABC):
    @abstractmethod
    def quack(self):
        pass


class Fly(Flyable):
    def fly(self):
        print("Normal Fly!!!")

class RocketFly(Flyable):
    def fly(self):
        print("Rocket Fly")

class Glide_Fly(Flyable):
    def fly(self):
        print("glideFly Fly")

class CantFly(Flyable):
    def fly(self):
        print("Cant fly!!!!")


class Normal_Duck(Duck):

    def display(self):
        print("I am an ordinary duck")