from graphviz import Digraph


class TreeNode:
    def __init__(self, node):
        self.node = node
        self.child_left = None
        self.child_right = None

    # set the left child of current node
    def set_child_left(self, node):
        self.child_left = TreeNode(node)

    # set the right child of current node
    def set_child_right(self, node):
        self.child_right = TreeNode(node)

    # returns recursively all childs beginning from the current node as string
    def print_childs(self):
        if self.child_left is None and self.child_right is None:
            return f"{self.node}"
        elif self.child_left is not None and self.child_right is None:
            return f"{self.node}(L_{self.child_left.print_childs()})"
        elif self.child_left is None and self.child_right is not None:
            return f"{self.node}(R_{self.child_right.print_childs()})"
        elif self.child_left is not None and self.child_right is not None:
            return f"{self.node}(L_{self.child_left.print_childs()}, R_{self.child_right.print_childs()})"


class BinarySearchTree:
    def __init__(self, root):
        self.root = TreeNode(root)
        self.dot = None
        self.node_count = 1

    # insert a new node into the BST
    def insert_node(self, node):
        recent_node = self.root
        place_found = False
        while not place_found:
            if node < recent_node.node:
                if recent_node.child_left is None:
                    recent_node.set_child_left(node)
                    place_found = True
                    self.node_count += 1
                else:
                    recent_node = recent_node.child_left
            elif node > recent_node.node:
                if recent_node.child_right is None:
                    recent_node.set_child_right(node)
                    place_found = True
                    self.node_count += 1
                else:
                    recent_node = recent_node.child_right

    # print the whole BST
    def print_tree(self):
        print(self.root.print_childs())

    # search node in BST
    # returns if found and amount of comparisons needed
    def search_node(self, node):
        compare_count = 0
        recent_node = self.root
        while recent_node is not None:
            if node < recent_node.node:
                compare_count += 1
                if recent_node.child_left is None:
                    return False, compare_count
                else:
                    recent_node = recent_node.child_left
            elif node > recent_node.node:
                compare_count += 1
                if recent_node.child_right is None:
                    return False, compare_count
                else:
                    recent_node = recent_node.child_right
            else:
                compare_count += 1
                return True, compare_count

    # print if found node in BST and how many comparisons needed
    def search_node_print(self, node):
        in_tree, steps_tree = self.search_node(node)
        if in_tree:
            print(f"{node} in Tree ({steps_tree} nodes compared)")
        else:
            print(f"{node} not in Tree ({steps_tree} nodes compared)")

    # important helper method to render the BST with graphviz
    def gen_graph_node(self, graph_node):
        if graph_node.child_left is not None:
            self.dot.node(str(graph_node.child_left.node), str(graph_node.child_left.node))
            self.dot.edge(str(graph_node.node), str(graph_node.child_left.node))
            self.gen_graph_node(graph_node.child_left)
        else:
            self.dot.node(str(graph_node.node) + "LNone", "")
            self.dot.edge(str(graph_node.node), str(graph_node.node) + "LNone")
        if graph_node.child_right is not None:
            self.dot.node(str(graph_node.child_right.node), str(graph_node.child_right.node))
            self.dot.edge(str(graph_node.node), str(graph_node.child_right.node))
            self.gen_graph_node(graph_node.child_right)
        else:
            self.dot.node(str(graph_node.node) + "RNone", "")
            self.dot.edge(str(graph_node.node), str(graph_node.node) + "RNone")

    # generate png image of the BST
    def gen_graph_tree(self):
        self.dot = Digraph(format='png')
        self.dot.node(str(self.root.node), str(self.root.node))
        self.gen_graph_node(self.root)
        self.dot.render("BST", "images")
        del self.dot


if __name__ == '__main__':
    B = BinarySearchTree(8)
    B.insert_node(3)
    B.insert_node(2)
    B.insert_node(10)
    B.insert_node(5)
    B.insert_node(4)
    B.insert_node(7)
    B.insert_node(12)
    B.insert_node(11)
    B.print_tree()
    B.search_node_print(4)
    B.search_node_print(11)
    B.gen_graph_tree()
