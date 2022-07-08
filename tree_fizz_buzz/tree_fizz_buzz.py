class TNode:
    """Node constructor"""
    def __init__(self, value=None):
        self.value = value
        self.child  = []


class kTree:
    """root comstructor"""
    def __init__(self, root=None):
        self.root = root
    """method to check the values"""
    def show_all_vals(self):
        all_values = []
        def check_values(node):
            all_values.append(node.value)
            if node.child:
                for child in node.child:
                    check_values(child)
        check_values(self.root)
        return all_values


def fizz_buzz_tree(kTree):
    """function to determine Fizz & Buzz"""
    def _walk(node):
        if node.child :
            for i in node.child :
                node.value = str(node.value)
                if i.value % 3 == 0 and i.value % 5 == 0:
                    i.value = "FizzBuzz"
                elif i.value % 3 == 0:
                    i.value = "Fizz"
                elif i.value % 5 == 0:
                    i.value = "Buzz"
                else:
                    i.value = str(i.value)

    _walk(kTree.root)
    return(kTree)


# if __name__ == "__main__":
#     tree = kTree()
#     expected = ["FizzBuzz" if (i % 5 == 0 and i % 3 == 0) else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, 30)]
#     print(expected)
#
#     k_tree = kTree()
#     k_tree.root = TNode(1)
#     nodes = []
#
#     for val in range(2, 50):
#         nodes.append(TNode(val))
#
#     for node in nodes:
#         k_tree.root.child.append(node)
#     fizz_buzz_tree(k_tree)
#     actual = k_tree.show_all_vals()
#
#     print(actual)