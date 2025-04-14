class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    # insertion

    def enqueue(self, item):

        if (self.rear + 1 % self.size) == self.front:
            print("The circular queue is full\n")

        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item

        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

        # dequeue

    def dequeue(self):

        if self.front == -1:
            print("The circular queue is empty, please enqueue an item")

        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp

        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def print_circular_queue(self):
        if self.front == -1:
            print("No element in circular queue")

        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")

            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")

            print()


obj = CircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.print_circular_queue()

obj.dequeue()
print("After removing an element from the queue")
obj.print_circular_queue()
