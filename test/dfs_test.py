from src.dfs import Graph

def test_simple_graph():
    vertices = [1, 2, 3, 4]
    edges = [(1, 2), (2, 3), (3, 4)]
    graph = Graph(vertices, edges)
    result = list(graph)
    assert result == [1, 2, 3, 4]

def test_single_vertex():
    vertices = [1]
    edges = []
    graph = Graph(vertices, edges)
    result = list(graph)
    assert result == [1]

def test_empty_graph():
    vertices = []
    edges = []
    graph = Graph(vertices, edges)
    result = list(graph)
    assert result == []