from gameobj import characteristics

total_rows = 20
total_cols = 31

class archer(characteristics): # INHERITANCE
   

    def __init__(self, vil,points, no):
        self.damage=12 # half of barbarian
        self.health=25
        self.Maxhealth = 25 # half of barbarian
        self.x = points.x + 1
        self.y = points.y
        self.count = no 
        self.speed=2
        self.Range= 5 # more than cannon
        self.attacking = 0
        self.create(vil)
        
    
    def create(self, vil):
        r = self.count
        vil[self.x][self.y] = 'arc' + str(r)

    def check_range(self,vil, b,c,h,TH,towers):
        if self.health <= 0:
            return 0
        minrow = self.x - self.Range
        maxrow = self.x + self.Range 
        mincol = self.y - self.Range 
        maxcol = self.y + self.Range

        if minrow < 0: minrow = 0
        if mincol < 0: mincol = 0
        if maxrow >= total_rows: maxrow = total_rows - 1
        if maxcol >= total_cols: maxcol = total_cols - 1

        
        i = minrow
        while i <= maxrow:
            j = mincol
            while j <= maxcol:
                distance = abs(self.x - i) + abs(self.y - j)
                if vil[i][j][0] == 'b' and vil[i][j][1] != 'a' and distance <= self.Range:
                    b[int(vil[i][j][1])-1].health -= self.damage
                    if  b[int(vil[i][j][1])-1].health <= 0:
                        b[int(vil[i][j][1])-1].health = 0
                        vil[b[int(vil[i][j][1])-1].x][b[int(vil[i][j][1])-1].y] = ' '
                    self.attacking = 1
                    return 1
                if vil[i][j][0] == 'c' and distance <= self.Range:
                    c[int(vil[i][j][1])-1].health -= self.damage
                    if  c[int(vil[i][j][1])-1].health <= 0:
                        c[int(vil[i][j][1])-1].health = 0
                        vil[c[int(vil[i][j][1])-1].x][c[int(vil[i][j][1])-1].y] = ' '
                    self.attacking = 1
                    return 1
                if vil[i][j][0] == 'z' and distance <= self.Range:
                    towers[int(vil[i][j][1])-1].health -= self.damage
                    if  towers[int(vil[i][j][1])-1].health <= 0:
                        towers[int(vil[i][j][1])-1].health = 0
                        vil[towers[int(vil[i][j][1])-1].x][towers[int(vil[i][j][1])-1].y] = ' '
                    self.attacking = 1
                    return 1
                if vil[i][j][0] == 'h' and distance <= self.Range:
                    h[int(vil[i][j][1])-1].health -= self.damage
                    if  h[int(vil[i][j][1])-1].health <= 0:
                        h[int(vil[i][j][1])-1].health = 0
                        vil[h[int(vil[i][j][1])-1].x][h[int(vil[i][j][1])-1].y] = ' '
                    self.attacking = 1
                    return 1
                if vil[i][j][0] == 't' and distance <= self.Range:
                    
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
                    self.attacking = 1
                    return 1
               
                j+=1
            i+=1          
        return 0

    
    
    def attack_wall(self, vil, w, fi, fj):
        
        if self.health <= 0:
            return -1                   
                
       
        if vil[fi][fj][0]>="0" and vil[fi][fj][0]<="9":
            index = int(vil[fi][fj])
            w[index].health -= self.damage
            if w[index].health <= 0:
                w[index].health = 0
                vil[w[index].x][w[index].y] = ' '
            return 1

    def walk_ahead(self, vil, b,c,h,t,w,towers): 
        min_dist = 1000000
        fi = 0
        fj = 0
        pi = self.x 
        pj = self.y 
        for i in range(0, total_rows):
            for j in range(0, total_cols):
                if ('b' in vil[i][j] and vil[i][j][1] != 'a') :
                    dist = abs(pj-j) + abs(pi-i)
                    if dist <= min_dist:
                        min_dist = dist
                        fj = j
                        fi = i 
                elif  vil[i][j][0]=='c':
                    dist = abs(pj-j) + abs(pi-i)
                    if dist <= min_dist:
                        min_dist = dist
                        fj = j
                        fi = i 
                elif  vil[i][j][0]=='z':
                    dist = abs(pj-j) + abs(pi-i)
                    if dist <= min_dist:
                        min_dist = dist
                        fj = j
                        fi = i 
                elif 'h' in vil[i][j] :
                    dist = abs(pj-j) + abs(pi-i)
                    if dist <= min_dist:
                        min_dist = dist
                        fj = j
                        fi = i 
                elif 't' in vil[i][j] :
                    dist = abs(pj-j) + abs(pi-i)
                    if dist <= min_dist:
                        min_dist = dist
                        fj = j
                        fi = i 
                else:
                    continue 
        
        
        ni = 1
        nj = 1
        if fi > pi : ni = 1
        elif fi < pi : ni = -1

        if fj > pj : nj = 1
        elif fj < pj : nj = -1

        if pi != fi and vil[pi+ni][pj] == ' ':
            
            pi = pi + ni 
            self.x = self.x + ni
            vil[self.x][self.y] = 'arc' + str(self.count)
            if 'arc' in vil[self.x-ni][self.y]:
                vil[self.x-ni][self.y] = ' '
            return 1
        elif pj != fj and vil[pi][pj+nj] == ' ':
            
            pj = pj + nj 
            self.y = self.y + nj
            vil[self.x][self.y] = 'arc' + str(self.count)
            if 'arc' in vil[self.x][self.y-nj]:
                vil[self.x][self.y-nj] = ' '
            return 1
        elif pj != fj and vil[pi][pj+nj][0] >= '0' and vil[pi][pj+nj][0] <= '9':
            
            
            self.attacking = self.attack_wall(vil,w, pi, pj+nj)
            return 1
        elif pi != fi and vil[pi+ni][pj][0] >= '0' and vil[pi+ni][pj][0] <= '9':
            
             
            self.attacking =self.attack_wall(vil, w, pi+ni, pj)
            return 1
        elif pi != fi and 's' in vil[pi+ni][pj]:
            self.x = pi+ni
            self.y = pj 
            vil[self.x - ni][self.y] = ' '
            
            return 1
        elif pi == fi and 's' in vil[pi][pj+nj] :
            self.y = self.y + nj 
            vil[self.x][self.y - nj] = ' '
            
            return 1


