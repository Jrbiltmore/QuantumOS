# Placeholder content for mesh_network_builder.py
import random

class MeshNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.connected_nodes = []

    def connect_node(self, node):
        if node not in self.connected_nodes:
            self.connected_nodes.append(node)
            node.connect_node(self)  # Ensure bidirectional connection

    def disconnect_node(self, node):
        if node in self.connected_nodes:
            self.connected_nodes.remove(node)
            node.disconnect_node(self)  # Ensure bidirectional disconnection

    def display_connections(self):
        connected_node_ids = [node.node_id for node in self.connected_nodes]
        print(f"Node {self.node_id} is connected to: {connected_node_ids}")

class MeshNetwork:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def remove_node(self, node):
        for n in self.nodes:
            n.disconnect_node(node)
        self.nodes.remove(node)

    def build_random_mesh(self):
        for node in self.nodes:
            possible_connections = [n for n in self.nodes if n != node]
            random_connections = random.sample(possible_connections, k=random.randint(1, len(possible_connections)))
            for connection in random_connections:
                node.connect_node(connection)

    def display_network(self):
        for node in self.nodes:
            node.display_connections()

# Example usage
if __name__ == "__main__":
    mesh_network = MeshNetwork()
    nodes = [MeshNode(node_id=f"Node_{i}") for i in range(5)]
    
    for node in nodes:
        mesh_network.add_node(node)

    mesh_network.build_random_mesh()
    mesh_network.display_network()
