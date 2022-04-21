

from  colorama import Fore,Back,Style

import builtins

def CheckEnd(Village,lead,cannons,towers,buildings,huts,barbarians,archers,baloons,count_bar , max_bar,count_arc , max_arc,count_bal , max_bal,level):
    
    win = 1
    for i in cannons:
        if i.health > 0: 
            win = 0
            break
    for i in towers:
        if i.health > 0: 
            win = 0
            break 
    for i in buildings:
        if i.health > 0: 
            win = 0
            break
    for i in huts:
        if i.health > 0: 
            win = 0
            break
    if Village.TH.health > 0: 
        win = 0
    
    if win == 1:    
        print(Fore.RED + "You are victorious" + Fore.RESET)

        char=builtins.input("Do you want to replay the game u have just played (y/n) :")
        if(char=='y'):
            return 4
        
        if (level==3):
            c=builtins.input("Do you want to go to next level (y/n) :")
            if(c=="y"):
                print("oops! there are no further levels")
                exit()
            elif(c=='n'):
                return level
            else :
                print("INVALID INPUT")
                exit()
        else:
            c=builtins.input("Do you want to go to next level (y/n) :")
            if(c=="y"):
                return (level+1)
            elif(c=='n'):
                return level
            else :
                print("INVALID INPUT")
                exit()
    
       
    loose=1
     #Uncomment this if you want to see barbarians to die
    if count_bar < max_bar: 
        loose=0 
    for i in barbarians:
        if i.health > 0:
            loose=0 
            break
    if count_arc < max_arc: 
        loose=0 
    for i in archers:
        if i.health > 0:
            loose=0 
            break
    if count_bal < max_bal: 
        loose=0 
    for i in baloons:
        if i.health > 0:
            loose=0 
            break
    if lead.health > 0: 
        loose=0
    
    if loose==1 :
        print(Fore.RED + "You have been defeated" +Fore.RESET)
        char=builtins.input("Do you want to replay the game u have just played (y/n) :")
        if(char=='y'):
            return 4

        c=builtins.input("Do you want to try again (y/n) :")
        if(c=="y"):
            return level
        elif(c=="n"):
            print("hope to see you again")
            exit()
        else :
            print("INVALID INPUT")
            exit()
    
    return 0
        