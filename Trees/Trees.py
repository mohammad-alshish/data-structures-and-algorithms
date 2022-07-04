class TNode():
    """This the constructor for the tree node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self,root =None):
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
  tree1 = BinarySearchTree()
  tree1.root = TNode(10)
  tree1.root.left = TNode(8)
  tree1.root.right = TNode(15)
  tree1.root.left.left = TNode(5)
  tree1.root.left.right = TNode(7)
  tree1.root.right.right = TNode(20)
  tree1.root.right.left = TNode(17)
  tree1.add(6)
  print(tree1.pre_order())
  print(tree1.contains())
