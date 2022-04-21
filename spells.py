#only damage is increased here
#movement speed is increased in main.py


def activate_rage(lead, barbarians):
    lead.damage = 2*lead.damage
    
    for i in barbarians:
        i.damage = 2*i.damage
        
def activate_heal(lead, barbarians):
    lead.health = 3*lead.health
    lead.health = int(lead.health/2)
    if lead.health > lead.Maxhealth:
        lead.health = lead.Maxhealth

    for i in barbarians:
        i.health = 3*i.health
        i.health =  int(i.health/2)
        if i.health > i.Maxhealth:
            i.health = i.Maxhealth
            
def deactivate(lead, barbarians):
    lead.damage = int(lead.damage/2)
    for i in barbarians:
        i.damage = int(i.damage/2)