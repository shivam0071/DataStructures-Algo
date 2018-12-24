class Element(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList(object):
    def __init__(self, head=None):
      self.head = head

    def append(self, new_element):
      current = self.head
      if self.head:
        while current.next:
          current = current.next
        current.next = new_element
      else:
        self.head = new_element

    def get_position(self, position):
      """Get an element from a particular position.
      Assume the first position is "1".
      Return "None" if position is not in the list."""
      current = self.head
      if self.head:
        for item in range(1, position):
          if current.next == None:
            # print('No ITEM at position {} the current item is {}'.format(position,current.value))
            return None
          current = current.next
        else:
          # print('The Item at position {} is {}'.format(position,current.value))
          return current
      else:
        return None

    def insert(self, new_element, position):
      """Insert a new node at the given position.
      Assume the first position is "1".
      Inserting at position 3 means between
      the 2nd and 3rd elements."""
      current = self.head
      if self.head:
        if position == 1:
          new_element.next = current
          self.head = new_element
          return None

        for item in range(1,position-1):
          if current.next == None:
            return None
          current = current.next
        else:
          new_element.next = current.next
          current.next = new_element
      else:
        if position == 1:
          self.head = new_element

    def delete(self, value):
      """Delete the first node with a given value."""
      current = self.head
      previous = current
      if self.head:
        if self.head.value == value:
          self.head = self.head.next
          return None
        while current.next:
          if current.value == value:
            previous.next = current.next
            current.next = None
            return None
          previous = current
          current = current.next
        else:
          if current.value == value:
            previous.next = current.next




    def traverse(self):
      current = self.head
      if self.head:
        while current.next:
          print(current.value,end=' ')
          current = current.next
        else:
          print(current.value)
      else:
        print('Linked List is Empty')

if __name__ == '__main__':
  # list1 = LinkedList()
  # list1.traverse()
  # list1.append(Element(33))
  # list1.get_position(1)
  # list1.traverse()
  # list1.append(Element(44))
  # list1.append(Element(45))
  # list1.append(Element(46))
  # list1.append(Element(47))
  # list1.append(Element(48))
  # list1.traverse()
  # list1.get_position(4)
  # list1.get_position(1)
  # list1.get_position(5)
  # list1.get_position(6)
  # list1.get_position(10)
  # list1.traverse()
  # list1.insert(Element(51),3)
  # list1.insert(Element(52), 1)
  # list1.insert(Element(53), 1)
  # list1.insert(Element(59), 20)
  # list1.traverse()
  # list1.delete(51)
  # list1.traverse()
  # list1.delete(52)
  # list1.traverse()
  # list1.delete(46)
  # list1.traverse()
  # list1.delete(47)
  # list1.traverse()
  # list1.delete(53)
  # list1.traverse()
  # list1.delete(48)
  # list1.traverse()
  e1 = Element(1)
  e2 = Element(2)
  e3 = Element(3)
  e4 = Element(4)

  ll = LinkedList(e1)
  ll.append(e2)
  ll.append(e3)

  ll.traverse()
  print (ll.head.next.next.value)
  print(ll.get_position(3).value)