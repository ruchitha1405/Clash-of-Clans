from gameobj import characteristics

rows = 20
cols = 31

class barbarian(characteristics): # INHERITANCE
    
    def __init__(self, vil, points, no):
        self.damage=25
        self.health=50
        self.Maxhealth = 50
        self.x = points.x + 1
        self.y = points.y
        self.count = no 
        self.speed =1
        self.create(vil)
        
    
    def create(self, vil):
        r = self.count
        vil[self.x][self.y] = 'bar' + str(r)
    
    def attack(self, vil, b,c,h,t,w,towers, fi, fj):
        
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
            return 1
        elif 'h' in vil[fi][fj]:
            index = int(vil[fi][fj][1:]) - 1
            h[index].health -= self.damage
            if h[index].health <= 0:
                h[index].health = 0
                vil[h[index].x][h[index].y] = ' '
            return 1

        elif  vil[fi][fj][0]=="c":
            index = int(vil[fi][fj][1:]) - 1
            c[index].health -= self.damage
            if c[index].health <= 0:
                c[index].health = 0
                vil[c[index].x][c[index].y] = ' '
            return 1
        elif  vil[fi][fj][0]=="z":
            index = int(vil[fi][fj][1:]) - 1
            towers[index].health -= self.damage
            if towers[index].health <= 0:
                towers[index].health = 0
                vil[towers[index].x][towers[index].y] = ' '
            return 1

        elif 'b' in vil[fi][fj] and vil[fi][fj][1] != 'a':
            index = int(vil[fi][fj][1:]) - 1
            b[index].health -= self.damage
            if b[index].health <= 0:
                b[index].health = 0
                vil[b[index].x][b[index].y] = ' '
            return 1

        # elif 's' in vil[fi][fj]:
        #     return 0
        elif vil[fi][fj][0]>="0" and vil[fi][fj][0]<="9":
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
        for i in range(0, rows):
            for j in range(0, cols):
                if ('b' in vil[i][j] and vil[i][j][1] != 'a') :
                    dist = abs(pj-j) + abs(pi-i)
                    if dist <= min_dist:
                        min_dist = dist
                        fj = j
                        fi = i 
                elif  vil[i][j][0]=='c' :
                    dist = abs(pj-j) + abs(pi-i)
                    if dist <= min_dist:
                        min_dist = dist
                        fj = j
                        fi = i 
                elif  vil[i][j][0]=='z' :
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
        
        # #while 1:
        # pi = self.x
        # pj = self.y
        
        if pi == fi and (pj+1 == fj or pj-1 == fj):
            self.attack(vil, b,c,h,t,w,towers, fi, fj)
        elif pj == fj and (pi + 1 == fi or pi - 1 == fi):
            self.attack(vil, b,c,h,t,w,towers, fi, fj)        
        else:
            ni = 1
            nj = 1
            if fi > pi : ni = 1
            elif fi < pi : ni = -1

            if fj > pj : nj = 1
            elif fj < pj : nj = -1

            if pi != fi and vil[pi+ni][pj] == ' ':
                # if vil[pi+ni][pj][0] == 's':
                #     pi = pi + ni
                #     self.x = self.x + ni 
                pi = pi + ni 
                self.x = self.x + ni
                vil[self.x][self.y] = 'bar' + str(self.count)
                if 'bar' in vil[self.x-ni][self.y]:
                    vil[self.x-ni][self.y] = ' '
                return 1
            elif pj != fj and vil[pi][pj+nj] == ' ':
                # if vil[pi][pj+nj][0] == 's':
                #     pj = pj + nj
                #     self.y = self.y + nj
                pj = pj + nj 
                self.y = self.y + nj
                vil[self.x][self.y] = 'bar' + str(self.count)
                if 'bar' in vil[self.x][self.y-nj]:
                    vil[self.x][self.y-nj] = ' '
                return 1
            elif pj != fj and vil[pi][pj+nj][0] >= '0' and vil[pi][pj+nj][0] <= '9':
                self.attack(vil, b,c,h,t,w,towers, pi, pj+nj)     
                return 1
            elif pi != fi and vil[pi+ni][pj][0] >= '0' and vil[pi+ni][pj][0] <= '9':
                self.attack(vil, b,c,h,t,w,towers, pi+ni, pj)     
                return 1
            elif pi != fi and 's' in vil[pi+ni][pj]:
                self.x = pi+ni
                self.y = pj 
                vil[self.x - ni][self.y] = ' '
                #self.walk_ahead(vil, b,c,h,t,w)
                return 1
            elif pi == fi and 's' in vil[pi][pj+nj] :
                self.y = self.y + nj 
                vil[self.x][self.y - nj] = ' '
                #self.walk_ahead(vil, b,c,h,t,w)
                return 1

    