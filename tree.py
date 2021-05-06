class Node:
    # __slots__ = ['_value', '_parent', '_children']
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
        else:
            print('Node already exists in list.')

    @parent.setter
    def parent(self, node):
        if node not in self._children:
            self._parent = node
            node.add_child(self)  # might need node.value
        else:
            print('Node already exists in list.')
        
    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node._parent = None
        else:
            print("Node doesn't exist in list.")
