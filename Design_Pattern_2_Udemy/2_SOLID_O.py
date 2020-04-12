# 10TH April 2020 11:42 AM
# Think of the scenario here as you are selling different products and
# you have different size and colors product, so you might need to filter those products to show it to the
 # clients or customers

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

# NOTE: WE SHOULD AVOID THIS as it VIOLATES Open Close Principal
class ProductFilter:
    """
    here in fist release we only filtered all the products by color, then we were asked to add size and then color and size and so on
    """

    def filter_by_color(self, products, color):
        for product in products:
            if product.color == color:
                yield product

    def filter_by_size(self, products, size):
        for product in products:
            if product.size == size:
                yield product

    def filter_by_size_and_color(self, products, size, color):
        for product in products:
            if product.color == color and product.size == size:
                yield product

    # here we have state space explosion
    # if we had 3 criteria
    # c, s, w, cs, cw, sw, cws = 7 methods


# WE SHOULD USE THIS INSTEAD

class Specification:

    # Each and every filter should inherit this and overright the below function
    def is_satisfied(self, item):
        pass

    # lets overright "&" giving it another specification
    def __and__(self, other):
        return AndSpecification(self, other)

class Filter:
    """Provide items to filter and specification/filter on value, every new filter should implement this(Open Extension)"""
    def filter(self, items, spec):
        pass


# Base classes have been defined, base for specifications and filters
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    """Overriding & and AND specifications"""

    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))

class Newfilter(Filter):

    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):  # go to spec and check if this single item's color is equal to spec's color or size
                yield item

if __name__ == "__main__":
    p1 = Product("diamond", Color.RED, Size.SMALL)
    p2 = Product("Spade", Color.GREEN, Size.SMALL)
    p3 = Product("ACE", Color.BLUE, Size.MEDIUM)
    p4 = Product("heart", Color.RED, Size.LARGE)

    products = [p1, p2, p3, p4]
    old_filter = ProductFilter()
    # map(lamda x: x.name,old_filter.filter_by_color(products, Color.RED))
    print(f"OLD Filter - {list(map(lambda y: (y.name, y.color, y.size), old_filter.filter_by_color(products, Color.RED)))}")
    print(f"OLD Filter - {list(map(lambda y: (y.name, y.color, y.size), old_filter.filter_by_size(products, Size.LARGE)))}")

    new_filter = Newfilter()
    green_spec = ColorSpecification(Color.GREEN)

    for prod in new_filter.filter(products, green_spec):
        print(prod.name, prod.color)

    large_red = SizeSpecification(Size.LARGE) & ColorSpecification(Color.RED)
    for prod in new_filter.filter(products, large_red):
        print(prod.name, prod.color)


    # One benifit i see here is you can have N no of "&" specifications and you don't have to add methods explicitly
    # just different types of objects working together
    # KINDA COMPLEX THO