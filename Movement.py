import pygame

class Moove():
    def __init__(self):
        self.MovementSpot = 0
        self.isBoxColision = False
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

    def VerifMovement(self,movement):
        return 
                    
        
    def mooveRight(self,x,y,matrice):
        self.MovementSpot= matrice[y-1][x]
        return self.MovementSpot 
    
    def test(self, matrice,x,y):
        if matrice[y][x+1] ==0 or matrice[y][x+1] ==1:
            matrice[y][x]= 0
            matrice[y][x+1]= 3
            x+=1
        elif matrice[y][x+1] == 2:
            if matrice[y][x+2] ==-1:
                return False
            
            elif matrice[y][x+2] == 1:
                matrice[y][x]= 0
                matrice[y][x+1]= 3
                matrice[y][x+2] = 4
                x+=1
                print("bravo , la box a été poussé au bon endroit")                
            elif matrice[y][x+2] == 0 or matrice[y][x+2] ==1:
                matrice[y][x]= 0
                matrice[y][x+1]= 3
                matrice[y][x+2] = 2
                x+=1
            
    



    # def mooveLeft(self):
    #     self.MovementSpot= self.matriceMapMedium[self.Character_y][self.Character_x-1]
    #     return self.MovementSpot

    # def mooveUp(self):
    #     self.MovementSpot= self.matriceMapMedium[self.Character_y-1][self.Character_x]
    #     return self.MovementSpot

    # def mooveDown(self):  
    #     self.MovementSpot= self.matriceMapMedium[self.Character_y+1][self.Character_x+1]
    #     return self.MovementSpot

movement= Moove()
