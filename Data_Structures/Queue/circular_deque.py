class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = 0
        self.front = 0
        self.rear = 0
        self.max_size = k
        self.queue = [None] * k


    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.queue[self.front] = value
            self.front += 1
            self.rear += 1
            self.size += 1
            return True
        elif self.front == 0:
            self.front = self.max_size - 1
            self.queue[self.front] = value
            self.size += 1
            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = value
            self.size += 1


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        elif self.rear == 0:
            self.rear = self.max_size - 1
            self.size -= 1
            return True
        else:
            self.rear -= 1
            self.size -= 1
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.queue[self.front] if not self.isEmpty() else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.queue[self.rear] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self.size == self.max_size:

            return True
        return False

if __name__ == "__main__":

    # Your MyCircularDeque object will be instantiated and called as such:
    k = 7
    obj = MyCircularDeque(k)
    param_1 = obj.insertFront(2)
    print(obj.queue)
    param_2 = obj.insertLast(3)
    print(param_1)
    print(obj.queue)
    # param_3 = obj.deleteFront()
    # param_4 = obj.deleteLast()
    # param_5 = obj.getFront()
    # param_6 = obj.getRear()
    # param_7 = obj.isEmpty()
    # param_8 = obj.isFull()