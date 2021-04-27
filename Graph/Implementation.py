class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = [end]
            else:
                self.graph_dict[start].append(end)
        print(self.graph_dict)


routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")]
g = Graph(routes)