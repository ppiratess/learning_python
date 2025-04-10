# # FIFO


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        item = self.queue.pop(0)
        print(f"Dequeued: {item}")
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        print(f"Peek: {self.queue[0]}")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        print(f"Size: {len(self.queue)}")
        return len(self.queue)

    def clear(self):
        self.queue = []
        print("Queue cleared")


# Example usage
list_queue = Queue()
list_queue.enqueue(1)
list_queue.enqueue(2)
list_queue.peek()
list_queue.dequeue()
list_queue.size()
list_queue.clear()
