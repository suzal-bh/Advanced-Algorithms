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
def preorder_traversal(root):
    result = []

    if root is None:
        return result

    s = stack()
    s.push(root)

    while not s.empty():
        current = s.pop()
        result.append(current.value)

        # push right first so left is processed first
        if current.rightChild is not None:
            s.push(current.rightChild)
        if current.leftChild is not None:
            s.push(current.leftChild)

    return result
