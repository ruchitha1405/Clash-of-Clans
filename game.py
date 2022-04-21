import colorama
import os
import input
import king 
import barbarians
import village 
import spells 
import gameendings
import builtins
import archers
import queen
import baloons

import time

# getchar = input.Get()
# recent_Game=[]
def game (ch,level,replay):
    village.vil.clear()
    village.walls.clear()
    village.huts.clear()
    village.buildings.clear()
    village.cannons.clear()
    village.barbarians.clear()
    village.archers.clear()
    village.baloons.clear()
    village.towers.clear()

    if replay!=1:
        recent_Game.clear()

    Village=village.village(20,31,sp1,sp2,sp3,level)
    Village.create()
    if ch=="k": 
        village.King = king.king(35, 5000)
        village.King.create(village.vil)
    elif ch=="a":
        village.Queen= queen.queen(30,4000)
        village.Queen.create(village.vil)
    else :
        print("INVALID INPUT")
        exit()
    
    Village.display(ch,replay)

    
    

    max_bar = 5
    count_bar = 0
    max_arc =3
    count_arc=0
    max_bal=2
    count_bal=0


    rage_timer = 0
    rage_flag = 1

    health_flag = 1
    
    if replay!=1:
        while 1:
            
            key  = input.input_to(getchar)
            
            

            

            if ch=="k":
                l=gameendings.CheckEnd(Village,village.King,village.cannons,village.towers,village.buildings,village.huts,village.barbarians,village.archers,village.baloons,count_bar , max_bar,count_arc , max_arc,count_bal , max_bal,level)
                if (l>=1 and l<=3):
                    game(ch,l,0)
                elif l==0:
                    recent_Game.append(key)
                elif l==4:
                    game(ch,level,1)

            elif ch=='a':
                l=gameendings.CheckEnd(Village,village.Queen,village.cannons,village.towers,village.buildings,village.huts,village.barbarians,village.archers,village.baloons,count_bar , max_bar,count_arc , max_arc,count_bal , max_bal,level)      
                if (l>=1 and l<=3):
                    game(ch,l,0)
                elif l==0:
                    recent_Game.append(key)
                elif l==4:
                    game(ch,level,1)
            
            

            if rage_timer > 0:
                rage_timer = rage_timer - 1
                if(rage_timer == 0):
                    if ch=="k":
                        spells.deactivate(village.King, village.barbarians)
                    elif ch=='a':   
                        spells.deactivate(village.Queen, village.barbarians)      

            attacked = 0
            for i in village.cannons:
                x = i.check_range()
                if x == 1:
                    attacked = 1
            
            if attacked == 1:
                Village.display(ch,replay)

            attacked = 0
            for i in village.towers:
                x = i.check_range()
                if x == 1:
                    attacked = 1
            
            if attacked == 1:
                Village.display(ch,replay)

            attacked = 0
            for i in village.archers:
                x = i.check_range(village.vil,village.buildings,village.cannons,village.huts,Village.TH,village.towers)
                if x == 1:
                    attacked = 1
            
            if attacked == 1:
                Village.display(ch,replay)

            i = 0
            #if you want archers to walk uncomment this
            while i < count_arc :
                #print("it reached here " + str(i))
                if village.archers[i].health >0:
                    village.archers[i].walk_ahead(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                    village.archers[i].walk_ahead(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                    
                
                i = i + 1   
            Village.display(ch,replay)
            
            i = 0
            #if you want barbarians to walk uncomment this
            while i < count_bar :
                #print("it reached here " + str(i))
                if village.barbarians[i].health >0:
                    village.barbarians[i].walk_ahead(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                    # Village.display()
                    
                    if rage_timer > 0:
                        village.barbarians[i].walk_ahead(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                        # Village.display()
                
                i = i + 1   
            Village.display(ch,replay)     

            i = 0
            #if you want baloons to walk uncomment this
            while i < count_bal :
                #print("it reached here " + str(i))
                if village.baloons[i].health >0:
                    village.baloons[i].walk_ahead(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                    village.baloons[i].walk_ahead(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                
                i = i + 1   
            Village.display(ch,replay)     
            
            del(i)
            if key == 'q' or key == 'Q':
                #break
                exit()

            elif key == 'a' or key == 'A':
                if ch=="k":
                    village.King.MoveLeft(village.vil) 
                elif ch=="a" :     
                    village.Queen.MoveLeft(village.vil)  
                Village.display(ch,replay)
                if rage_timer > 0:
                    if ch=="k":
                        village.King.MoveLeft(village.vil) 
                    elif ch=="a" :     
                        village.Queen.MoveLeft(village.vil)        
                    Village.display(ch,replay)

            elif key == 's' or key == 'S':
                if ch=="k":
                    village.King.MoveDown(village.vil)
                elif ch=="a" : 
                    village.Queen.MoveDown(village.vil)  
                Village.display(ch,replay)
                if rage_timer > 0:
                    if ch=="k":
                        village.King.MoveDown(village.vil)
                    elif ch=="a" : 
                        village.Queen.MoveDown(village.vil)        
                    Village.display(ch,replay)

            elif key == 'd' or key == 'D':
                if ch=="k":
                    village.King.MoveRight(village.vil)
                elif ch=="a" :
                    village.Queen.MoveRight(village.vil) 
                Village.display(ch,replay)
                if rage_timer > 0:
                    if ch=="k":
                        village.King.MoveRight(village.vil)
                    elif ch=="a" :
                        village.Queen.MoveRight(village.vil)       
                    Village.display(ch,replay)

            elif key == 'w' or key == 'W':
                if ch=="k":
                    village.King.MoveUp(village.vil)
                elif ch=="a" :
                    village.Queen.MoveUp(village.vil)
                Village.display(ch,replay)
                if rage_timer > 0:
                    if ch=="k":
                        village.King.MoveUp(village.vil)
                    elif ch=="a" :
                        village.Queen.MoveUp(village.vil)       
                    Village.display(ch,replay)

            elif key == ' ':
                if ch=="k":
                    village.King.Attack(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls, village.towers)
                elif ch=="a" :
                    village.Queen.Attack(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                Village.display(ch,replay)
            
            elif key=='e' or key=='E':
                
                if ch=='a':
                    time.sleep(2) # should be 1 as per requirements
                    village.Queen.eagle_arrow(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
            
            elif key=='x' or key=='X':
                if ch=='k':
                    village.King.axe_attack(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls, village.towers)
            
            elif key == '1':
                if count_bar < max_bar:
                    village.barbarians.append(barbarians.barbarian(village.vil,sp1,count_bar))
                    count_bar+=1
                    Village.display(ch,replay)

            elif key == '2':
                if count_bar < max_bar:
                    village.barbarians.append(barbarians.barbarian(village.vil, sp2,count_bar))
                    count_bar+=1
                    Village.display(ch,replay)
            elif key == '3':
                if count_bar < max_bar:
                    village.barbarians.append(barbarians.barbarian(village.vil, sp3,count_bar))
                    count_bar+=1
                    Village.display(ch,replay)
            elif key == '4':
                if count_bal < max_bal:
                    village.baloons.append(baloons.baloon(village.vil, sp1,count_bal))
                    count_bal+=1
                    Village.display(ch,replay)
            elif key == '5':
                if count_bal < max_bal:
                    village.baloons.append(baloons.baloon(village.vil, sp2,count_bal))
                    count_bal+=1
                    Village.display(ch,replay)
            elif key == '6':
                if count_bal < max_bal:
                    village.baloons.append(baloons.baloon(village.vil, sp3,count_bal))
                    count_bal+=1
                    Village.display(ch,replay)

            elif key == '7':
                if count_arc < max_arc:
                    village.archers.append(archers.archer(village.vil, sp1,count_arc))
                    count_arc+=1
                    Village.display(ch,replay)
        
            elif key == '8':
                if count_arc < max_arc:
                    village.archers.append(archers.archer(village.vil, sp2,count_arc))
                    count_arc+=1
                    Village.display(ch,replay)
            elif key == '9':
                if count_arc < max_arc:
                    village.archers.append(archers.archer(village.vil, sp3,count_arc))
                    count_arc+=1
                    Village.display(ch,replay)
            

            elif key == 'r' or key == 'R':
                if rage_flag == 1:
                    if ch=="k":
                        spells.activate_rage(village.King, village.barbarians)
                    elif ch=="a" :
                        spells.activate_rage(village.Queen, village.barbarians)
                    rage_timer = 100
                    rage_flag = 0
                    Village.display(ch,replay)
                else:
                    continue

            elif key == 'h' or key == 'H':
                if health_flag == 1:
                    if ch=="k":
                        spells.activate_heal(village.King, village.barbarians)
                    elif ch=="a" :
                        spells.activate_heal(village.Queen, village.barbarians)
                    Village.display(ch,replay)
                    health_flag = 0
                else: 
                    continue

    if replay==1:
        for key in recent_Game:
            
            #key  = input.input_to(getchar)
            
            

            

            if ch=="k":
                l=gameendings.CheckEnd(Village,village.King,village.cannons,village.towers,village.buildings,village.huts,village.barbarians,village.archers,village.baloons,count_bar , max_bar,count_arc , max_arc,count_bal , max_bal,level)
                if (l>=1 and l<=3):
                    game(ch,l,0)
                elif l==0:
                    pass
                    #recent_Game.append(key)
                elif l==4:
                    game(ch,level,1)

            elif ch=='a':
                l=gameendings.CheckEnd(Village,village.Queen,village.cannons,village.towers,village.buildings,village.huts,village.barbarians,village.archers,village.baloons,count_bar , max_bar,count_arc , max_arc,count_bal , max_bal,level)      
                if (l>=1 and l<=3):
                    game(ch,l,0)
                elif l==0:
                    pass
                    #recent_Game.append(key)
                elif l==4:
                    game(ch,level,1)
            
            

            if rage_timer > 0:
                rage_timer = rage_timer - 1
                if(rage_timer == 0):
                    if ch=="k":
                        spells.deactivate(village.King, village.barbarians)
                    elif ch=='a':   
                        spells.deactivate(village.Queen, village.barbarians)      

            attacked = 0
            for i in village.cannons:
                x = i.check_range()
                if x == 1:
                    attacked = 1
            
            if attacked == 1:
                Village.display(ch,replay)

            attacked = 0
            for i in village.towers:
                x = i.check_range()
                if x == 1:
                    attacked = 1
            
            if attacked == 1:
                Village.display(ch,replay)

            attacked = 0
            for i in village.archers:
                x = i.check_range(village.vil,village.buildings,village.cannons,village.huts,Village.TH,village.towers)
                if x == 1:
                    attacked = 1
            
            if attacked == 1:
                Village.display(ch,replay)

            i = 0
            #if you want archers to walk uncomment this
            while i < count_arc :
                #print("it reached here " + str(i))
                if village.archers[i].health >0:
                    village.archers[i].walk_ahead(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                    village.archers[i].walk_ahead(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                    # Village.display()
                    
                    
                
                i = i + 1   
            Village.display(ch,replay)
            
            i = 0
            #if you want barbarians to walk uncomment this
            while i < count_bar :
                #print("it reached here " + str(i))
                if village.barbarians[i].health >0:
                    village.barbarians[i].walk_ahead(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                    # Village.display()
                    
                    if rage_timer > 0:
                        village.barbarians[i].walk_ahead(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                        # Village.display()
                
                i = i + 1   
            Village.display(ch,replay)     

            i = 0
            #if you want baloons to walk uncomment this
            while i < count_bal :
                #print("it reached here " + str(i))
                if village.baloons[i].health >0:
                    village.baloons[i].walk_ahead(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                    village.baloons[i].walk_ahead(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                
                i = i + 1   
            Village.display(ch,replay)     
            
            del(i)
            if key == 'q' or key == 'Q':
                #break
                exit()

            elif key == 'a' or key == 'A':
                if ch=="k":
                    village.King.MoveLeft(village.vil) 
                elif ch=="a" :     
                    village.Queen.MoveLeft(village.vil)  
                Village.display(ch,replay)
                if rage_timer > 0:
                    if ch=="k":
                        village.King.MoveLeft(village.vil) 
                    elif ch=="a" :     
                        village.Queen.MoveLeft(village.vil)        
                    Village.display(ch,replay)

            elif key == 's' or key == 'S':
                if ch=="k":
                    village.King.MoveDown(village.vil)
                elif ch=="a" : 
                    village.Queen.MoveDown(village.vil)  
                Village.display(ch,replay)
                if rage_timer > 0:
                    if ch=="k":
                        village.King.MoveDown(village.vil)
                    elif ch=="a" : 
                        village.Queen.MoveDown(village.vil)        
                    Village.display(ch,replay)

            elif key == 'd' or key == 'D':
                if ch=="k":
                    village.King.MoveRight(village.vil)
                elif ch=="a" :
                    village.Queen.MoveRight(village.vil) 
                Village.display(ch,replay)
                if rage_timer > 0:
                    if ch=="k":
                        village.King.MoveRight(village.vil)
                    elif ch=="a" :
                        village.Queen.MoveRight(village.vil)       
                    Village.display(ch,replay)

            elif key == 'w' or key == 'W':
                if ch=="k":
                    village.King.MoveUp(village.vil)
                elif ch=="a" :
                    village.Queen.MoveUp(village.vil)
                Village.display(ch,replay)
                if rage_timer > 0:
                    if ch=="k":
                        village.King.MoveUp(village.vil)
                    elif ch=="a" :
                        village.Queen.MoveUp(village.vil)       
                    Village.display(ch,replay)

            elif key == ' ':
                if ch=="k":
                    village.King.Attack(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls, village.towers)
                elif ch=="a" :
                    village.Queen.Attack(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)
                Village.display(ch,replay)

            elif key=='e' or key=='E':
                
                if ch=='a':
                    time.sleep(1)
                    village.Queen.eagle_arrow(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls,village.towers)

            elif key=='x' or key=='X':
                if ch=='k':
                    village.King.axe_attack(village.vil, village.buildings,village.cannons, village.huts, Village.TH, village.walls, village.towers)

            elif key == '1':
                if count_bar < max_bar:
                    village.barbarians.append(barbarians.barbarian(village.vil,sp1,count_bar))
                    count_bar+=1
                    Village.display(ch,replay)

            elif key == '2':
                if count_bar < max_bar:
                    village.barbarians.append(barbarians.barbarian(village.vil, sp2,count_bar))
                    count_bar+=1
                    Village.display(ch,replay)
            elif key == '3':
                if count_bar < max_bar:
                    village.barbarians.append(barbarians.barbarian(village.vil, sp3,count_bar))
                    count_bar+=1
                    Village.display(ch,replay)
            elif key == '4':
                if count_bal < max_bal:
                    village.baloons.append(baloons.baloon(village.vil, sp1,count_bal))
                    count_bal+=1
                    Village.display(ch,replay)
            elif key == '5':
                if count_bal < max_bal:
                    village.baloons.append(baloons.baloon(village.vil, sp2,count_bal))
                    count_bal+=1
                    Village.display(ch,replay)
            elif key == '6':
                if count_bal < max_bal:
                    village.baloons.append(baloons.baloon(village.vil, sp3,count_bal))
                    count_bal+=1
                    Village.display(ch,replay)

            elif key == '7':
                if count_arc < max_arc:
                    village.archers.append(archers.archer(village.vil, sp1,count_arc))
                    count_arc+=1
                    Village.display(ch,replay)
        
            elif key == '8':
                if count_arc < max_arc:
                    village.archers.append(archers.archer(village.vil, sp2,count_arc))
                    count_arc+=1
                    Village.display(ch,replay)
            elif key == '9':
                if count_arc < max_arc:
                    village.archers.append(archers.archer(village.vil, sp3,count_arc))
                    count_arc+=1
                    Village.display(ch,replay)
            

            elif key == 'r' or key == 'R':
                if rage_flag == 1:
                    if ch=="k":
                        spells.activate_rage(village.King, village.barbarians)
                    elif ch=="a" :
                        spells.activate_rage(village.Queen, village.barbarians)
                    rage_timer = 100
                    rage_flag = 0
                    Village.display(ch,replay)
                else:
                    continue

            elif key == 'h' or key == 'H':
                if health_flag == 1:
                    if ch=="k":
                        spells.activate_heal(village.King, village.barbarians)
                    elif ch=="a" :
                        spells.activate_heal(village.Queen, village.barbarians)
                    Village.display(ch,replay)
                    health_flag = 0
                else: 
                    continue

            time.sleep(0.1) # main thing for replay

if __name__ == '__main__':
    getchar = input.Get() # global variable
    
    colorama.init()
    os.system('clear')
    
    sp1=village.point(1,3)
    sp2=village.point(3,4)
    sp3=village.point(5,6)
    # created spawning points (in global scope)
    recent_Game=[] # global variable
    ch=builtins.input("enter 'k' if u want king or 'a' if u want archer queen : ")
    game(ch,1,0)

