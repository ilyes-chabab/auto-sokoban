import numpy as np

class Matrix:
    def __init__(self):
        self.matrix = np.array([
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
            [-1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,-1],
            [-1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,-1],
            [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
            [-1, 0, 0, 0, 0, 2, 0, 3, 0, 2, 0, 0, 0, 0,-1],
            [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
            [-1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,-1],
            [-1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,-1],
            [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        ])
    
    def show_matrix(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))
        print()

    def find_player(self):
        position = np.argwhere(self.matrix == 3)
        return position[0] if len(position) > 0 else None

    def move_player(self, direction):
        player_pos = self.find_player()
        if player_pos is None:
            print("Player not found!")
            return

        x, y = player_pos
        if direction == "up":
            new_x, new_y = x - 1, y
        elif direction == "down":
            new_x, new_y = x + 1, y
        elif direction == "left":
            new_x, new_y = x, y - 1
        elif direction == "right":
            new_x, new_y = x, y + 1
        else:
            print("Invalid direction!")
            return

        if self.matrix[new_x][new_y] == -1:
            print("Move blocked by a wall!")
            return

        if self.matrix[new_x][new_y] == 2:
            push_x, push_y = new_x + (new_x - x), new_y + (new_y - y)
            if self.matrix[push_x][push_y] in (0, 1):
                if self.matrix[push_x][push_y] == 1:
                    print("Box in place!")
                self.matrix[push_x][push_y] = 2
                self.matrix[new_x][new_y] = 3
                self.matrix[x][y] = 0
            else:
                print("Move blocked by another box or a wall!")
                return
        else:
            self.matrix[new_x][new_y] = 3
            self.matrix[x][y] = 0
        
        # Check if any box is in a hole after the move
        self.check_box_in_hole()

    def check_for_box(self):
        return np.argwhere(self.matrix == 2)
    
    def check_for_hole(self):
        return np.argwhere(self.matrix == 1)
    
    def check_box_in_hole(self):
        holes = self.check_for_hole()
        boxes = self.check_for_box()
        for hole in holes:
            if any(np.array_equal(hole, box) for box in boxes):
                print("Box in place at position:", hole.tolist())

matrix = Matrix()

# Example of moving the player and pushing boxes
matrix.move_player("right")
matrix.move_player("right")
matrix.move_player("right")
matrix.move_player("right")
matrix.move_player("up")
matrix.move_player("right")
matrix.move_player("down")
matrix.move_player("down")
matrix.move_player("down")

matrix.show_matrix()
