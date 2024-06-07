import pygame
import sys
from collections import deque

class Sokoban:
    def __init__(self, grid):
        self.grid = grid
        self.player_pos = self.find_player()
        self.targets = self.find_targets()

    def find_player(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == 'P':
                    return (x, y)
        return None

    def find_targets(self):
        targets = []
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == '.':
                    targets.append((x, y))
        return targets

    def is_solved(self, grid):
        for target in self.targets:
            if grid[target[1]][target[0]] != 'B':
                return False
        return True

    def is_valid_move(self, pos, grid):
        x, y = pos
        return 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] not in ['#', 'B']

    def move(self, old_pos, new_pos, grid):
        new_grid = [row[:] for row in grid]
        x_old, y_old = old_pos
        x_new, y_new = new_pos
        new_grid[y_old][x_old] = ' '
        new_grid[y_new][x_new] = 'P'
        return new_grid

def bfs(sokoban):
    queue = deque([(sokoban.player_pos, sokoban.grid, [])])
    visited = set()
    visited.add(sokoban.player_pos)

    while queue:
        pos, grid, path = queue.popleft()

        if sokoban.is_solved(grid):
            return path

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if sokoban.is_valid_move(new_pos, grid):
                new_grid = sokoban.move(pos, new_pos, grid)
                if new_pos not in visited:
                    visited.add(new_pos)
                    queue.append((new_pos, new_grid, path + [new_grid]))

    return None

def draw_grid(screen, grid):
    colors = {
        ' ': (255, 255, 255),
        '#': (0, 0, 0),
        'P': (0, 255, 0),
        'B': (255, 0, 0),
        '.': (0, 0, 255)
    }
    cell_size = 40
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            color = colors[cell]
            pygame.draw.rect(screen, color, pygame.Rect(x*cell_size, y*cell_size, cell_size, cell_size))

def main():
    pygame.init()
    grid = [
    "#####",
    "#P  #",
    "# B.#",
    "#  .#",
    "#####"
]
    sokoban = Sokoban([list(row) for row in grid])
    path = bfs(sokoban)

    if path is None:
        print("No solution found!")
        return

    screen = pygame.display.set_mode((len(grid[0]) * 40, len(grid) * 40))
    pygame.display.set_caption("Sokoban Solver")

    clock = pygame.time.Clock()
    for state in path:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        draw_grid(screen, state)
        pygame.display.flip()
        clock.tick(1)

    pygame.quit()

if __name__ == "__main__":
    main()
