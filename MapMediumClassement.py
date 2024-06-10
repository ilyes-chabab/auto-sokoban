import pygame
import time
from Movement import Moove
from collections import deque
from database import Database

class Game:
    def __init__(self):
        self.movement = Moove()
        # matrice of the map
        # obstacle : -1, empty spot : 0, box spot : 1, Box : 2, Player : 3 , BoxIn : 4 , Player On box Spot : 5 , player on box : 6
        self.matriceMapMedium = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                 [-1,  0,  0,  0, -1, -1,  0,  0,  0, -1],
                                 [-1,  0,  2,  0,  0, -1,  0,  2,  0, -1],
                                 [-1,  0,  0,  0,  0,  1,  0,  0,  0, -1],
                                 [-1, -1, -1,  0, -1, -1, -1,  0, -1, -1],
                                 [-1,  0,  0,  0,  0,  3,  0,  0,  0, -1],
                                 [-1,  0,  2,  0, -1,  0,  0,  2,  0, -1],
                                 [-1,  0,  0,  0,  1,  0,  0,  0,  0, -1],
                                 [-1,  0,  1,  0,  0,  0,  1,  0,  0, -1],
                                 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
        self.Character_x = 5
        self.Character_y = 5
        self.character_pos = self.Character_x, self.Character_y
        self.BoxInSpot = 0
        self.last_matriceMapMedium = []
        self.last_Character_x = 0
        self.last_Character_y = 0
        self.running = True
        self.win = False
        self.time_logged = False  # New variable to track if the time has been logged
        self.start_time = time.time()

        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        
        self.initOakBlock = pygame.image.load('image/block_07.png')
        self.OakBlock = pygame.transform.scale(self.initOakBlock, (65, 65))
        self.initOakWall = pygame.image.load('image/block_03.png')
        self.OakWall = pygame.transform.scale(self.initOakWall, (65, 65))
        self.initcharacterDown = pygame.image.load('image/player_01.png')
        self.characterDown = pygame.transform.scale(self.initcharacterDown, (60, 60))
        self.initcharacterUp = pygame.image.load('image/player_04.png')
        self.characterUp = pygame.transform.scale(self.initcharacterUp, (60, 60))
        self.initcharacterRight = pygame.image.load('image/player_18.png')
        self.characterRight = pygame.transform.scale(self.initcharacterRight, (60, 60))
        self.initcharacterLeft = pygame.image.load('image/player_22.png')
        self.characterLeft = pygame.transform.scale(self.initcharacterLeft, (60, 60))
        self.initBox = pygame.image.load('image/crate_05.png')
        self.Box = pygame.transform.scale(self.initBox, (60, 60))
        self.initSpotBox = pygame.image.load('image/environment_06.png')
        self.SpotBox = pygame.transform.scale(self.initSpotBox, (60, 60))
        self.initBoxIn = pygame.image.load('image/crate_10.png')
        self.BoxIn = pygame.transform.scale(self.initBoxIn, (60, 60))
        self.initButton_Retsart_Image = pygame.image.load('image/restart_button_image.jpg')
        self.Button_Retsart_Image = pygame.transform.scale(self.initButton_Retsart_Image, (100, 40))
        self.initButton_Undo_Image = pygame.image.load('image/button_undo.png')
        self.Button_Undo_Image = pygame.transform.scale(self.initButton_Undo_Image, (60, 40))

        self.restart_button = pygame.Rect(900, 0, 100, 40)
        self.Undo_button = pygame.Rect(940, 40, 100, 40)

        self.database = Database()  # Using the new database

    def message(self, size, message, message_rectangle, color):
        font = pygame.font.SysFont("arial", size)
        message = font.render(message, False, color)
        self.screen.blit(message, message_rectangle)

    def distance_manhattan(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def displayMap(self):
        y = -30
        for i in range(len(self.matriceMapMedium)):  # Changed to dynamically get row count
            y += 60
            x = 200
            for j in range(len(self.matriceMapMedium[i])):  # Changed to dynamically get column count
                x += 60
                if self.matriceMapMedium[i][j] == -1:
                    self.screen.blit(self.OakWall, (x, y))
                elif self.matriceMapMedium[i][j] == 1:
                    self.screen.blit(self.SpotBox, (x, y))
                elif self.matriceMapMedium[i][j] == 2:
                    self.screen.blit(self.Box, (x, y))
                elif self.matriceMapMedium[i][j] == 3:
                    self.screen.blit(self.OakBlock, (x, y))
                    self.screen.blit(self.characterUp, (x, y))
                elif self.matriceMapMedium[i][j] == 4:
                    self.screen.blit(self.BoxIn, (x, y))
                elif self.matriceMapMedium[i][j] == 5:
                    self.screen.blit(self.OakBlock, (x, y))
                elif self.matriceMapMedium[i][j] == 6:
                    self.screen.blit(self.BoxIn, (x, y))
                    self.screen.blit(self.characterUp, (x, y))
                else:
                    self.screen.blit(self.OakBlock, (x, y))

    def restart(self):
        self.matriceMapMedium = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                 [-1,  0,  0,  0, -1, -1,  0,  0,  0, -1],
                                 [-1,  0,  2,  0,  0, -1,  0,  2,  0, -1],
                                 [-1,  0,  0,  0,  0,  1,  0,  0,  0, -1],
                                 [-1, -1, -1,  0, -1, -1, -1,  0, -1, -1],
                                 [-1,  0,  0,  0,  0,  3,  0,  0,  0, -1],
                                 [-1,  0,  2,  0, -1,  0,  0,  2,  0, -1],
                                 [-1,  0,  0,  0,  1,  0,  0,  0,  0, -1],
                                 [-1,  0,  1,  0,  0,  0,  1,  0,  0, -1],
                                 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
        self.Character_x = 5
        self.Character_y = 5
        self.character_pos = self.Character_x, self.Character_y
        self.BoxInSpot = 0
        self.last_matriceMapMedium = []
        self.last_Character_x = 0
        self.last_Character_y = 0
        self.running = True
        self.win = False
        self.time_logged = False  # Reset this variable when restarting
        self.start_time = time.time()

    def main(self):
        while self.running:
            self.screen.fill((135, 135, 135))
            self.displayMap()
            pygame.draw.rect(self.screen, (137, 40, 20), self.restart_button)
            pygame.draw.rect(self.screen, (137, 40, 20), self.Undo_button)
            self.screen.blit(self.Button_Retsart_Image, (900, 0))
            self.screen.blit(self.Button_Undo_Image, (940, 40))
            if self.win:
                if not self.time_logged:  # Only log the time once
                    end_time = time.time()
                    elapsed_time = end_time - self.start_time
                    self.database.insert_time(elapsed_time)
                    self.time_logged = True  # Set the flag to indicate the time has been logged
                self.show_leaderboard()
                self.message(56, "Bravo, vous avez gagné!", (300, 200, 0, 0), (0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.database.close()
                if self.BoxInSpot == 4:
                    self.win = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart_button.collidepoint(event.pos):
                        self.restart()
                    elif self.Undo_button.collidepoint(event.pos):
                        self.undo()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.save_last_move()
                        if self.movement.verifBoxInRight(self.matriceMapMedium, self.Character_x, self.Character_y):
                            self.BoxInSpot += 1
                        if self.movement.MooveRight(self.matriceMapMedium, self.Character_x, self.Character_y, self.BoxInSpot):
                            if self.Character_x < 9:
                                self.Character_x += 1
                    elif event.key == pygame.K_LEFT:
                        self.save_last_move()
                        if self.movement.verifBoxInLeft(self.matriceMapMedium, self.Character_x, self.Character_y):
                            self.BoxInSpot += 1
                        if self.movement.MooveLeft(self.matriceMapMedium, self.Character_x, self.Character_y, self.BoxInSpot):
                            if self.Character_x > 1:
                                self.Character_x -= 1
                    elif event.key == pygame.K_DOWN:
                        self.save_last_move()
                        if self.movement.verifBoxInDown(self.matriceMapMedium, self.Character_x, self.Character_y):
                            self.BoxInSpot += 1
                        if self.movement.MooveDown(self.matriceMapMedium, self.Character_x, self.Character_y, self.BoxInSpot):
                            if self.Character_y < 9:
                                self.Character_y += 1
                    elif event.key == pygame.K_UP:
                        self.save_last_move()
                        if self.movement.verifBoxInUp(self.matriceMapMedium, self.Character_x, self.Character_y):
                            self.BoxInSpot += 1
                        if self.movement.MooveUp(self.matriceMapMedium, self.Character_x, self.Character_y, self.BoxInSpot):
                            if self.Character_y > 1:
                                self.Character_y -= 1
                    elif event.key == pygame.K_RETURN:
                        pass  # Removed the call to self.solve()
            
            pygame.display.flip()

    def save_last_move(self):
        self.last_matriceMapMedium.append([row.copy() for row in self.matriceMapMedium])
        self.last_Character_x = self.Character_x
        self.last_Character_y = self.Character_y

    def undo(self):
        if self.last_matriceMapMedium:
            self.matriceMapMedium = self.last_matriceMapMedium.pop()
            self.Character_x = self.last_Character_x
            self.Character_y = self.last_Character_y

    def show_leaderboard(self):
        top_times = self.database.get_top_times()
        y_offset = 300
        for idx, (time,) in enumerate(top_times):
            self.message(30, f"{idx + 1}. {time:.2f} seconds", (300, y_offset, 0, 0), (0, 0, 0))
            y_offset += 40

if __name__ == "__main__":
    game = Game()
    game.main()
