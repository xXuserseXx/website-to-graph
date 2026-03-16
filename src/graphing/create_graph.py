import json


graph = {}

def create_node(node):
    graph.setdefault(node, set())

def add_edge(current_node, adjacent_node):
    graph.setdefault(current_node, set()).add(adjacent_node)

def save_graph_to_json(file_path: str):
    serializable_graph = {
        node: sorted(adjacent_nodes)
        for node, adjacent_nodes in graph.items()
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(serializable_graph, file, indent=2)
