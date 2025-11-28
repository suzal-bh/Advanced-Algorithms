class node:
    def __init__(self, value, parent, leftChild, rightChild):
        self.value = value
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
class stack:
    def __init__(self):
        self.elements = []
    def push(self, x):
        self.elements.append(x)
    def pop(self):
        return self.elements.pop(-1)
    def empty(self):
        return len(self.elements) == 0

# function to do pre order traversal using the stack
def preorder_collect(start):

    collected = []
    nodes_to_visit = stack()

    if start is None:
        return collected

    nodes_to_visit.push(start)

    while not nodes_to_visit.empty():
        node_item = nodes_to_visit.pop()
        collected.append(node_item.value)

        # push right before left
        right = node_item.rightChild
        left = node_item.leftChild

        if right is not None:
            nodes_to_visit.push(right)

        if left is not None:
            nodes_to_visit.push(left)

    return collected

A = node('A', None, None, None)
B = node('B', A, None, None)
C = node('C', A, None, None)
D = node('D', B, None, None)
E = node('E', B, None, None)

A.leftChild = B
A.rightChild = C
B.leftChild = D
B.rightChild = E

print(preorder_collect(A))