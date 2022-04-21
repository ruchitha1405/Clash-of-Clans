from gameobj import characteristics

total_rows = 20
total_cols = 31

class queen(characteristics): # INHERITANCE
   
    def __init__(self,damage, maxhealth):
        self.damage = damage
        self.health = maxhealth
        self.Maxhealth = maxhealth
        self.x = 0
        self.y = 0
        self.facing = 'R'
    
    def create(self, vil):
        vil[self.x][self.y] = 'q'

    def MoveUp(self,vil):
        if self.health <= 0:
            return -1
        self.facing = 'U'
        if self.x-1 < 0:
            return -1
        if vil[self.x-1][self.y] == ' ':
            self.x = self.x - 1
            vil[self.x][self.y] = 'q'
            vil[self.x+1][self.y] = ' '
        
    def MoveLeft(self,vil):
        if self.health <= 0:
            return -1
        self.facing = 'L'
        if self.y-1 < 0 :
            return -1
        if vil[self.x][self.y-1] == ' ':
            self.y = self.y - 1
            vil[self.x][self.y] = 'q'
            vil[self.x][self.y+1] = ' '

    def MoveDown(self,vil):
        if self.health <= 0:
            return -1
        self.facing = 'D'
        if self.x+1 >=total_rows:
            return -1
        if vil[self.x+1][self.y] == ' ':
            self.x = self.x + 1
            vil[self.x][self.y] = 'q'
            vil[self.x-1][self.y] = ' '
    def MoveRight (self, vil):
        if self.health <= 0:
            return -1
        self.facing = 'R'
        if self.y+1 >= total_cols:
            return -1
        
        if vil[self.x][self.y+1] == ' ':
            self.y = self.y + 1
            vil[self.x][self.y] = 'q'
            vil[self.x][self.y-1] = ' '
    
    def Attack(self, vil, buildings, cannons, huts, TH, walls,towers):
        x = self.x
        y = self.y 
        if self.health <= 0:
            return -1
        
        if self.facing == 'R':
            ki=x
            kj=y+8
            
        elif self.facing == 'L':
            ki=x
            kj=y-8
         
        elif self.facing == 'D':
            ki=x+8
            kj=y 
        elif self.facing == 'U':
            ki=x-8
            kj=y 
        
        minrow = ki - 2
        maxrow = ki + 2
        mincol = kj - 2
        maxcol = kj + 2
        if minrow < 0: minrow = 0
        if mincol < 0: mincol = 0
        if maxrow >= total_rows: maxrow = total_rows - 1
        if maxcol >= total_cols: maxcol = total_cols - 1

        TH_flag=0
        i = minrow
        while i <= maxrow:
            j = mincol
            while j <= maxcol:
                
                if vil[i][j][0] == 'b' and vil[i][j][1] != 'a':
                    index=int(vil[i][j][1])-1
                    buildings[index].health -= self.damage
                    if buildings[index].health <= 0:
                        buildings[index].health = 0
                        vil[buildings[index].x][buildings[index].y] = ' '
                    
                    
                elif vil[i][j][0] == 'c' :
                    index=int(vil[i][j][1])-1
                    cannons[index].health -= self.damage
                    if cannons[index].health <= 0:
                        cannons[index].health = 0
                        vil[cannons[index].x][cannons[index].y] = ' '
                elif vil[i][j][0] == 'z' :
                    index=int(vil[i][j][1])-1
                    towers[index].health -= self.damage
                    if towers[index].health <= 0:
                        towers[index].health = 0
                        vil[towers[index].x][towers[index].y] = ' '
                    
                    
                elif vil[i][j][0] == 'h' :
                    index=int(vil[i][j][1])-1
                    huts[index].health -= self.damage
                    if huts[index].health <= 0:
                        huts[index].health = 0
                        vil[huts[index].x][huts[index].y] = ' '
                    
                    
                elif vil[i][j]=="t":
                    if TH_flag==0:
                        TH.health -= self.damage
                        if TH.health <= 0:
                            TH.health = 0
                            m = TH.i
                            while m<TH.i+4:
                                n=TH.j
                                while n<TH.j+3:
                                    vil[m][n]=' '
                                    n+=1
                                m+=1 
                        TH_flag=1 
                elif vil[i][j][0]>="0" and vil[i][j][0]<="9":
                    index = int(vil[i][j])
                    
                    walls[index].health -= self.damage
                    if walls[index].health <= 0:
                        walls[index].health = 0
                        vil[walls[index].x][walls[index].y] = ' '
                        
                
                    
                j+=1
            i+=1  

    def eagle_arrow(self, vil, buildings, cannons, huts, TH, walls,towers):
        x = self.x
        y = self.y 
        if self.health <= 0:
            return -1
        
        if self.facing == 'R':
            ki=x
            kj=y+16
            
        elif self.facing == 'L':
            ki=x
            kj=y-16
         
        elif self.facing == 'D':
            ki=x+16
            kj=y 
        elif self.facing == 'U':
            ki=x-16
            kj=y 
        
        minrow = ki - 4
        maxrow = ki + 4
        mincol = kj - 4
        maxcol = kj + 4
        if minrow < 0: minrow = 0
        if mincol < 0: mincol = 0
        if maxrow >= total_rows: maxrow = total_rows - 1
        if maxcol >= total_cols: maxcol = total_cols - 1

        TH_flag=0
        i = minrow
        while i <= maxrow:
            j = mincol
            while j <= maxcol:
                
                if vil[i][j][0] == 'b' and vil[i][j][1] != 'a':
                    index=int(vil[i][j][1])-1
                    buildings[index].health -= self.damage
                    if buildings[index].health <= 0:
                        buildings[index].health = 0
                        vil[buildings[index].x][buildings[index].y] = ' '
                    
                    
                elif vil[i][j][0] == 'c' :
                    index=int(vil[i][j][1])-1
                    cannons[index].health -= self.damage
                    if cannons[index].health <= 0:
                        cannons[index].health = 0
                        vil[cannons[index].x][cannons[index].y] = ' '
                elif vil[i][j][0] == 'z' :
                    index=int(vil[i][j][1])-1
                    towers[index].health -= self.damage
                    if towers[index].health <= 0:
                        towers[index].health = 0
                        vil[towers[index].x][towers[index].y] = ' '
                    
                    
                elif vil[i][j][0] == 'h' :
                    index=int(vil[i][j][1])-1
                    huts[index].health -= self.damage
                    if huts[index].health <= 0:
                        huts[index].health = 0
                        vil[huts[index].x][huts[index].y] = ' '
                    
                    
                elif vil[i][j]=="t":
                    if TH_flag==0:
                        TH.health -= self.damage
                        if TH.health <= 0:
                            TH.health = 0
                            m = TH.i
                            while m<TH.i+4:
                                n=TH.j
                                while n<TH.j+3:
                                    vil[m][n]=' '
                                    n+=1
                                m+=1 
                        TH_flag=1 
                
                elif vil[i][j][0]>="0" and vil[i][j][0]<="9":
                    index = int(vil[i][j])
                    
                    walls[index].health -= self.damage
                    if walls[index].health <= 0:
                        walls[index].health = 0
                        vil[walls[index].x][walls[index].y] = ' '
                        
                
                    
                j+=1
            i+=1    
            
            
            
            
            
            
            