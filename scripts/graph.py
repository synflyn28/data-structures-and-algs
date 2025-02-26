"""
This script contains the implementation of a graph and various graph algorithms.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent_list = []
        self.visited = False

class Graph:
    def BFS(self, node):
        """
        This method performs a breadth-first search on the graph.
        """
        queue = []
        queue.append(node)
        node.visited = True

        traversal = []

        while queue:
            actual_node = queue.pop(0)
            traversal.append(actual_node.value)

            for element in actual_node.adjacent_list:
                if element.visited is False:
                    queue.append(element)
                    element.visited = True
        
        return traversal
    
    def DFS(self, node, traversal):
        """
        Traverse the graph using a depth-first search.
        """
        node.visited = True
        traversal.append(node.value)

        for element in node.adjacent_list:
            if element.visited is False:
                self.DFS(element, traversal)

        return traversal
                

if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    node1.adjacent_list.append(node2)
    node1.adjacent_list.append(node3)
    node1.adjacent_list.append(node4)
    node2.adjacent_list.append(node5)
    node2.adjacent_list.append(node6)
    node4.adjacent_list.append(node7)
    node6.adjacent_list.append(node8)

    graph = Graph()
    #print(graph.BFS(node1))
    print(graph.DFS(node1, []))