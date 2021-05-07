from tree import Node

class KnightPathFinder:
    def __init__(self, value):
        self._x = value[0]
        self._y = value[1]
        self._root = Node((value[0], value[1]))
        self._considered_positions = {value}

    def get_valid_moves(self, pos):
        valid_moves = set()
        right1 = pos[0] + 1
        right2 = pos[0] + 2
        left1 = pos[0] - 1
        left2 = pos[0] - 2
        up1 = pos[1] + 1
        up2 = pos[1] + 2
        down1 = pos[1] - 1
        down2 = pos[1] - 2
        if(right1 >= 0 and right1 <= 7):
            if(up2 >= 0 and up2 <= 7):
                valid_moves.add((right1, up2))
            if(down2 >= 0 and down2 <= 7):
                valid_moves.add((right1, down2))
        if(right2 >= 0 and right2 <= 7):
            if(up1 >= 0 and up1 <= 7):
                valid_moves.add((right2, up1))
            if(down1 >= 0 and down1 <= 7):
                valid_moves.add((right2, down1))
        if(left1 >= 0 and left1 <= 7):
            if(up2 >= 0 and up2 <= 7):
                valid_moves.add((left1, up2))
            if(down2 >= 0 and down2 <= 7):
                valid_moves.add((left1, down2))
        if(left2 >= 0 and left2 <= 7):
            if(up1 >= 0 and up1 <= 7):
                valid_moves.add((left1, up1))
            if(down1 >= 0 and down1 <= 7):
                valid_moves.add((left2, down1))
        return valid_moves

    def new_move_positions(self, pos):
        valid = self.get_valid_moves(pos)
        filtered = (valid - self._considered_positions)
        self._considered_positions.update(filtered)
        return filtered

    def build_move_tree(self):
        queue = [self._root]
        while queue:
            children = self.new_move_positions(queue[0].value)
            for child in children:
                node_child = Node(child)
                queue.append(node_child)
                queue[0].add_child(node_child)
            queue.pop(0)
    
    def find_path(self, end_position):
        print(self._root.depth_search(end_position))
        # return self.trace_to_root(self._root.depth_search(end_position))

    def trace_to_root(self, end_node):
        node = end_node
        trace = [node.value]
        while node.parent:
            trace.append(node.parent)
            node = node.parent.value
        return trace.reverse()



# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((1, 2)))   # Expected outcome: {(1, 2), (2, 1)}
finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder.find_path((2, 1)))  # => [(0, 0), (2, 1)]
print(finder.find_path((3, 3)))  # => [(0, 0), (2, 1), (3, 3)]
print(finder.find_path((6, 2)))  # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
# => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
print(finder.find_path((7, 6)))
