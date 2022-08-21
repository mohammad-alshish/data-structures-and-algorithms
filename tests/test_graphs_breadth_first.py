from graphs_breadth_first.graphs_breadth_first import Graph


def test_breadth_first():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    e_1 = graph.add_edge(a, b, 2)
    e_2 = graph.add_edge(a, c, 2)
    actual = graph.breadth_first(a)
    assert actual == [a, b, c]
