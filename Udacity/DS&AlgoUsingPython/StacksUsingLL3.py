"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""


class Element():
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
      self.head = new_element
    else:
      self.head = new_element

  def insert_first(self, new_element): # Can be improved...check course answer
    if self.head:
      new_element.next = self.head
      self.head = new_element
    else:
      self.head = new_element

  def delete_first(self): # i think mine is better...in fact recommended solution
    current = self.head
    if self.head:
      self.head = current.next
      current.next = None
      return current
    else:
      # print("Empty")
      return None

  def traverse(self):
    current = self.head
    if self.head:
      while current.next:
        print(current.value)
        current = current.next
      else:
        print(current.value)
    else:
      print('Linked List is Empty')

class Stack():
  def __init__(self, top=None):
    self.ll = LinkedList(top)

  def push(self, new_element):
    "Push (add) a new element onto the top of the stack"
    self.ll.insert_first(new_element)

  def pop(self):
    "Pop (remove) the first element off the top of the stack and return it"
    return self.ll.delete_first()



# ll = LinkedList()
# ll.insert_first(Element(1))
# ll.insert_first(Element(2))
# ll.insert_first(Element(3))
# ll.insert_first(Element(4))
# ll.traverse()
# ll.delete_first()
# ll.delete_first()
# ll.delete_first()
# ll.traverse()


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)

print (stack.pop().value)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop())
stack.push(e4)
print (stack.pop().value)