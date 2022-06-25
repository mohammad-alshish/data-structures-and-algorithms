class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class Stack():
    def __init__(self, node=None):
        self.top = node

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop (self):
        if self.is_empty():
            raise BaseException("The stack is empty")
        else:
           node = self.top
           self.top = self.top.next
           return node.value

    def peek(self):
        if self.is_empty():
            raise BaseException("The stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top == None


class Queue():
    def __init__(self, front=None):
        self.front = front
        self.back = None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node

    def dequeue(self):
        if self.is_empty():
            raise BaseException("The stack is empty")
        temp = self.front
        self.front = self.front.next
        return temp.value

    def peek(self):
        if self.is_empty():
            raise BaseException("The stack is empty")
        return self.front.value

    def is_empty(self):
        return self.front == None