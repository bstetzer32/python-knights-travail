from tree import Node

class KnightPathFinder:
    def __init__(self, value):
        self._x = value[0]
        self._y = value[1]
        self._root = Node((value[0], value[1]))
        self._considered_positions = set(self._root)

    def get_valid_moves(self, pos):
        valid_moves = {}
        right1 = pos(0) + 1
        right2 = pos(0) + 2
        left1 = pos(0) - 1
        left2 = pos(0) - 2
        up1 = pos(1) + 1
        up2 = pos(1) + 2
        down1 = pos(1) - 1
        down2 = pos(1) - 2
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
        self._cosidered_positions.update(filtered)
        return filtered


finder = KnightPathFinder((0, 0))
print(finder.new_move_positions((0, 0)))   # Expected outcome: {(1, 2), (2, 1)}
