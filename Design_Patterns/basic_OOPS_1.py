class User:
  def __init__(self, name):
    self.name = name

  def show_name(self):
    print("Hi There, what's happening {}". format(self.name))


if __name__ == "__main__":
  user = User(name = "Shaan")
  user.show_name()
  print("*" * 10)