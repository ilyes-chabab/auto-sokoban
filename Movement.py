import pygame

class Moove():

    def verifBoxInRight(self,matrice,x,y):
        if matrice[y][x+1] == 2:
            if matrice[y][x+2] == 1:
                return True 
            else : 
                return False
    
    def verifBoxInLeft(self,matrice,x,y):
        if matrice[y][x-1] == 2:
            if matrice[y][x-2] == 1:
                return True 
            else : 
                return False
            

    def verifBoxInUp(self,matrice,x,y):
        if matrice[y-1][x] == 2:
            if matrice[y-2][x] == 1:
                return True 
            else : 
                return False
            
    def verifBoxInDown (self,matrice,x,y):
        if matrice[y+1][x] == 2:
            if matrice[y+2][x] == 1:
                return True 
            else : 
                return False
    
    def MooveRight(self, matrice,x,y , boxIn):
        if matrice[y][x+1] ==0 :
            matrice[y][x]= 0
            matrice[y][x+1]= 3
            return True

        elif matrice[y][x+1] ==1:
            return False

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
                matrice[y][x]= 7
                matrice[y][x+1]= 6
                if not matrice[y+1][x+1] == -1 :
                    matrice[y+1][x+1]= 7
                if not matrice[y-1][x+1] == -1 :
                    matrice[y-1][x+1]= 7
                if not matrice[y][x+2] == -1 :
                    matrice[y][x+2]= 7
                return True
        
        elif matrice[y][x+1] ==5:
            matrice[y][x]= 1
            matrice[y][x+1]= 3
            return True
        
        elif matrice[y][x+1] ==7:
            matrice[y][x]= 4
            matrice[y][x+1]= 3
            for i in range(9):
                for j in range(9):
                    print(i,j)
                    if matrice[i][j] == 7:
                        matrice[i][j] = 0
        
            return True
    
    def MooveLeft(self, matrice,x,y , boxIn):
        if matrice[y][x-1] ==0 :
            matrice[y][x]= 0
            matrice[y][x-1]= 3
            return True

        elif matrice[y][x-1] ==1:
            return False

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
                matrice[y][x]= 7
                matrice[y][x-1]= 6
                if not matrice[y+1][x-1] == -1 :
                    matrice[y+1][x-1]= 7
                if not matrice[y-1][x-1] == -1 :
                    matrice[y-1][x-1]= 7
                if not matrice[y][x-2] == -1 :
                    matrice[y][x-2]= 7
                return True
        
        elif matrice[y][x-1] ==5:
            matrice[y][x]= 1
            matrice[y][x-1]= 3
            return True

        elif matrice[y][x-1] == 7:
                matrice[y][x]= 4
                matrice[y][x-1]= 3
                for i in range(9):
                    for j in range(9):
                        print("hello worldddd")
                        if matrice[i][j] == 7:
                            matrice[i][j] = 0
                            print(matrice[i][j], i , j )
                return True
    
    def MooveUp(self, matrice,x,y , boxIn):
        if matrice[y-1][x] ==0 :
            matrice[y][x]= 0
            matrice[y-1][x]= 3
            return True

        elif matrice[y-1][x] ==1:
            return False

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
                matrice[y][x]= 7
                matrice[y-1][x]= 6
                if not matrice[y-1][x-1] == -1 :
                    matrice[y-1][x-1]= 7
                if not matrice[y-1][x+1] == -1 :
                    matrice[y-1][x+1]= 7
                if not matrice[y-2][x] == -1 :
                    matrice[y-2][x]= 7
                return True
        
        elif matrice[y-1][x] ==5:
            matrice[y][x]= 1
            matrice[y-1][x]= 3
            return True
    
        elif matrice[y-1][x] ==7:
            matrice[y][x]= 4
            matrice[y-1][x]= 3
            for i in range(9):
                for j in range(9):
                    if matrice[i][j] == 7:
                        matrice[i][j] = 0
            return True
    
        
    
    
    def MooveDown(self, matrice,x,y , boxIn):
        if matrice[y+1][x] ==0 :
            matrice[y][x]= 0
            matrice[y+1][x]= 3
            return True

        elif matrice[y+1][x] ==1:
            return False

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
                matrice[y][x]= 7
                matrice[y+1][x]= 6
                if not matrice[y+1][x-1] == -1 :
                    matrice[y+1][x-1]= 7
                if not matrice[y+1][x+1] == -1 :
                    matrice[y+1][x+1]= 7
                if not matrice[y+2][x] == -1 :
                    matrice[y+2][x]= 7
                return True
        
        elif matrice[y+1][x] ==5:
            matrice[y][x]= 1
            matrice[y+1][x]= 3
            return True
    
        elif matrice[y+1][x] ==7:
            matrice[y][x]= 4
            matrice[y+1][x]= 3
            for i in range(9):
                for j in range(9):
                    if matrice[i][j] == 7:
                        matrice[i][j] = 0
            return True
    
movement= Moove()
