
# CIRCULAR QUEUE....not really as we are using list and pop actually shifts the items to the left
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.cqueue = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.cqueue) < self.k:
            self.cqueue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if len(self.cqueue) != 0:
            self.cqueue.pop(0)
            return True
        return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if len(self.cqueue) > 0:
            return self.cqueue[0]
        return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if len(self.cqueue) > 0:
            return self.cqueue[-1]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if len(self.cqueue) == 0:
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if len(self.cqueue) == self.k:
            return True
        return False

class REAL_MyCircularQueue:
    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.queue = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = value
            self.size += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return True

    def Front(self) -> int:
        return self.queue[self.front] if self.size else -1

    def Rear(self) -> int:
        return self.queue[self.rear] if self.size else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size

class My_CircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None] * k
        self.front = 0
        self.rear = 0
        self.size = 0
        self.max_size = k


    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = value
            self.size += 1
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return True

    def Front(self) -> int:
        return self.queue[self.front] if self.size else -1

    def Rear(self) -> int:
        return self.queue[self.rear] if self.size else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size

if __name__ == "__main__":

# Your MyCircularQueue object will be instantiated and called as such:
    k = 10
    value = 1
    obj = My_CircularQueue(k)
    param_1 = obj.enQueue(value)
    print(obj.queue)
    obj.enQueue(33)
    print(obj.queue)
    param_2 = obj.deQueue()
    print(obj.queue)
    param_3 = obj.Front()
    obj.enQueue(4)
    obj.enQueue(545)
    print(obj.queue)
    param_4 = obj.Rear()
    param_5 = obj.isEmpty()
    param_6 = obj.isFull()

    print(param_1,param_2,param_3,param_4,param_5,param_6)