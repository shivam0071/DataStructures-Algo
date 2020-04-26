class Person:

    def __init__(self):
        # address
        self.street_address = None
        self.postcode = None
        self.city = None

        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f"Address - {self.street_address}, {self.postcode}, {self.city}\n" \
               f"Employed at - {self.company_name} as {self.position} earning {self.annual_income}"

#builder
class PersonBuilder: # Facede

    def __init__(self, person=Person()): # if nothing is passed it will create a blank obj...which will be used by other builders
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)  # self.person is the init person obj...initilazed once

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)  # self.person is the init person obj...initilazed once

    def build(self):
        return self.person

#Sub-builders
class PersonJobBuilder(PersonBuilder):

    def __init__(self, person): # We did not do that above trick here because
        # its a subbuilder and we will only pass the same person used above
        super().__init__(person)  # calling parent class's init..

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):

    def __init__(self, person):  # We did not do that above trick here because
        # its a subbuilder and we will only pass the same person used above
        super().__init__(person)  # calling parent class's init..

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def city(self, city):
        self.person.city = city
        return self


if __name__ == "__main__":
    p = Person()
    print(p) # Initially everything is None, we have not initialized anything here...we could have tho

    # We will make 2 builders
    # 1 for job address
    # 2 for job details

    # and 3rd builder which actually build the person...

    # First make a person builder
    #  then make job builder...

    # in order to use the PersonJobBuilder add a property to Person Builder check line 24

    # everything is set up now

    person_builder = PersonBuilder()
    # works = person_builder.works
    # works.at("Google")
    # print(person_builder.person)
    person_builder.lives.at("Groove Street").postcode("Groove4Life").city("San Andreas")
    person_builder.works.at("Titans").as_a("Cyborg").earning(999999)
    print(person_builder.person)

    # New Person
    person2 = Person()
    person_builder2 = PersonBuilder(person2)
    print(person_builder2.person)