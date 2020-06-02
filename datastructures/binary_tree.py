class TreeNode:
    def __init__(self, node):
        self.node = node
        self.child_left = None
        self.child_right = None

    def set_child_left(self, node):
        self.child_left = TreeNode(node)

    def set_child_right(self, node):
        self.child_right = TreeNode(node)

    def print_childs(self):
        if self.child_left is None and self.child_right is None:
            return "{}".format(
                self.node
            )
        elif self.child_left is not None and self.child_right is None:
            return "{}: (L: {})".format(
                self.node,
                self.child_left.print_childs()
            )
        elif self.child_left is None and self.child_right is not None:
            return "{}: (R: {})".format(
                self.node,
                self.child_right.print_childs()
            )
        elif self.child_left is not None and self.child_right is not None:
            return "{}: (L: {}, R: {})".format(
                self.node,
                self.child_left.print_childs(),
                self.child_right.print_childs()
            )


class BinarySearchTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def insert_node(self, node):
        recent_node = self.root
        place_found = False
        while not place_found:
            if node < recent_node.node:
                if recent_node.child_left is None:
                    recent_node.set_child_left(node)
                    place_found = True
                else:
                    recent_node = recent_node.child_left
            elif node > recent_node.node:
                if recent_node.child_right is None:
                    recent_node.set_child_right(node)
                    place_found = True
                else:
                    recent_node = recent_node.child_right

    def print_tree(self):
        print(self.root.print_childs())


if __name__ == '__main__':
    B = BinarySearchTree(8)
    B.insert_node(3)
    B.insert_node(10)
    B.insert_node(5)
    B.insert_node(7)
    B.insert_node(12)
    B.insert_node(11)
    B.print_tree()
