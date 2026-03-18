class Tree:
    """
    Class tree acts as a lookup table for Node objects

    Attributes:
        - nodes (dict): A dictionary of {name: Node} objects
    Methods:
        - add_node: Adds Node object to tree using the name as key and Node Object as value
        - convert_to_newick: TBD
    """
    def __init__(self, seq_ids):
      self.nodes = {}
      for seq_id in seq_ids:
          self.add_node(seq_id, [])

    def add_node(self, name, neighbors):
      self.nodes[name] = Node(name, neighbors)

    def convert_to_newick(self):
        """Build an unrooted Newick string based on nodes and their neighbors"""

        # Build undirected adjacency list --> adj[node_name] = {neighbor_name: branch_length}
        adj = {name: {} for name in self.nodes}
        for name, node in self.nodes.items():
            for neighbor, branch in node.neighbors.items():

                # Add both directions
                adj[name][neighbor] = branch
                adj[neighbor][name] = branch  

        # Pick internal node as the arbitrary virtual display root
        start = next(name for name in self.nodes if name.startswith("internal"))

        # Recursive DFS search 
        def _build(node_name, came_from):

            # Get all neighbors and branch lengths from current node, exclude node we just visited
            neighbors = {nbr: bl for nbr, bl in adj[node_name].items() if nbr != came_from}

            # If we have a leaf node (no neighbors) just return its name
            if not neighbors:
                return node_name

            # Iterate recursively through each neighbor and add the branch length --> create a list
            parts = [f"{_build(nbr, node_name)}:{round(bl, 3)}" for nbr, bl in neighbors.items()]
            print(parts)

            # Internal nodes get no label in Newick string format
            label = "" if node_name.startswith("internal") else node_name

            # Join all parts with commas and wrap with parantheses
            return f"({','.join(parts)}){label}"

        # Iterate recursively through the tree starting with start node
        return _build(start, None) + ";"


class Node:
    """
    Class Node represents all nodes in a phylogenetic tree

    Attributes:
    - name (str): Name of node
    - neighbors (dict): Dictionary of {neighbor_name: branch_length}, built from input list of tuples [(neighbor_name, branch_length)]

    """
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = {}
        for seq_id, branch_length in neighbors:
             self.neighbors[seq_id] = branch_length