from graphs.graphs import Graph

'''
Arguments: Node
Return: A collection of nodes in the order they were visited.
Display the collection
'''


class Graph(Graph):
    def breadth_first(self, vertex):
        nodes = []
        breadth = [vertex]
        visited = set()

        visited.add(vertex)

        while breadth:
            front = breadth.pop(0)
            nodes.append(front)

            for neighbor in self.get_neighbors(front):
                if neighbor.vertex not in visited:
                    visited.add(neighbor)
                    breadth.append(neighbor.vertex)

        return nodes
