graph = {}

def create_node(node):
    graph.setdefault(node, set())

def add_edge(current_node, adjacent_node):
    graph.setdefault(current_node, set()).add(adjacent_node)