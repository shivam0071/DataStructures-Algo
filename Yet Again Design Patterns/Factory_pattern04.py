# We have a pizza store that creates a pizza object and do things with pizza
# A pizza store can be located in any country and can make different kinds of PIZZA

from abc import ABC, abstractmethod

class Pizza(ABC):

    def __init__(self, name):
        self.name = name

    def prepare(self):
        print(f"Preparing {self.name} PIZZA")

    def bake(self):
        print(f"BAKING {self.name} PIZZA!!!!")

    def cut(self):
        print(f"Cutting {self.name} Pizza into 6 pieces")

    def box(self):
        print(f"BOXING THE GODDAMN PIZZA!!!")


class CheezePizza(Pizza):

    def __init__(self):
        self.name = "Cheeze"

class VeggiePizza(Pizza):

    def __init__(self):
        self.name = "Veggie"

class CalmPizza(Pizza):

    def __init__(self):
        self.name = "Calm"


# FACTORY HERE
class PizzaStore(ABC):

    def __init__(self, type_of_pizza):
        self.pizza_type = type_of_pizza

    def order_pizze(self):
        pizza = self.create_pizza(self.pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    # Each Country Store can define how it creates a Pizza by implementing this
    # Delhi cheeze pizza can be different than Kerela Cheeze pizza
    # So delhi store can define how it creates the pizza(the pizza objects to be made)
    # meanwhile Pizzastore abstract class is unaware of what pizza object will be created.
    # it just knows that it will be a pizza
     
    @abstractmethod
    def create_pizza(self, pizza_type):
        pass

class DelhiPizzaStore(PizzaStore):

    def __init__(self, pizza_type):
        super().__init__(pizza_type)

    def create_pizza(self, pizza_type):
        if pizza_type == "cheeze":
            return CheezePizza()
        elif pizza_type == "calm":
            return CalmPizza()
        else:
            return VeggiePizza()

if __name__ == "__main__":
    cheeze = CheezePizza()
    veggie = VeggiePizza()
    calm = CalmPizza()
    cheeze.cut()
    veggie.cut()
    calm.cut()

    delhiKaPizza = DelhiPizzaStore("cheeze")
    delhiKaPizza.order_pizze()