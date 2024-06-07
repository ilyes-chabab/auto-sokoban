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
            print("Joueur introuvable !")
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
            print("Direction invalide")
            return

        if self.matrix[new_x][new_y] == -1:
            print("MUR !")
            return

        if self.matrix[new_x][new_y] == 2:
            push_x, push_y = new_x + (new_x - x), new_y + (new_y - y)
            if self.matrix[push_x][push_y] in (0, 1):
                if self.matrix[push_x][push_y] == 1:
                    print("Caisse en place")
                self.matrix[push_x][push_y] = 2
                self.matrix[new_x][new_y] = 3
                self.matrix[x][y] = 0
            else:
                print("Caisse bloqué par un mur ou une autre caisse")
                return
        else:
            self.matrix[new_x][new_y] = 3
            self.matrix[x][y] = 0
        
        self.check_box_in_hole()

    def check_for_box(self):
        position = np.argwhere(self.matrix == 2)
        for i in position:
            print (i)
    
    def check_for_hole(self):
        return np.argwhere(self.matrix == 1)
    

matrix = Matrix()


# matrix.move_player("right")
# matrix.move_player("right")
# matrix.move_player("right")
# matrix.move_player("right")
# matrix.move_player("up")
# matrix.move_player("right")
# matrix.move_player("down")
# matrix.move_player("down")
# matrix.move_player("down")
# matrix.move_player("left")
# matrix.move_player("left")
# matrix.move_player("left")
# matrix.move_player("left")
# matrix.move_player("left")
# matrix.move_player("left")
# matrix.move_player("left")
# matrix.move_player("left")
# matrix.move_player("left")
# matrix.move_player("up")
# matrix.move_player("left")
# matrix.move_player("down")

print(matrix.find_player())

print (matrix.check_for_box())

# matrix.show_matrix()
