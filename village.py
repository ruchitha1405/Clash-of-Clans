#import numpy as np
from sre_constants import RANGE
import colorama
from colorama import Fore, Back, Style
import os

colorama.init(autoreset=True)

vil=[]
walls=[] # list of wall objects
huts=[] # list of hut objects
buildings=[] # list of building objects
cannons=[] # list of cannon objects
King = 0 # creating king variable
Queen=0 # creating queen variable
barbarians = []
archers=[]
baloons=[]
towers=[] # wizard towers

total_rows = 20
total_cols = 31



class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class SP():
    def __init__(self,point,sym):
        self.x=point.x
        self.y=point.y
        
        self.sym=sym
        self.CreateSP()
    def CreateSP(self):
       
        vil[self.x][self.y]=self.sym
        
class cannon:
    def __init__(self,x,y,size,range,sym,damage_value,MaxHealth):
        self.x=x
        self.y=y
        self.size=size #should same as Size of cannon defined in vilage class
        self.Range=range
        self.sym=sym
        self.damage=damage_value
        self.health=MaxHealth
        self.Maxhealth=MaxHealth
        self.attacking = 0
        self.switch = 1
        self.create()
    def create(self):
        vil[self.x][self.y]=self.sym
    def check_range(self):
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
                if vil[i][j] == 'k' and distance <= self.Range:
                    King.health -= self.damage
                    if King.health <= 0:
                        King.health = 0
                        vil[King.x][King.y] = ' '
                    self.attacking = 1
                    return 1
                if vil[i][j] == 'q' and distance <= self.Range:
                    Queen.health -= self.damage
                    if Queen.health <= 0:
                        Queen.health = 0
                        vil[Queen.x][Queen.y] = ' '
                    self.attacking = 1
                    return 1
                if 'bar' in vil[i][j] and distance <= self.Range:
                    index = int(vil[i][j][3:])
                    barbarians[index].health -= self.damage
                    if barbarians[index].health <= 0:
                        barbarians[index].health = 0
                        vil[barbarians[index].x][barbarians[index].y] = ' '
                    self.attacking = 1
                    return 1
                if 'arc' in vil[i][j] and distance <= self.Range:
                    index = int(vil[i][j][3:])
                    archers[index].health -= self.damage
                    if archers[index].health <= 0:
                        archers[index].health = 0
                        vil[archers[index].x][archers[index].y] = ' '
                    self.attacking = 1
                    return 1 
                # cannon cant attack ballons
                j+=1
            i+=1          
        return 0

class hut:
    def __init__(self,x,y,sym,MaxHealth):
        self.x=x
        self.y=y
        self.sym=sym
        self.health=MaxHealth
        self.Maxhealth=MaxHealth
        self.create()
    def create(self):
        vil[self.x][self.y]=self.sym
        

class building:
    def __init__(self,x,y,size,sym,MaxHealth):
        self.x=x
        self.y=y
        self.size=size
        self.sym=sym
        self.health=MaxHealth
        self.Maxhealth=MaxHealth
        self.create()
    def create(self):
        vil[self.x][self.y]=self.sym

class TownHall:
    def __init__(self,x,y,MaxHealth):
        self.i=x
        self.j=y
        self.health=MaxHealth
        
        self.Maxhealth=MaxHealth
        self.create()
    def create(self):
        i=self.i
        while i<self.i+4:
            j=self.j
            while j<self.j+3:
                vil[i][j]='t'
                j+=1
            i+=1   

    


        
    

class wall:
    def __init__(self,x,y,sym,MaxHealth):
        self.x=x
        self.y=y
        self.sym=sym
        self.health=MaxHealth
        self.Maxhealth=MaxHealth
        self.Create()
    def Create(self):
        vil[self.x][self.y]=str(self.sym)

def MakeString(k):
    
    return str(k)
    
def CreateWalls(m,n,maxhealth):
    #wm=tm-2 # upto tm +4
    #wn=tn-2 # upto tn+5
    
    tm= (int)((m+1)/2) -1
    tn= (int)((n)/2 )-1
    #print(tm,tn)
    j=tm-3
    i=tn-3
    k=0
    
    while j<tm+4:
        sym=MakeString(k)
        
        a=wall(tn-3,j,sym,maxhealth)
        walls.append(a)
        #vil[i][j]='w'
        k+=1
        sym=MakeString(k)
        
        b=wall(tn+4,j,sym,maxhealth)
        walls.append(b)
        #vil[tn+4][j]='w'
        k+=1

        j+=1
   
    while i<tn+5:
        if vil[i][tm-3]==" " :
            sym=MakeString(k)
        #sym='w'+str(k)
            a=wall(i,tm-3,sym,maxhealth)
            walls.append(a)
        #vil[i][j]='w'
            k+=1
        if vil[i][tm+3]==" " :
            sym=MakeString(k)
        #sym='w'+str(k)
            b=wall(i,tm+3,sym,maxhealth)
            walls.append(b)
        #vil[tn+4][j]='w'
            k+=1
        
        i+=1

def HealthPercent(obj):
    p= obj.health/obj.Maxhealth
    return p*100
    
class tower:
    def __init__(self,x,y,size,range,sym,damage_value,MaxHealth):
        self.x=x
        self.y=y
        self.size=size #1
        self.Range=range # same as cannon
        self.sym=sym # z
        self.damage=damage_value # same as cannon # 10 seems good
        self.health=MaxHealth
        self.Maxhealth=MaxHealth
        self.attacking = 0
        self.create()
    def create(self):
        vil[self.x][self.y]=self.sym

    def attack_prev(self,previous):
        
        if previous == 'k' :
                    
            King.health -= self.damage
            if King.health <= 0:
                King.health = 0
                vil[King.x][King.y] = ' '
            
        if previous == 'q' :
            
            Queen.health -= self.damage
            if Queen.health <= 0:
                Queen.health = 0
                vil[Queen.x][Queen.y] = ' '
            
        if 'bar' in previous :
            
            index = int(previous[3:])
            barbarians[index].health -= self.damage
            if barbarians[index].health <= 0:
                barbarians[index].health = 0
                vil[barbarians[index].x][barbarians[index].y] = ' '
            
        if 'arc' in previous :
            
            index = int(previous[3:])
            archers[index].health -= self.damage
            if archers[index].health <= 0:
                archers[index].health = 0
                vil[archers[index].x][archers[index].y] = ' '

        if previous[0]=='o' :
            
            index = int(previous[1:])
            baloons[index].health -= self.damage
            if baloons[index].health <= 0:
                baloons[index].health = 0
                vil[baloons[index].x][baloons[index].y] = ' '
            
            self.attack_prev(baloons[index].previous)
            


    def attack_region(self,fi,fj):
        
        minrow = fi - 1
        maxrow = fi+ 1
        mincol = fj - 1
        maxcol = fj + 1

        if minrow < 0: minrow = 0
        if mincol < 0: mincol = 0
        if maxrow >= total_rows: maxrow = total_rows - 1
        if maxcol >= total_cols: maxcol = total_cols - 1
        
        i = minrow
        while i <= maxrow:
            j = mincol
            while j <= maxcol:
               
                if vil[i][j] == 'k' :
                    
                    King.health -= self.damage
                    if King.health <= 0:
                        King.health = 0
                        vil[King.x][King.y] = ' '
                    
                if vil[i][j] == 'q' :
                    
                    Queen.health -= self.damage
                    if Queen.health <= 0:
                        Queen.health = 0
                        vil[Queen.x][Queen.y] = ' '
                    
                if 'bar' in vil[i][j] :
                    
                    index = int(vil[i][j][3:])
                    barbarians[index].health -= self.damage
                    if barbarians[index].health <= 0:
                        barbarians[index].health = 0
                        vil[barbarians[index].x][barbarians[index].y] = ' '
                    
                if 'arc' in vil[i][j] :
                    
                    index = int(vil[i][j][3:])
                    archers[index].health -= self.damage
                    if archers[index].health <= 0:
                        archers[index].health = 0
                        vil[archers[index].x][archers[index].y] = ' '

                if vil[i][j][0]=='o' :
                    
                    index = int(vil[i][j][1:])
                    baloons[index].health -= self.damage
                    if baloons[index].health <= 0:
                        baloons[index].health = 0
                        vil[baloons[index].x][baloons[index].y] = ' '

                    self.attack_prev(baloons[index].previous)
                    
                j+=1
            i+=1          
        return 0
    def check_range(self):
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
                if vil[i][j] == 'k' and distance <= self.Range:
                    self.attack_region(i,j)
                    
                    self.attacking = 1
                    return 1
                if vil[i][j] == 'q' and distance <= self.Range:
                    self.attack_region(i,j)
                   
                    self.attacking = 1
                    return 1
                if 'bar' in vil[i][j] and distance <= self.Range:
                    self.attack_region(i,j)
                  
                    self.attacking = 1
                    return 1
                if 'arc' in vil[i][j] and distance <= self.Range:
                    self.attack_region(i,j)
                   
                    self.attacking = 1
                    return 1 
                if vil[i][j][0]=='o' and distance <= self.Range:
                    self.attack_region(i,j)
                   
                    self.attacking = 1
                    return 1 
                j+=1
            i+=1          
        return 0

    

    

class village:
    
        
    def __init__(self,n,m,point1,point2,point3,level):
        self.n=n 
        self.m=m 
        self.NumOfHuts=5 #atlest 5
        self.SizeOfHut=1
        self.SpawnPoint1=point1
        self.SpawnPoint2=point2
        self.SpawnPoint3=point3
       
        self.SizeOfCannon=1 
        
        self.SizeOfBuildings=1 
        self.Level=level
        
        
    
    def create(self):
        """
        s-spawning points,t-town hall,h-huts,w-wall, c-cannon,b-building
        k-king,B-barbarian,o-baloon 
        " "- empty   
        """
        
        
        
        i = 0
        while i < self.n:
            temp = []
            j = 0
            while j < self.m:
                temp.append(" ")
                j = j+1
            vil.append(temp)
            i = i + 1
            
        # created empty village
        
           
        
       
        self.MaxHealthTH=90
        #CreateTH(self.m,self.n)
        self.tm= (int)((self.m+1)/2) -1
        self.tn= (int)((self.n)/2 )-1
        self.TH=TownHall(self.tn-1,self.tm-1,self.MaxHealthTH)
        
       
        
        # created town hall
        
        self.MaxHealthHut=45
        self.h1= hut(11,5,'h1',self.MaxHealthHut)
       
        self.h2=hut(5,8,'h2',self.MaxHealthHut)
        self.h3=hut(6,2,'h3',self.MaxHealthHut)
        self.h4=hut(10,23,'h4',self.MaxHealthHut)
        self.h5=hut(17,15,'h5',self.MaxHealthHut)
        
        huts.append(self.h1)
        huts.append(self.h2)
        huts.append(self.h3)
        huts.append(self.h4)
        huts.append(self.h5)
        
        # created huts
       
        self.MaxHealthWall=51 #49 #50
        CreateWalls(self.m,self.n,self.MaxHealthWall)
        # created walls around town hall

        self.s1=SP(self.SpawnPoint1,"s1")
        self.s2=SP(self.SpawnPoint2,"s2")
        self.s3=SP(self.SpawnPoint3,"s3")
        
        # created spawning points
        self.RangeOfCannon=4 #5

        self.DamageOfCannon=10
        self.MaxHealthCannon=60
       
        self.c1=cannon(15,15,self.SizeOfCannon,self.RangeOfCannon,'c1',self.DamageOfCannon,self.MaxHealthCannon)
        cannons.append(self.c1)
        self.c2=cannon(11,2,self.SizeOfCannon,self.RangeOfCannon,'c2',self.DamageOfCannon,self.MaxHealthCannon)
        cannons.append(self.c2)

        if self.Level>=2:
            self.c3=cannon(8,23,self.SizeOfCannon,self.RangeOfCannon,'c3',self.DamageOfCannon,self.MaxHealthCannon)
            cannons.append(self.c3)
        if self.Level==3:
            self.c4=cannon(1,10,self.SizeOfCannon,self.RangeOfCannon,'c4',self.DamageOfCannon,self.MaxHealthCannon)
            cannons.append(self.c4)

        

        #created cannons
         
        self.MaxHealthBuilding=51 #50
        
        self.b1=building(3,15,self.SizeOfBuildings,'b1',self.MaxHealthBuilding)
        buildings.append(self.b1)
        self.b2=building(10,9,self.SizeOfBuildings,'b2',self.MaxHealthBuilding)
        buildings.append(self.b2)
        self.b3=building(3,13,self.SizeOfBuildings,'b3',self.MaxHealthBuilding)
        buildings.append(self.b3)
        #created  buildings

        self.MaxHealthTower=50
        self.z1=tower(15,12,self.SizeOfCannon,self.RangeOfCannon,"z1",self.DamageOfCannon,self.MaxHealthBuilding)
        towers.append(self.z1)
        self.z2=tower(3,18,self.SizeOfCannon,self.RangeOfCannon,"z2",self.DamageOfCannon,self.MaxHealthBuilding)
        towers.append(self.z2)

        if self.Level>=2:
            self.z3=tower(17,23,self.SizeOfCannon,self.RangeOfCannon,"z3",self.DamageOfCannon,self.MaxHealthBuilding)
            towers.append(self.z3)
        if self.Level==3:
            self.z4=tower(15,5,self.SizeOfCannon,self.RangeOfCannon,"z4",self.DamageOfCannon,self.MaxHealthBuilding)
            towers.append(self.z4)

        # created wizard towers
        
        #print(vil)
        del(i)
        del(j)
        
       
    def display(self,ch,replay):

        os.system('clear')
        if (replay==1):
            print ("             Replaying the recent game u had played               ")
            print("")
            print("")
        for i in vil:
            for j in i:
                if j==" ":
                    print(Back.GREEN + f"{j} ", end ="")
                
                elif j[0]=="h":
                    
                    a=int(j[1])
                    p=HealthPercent(huts[a-1])
                    if p>50:
                        print(Back.MAGENTA + f"{j}", end ="")
                    elif p >20 and p<=50 :
                        print(Back.YELLOW + f"{j}", end ="")
                    elif p >0 and p<=20 :
                        print(Back.RED+ f"{j}", end ="")
                    
                elif  j[0] == "c":
                    a=int(j[1])
                    p=HealthPercent(cannons[a-1])
                    if cannons[a-1].attacking == 1 :
                        print(Back.WHITE + Fore.RED + f"{j}", end="")
                        #cannons[a-1].switch = 0
                        cannons[a-1].attacking = 0                    
                    elif p>50:
                        print(Back.MAGENTA + f"{j}", end ="")
                        #cannons[a-1].switch = 1   

                    elif p >20 and p<=50 :
                        print(Back.YELLOW + f"{j}", end ="")
                        #cannons[a-1].switch = 1                    

                    elif p >0 and p<=20 :
                        print(Back.RED+ f"{j}", end ="")
                        #cannons[a-1].switch = 1                   
                        
                elif  j[0] == "z":
                    a=int(j[1])
                    p=HealthPercent(towers[a-1])
                    if towers[a-1].attacking == 1:
                        print(Back.WHITE + Fore.RED + f"{j}", end="")
                        towers[a-1].attacking = 0                    
                    elif p>50:
                        print(Back.MAGENTA + f"{j}", end ="")
                    elif p >20 and p<=50 :
                        print(Back.YELLOW + f"{j}", end ="")
                    elif p >0 and p<=20 :
                        print(Back.RED+ f"{j}", end ="")
                    
                    
                elif j[0]=="b" and j[1] != 'a' :                    
                    a=int(j[1])
                    p=HealthPercent(buildings[a-1])
                    if p>50:
                        print(Back.MAGENTA + f"{j}", end ="")
                    elif p >20 and p<=50 :
                        print(Back.YELLOW + f"{j}", end ="")
                    elif p >0 and p<=20 :
                        print(Back.RED+ f"{j}", end ="")
                    
                   
                elif j[0]=="s":
                    #print(Back.MAGENTA + f"{j}", end ="")
                    print(Back.BLACK + f"{j}", end ="")
                    
                elif j[0]=="t":
                    p=HealthPercent(self.TH)
                    if p>50:
                        print(Back.MAGENTA + f"{j} ", end ="")
                    elif p >20 and p<=50 :
                        print(Back.YELLOW + f"{j} ", end ="")
                    elif p >0 and p<=20 :
                        print(Back.RED+ f"{j} ", end ="")
                    
                    
                elif j[0]=="k":
                    if King.facing == 'R':
                        print(Back.CYAN  + 'R ', end="")
                    elif King.facing == 'L':
                        print(Back.CYAN  + 'L ', end="")
                    elif King.facing == 'D':
                        print(Back.CYAN + 'D ', end="")
                    elif King.facing == 'U':
                        print(Back.CYAN+ 'U ', end="")
                
                elif j[0]=="q":
                    if Queen.facing == 'R':
                        print(Back.CYAN  + 'R ', end="")
                    elif Queen.facing == 'L':
                        print(Back.CYAN  + 'L ', end="")
                    elif Queen.facing == 'D':
                        print(Back.CYAN + 'D ', end="")
                    elif Queen.facing == 'U':
                        print(Back.CYAN+ 'U ', end="")
                
                elif 'bar' in j:
                    a = int(j[3:])
                    p = HealthPercent(barbarians[a])
                    if p >= 50:
                        print(Back.BLUE + 'B ', end="")
                    else:
                        print(Back.LIGHTBLUE_EX + 'B ', end="")
                
                elif j[0]=='o':
                    a = int(j[1])
                    p = HealthPercent(baloons[a])
                    if p>50:
                        print(Back.WHITE + Fore.BLACK + f"O ", end ="")
                    elif p >20 and p<=50 :
                        print(Back.YELLOW + Fore.BLACK +f"O ", end ="")
                    elif p >0 and p<=20 :
                        print(Back.RED+ Fore.BLACK +f"O ", end ="")
                
                elif 'arc' in j:
                    a = int(j[3:])
                    p = HealthPercent(archers[a])
                   

                    if archers[a].attacking == 1:
                        print(Back.WHITE + Fore.RED + f"A ", end="")
                        archers[a].attacking = 0                    
                    if p>50:
                        print(Back.LIGHTMAGENTA_EX + f"A ", end ="")
                    elif p >20 and p<=50 :
                        print(Back.YELLOW + f"A ", end ="")
                    elif p >0 and p<=20 :
                        print(Back.RED+ f"A ", end ="")
                

                elif int((int(j))/10) == 0:
                    a=int(j)
                    p=HealthPercent(walls[a])
                    if p>50:
                        print(Back.MAGENTA + f"w ", end ="")
                    elif p >20 and p<=50 :
                        print(Back.YELLOW + f"w ", end ="")
                    elif p >0 and p<=20 :
                        print(Back.RED+ f"w ", end ="")
                    
                    
                else:
                    a=int(j)
                    p=HealthPercent(walls[a])
                    if p>50:
                        print(Back.MAGENTA + f"w ", end ="")
                    elif p >20 and p<=50 :
                        print(Back.YELLOW + f"w ", end ="")
                    elif p >0 and p<=20 :
                        print(Back.RED+ f"w ", end ="")
                    
                    
            print("")

        print("")
        print("")
        print(f"************************** LEVEL {self.Level} ****************************")
        if(ch=="k"):
            print(Fore.RED + "King's health : {}/{}".format(King.health, King.Maxhealth), end=" ")
            p = int(HealthPercent(King))
            p = (p-1)/10 + 1
            temp = 1
            while temp <= p:
                print(Fore.RED + '+',end='')
                temp+=1
            print("")
        if(ch=="a"):
            print(Fore.RED + "Queen's health : {}/{}".format(Queen.health, Queen.Maxhealth), end=" ")
            p = int(HealthPercent(Queen))
            p = (p-1)/10 + 1
            temp = 1
            while temp <= p:
                print(Fore.RED + '+',end='')
                temp+=1
            print("")
        







