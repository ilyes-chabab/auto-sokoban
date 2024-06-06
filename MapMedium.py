import pygame
from Movement import Moove


class Game:
    def __init__(self)  : 
        self.movement = Moove()
        # matrice of the map 
        #obstacle : -1, empty spot : 0, box spot  : 1, Box : 2,Player : 3 , BoxIn : 4 , Player On box Spot : 5 
        #, player on box : 6 , 

        self.matriceMapMedium = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
                                [-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1],
                                [-1,0 ,2 ,0 ,0 ,0 ,2 ,0 ,-1],
                                [-1,0 ,0 ,1 ,-1,1 ,0 ,0 ,-1],
                                [-1,0 ,0 ,-1,-1,-1,0 ,0 ,-1],
                                [-1,0 ,0 ,1 ,-1, 1,0 ,0 ,-1],
                                [-1,0 ,2 ,0 ,3 ,0 ,2 ,0 ,-1],
                                [-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1],
                                [-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        self.Character_x=4
        self.Character_y = 6
        self.BoxInSpot =3
        self.last_matriceMapMedium = []
        self.last_Character_x=0
        self.last_Character_y = 0
        self.running = True
        self.win=False

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
        self.initSpotBox = pygame.image.load('image/environment_06.png')
        self.SpotBox=pygame.transform.scale(self.initSpotBox , (60,60))
        self.initBoxIn = pygame.image.load('image/crate_10.png')
        self.BoxIn=pygame.transform.scale(self.initBoxIn , (60,60))

        self.restart_button = pygame.Rect(900,0,100,40)
        self.Undo_button = pygame.Rect(940,40,100,40)
    
    def message(self,size,message,message_rectangle,color):
        font=pygame.font.SysFont("arial",size)
        message = font.render(message,False,color)
        self.screen.blit(message,message_rectangle) 
    
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
                    self.screen.blit(self.SpotBox , (x,y))

                elif self.matriceMapMedium[i][j] == 2: 
                    self.screen.blit(self.Box , (x,y))

                elif self.matriceMapMedium[i][j] == 3:
                    self.screen.blit(self.OakBlock , (x,y))
                    self.screen.blit(self.characterUp,(x,y))
                
                elif self.matriceMapMedium[i][j] == 4: 
                    self.screen.blit(self.BoxIn , (x,y))
                
                elif self.matriceMapMedium[i][j] == 5: 
                    self.screen.blit(self.OakBlock , (x,y))
                
                elif self.matriceMapMedium[i][j] == 6: 
                    self.screen.blit(self.BoxIn , (x,y))
                    self.screen.blit(self.characterUp,(x,y))
                

                else:
                    self.screen.blit(self.OakBlock , (x,y))
    
    def restart(self):
        self.matriceMapMedium = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
                                [-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1],
                                [-1,0 ,2 ,0 ,0 ,0 ,2 ,0 ,-1],
                                [-1,0 ,0 ,1 ,-1,1 ,0 ,0 ,-1],
                                [-1,0 ,0 ,-1,-1,-1,0 ,0 ,-1],
                                [-1,0 ,0 ,1 ,-1, 1,0 ,0 ,-1],
                                [-1,0 ,2 ,0 ,3 ,0 ,2 ,0 ,-1],
                                [-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,-1],
                                [-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        self.Character_x=4
        self.Character_y = 6
        self.BoxInSpot =0
        self.win=False
        self.displayMap()
    
    def save_last_move(self):
        self.last_matriceMapMedium = self.matriceMapMedium
        print(self.last_matriceMapMedium)
        self.last_Character_x=self.Character_x
        self.last_Character_y=self.Character_y  
    
    def undo(self):
        print("undo", self.last_matriceMapMedium)
        self.matriceMapMedium = self.last_matriceMapMedium
        self.Character_x= self.last_Character_x
        self.Character_y = self.last_Character_y


        


    #main fun*
    def main(self):
        while self.running:
            self.screen.fill((135,135,135))
            self.displayMap()
            pygame.draw.rect(self.screen , (137,40,20), self.restart_button)
            pygame.draw.rect(self.screen , (137,40,20), self.Undo_button)
            if self.win:
                self.message(56,"Bravo , vous avez gagné!",(300,200,0,0),(0,0,0))
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running =False
                if self.BoxInSpot == 4:
                    self.win = True
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart_button.collidepoint(event.pos):
                        self.restart()
                    elif self.Undo_button.collidepoint(event.pos):
                        print(self.last_matriceMapMedium)
                        print(self.matriceMapMedium)
                        print(self.Character_x , self.Character_y)
                        print(self.last_Character_x , self.last_Character_y)
                        self.undo()
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.save_last_move()
                        if self.movement.verifBoxInRight(self.matriceMapMedium, self.Character_x , self.Character_y):
                                self.BoxInSpot +=1
                        if self.movement.MooveRight(self.matriceMapMedium, self.Character_x , self.Character_y, self.BoxInSpot):
                            if self.Character_x <7:
                                self.Character_x += 1
                            
                            print(self.BoxInSpot)
                            
                    elif event.key == pygame.K_LEFT:
                        self.save_last_move()
                        if self.movement.verifBoxInLeft(self.matriceMapMedium, self.Character_x , self.Character_y):
                                self.BoxInSpot +=1
                        if self.movement.MooveLeft(self.matriceMapMedium, self.Character_x , self.Character_y , self.BoxInSpot) :
                            if self.Character_x >1:
                                self.Character_x -=1
                            
                                
                        print("hello",{self.Character_x})
                    
                    elif event.key == pygame.K_DOWN:
                        self.save_last_move()
                        if self.movement.verifBoxInDown(self.matriceMapMedium, self.Character_x , self.Character_y):
                                self.BoxInSpot +=1
                        if self.movement.MooveDown(self.matriceMapMedium, self.Character_x , self.Character_y , self.BoxInSpot) :
                            if self.Character_y <7:
                                self.Character_y +=1
                            
                        print("hello",{self.Character_y})
                    
                    elif event.key == pygame.K_UP:
                        self.save_last_move()
                        if self.movement.verifBoxInUp(self.matriceMapMedium, self.Character_x , self.Character_y):
                                self.BoxInSpot +=1
                        if self.movement.MooveUp(self.matriceMapMedium, self.Character_x , self.Character_y , self.BoxInSpot) :
                            if self.Character_y >1:
                                self.Character_y -=1
                            

            pygame.display.flip()

main=Game()
main.main()