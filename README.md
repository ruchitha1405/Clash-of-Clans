<h1 align="center"> clash-of-clans </h1>

<h2><b>overview</b></h2>
a 2 D game in Python3 (terminal-based), heavily inspired by Clash of clans where the user will control the King/Archer queen, move it up, down, forward and backward, while destroying buildings and fighting defences on its way.<br>
The objective of the game is to destroy as many buildings as possible, and collect the maximum amount of loot while doing so. There will be an army of troops to help the king clean up.<br>
Concepts of object oriented programming are present within the code and The game simulate a basic version of Clash of clans.

## Compile and Run
If you don't have python or colorama installed, run the following lines on your terminal:
```
$ sudo apt-get install python3
$ python3 -m pip install coloroma
```
And then to run the game:
```
$ python3 game.py
```
## controls
leader of the clan can be either king or archer queen.<br>
The user can control only the lead .<br>
The following keys are used to control the lead:
- 'w' - move it up
- 's' - move it down
- 'd' - move it forward
- 'a' - move it backward
- ' ' - to make it attack
### Additional attacks
- 'x' - to make king use his leviathan axe
- 'e' - to make queen use her eagle's arrow
### using spells
The spells can effect only the lead and the barbarians.<br>
Both the spells can be used atmost once in a game.
- press 'r' key to activate ragespell 
- press 'h' key to activate heal spell
### spawning troops
- press key '1' or '2' or '3' to spawn a barbarain at sp1 or sp2 or sp3 respectively.
- press key '4' or '5' or '6' to spawn a balloon at sp1 or sp2 or sp3 respectively.
- press key '7' or '8' or '9' to spawn an archer at sp1 or sp2 or sp3 respectively.
### quitting the game
- press 'q' to exit the game



### village 


#### Huts:

<!-- - max health=45 -->

- h1,h2,h3,h4,h5 are huts
- s1,s2,s3 are spawning points (sp)
- b1,b2 are buildings
- Town hall is represented with 't'
- walls are represented with 'w'
- c1,c2 are cannons with range = 4 
- z1,z2 are wizard towers with range = 4 
- king/queen's initial co-ordiantes are ( 0,0 ) 
- everything moves with default speed=1 unless it is specified
- max num of barbarians is 5 and are represented with 'B'
- max num of archers is 3 and are represented with 'A'
- Range of archer=5 which is greater than cannon
- max num of balloons is 2 and are represented with 'O'
- There are atmost 3 levels in the game
>>Level 1: 2 cannons and 2 wizard towers
>>Level 2: 3 cannons and 3 wizard towers
>>Level 3: 4 cannons and 4 wizard towers

#### Spawning points:


- 's1'-sp1

- 's2'-sp2

- 's3'-sp3


#### Town hall:

- max health=90
- represented by 't'

#### walls:
- represented with wall number
- each wall object is stored in 
- max health=51

#### building:

 - max health=51

 - 'b1'-building1

 - 'b2'-building2



#### cannons:

- default damage value=10

- max health =60
- range = 4
- 'c1' -cannon1

- 'c2'-cannon2

#### wizard towers:
- default damage value=10

- max health =51
- range= 4
- 'z1' -tower1

- 'z2'-tower2



### king :

- default damage value = 35
- maxhealth = 5000
- speed =1
- initial co-ordiantes = ( 0,0 )
- press 'x' to use king's axe

### Archer Queen :
- default damage value = 30
- maxhealth = 4000
- speed =1
- initial co-ordiantes = ( 0,0 )
- press 'e' to use eagle's arrow


### barbarians :
- represented with 'B'
- default damage value = 25
- default health value = 50
- max num= 5
- press keys 1,2,3 to spawn the barbarians

### archers :
- represented with 'A'
- default damage value = 25/2 =12
- default health value = 50/2=25
- range = 5 > cannon
- max num=3
- press keys 7,8,9 to spawn the archers

### baloons :
- represented with 'O'
- default damage value = 25*2 =50
- default health value = 50
- max num =2
- press keys 4,5,6 to spawn the balloons

### spells:



### levels:
- There are atmost 3 levels in the game
    Level 1: 2 cannons and 2 wizard towers
    Level 2: 3 cannons and 3 wizard towers
    Level 3: 4 cannons and 4 wizard towers


health >50% is represented by magenta.

