adj_list = {"A": ["B", "C"],
            "B": ["A", "D", "E"],
            "C": ["A", "D"],
            "D": ["C", "B", "E"],
            "E": ["B", "D"]     }

edges = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "D"), ("D", "E")]

class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_list = {}

        #initalize each node with an empty list
        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self, v, e):
        self.adj_list[v].append(e)
        self.adj_list[e].append(v)

    def degree_vertex(self, node):
        degree = len(self.adj_list[node])
        return degree

    def print_adj(self):
        for node in self.nodes:
            print(node, ":", self.adj_list[node])


nodes = ["A", "B", "C", "D", "E"]
graph = Graph(nodes)
for v, e in edges:
    graph.add_edge(v,e)

print(graph.degree_vertex("B")) #wrong
