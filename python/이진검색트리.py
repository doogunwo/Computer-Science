class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self.insert_value(self.root, data)
        return self.root is not None

    def insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self.insert_value(node.left, data)
            else:
                node.right = self.insert_value(node.right, data)
        return node

    def postorder_traversal(self, node, result):
        if node is not None:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.data)

if __name__ == "__main__":
    array = []
    while True:
        try:
            array.append(int(input()))
        except EOFError:
            break
    
    bst = BinaryTree()
    for x in array:
        bst.insert(x)

    result = []
    bst.postorder_traversal(bst.root, result)

    for num in result:
        print(num)
