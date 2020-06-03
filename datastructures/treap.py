class TreapNode:
    def __init__(self, priority, key):
        self.priority = priority
        self.key = key
        self.child_left = None
        self.child_right = None

    # set the left child of current node
    def set_child_left(self, priority, key):
        self.child_left = TreapNode(priority, key)

    # set the right child of current node
    def set_child_right(self, priority, key):
        self.child_right = TreapNode(priority, key)

    # returns recursively all childs beginning from the current node as string
    def print_childs(self):
        if self.child_left is None and self.child_right is None:
            return f"[{self.key},priority:{self.priority}]"
        elif self.child_left is not None and self.child_right is None:
            return f"[{self.key},priority:{self.priority}](L_{self.child_left.print_childs()})"
        elif self.child_left is None and self.child_right is not None:
            return f"[{self.key},priority:{self.priority}](R_{self.child_right.print_childs()})"
        elif self.child_left is not None and self.child_right is not None:
            return f"[{self.key},priority:{self.priority}](L_{self.child_left.print_childs()}, R_{self.child_right.print_childs()})"


class Treap:
    def __init__(self):
        self.root = None
        self.nodes = {}
        self.node_count = 0

    # insert a new node into the treap
    def insert_node(self, priority, key):
        self.nodes[priority] = key
        self.root = None
        for node in sorted(self.nodes.items()):
            if self.root is None:
                self.root = TreapNode(node[0], node[1])
            else:
                recent_node = self.root
                place_found = False
                while not place_found:
                    if node[1] < recent_node.key:
                        if recent_node.child_left is None:
                            recent_node.set_child_left(node[0], node[1])
                            place_found = True
                            self.node_count += 1
                        else:
                            recent_node = recent_node.child_left
                    elif node[1] > recent_node.key:
                        if recent_node.child_right is None:
                            recent_node.set_child_right(node[0], node[1])
                            place_found = True
                            self.node_count += 1
                        else:
                            recent_node = recent_node.child_right

    # insert a dictionary of nodes into treap
    def insert_node_dict(self, prio_key_dict):
        for prio, key in prio_key_dict.items():
            self.insert_node(prio, key)

    # delete a node in treap by using the priority
    def delete_node(self, prio):
        self.root = None
        self.nodes.pop(prio)
        self.insert_node_dict(self.nodes)

    # print the whole treap
    def print_treap(self):
        print(self.root.print_childs())


if __name__ == '__main__':
    T = Treap()
    nodes = {
        8985: 1,
        4588: 2,
        1847: 3,
        313: 4,
        4254: 5,
        4904: 6,
        4434: 7,
        6606: 8,
        9978: 9,
        1748: 10,
        6569: 11,
        8473: 12
    }
    T.insert_node_dict(nodes)
    T.print_treap()
