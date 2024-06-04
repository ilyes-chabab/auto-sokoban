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
    
    def MooveRight(self, matrice,x,y , boxIn):
        if matrice[y][x+1] ==0 :
            matrice[y][x]= 0
            matrice[y][x+1]= 3
            return True

        elif matrice[y][x+1] ==1:
            matrice[y][x]= 5
            matrice[y][x+1]= 3
            return True

        elif matrice[y][x+1] == 2:

            if matrice[y][x+2] ==-1:
                return False
            
            elif matrice[y][x+2] == 1:
                matrice[y][x]= 0
                matrice[y][x+1]= 3
                matrice[y][x+2] = 4
                print("bravo , la box a été poussé au bon endroit")   
                boxIn -=1        
                return True     

            elif matrice[y][x+2] == 0:
                matrice[y][x]= 0
                matrice[y][x+1]= 3
                matrice[y][x+2] = 2
                return True


        elif matrice[y][x+1] == -1:
            return False
    
        elif matrice[y][x+1] == 4:
                matrice[y][x]= 0
                matrice[y][x+1]= 6
                return True
        
        elif matrice[y][x+1] ==5:
            matrice[y][x]= 1
            matrice[y][x+1]= 3
            return True
        
        elif matrice[y][x+1] ==5:
            matrice[y][x]= 1
            matrice[y][x+1]= 3
            return True


    
    def MooveLeft(self, matrice,x,y , boxIn):
        if matrice[y][x-1] ==0 :
            matrice[y][x]= 0
            matrice[y][x-1]= 3
            return True

        elif matrice[y][x-1] ==1:
            matrice[y][x]= 5
            matrice[y][x-1]= 3
            return True

        elif matrice[y][x-1] == 2:

            if matrice[y][x-2] ==-1:
                return False
            
            elif matrice[y][x-2] == 1:
                matrice[y][x]= 0
                matrice[y][x-1]= 3
                matrice[y][x-2] = 4
                print("bravo , la box a été poussé au bon endroit")   
                boxIn -=1        
                return True     

            elif matrice[y][x-2] == 0:
                matrice[y][x]= 0
                matrice[y][x-1]= 3
                matrice[y][x-2] = 2
                return True


        elif matrice[y][x-1] == -1:
            return False
    
        elif matrice[y][x-1] == 4:
                matrice[y][x]= 4
                matrice[y][x-1]= 3
                return True
        
        elif matrice[y][x-1] ==5:
            matrice[y][x]= 1
            matrice[y][x-1]= 3
            return True
    
    def MooveUp(self, matrice,x,y , boxIn):
        if matrice[y-1][x] ==0 :
            matrice[y][x]= 0
            matrice[y-1][x]= 3
            return True

        elif matrice[y-1][x] ==1:
            matrice[y][x]= 5
            matrice[y-1][x]= 3
            return True

        elif matrice[y-1][x] == 2:

            if matrice[y-2][x] ==-1:
                return False
            
            elif matrice[y-2][x] == 1:
                matrice[y][x]= 0
                matrice[y-1][x]= 3
                matrice[y-2][x] = 4
                print("bravo , la box a été poussé au bon endroit")   
                boxIn -=1        
                return True     

            elif matrice[y-2][x] == 0:
                matrice[y][x]= 0
                matrice[y-1][x]= 3
                matrice[y-2][x] = 2
                return True


        elif matrice[y-1][x] == -1:
            return False
    
        elif matrice[y-1][x] == 4:
                matrice[y][x]= 4
                matrice[y-1][x]= 3
                return True
        
        elif matrice[y-1][x] ==5:
            matrice[y][x]= 1
            matrice[y-1][x]= 3
            return True
    
    
    def MooveDown(self, matrice,x,y , boxIn):
        if matrice[y+1][x] ==0 :
            matrice[y][x]= 0
            matrice[y+1][x]= 3
            return True

        elif matrice[y+1][x] ==1:
            matrice[y][x]= 5
            matrice[y+1][x]= 3
            return True

        elif matrice[y+1][x] == 2:

            if matrice[y+2][x] ==-1:
                return False
            
            elif matrice[y+2][x] == 1:
                matrice[y][x]= 0
                matrice[y+1][x]= 3
                matrice[y+2][x] = 4
                print("bravo , la box a été poussé au bon endroit")   
                boxIn -=1        
                return True     

            elif matrice[y+2][x] == 0:
                matrice[y][x]= 0
                matrice[y+1][x]= 3
                matrice[y+2][x] = 2
                return True


        elif matrice[y+1][x] == -1:
            return False
    
        elif matrice[y+1][x] == 4:
                matrice[y][x]= 4
                matrice[y+1][x]= 3
                return True
        
        elif matrice[y+1][x] ==5:
            matrice[y][x]= 1
            matrice[y+1][x]= 3
            return True
    
movement= Moove()
