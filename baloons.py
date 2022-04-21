from gameobj import characteristics

rows = 20
cols = 31

class baloon(characteristics): # INHERITANCE
   

    def __init__(self, vil, point, no):
        self.damage=25 #change to 25 later
        self.health=50
        self.Maxhealth = 50
        self.x = point.x
        self.y = point.y
        self.count = no 
        self.speed = 2
        self.previous = vil[point.x][point.y]
        self.target_type = 0
        self.create(vil)
        
    
    def create(self, vil):
        r = self.count
        vil[self.x][self.y] = 'o' + str(r)
    
    def attack(self, vil, b,c,h,t,towers, fi, fj):
        
        if self.health <= 0:
            return -1                   
                
        if vil[fi][fj] == 't':
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
                self.target_type = 0  
            return 1
        elif 'h' in vil[fi][fj]:
            index = int(vil[fi][fj][1:]) - 1
            h[index].health -= self.damage
            if h[index].health <= 0:
                h[index].health = 0
                vil[h[index].x][h[index].y] = ' '
                self.target_type = 0 
            return 1

        elif  vil[fi][fj][0]=="c":
            index = int(vil[fi][fj][1:]) - 1
            c[index].health -= self.damage
            if c[index].health <= 0:
                c[index].health = 0
                vil[c[index].x][c[index].y] = ' '
                self.target_type = 0 
            return 1
        elif  vil[fi][fj][0]=="z":
            index = int(vil[fi][fj][1:]) - 1
            towers[index].health -= self.damage
            if towers[index].health <= 0:
                towers[index].health = 0
                vil[towers[index].x][towers[index].y] = ' '
                self.target_type = 0 
            return 1

        elif 'b' in vil[fi][fj] and vil[fi][fj][1] != 'a':
            index = int(vil[fi][fj][1:]) - 1
            b[index].health -= self.damage
            if b[index].health <= 0:
                b[index].health = 0
                vil[b[index].x][b[index].y] = ' '
                self.target_type = 0 
            return 1

       
       
    def walk_ahead(self, vil, b,c,h,t,w,towers): 
        min_dist = 1000000
        fi = 0
        fj = 0
        pi = self.x 
        pj = self.y 

        

        for i in range(0, rows):
            for j in range(0, cols):
                if vil[i][j][0] == 'z':
                    dist = abs(pj-j) + abs(pi-i)
                    if dist <= min_dist:
                        min_dist = dist 
                        fj = j
                        fi = i
                        self.target_type = 'Towers'
                    elif self.target_type != 'Cannons' and self.target_type != 'Towers':
                        min_dist = dist 
                        fj = j
                        fi = i
                        self.target_type = 'Towers'
                elif vil[i][j][0] == 'c':
                    dist = abs(pj-j) + abs(pi-i)
                    if dist <= min_dist:
                        min_dist = dist
                        fj = j
                        fi = i 
                        self.target_type = 'Cannons'
                    elif self.target_type != 'Cannons' and self.target_type != 'Towers':
                        min_dist = dist
                        fj = j
                        fi = i
                        self.target_type = 'Cannons'
                elif self.target_type != 'Cannons' and self.target_type != 'Towers':
                    if ('b' in vil[i][j] and vil[i][j][1] != 'a') :
                        dist = abs(pj-j) + abs(pi-i)
                        if dist <= min_dist:
                            min_dist = dist
                            fj = j
                            fi = i 
                            self.target_type = 'Buildings'
                   
                    elif 'h' in vil[i][j] :
                        dist = abs(pj-j) + abs(pi-i)
                        if dist <= min_dist:
                            min_dist = dist
                            fj = j
                            fi = i 
                            self.target_type = 'Huts'
                    elif 't' in vil[i][j] :
                        dist = abs(pj-j) + abs(pi-i)
                        if dist <= min_dist:
                            min_dist = dist
                            fj = j
                            fi = i
                            self.target_type = 'Townhall' 
                    else:
                        continue 
        
        
        temp = self.previous

        if pi == fi and (pj+1 == fj or pj-1 == fj):
            self.attack(vil, b,c,h,t,towers, fi, fj)
        elif pj == fj and (pi + 1 == fi or pi - 1 == fi):
            self.attack(vil, b,c,h,t,towers, fi, fj)        
        else:
            ni = 1
            nj = 1
            if fi > pi : ni = 1
            elif fi < pi : ni = -1

            if fj > pj : nj = 1
            elif fj < pj : nj = -1

            if pi != fi : #and (pj != fj or pi+ni != fi):
                
                pi = pi + ni
                self.x = self.x + ni
                self.previous = vil[self.x][self.y]
                vil[self.x][self.y] = 'o' + str(self.count)
                if 'o' in vil[self.x-ni][self.y]:
                    vil[self.x-ni][self.y] = temp
                return 1
            elif pj != fj :#and pj+nj != fj:
               
                pj = pj + nj 
                self.y = self.y + nj
                self.previous = vil[self.x][self.y]
                vil[self.x][self.y] = 'o' + str(self.count)
                if 'o' in vil[self.x][self.y-nj]:
                    vil[self.x][self.y-nj] = temp 
                return 1
           
