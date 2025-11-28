class Graph:
    def __init__(self, vertices: list[int], edges: list[tuple[int, int]]):
        self.vertices = vertices
        self.edges = edges
        self.passage= []
    
    def __iter__(self):
        if not self.passage:
            self.dfs()
        return iter(self.passage)

    def dfs(self):
        passed = set()
        self.passage = []

        def step(vertex):
            if vertex not in passed:
                passed.add(vertex)
                self.passage.append(vertex)

                neighbors = []
                for edge in self.edges:
                    if edge[0] == vertex:
                        neighbors.append(edge[1])
                    elif edge[1] == vertex:
                        neighbors.append(edge[0])
                    
                for neighbor in neighbors:
                    step(neighbor)

        for vertex in self.vertices:
            if vertex not in passed:
                step(vertex)

        return self.passage
