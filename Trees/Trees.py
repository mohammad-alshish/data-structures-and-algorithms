from stack_and_queue.stack_and_queue import Queue


class TNode():
    """This the constructor for the tree node"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        """method handle the pre-order by recurssion and return the values in tree as array"""
        if not self.root:
            return self.root

        result = []

        def _walk(root):
            result.append(root.value)

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

        _walk(self.root)

        return result

    def in_order(self):
        """method handle the in-order by recurssion and return the values in tree as array"""
        if not self.root:
            return self.root

        result = []

        def _walk(root):

            if root.left:
                _walk(root.left)

            result.append(root.value)

            if root.right:
                _walk(root.right)

        _walk(self.root)

        return result

    def post_order(self):
        """method handle the post-order by recurssion and return the values in tree as array"""
        if not self.root:
            return self.root

        result = []

        def _walk(root):

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

            result.append(root.value)

        _walk(self.root)

        return result

    def find_maximum_value(self) -> int:
        """this method is used to find the highest number in tree and return it"""
        max_value = self.root.value

        def _walk(root):
            nonlocal max_value
            if max_value < root.value:
                max_value = root.value
            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return max_value

    def breadth_first(self) -> list:
        """this method is using Queue methods to loop through the tree and add the values to our list (it's pre-order + fitst-in first-out concept) """
        breadth_queue = Queue()
        list = []
        breadth_queue.enqueue(self.root)

        while not breadth_queue.is_empty():
            front = breadth_queue.dequeue()
            list.append(front.value)
            if front.left:
                breadth_queue.enqueue(front.left)
            if front.right:
                breadth_queue.enqueue(front.right)
        return list


class BinarySearchTree(BinaryTree):

    def add(self, value):
        """add a value depending on the binary search concept"""

        node = TNode(value)
        current = self.root

        if current is None:
            self.root = node

        if node == current:
            return

        while current is not None:
            if node.value < current.value:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right

    def contains(self, value):
        """check if the a given value is in tree or not by returning True or False"""
        current = self.root

        while current:

            if value == current.value:
                return True

            elif value < current.value:
                current = current.left


            elif value > current.value:
                current = current.right

        return False


if __name__ == "__main__":
    tree = BinaryTree()
    # tree = BinarySearchTree()
    tree.root = TNode(2)
    tree.root.left = TNode(7)
    tree.root.right = TNode(5)
    tree.root.left.left = TNode(2)
    tree.root.left.right = TNode(6)
    tree.root.right.right = TNode(8)
    tree.root.right.left = TNode(9)
    tree.root.right.right.right = TNode(4)
    tree.root.right.right.right.right = TNode(7)
    tree.root.right.right.right.right.right = TNode(15)

    print(tree.breadth_first())
