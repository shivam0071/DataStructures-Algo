from enum import Enum
from abc import abstractmethod

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# DEFINE A RULE TO BE FOLLED as a solution
class RelationshipBrowser:

    @abstractmethod
    def find_all_children_of(self, name):
        pass

# Low level module
class Relationships_OLD:
    def __init__(self):
        self.relation = [] # low level as we are dealing with storages...it can be DB too..it has the main logic

    def add_parent_child(self, parent, child):
        self.relation.append((parent, Relationship.PARENT, child))

    def show_relations(self):
        print(self.relation)

class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relation = [] # low level as we are dealing with storages...it can be DB too..it has the main logic

    def add_parent_child(self, parent, child):
        self.relation.append((parent, Relationship.PARENT, child))

    def show_relations(self):
        print(self.relation)

    def find_all_children_of(self, name):
        for data in self.relation:
            if data[0].name == name and data[1] == Relationship.PARENT:
                yield data[2].name

class Research:
    # This is wrong as it is greatly dependent on low level class
    # what is relation list gets changed and dictionary or DB is added, We have to change this as well then
    # Instead handle the logic in the low level class only
    # def __init__(self, relationships):
    #     for data in relationships.relation:
    #         if data[0].name == "John" and data[1] == Relationship.PARENT:
    #             print(f"JOHN is the FATHER of {data[2].name}")

    # USE THIS
    def __init__(self, browser):
        for child in browser.find_all_children_of("John"):
            print(f"JOHN is the FATHER of {child}")

john = Person("John")
kid1 = Person("kid1")
kid2 = Person("kid2")

relation = Relationships()
relation.add_parent_child(john, kid1)
relation.add_parent_child(john, kid2)
relation.show_relations()

# lets research the realtion using another class
research = Research(relation)