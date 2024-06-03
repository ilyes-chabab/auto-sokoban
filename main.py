import numpy as np

class Matrix:

    def __init__(self):
        self.matrix = np.array([[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,1,0,0,0,0,0,0,0,0,0,1,0,-1],
        [-1,0,0,0,0,0,0,2,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,2,0,3,0,2,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,2,0,0,0,0,0,0,-1],
        [-1,0,1,0,0,0,0,0,0,0,0,0,1,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]])

    def show_matrix(self):
        print(self.matrix)

    def move_player(self, direction):
        if direction == "up":
            x = 5
            y = 7
            self.matrix[x][y], self.matrix[x-1][y] = self.matrix[x-1][y], self.matrix[x][y]
            x-=1
        if direction == "down":
            x = 5
            y = 7
            self.matrix[x][y], self.matrix[x+1][y] = self.matrix[x+1][y], self.matrix[x][y]
            x+=1
        if direction == "left":
            x = 5
            y = 7
            self.matrix[x][y], self.matrix[x][y-1] = self.matrix[x][y-1], self.matrix[x][y]
            y-+1
        if direction == "right":
            x = 5
            y = 7
            self.matrix[x][y], self.matrix[x][y+1] = self.matrix[x][y+1], self.matrix[x][y]
            y+=1
    
    def obstacle(self):
        obstacle = -1
    
    def search_player(self):
        self.matrix = self.matrix.all()
        for i in self.matrix:
            if i == 0:
                print(i)

matrix = Matrix()

matrix.search_player()

# matrix.move_player("right")
# matrix.move_player("up")
# matrix.show_matrix()