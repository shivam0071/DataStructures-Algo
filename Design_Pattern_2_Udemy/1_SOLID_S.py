# SRP
class Journal:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(text)
        self.count += 1

    def remove_entry(self, idx):
        return self.entries.pop(idx)

    def __str__(self):
        return '\n'.join(self.entries)

    # THIS is a bad practice
    # def save_journal(self):
    #     pass
    #
    # def load_journal(self):
    #     pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as f:
            f.write(str(journal))

    @staticmethod
    def load_from_file(filename):
        with open(filename) as f:
            print(f.read())

j = Journal()
j.add_entry("This is note 1")
j.add_entry("This is note 2")
j.add_entry("This is note 3")
print(j)
print(j.remove_entry(1))
# lets make a persistent class to save it

PersistenceManager.save_to_file(j, "1_SOLD_S.txt")
PersistenceManager.load_from_file("1_SOLD_S.txt")
