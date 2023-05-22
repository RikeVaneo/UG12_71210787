class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class Tree:
    def __init__(self, root):
        self.root = root

    def sums(self, node):
        if node is None:
            return 0

        total = node.data
        for child in node.children:
            total += self.sums(child)

        return total

    def sibling(self, node):
        if node is None or node == self.root:
            return 0

        total = 0
        parent = self.find_parent(node)
        for child in parent.children:
            total += child.data

        return total

    def find_parent(self, node):
        # Cari parent dari node
        stack = [self.root]
        while stack:
            current = stack.pop()
            if node in current.children:
                return current
            stack.extend(current.children)

        return None

n1 = Node(200)
n2 = Node(23)
n3 = Node(11)
n1.add_child(n2)
n1.add_child(n3)

n4 = Node(13)
n5 = Node(57)
n2.add_child(n4)
n2.add_child(n5)

n6 = Node(32)
n3.add_child(n6)

n7 = Node(42)
n8 = Node(51)
n9 = Node(71)
n4.add_child(n7)
n4.add_child(n8)
n4.add_child(n9)

n10 = Node(12)
n11 = Node(15)
n5.add_child(n10)
n5.add_child(n11)

n12 = Node(33)
n13 = Node(8)
n6.add_child(n12)
n6.add_child(n13)
t = Tree(n1)

val200 = n1
val33 = n12

print(f'Total value of node {val200.data} and all of its decendands = {t.sums(val200)}')
print(f'Total value of all sibling on node {val33.data} = {t.sibling(val33)}')