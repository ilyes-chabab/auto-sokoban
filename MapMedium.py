import pygame
from Movement import Moove


class Game:
    def __init__(self)  : 
        self.movement = Moove()
        # matrice of the map 
        #obstacle : -1, empty spot : 0, box spot  : 1, Box : 2,Player : 3 , BoxIn : 4
        self.matriceMapMedium = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
                                [-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1],
                                [-1,0 ,2 ,0 ,0 ,0 ,2 ,0 ,-1],
                                [-1,0 ,0 ,1 ,-1,1 ,0 ,0 ,-1],
                                [-1,0 ,0 ,-1,-1,-1,0 ,0 ,-1],
                                [-1,0 ,0 ,1 ,-1, 4,0 ,0 ,-1],
                                [-1,0 ,2 ,0 ,3 ,0 ,0 ,0 ,-1],
                                [-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1],
                                [-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        self.Character_x=4
        self.Character_y = 6
        self.mooveRight = False
        self.running = True
        pygame.init() 
        self.screen=pygame.display.set_mode((1000,600))
        
        self.initOakBlock = pygame.image.load('image/block_07.png')
        self.OakBlock=pygame.transform.scale(self.initOakBlock , (65,65))
        self.initOakWall = pygame.image.load('image/block_03.png')
        self.OakWall=pygame.transform.scale(self.initOakWall , (65,65))
        self.initcharacterDown = pygame.image.load('image/player_01.png')
        self.characterDown=pygame.transform.scale(self.initcharacterDown , (60,60))
        self.initcharacterUp = pygame.image.load('image/player_04.png')
        self.characterUp=pygame.transform.scale(self.initcharacterUp , (60,60))
        self.initcharacterRight = pygame.image.load('image/player_18.png')
        self.characterRight=pygame.transform.scale(self.initcharacterRight , (60,60))
        self.initcharacterLeft = pygame.image.load('image/player_22.png')
        self.characterLeft=pygame.transform.scale(self.initcharacterLeft , (60,60))
        self.initBox = pygame.image.load('image/crate_05.png')
        self.Box=pygame.transform.scale(self.initBox , (60,60))
        self.initSpotBox = pygame.image.load('image/environment_10.png')
        self.SpotBox=pygame.transform.scale(self.initSpotBox , (60,60))
        self.initBoxIn = pygame.image.load('image/crate_10.png')
        self.BoxIn=pygame.transform.scale(self.initBoxIn , (60,60))
    
    def displayMap(self):
    
        y=-30
        for i in range(9):
            y+=60
            x=200
            for j in range(9):
                x+=60
                if self.matriceMapMedium[i][j] == -1: 
                    self.screen.blit(self.OakWall , (x,y))

                elif self.matriceMapMedium[i][j] == 1: 
                    self.screen.blit(self.OakBlock , (x,y))
                    self.screen.blit(self.SpotBox , (x,y))

                elif self.matriceMapMedium[i][j] == 2: 
                    self.screen.blit(self.Box , (x,y))

                elif self.matriceMapMedium[i][j] == 3:
                    self.screen.blit(self.OakBlock , (x,y))
                    self.screen.blit(self.characterUp,(x,y))
                
                elif self.matriceMapMedium[i][j] == 4: 
                    self.screen.blit(self.BoxIn , (x,y))

                else:
                    self.screen.blit(self.OakBlock , (x,y))

    #main func
    def main(self):
        while self.running:
            self.screen.fill((135,135,135))
            self.displayMap()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running =False
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.mooveRight= True
                        
                        

                    # elif event.key == pygame.K_DOWN:
                    #     self.movement.mooveDown()
                    # elif event.key == pygame.K_LEFT:
                    #     self.Movement.mooveLeft()
                    # elif event.key == pygame.K_UP:
                    #     self.Movement.mooveUp()

                    if self.mooveRight:
                        moove=True
                        self.movement.test( self.matriceMapMedium , self.Character_x , self.Character_y)
                        print("hello")
                        
                        if moove:
                            moove=False



            pygame.display.flip()

main=Game()
main.main()