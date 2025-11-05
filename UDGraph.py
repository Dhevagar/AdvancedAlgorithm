class UDGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start, end):
        if start in self.graph and end in self.graph:
            self.graph[start].append(end)
        else:
            print("One or both vertices not found.")

    def list_outgoing_adjacent_vertex(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return []
