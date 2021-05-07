class Node:
    __slots__ = ['_value', '_parent', '_children']
    def __init__(self, value):
        """
        Construct a new node with value, parent node, and child nodes.
        """
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children
    # node1.add_child(node2)
    # node2.add_parent(node1)
    def add_child(self, node):
        if node not in self._children:
            self._children.append(node) # might need node.value
            if node.parent != self:
                node.parent = self
        else:
            print('Node already exists in list.')

    @parent.setter
    def parent(self, node):
        # if node not in self._children:
        # if(node != None):
        if self._parent:
            self._parent.remove_child(self)
        self._parent = node
        if self._parent:
            node.add_child(self)  # might need node.value
        # else:
        #     print('Node already exists in list.')

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None
        else:
            print("Node doesn't exist in list.")
    
    def depth_search(self, value):
        if self._value == value:
            return self
        for node in self._children:
            node_were_looking_for = node.depth_search(value)
            if node_were_looking_for:
                return node_were_looking_for
        return None
    
    def breadth_search(self, value):
        res = None
        que = [self]
        while que:
            if que[0].value == value:
                res = que[0]
            for node in que[0].children:
                que.append(node)
            que.pop(0)
        return res

        


# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")

# node3.parent = node1
# node3.parent = node2

# print(node1.children)
# print(node2.children)
