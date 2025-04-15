# Data structure stored in form of chain


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)


# node1.next = node2
# node2.next = node3
# node3.next = node4

# current_node = node1


# while current_node:
#     print(current_node.data, end=" -> ")
#     current_node = current_node.next
# print("null")


# appending a node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # list1 targets node1 i.e current is node1
    def append(self, next_node):
        current_head = self.head

        # a node will always have a next
        if current_head:
            while current_head.next:
                current_head = current_head.next
            current_head.next = next_node

        # current is none i.e list is empty
        else:
            self.head = next_node

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next


li = LinkedList(node1)

li.append(node2)
li.append(node3)

# li.append(node4)


print(li.print())
