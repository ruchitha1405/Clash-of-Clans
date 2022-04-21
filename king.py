from gameobj import characteristics

row = 20
col = 31

class king(characteristics): # INHERITANCE
    
    def __init__(self,damage, maxhealth):
        self.damage = damage
        self.health = maxhealth
        self.Maxhealth = maxhealth
        self.x = 0
        self.y = 0
        self.facing = 'R'
    
    def create(self, vil):
        vil[self.x][self.y] = 'k'
        


    def Attack(self, vil, buildings, cannons, huts, t, walls,towers):
        x = self.x
        y = self.y 
        if self.health <= 0:
            return -1

        if self.facing == 'R':            
            if y+1 >= col: return -1
            if vil[x][y+1] == ' ':
                return 0
            elif vil[x][y+1] == 't':
                t.health -= self.damage
                if t.health <= 0:
                    t.health = 0
                    i = t.i
                    while i<t.i+4:
                        j=t.j
                        while j<t.j+3:
                            vil[i][j]=' '
                            j+=1
                        i+=1  
                return 1
            elif 'h' in vil[x][y+1]:
                index = int(vil[x][y+1][1:]) - 1
                huts[index].health -= self.damage
                if huts[index].health <= 0:
                    huts[index].health = 0
                    vil[huts[index].x][huts[index].y] = ' '

            elif  vil[x][y+1][0]=='c':
                index = int(vil[x][y+1][1:]) - 1
                cannons[index].health -= self.damage
                if cannons[index].health <= 0:
                    cannons[index].health = 0
                    vil[cannons[index].x][cannons[index].y] = ' '
            
            elif 'z' in vil[x][y+1]:
                index = int(vil[x][y+1][1:]) - 1
                towers[index].health -= self.damage
                if towers[index].health <= 0:
                    towers[index].health = 0
                    vil[towers[index].x][towers[index].y] = ' '
                
            elif  vil[x][y+1][0]=='b' and vil[x][y+1][1]!='a':
                index = int(vil[x][y+1][1:]) - 1
                buildings[index].health -= self.damage
                if buildings[index].health <= 0:
                    buildings[index].health = 0
                    vil[buildings[index].x][buildings[index].y] = ' '
            
            elif 's' in vil[x][y+1]:
                return 0
            elif vil[x][y+1][0]>="0" and vil[x][y+1][0]<="9":
                index = int(vil[x][y+1])
                walls[index].health -= self.damage
                if walls[index].health <= 0:
                    walls[index].health = 0
                    vil[walls[index].x][walls[index].y] = ' '
                
        elif self.facing == 'L':            
            if y-1 < 0: return -1
            if vil[x][y-1] == ' ':
                return 0
            elif vil[x][y-1] == 't':
                t.health -= self.damage
                if t.health <= 0:
                    t.health = 0
                    i = t.i
                    while i<t.i+4:
                        j=t.j
                        while j<t.j+3:
                            vil[i][j]=' '
                            j+=1
                        i+=1  
                return 1
            elif 'h' in vil[x][y-1]:
                index = int(vil[x][y-1][1:]) - 1
                huts[index].health -= self.damage
                if huts[index].health <= 0:
                    huts[index].health = 0
                    vil[huts[index].x][huts[index].y] = ' '

            elif  vil[x][y-1][0]=="c":
                index = int(vil[x][y-1][1:]) - 1
                cannons[index].health -= self.damage
                if cannons[index].health <= 0:
                    cannons[index].health = 0
                    vil[cannons[index].x][cannons[index].y] = ' '
            elif  vil[x][y-1][0]=="z":
                index = int(vil[x][y-1][1:]) - 1
                towers[index].health -= self.damage
                if towers[index].health <= 0:
                    towers[index].health = 0
                    vil[towers[index].x][towers[index].y] = ' '

            elif  vil[x][y-1][0]=='b' and vil[x][y-1][1]!='a':
                index = int(vil[x][y-1][1:]) - 1
                buildings[index].health -= self.damage
                if buildings[index].health <= 0:
                    buildings[index].health = 0
                    vil[buildings[index].x][buildings[index].y] = ' '
            elif 's' in vil[x][y-1]:
                return 0
            elif vil[x][y-1][0]>="0" and vil[x][y-1][0]<="9":
                index = int(vil[x][y-1])
                walls[index].health -= self.damage
                if walls[index].health <= 0:
                    walls[index].health = 0
                    vil[walls[index].x][walls[index].y] = ' '
            
        elif self.facing == 'D':            
            if x+1 >= row: return -1
            if vil[x+1][y] == ' ':
                return 0
            elif vil[x+1][y] == 't':
                t.health -= self.damage
                if t.health <= 0:
                    t.health = 0
                    i = t.i
                    while i<t.i+4:
                        j=t.j
                        while j<t.j+3:
                            vil[i][j]=' '
                            j+=1
                        i+=1  
                return 1
            elif 'h' in vil[x+1][y]:
                index = int(vil[x+1][y][1:]) - 1
                huts[index].health -= self.damage
                if huts[index].health <= 0:
                    huts[index].health = 0
                    vil[huts[index].x][huts[index].y] = ' '

            elif  vil[x+1][y][0]=='c':
                index = int(vil[x+1][y][1:]) - 1
                cannons[index].health -= self.damage
                if cannons[index].health <= 0:
                    cannons[index].health = 0
                    vil[cannons[index].x][cannons[index].y] = ' '

            elif  vil[x+1][y][0]=='z':
                index = int(vil[x+1][y][1:]) - 1
                towers[index].health -= self.damage
                if towers[index].health <= 0:
                    towers[index].health = 0
                    vil[towers[index].x][towers[index].y] = ' '

            elif vil[x+1][y][0]=='b' and vil[x+1][y][1]!='a':
                index = int(vil[x+1][y][1:]) - 1
                buildings[index].health -= self.damage
                if buildings[index].health <= 0:
                    buildings[index].health = 0
                    vil[buildings[index].x][buildings[index].y] = ' '
            elif 's' in vil[x+1][y]:
                return 0       
            elif vil[x+1][y][0]>="0" and vil[x+1][y][0]<="9":
                index = int(vil[x+1][y])
                walls[index].health -= self.damage
                if walls[index].health <= 0:
                    walls[index].health = 0
                    vil[walls[index].x][walls[index].y] = ' '
        
        elif self.facing == 'U':            
            if x-1 < 0: return -1
            if vil[x-1][y] == ' ':
                return 0
            elif vil[x-1][y] == 't':
                t.health -= self.damage
                if t.health <= 0:
                    t.health = 0
                    i = t.i
                    while i<t.i+4:
                        j=t.j
                        while j<t.j+3:
                            vil[i][j]=' '
                            j+=1
                        i+=1  
                return 1
            elif 'h' in vil[x-1][y]:
                index = int(vil[x-1][y][1:]) - 1
                huts[index].health -= self.damage
                if huts[index].health <= 0:
                    huts[index].health = 0
                    vil[huts[index].x][huts[index].y] = ' '

            elif  vil[x-1][y][0]=='c':
                index = int(vil[x-1][y][1:]) - 1
                cannons[index].health -= self.damage
                if cannons[index].health <= 0:
                    cannons[index].health = 0
                    vil[cannons[index].x][cannons[index].y] = ' '
            elif  vil[x-1][y][0]=='z':
                index = int(vil[x-1][y][1:]) - 1
                towers[index].health -= self.damage
                if towers[index].health <= 0:
                    towers[index].health = 0
                    vil[towers[index].x][towers[index].y] = ' '

            elif  vil[x-1][y][0]=='b' and vil[x-1][y][1]!='a' :
                index = int(vil[x-1][y][1:]) - 1
                buildings[index].health -= self.damage
                if buildings[index].health <= 0:
                    buildings[index].health = 0
                    vil[buildings[index].x][buildings[index].y] = ' '
            elif 's' in vil[x-1][y]:
                return 0
            elif vil[x-1][y][0]>="0" and vil[x-1][y][0]<="9":
                index = int(vil[x-1][y])
                walls[index].health -= self.damage
                if walls[index].health <= 0:
                    walls[index].health = 0
                    vil[walls[index].x][walls[index].y] = ' '
                
             
             

    def MoveUp(self,vil):
        if self.health <= 0:
            return -1
        self.facing = 'U'
        if self.x-1 < 0:
            return -1
        if vil[self.x-1][self.y] == ' ':
            self.x = self.x - 1
            vil[self.x][self.y] = 'k'
            vil[self.x+1][self.y] = ' '
        
    def MoveLeft(self,vil):
        if self.health <= 0:
            return -1
        self.facing = 'L'
        if self.y-1 < 0 :
            return -1
        if vil[self.x][self.y-1] == ' ':
            self.y = self.y - 1
            vil[self.x][self.y] = 'k'
            vil[self.x][self.y+1] = ' '

    def MoveDown(self,vil):
        if self.health <= 0:
            return -1
        self.facing = 'D'
        if self.x+1 >= row:
            return -1
        if vil[self.x+1][self.y] == ' ':
            self.x = self.x + 1
            vil[self.x][self.y] = 'k'
            vil[self.x-1][self.y] = ' '
    def MoveRight (self, vil):
        if self.health <= 0:
            return -1
        if self.y+1 >= col:
            return -1
        self.facing = 'R'
        if vil[self.x][self.y+1] == ' ':
            self.y = self.y + 1
            vil[self.x][self.y] = 'k'
            vil[self.x][self.y-1] = ' '

    def axe_attack(self, vil, b, c, h, TH, w,towers):
        if self.health <= 0:
            return 0
        minrow = self.x - 5
        maxrow = self.x + 5
        mincol = self.y - 5 
        maxcol = self.y + 5

        if minrow < 0: minrow = 0
        if mincol < 0: mincol = 0
        if maxrow >= row: maxrow = row - 1
        if maxcol >= col: maxcol = col - 1

        TH_flag=0

        i = minrow
        while i <= maxrow:
            j = mincol
            while j <= maxcol:
                distance = abs(self.x - i) + abs(self.y - j)
                if vil[i][j][0] == 'b' and vil[i][j][1] != 'a' and distance <= 5:
                    b[int(vil[i][j][1])-1].health -= self.damage
                    if  b[int(vil[i][j][1])-1].health <= 0:
                        b[int(vil[i][j][1])-1].health = 0
                        vil[b[int(vil[i][j][1])-1].x][b[int(vil[i][j][1])-1].y] = ' '
                   
                if vil[i][j][0] == 'c' and distance <= 5:
                    c[int(vil[i][j][1])-1].health -= self.damage
                    if  c[int(vil[i][j][1])-1].health <= 0:
                        c[int(vil[i][j][1])-1].health = 0
                        vil[c[int(vil[i][j][1])-1].x][c[int(vil[i][j][1])-1].y] = ' '
                    
                if vil[i][j][0] == 'z' and distance <= 5:
                    towers[int(vil[i][j][1])-1].health -= self.damage
                    if  towers[int(vil[i][j][1])-1].health <= 0:
                        towers[int(vil[i][j][1])-1].health = 0
                        vil[towers[int(vil[i][j][1])-1].x][towers[int(vil[i][j][1])-1].y] = ' '
                    
                if vil[i][j][0] == 'h' and distance <= 5:
                    h[int(vil[i][j][1])-1].health -= self.damage
                    if  h[int(vil[i][j][1])-1].health <= 0:
                        h[int(vil[i][j][1])-1].health = 0
                        vil[h[int(vil[i][j][1])-1].x][h[int(vil[i][j][1])-1].y] = ' '
                    
                if vil[i][j][0] == 't' and distance <= 5:
                    if TH_flag==0:
                        TH.health -= self.damage
                        if  TH.health <= 0:
                            TH.health = 0
                            a = TH.i
                            while a<TH.i+4:
                                b=TH.j
                                while b<TH.j+3:
                                    vil[a][b]=' '
                                    b+=1
                                a+=1  

                        TH_flag=1
                    
                if vil[i][j][0]>="0" and vil[i][j][0]<="9"and distance <= 5:
                    index = int(vil[i][j])
                    w[index].health -= self.damage
                    if w[index].health <= 0:
                        w[index].health = 0
                        vil[w[index].x][w[index].y] = ' '
                    
               
                j+=1
            i+=1          
        return 0
