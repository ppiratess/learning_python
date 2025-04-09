class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Empty stack"

        return self.stack.pop()

    def __str__(self):
        return str(self.stack)


stack = Stack()


# Reverse a word - example

word_to_reverse = list("example")

for string in word_to_reverse:
    stack.push(string)

reversed_word = "".join(stack.pop() for _ in range(len(stack.stack)))

print("reversed word :", reversed_word)
