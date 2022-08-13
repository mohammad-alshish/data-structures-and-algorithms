from hash_tables.hash_tables import Hashtable
from Trees.Trees import BinaryTree


def hash_intersection(tree_1, tree_2):
    common = []
    binary_tree1 = tree_1.pre_order()
    binary_tree2 = tree_2.pre_order()
    hashtable = Hashtable()

    for value in binary_tree1:
        hashtable.set(key=str(value), value=value)
    for value in binary_tree2:
        if hashtable.contains(str(value)):
            common.append(value)
    return common
