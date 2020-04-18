from abc import  abstractmethod
class Machines:
    """A printer interface that can print, scan and fax"""

    @abstractmethod
    def print_doc(self):
        pass

    @abstractmethod
    def scan_doc(self):
        pass

    @abstractmethod
    def fax_doc(self):
        pass

class NewPrinters(Machines):

    def print_doc(self):
        pass
    def scan_doc(self):
        pass
    def fax_doc(self):
        pass

class OldPrinters(Machines):

    def print_doc(self):
        print("Print Logic Here")

    def scan_doc(self):
        """
        An old printer can't scan or fax...what should we do of this method now
        This will be visible to OldPrinter clss users(objs) so they might try to call it
        """
        pass

    def fax_doc(self):
        pass

# WHAT WE CAN DO IS CREATE SEPARATE INTERFACES and then use them accordingly

class Printer:
    @abstractmethod
    def print_doc(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan_doc(self, document):
        pass

class OldPrinter(Printer):
    def print_doc(self, document):
        print(document)

class NewPrinter(Printer,Scanner):
    def print_doc(self, document):
        print(document)

    def scan_doc(self, document):
        print(document)