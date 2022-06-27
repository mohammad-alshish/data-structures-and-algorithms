from stack_and_queue.stack_and_queue import Node, Stack


class Pseudo_Queue():

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, value):
        self.s1.push(value)

    def dequeue(self):
        while not self.s1.is_empty():
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.pop()