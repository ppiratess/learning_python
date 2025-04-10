# implementing a dynamic queue where user can define the length


class Dynamic_Queue:

    def __init__(self, length):
        self.length = length
        # create a array of length with with no data [_,_,_,...]
        self.queue = [None] * length
        self.head = -1
        self.tail = -1

        # you can also assign -1 to both values like
        # self.head = self.tail = -1

    def enqueue(self, item):

        if self.tail == self.length - 1:
            print("The queue is full\n")

        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item

        else:
            self.tail += 1
            self.queue[self.tail] = item

    def dequeue(self):

        if self.head == -1:
            print("The head is empty")

        elif self.head == self.tail:
            temp_data = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp_data

        else:
            temp_data = self.queue[self.head]
            self.head += 1
            return temp_data

    def print_dynamic_queue(self):

        if self.head == -1:
            print("No element in the queue")

        else:
            for index in range(self.head, self.tail + 1):
                print(self.queue[index], end=" ")
            print()


obj = Dynamic_Queue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.print_dynamic_queue()

obj.dequeue()
print("After removing an element from the queue")
obj.print_dynamic_queue()
