import abc

class TaxCalculator(abc.ABC): # INTERFACE

  @abc.abstractmethod   # abstract method
  def tax_calculator(self):
    pass


class TaxCalculator2019(TaxCalculator):

  def tax_calculator(self):
    return 2


if __name__ == "__main__":
  tax_calc_2019 = TaxCalculator2019()
  print(tax_calc_2019.tax_calculator())