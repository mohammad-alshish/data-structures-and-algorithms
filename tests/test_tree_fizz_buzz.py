from tree_fizz_buzz.tree_fizz_buzz import TNode,kTree ,fizz_buzz_tree


def test_fizzbuzz():
    k_tree = kTree()
    k_tree.root = TNode(1)
    nodes = []

    for val in range(2, 30):
        nodes.append(TNode(val))

    for node in nodes:
        k_tree.root.child.append(node)

    fizz_buzz_tree(k_tree)

    expected = ["FizzBuzz" if (i % 5 == 0 and i % 3 == 0) else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, 30)]
    actual = k_tree.show_all_vals()

    assert actual == expected