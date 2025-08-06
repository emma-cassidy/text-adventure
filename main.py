#my baby rpg lol

import logging
import time
import random
import pygame
import ctypes
from rich.console import Console
from os import path
import sys
import datetime


console = Console()


logging.basicConfig(filename="FALSE-SOULS-CRASH.txt", encoding='utf-8', level=logging.DEBUG)

ctypes.windll.kernel32.SetConsoleTitleW("False Souls")

path_to_dat = path.abspath(path.join(path.dirname(__file__), 'bgmv3.mp3'))

def script():
    pygame.init()
    my_sound = pygame.mixer.Sound(path_to_dat)
    
    #loop sound
    my_sound.play(-1)

    playerhp = 0
    playerstr = 0
    playerlck = 0
    playeratk = 0
    char_name = ""
    char_class = ""
    weapondamage = 1
    finalbossturn = 1

    def characterselect():
      print('''
                                                                                                                                                        
         ████   █    ███                                                  ██████████                                                      
          ███   ██   ██  █████ ██    ██████    █████    █     █  █████    █   ██   █  █████                                               
           ██  ████  ██  ██    ██   ███     ███    ██  ██    ██   ██          ██    ██    ███                                             
           █████ █████   █████ ██   ██      ██     ██  ███  ███   ████        ██    ██     ██                                             
            ███   ███    ██    ██   ███     ██     ██ ██ ████ █   ██          ██    ██     ██                                             
            ██    ███    █████ █████ ███████  ██████  ██  ██  ██ █████        ██      ██████                                              
                                                                              ██                                                          

                                                                                                      
                                                        ███                                           
    █████████                                       ███████                                          
      ███         ██     ████     ████████████      ███    █  ████████   ███    ████████    ██████    
      ███         ███     ███    ███    ███          ███     ███     ███ ███     ██  ███    ██        
      ███████    █████    ███     ████  ██████        ████  ███       ██ ███     ██  ███    ████      
      ███   █   ██████    ███       ███ ███  █          ███████       ██ ███     ██  ███      ████    
      ███       ██   ██   ███   ██   ██████               ██████     ███  ██     ██  ███   █    ██    
      ███     ████   ████ ████████████  ██████      ██   ███   ███████     ███████  █████████████     
    █████                                          ██████                                            
                                                                                                                                  
                                                                                                                                  


============================================================================================================================================
select your starting character:
  cleric - 15hp, 2 strength, 2 luck 
  warrior - 12hp, 5 strength, 0 luck
  rogue - 10hp, 2 strength, 5 luck
        
  attack = (strength x weapon damage) + luck
============================================================================================================================================
    ''')
      while True:
        char_class = input("choose your class. enter cleric, warrior or rogue: ").lower().strip()
        if char_class in ["cleric", "warrior", "rogue", "altmer",]: #random test class at the end
            break
        else:
            print("please choose a valid class.")
      char_name = input("name your character: ").strip()
      if len(char_name) > 12:
          print("error; max length 12")
          time.sleep(3)
          print("restarting...")
          time.sleep(2)
          pygame.mixer.stop()
          script()


      if char_class == "cleric":
        playerhp = 15
        playerstr = 2
        playerlck = 2
      elif char_class == "warrior":
        playerhp = 12
        playerstr = 5
        playerlck = 0
      elif char_class == "rogue":
        playerhp = 10
        playerstr = 2
        playerlck = 5
      else:
        playerhp = 50
        playerstr = 15
        playerlck = 10
      
      return char_name, char_class, playerhp, playerstr, playerlck


    char_name, char_class, playerhp, playerstr, playerlck = characterselect()
    placeholder = "test"
    maxhp = playerhp

    def showinstructions():
      print(f'''
    welcome to False Souls, {char_class} {char_name}!
============================================================================================================================================
commands:
  go [direction]       (north, south, east, west)
  get [item]           (item name)
  use [item]           (item name)
  show map             (shows map)
  attack [enemy]       (initiates combat)
  show commands        (show commands)

  defeating enemies increases your maximum hp!
  defeating bosses increases your maximum strength!
============================================================================================================================================
    ''')

    def showstatus():
        #print the player's current status
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        #print description if there is one
        if "desc" in rooms[currentroom]:
            print((rooms[currentroom]['desc']))
        print('you are in the ' + currentroom)
        #show current stats
        print(f'you have {playerhp} hp of a maximum {maxhp}, {playerstr} strength, and {playerlck} luck.')
        print(f'your attack stat is {playeratk}.')
        #show the current inventory and equipment
        print('inventory : ' + str(inventory))
        print('equipment : ' + str(equipment))
        #show an item if there is one
        if "item" in rooms[currentroom]:
            print('you see a \"' + rooms[currentroom]['item'] + '\"')
        #show an enemy if there is one
        if "enemy" in rooms[currentroom]:
            console.print('[bold]there is a \"' + rooms[currentroom]['enemy'] + '\" enemy in here![/bold]')
            placeholder = rooms[currentroom]['enemy']
            print(enemies[placeholder]['enemyart'])
        if "boss" in rooms[currentroom]:
            if "boss" in rooms[currentroom] and action[0] == "attack" and len(action) < 2:
                print("what are you attacking?")
            else:
                console.print('[bold]the boss \"' + rooms[currentroom]['boss'] + '\" prepares to attack![/bold]')
                placeholder = rooms[currentroom]['boss']
                if bosses[placeholder]['enemyhp'] >= 45:
                    console.print((bosses[placeholder]['bossdesc']))
                    print(bosses[placeholder]['bossart'])
                    # del bosses[placeholder]['bossart']
                    # del bosses[placeholder]['bossdesc']
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def credits():
        time.sleep(2)
        print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
           Thank you for playing! 
        
          Made by spookyghost/Emma
              
            Inspired by Joe and
              our shared love 
              of FromSoftware

        With thanks to soulBit for his
         guidance, feedback and advice
              
          Thanks for Ashplaze for
         his excellent bug finding
               
       Thanks to pulchritudedude for his
           support and playtesting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')


    inventory = []
    equipment = ["bare hands"]

    rooms = {

                'cave cell' : {
                      'south' : 'cave tunnel',
                      'item'  : 'broken sword',
                      'desc'  : '''
============================================================================================================================================
you are in a dank, dark cave, with a broken chain at your feet. your neck is sore, as if you were restrained by it. the only way to go 
is through the cave tunnel you see to your south.
============================================================================================================================================''',
                    },

                'cave tunnel' : {
                      'north' : 'cave cell',
                      'south' : 'cave mouth - south',
                      'east'  : 'cave mouth - east',
                      'desc'  : '''
============================================================================================================================================
you are in a cave tunnel as fetid as the cell you just came from. there are two cave mouths. one to your east, and one to your south.
there are shuffling, moaning sounds coming from both directions.
============================================================================================================================================''',
                    },
                'cave mouth - south' : {
                      'north' : 'cave tunnel',
                      'east'  : 'cliff edge - east',
                      'enemy' : 'feral remnant',
                      'desc'  : '''
============================================================================================================================================
the cave mouth faces out onto a sheer cliff opening. you see dark, cloudy skies for a few miles with crashing - yet silent - waves below.
in the distance beyond the cloud and waves you see an endless abyss of darkness, as if you the land on which you stand has been plucked from
elsewhere. to your north is the cave tunnel.
============================================================================================================================================''',
                  },
                'cave mouth - east' : {
                      'west' : 'cave tunnel',
                      'north' : 'cliff ledge',
                      'south' : 'cliff edge - east',
                      'enemy' : 'feral remnant',
                      'desc'  : '''
============================================================================================================================================
the cave mouth faces out onto a sheer cliff opening. you see dark, cloudy skies for a few miles with crashing - yet silent - waves below.
in the distance beyond the cloud and waves you see an endless abyss of darkness, as if you the land on which you stand has been plucked from
elsewhere. to your west is the cave tunnel. to your south is the cliff edge, where you can hear a faint moaning. to your north, there seems
to be a ledge you could climb.
============================================================================================================================================''',
                  },
                'cliff edge - east' : {
                      'north' : 'cave mouth - east',
                      'west'  : 'cave mouth - south',
                      'enemy' : 'whispering mistborn',
                      'item'  : 'elixir of soul',
                      'desc'  : '''
============================================================================================================================================
you stand on the precipice, staring out into the silent darkness. there is no other way forward except back north to the cave mouth.
============================================================================================================================================''',
                    },
                'cliff ledge' : {
                      'north' : 'crack in the wall',
                      'south' : 'cave mouth - east',
                      'east'  : 'wrought iron fence',
                      'desc'  : '''
============================================================================================================================================
you scramble onto the ledge, and to your east notice a wrought iron fence you could climb. to your north, there is a crack in a large stone
wall, large enough for you to squeeze into. to your south below you lies the cave mouth.
============================================================================================================================================''',
                    },
                'crack in the wall' : {
                      'south' : 'cliff ledge',
                      'east'  : 'the maw between hours - corridor',
                      'enemy' : 'half-born remnant',
                      'item'  : 'elixir of flesh',
                      'desc'  : '''
============================================================================================================================================
from your location in the crevice of the thick stone wall, you notice what seems to be a grand corridor to your east. the air is pungent 
with rot and decay, punctured only by the fresh air flowing from the cliff ledge to your south. you hear movement in the building to your
east. 
============================================================================================================================================''',
                },
                'wrought iron fence' : {
                      'west' : 'cliff ledge',
                      'south' : 'graveyard',
                      'east'  : 'garden',
                      'desc'  : '''
============================================================================================================================================
from your position atop the wrought iron fence, to the east you spy what seems to be a derelict yet once loved garden, with a dried fountain, 
barren soil and withered trees. to your south there are unmistakeably graves whose inhabitants' names have been lost to time.
============================================================================================================================================''',
                  },
                'graveyard' : {
                      'north' : 'wrought iron fence',
                      'east'  : 'disused training yard',
                      'enemy' : 'whispering mistborn',
                      'item'  : 'elixir of flesh',
                      'desc'  : '''
============================================================================================================================================
the graveyard is full of tombstones of varying shapes and sizes, with some modern black marble and others crumbling sandstone and lime. they
have one thing in common - all have clearly been forgotten - but appear to be those of heroes, judging from the decayed and rusted weapons
and shields littered around them in tribute. the iron fence is to your north, and to your east you see a disused training yard.
============================================================================================================================================''',
                },
                'garden' : {
                      'west' : 'wrought iron fence',
                      'north' : 'main foyer',
                      'south' : 'disused training yard',
                      'east'  : 'carriage house',
                      'enemy' : 'whispering mistborn',
                      'desc'  : '''
============================================================================================================================================
you stand in the remains of a once-loved garden, evidenced by the dried earth of the former flower beds that garnished the mossy cobble path and
surround the bases of the corpses of trees. west is the iron fence, south is an old training yard, and east appears to be a derelict carriage
house. directly north is a grand entryway into what appears to be some kind of manor or castle. the arched ironwood door is an anomaly among 
the blatant disrepair, standing tall and imposing, as sound and polished as the day it was made. the carvings of the tympanum above are
unintelligble, however.
============================================================================================================================================''',
                  },
                'disused training yard' : {
                      'west' : 'graveyard',
                      'north' : 'garden',
                      'east'  : 'worn barracks',
                      'enemy' : 'fallen adventurer',
                      'item'  : 'rusted axe',
                      'desc'  : '''
============================================================================================================================================
rotten straw men lay strewn across the ground, clearly having been target practice in the past, surrounded by an assortment of old weapons.
to the west lays the graveyard, and to the east, an old barracks building. north is the garden.
============================================================================================================================================''',
                },
                'carriage house' : {
                      'west' : 'garden',
                      'south' : 'worn barracks',
                      'item'  : 'elixir of soul',
                      'desc'  : '''
============================================================================================================================================
the carriage house must have been a grand affair once, its simple design disguising the use of elegant woods in its construction. rusted
troughs lay to one side where horses must have been fed and watered by their coachmen. there are no signs of any vehicle or animal now save
for a bent old wheel to one side in the dusty building. looking out west, you see the garden and to the south, a similarly dusty barracks.
============================================================================================================================================''',
                  },
                'worn barracks' : {
                      'west' : 'disused training yard',
                      'north' : 'carriage house',
                      'enemy' : 'feral remnant',
                      'item'  : 'steel greatsword',
                      'desc'  : '''
============================================================================================================================================
you step through the splinters that were once a door into a musty old barracks. its a relatively small affair, with space and lodgings for
no more than ten guards. there are still a few mouldy hay mattresses dotted around, and an assortment of old weaponry. west lays the training
yard, and to the north is the carriage house.
============================================================================================================================================''',
                },
                'main foyer' : {
                      'north' : 'hall of the unnumbered trials - south',
                      'south' : 'garden',
                      'enemy' : 'whispering mistborn',
                      'desc'  : '''
============================================================================================================================================
the foyer seems out of place compared to outside - barring a little dust, it looks relatively modern, with ornate wainscoting in a lush dark
wood with lighter appliques surrounding the doorway to the garden in the south and a similar doorway to the north. 
============================================================================================================================================''',
                  },
                'hall of the unnumbered trials - south' : {
                      'west' : 'the maw between hours - foyer',
                      'north' : 'hall of the unnumbered trials - north',
                      'south' : 'main foyer',
                      'east'  : 'the cradle that remembers - foyer',
                      'desc'  : '''
============================================================================================================================================
the wainscoting of the main foyer continues in to a grand hall, so large you are almost unable to see the northern end. along the walls above the
wooden pannelling are stonecarved reliefs of figures, each wearing distinct attire and armour - as if in rememberance of previous heroes to tread
the same path you are on. there is an empty space, waiting for its next inhabitant. there are two doors, one to the west and one to the east.
to the north, there seem to be two more, similarly on each side.
============================================================================================================================================''',
                },
                'the maw between hours - corridor' : {
                      'west' : 'crack in the wall',
                      'north' : 'the maw between hours - foyer',
                      'enemy' : 'half-born remnant',
                      'item'  : 'elixir of soul',
                      'desc'  : '''
============================================================================================================================================
the thick miasma of stench tainted by decay almost overwhelms you, but the gentle breeze through the crack in the west wall aids in your
resolve. the otherwise fine hallway leads north to the foyer.
============================================================================================================================================''',
                  },
                'the maw between hours - foyer' : {
                      'west' : 'the maw between hours - hall',
                      'south' : 'the maw between hours - corridor',
                      'east'  : 'hall of the unnumbered trials - south',
                      'enemy' : 'grasp of many',
                      'desc'  : '''
============================================================================================================================================
the repugnant stench of decay and despair becomes suffocating as you near its source. to the east, you see the door back to the vast hall of
other doors, and to your south, the corridor with a crack in the wall to the outside. west lays a grand hall, where the source of the
miasma appears to be.
============================================================================================================================================''',
                  },
                'the maw between hours - hall' : {
                      'east'  : 'the maw between hours - foyer',
                      'boss' : 'the maw of gentle regret',
                      'desc'  : '''
============================================================================================================================================
the hall must once have been a grand dining room, the polished marbled floor thick with a sludge that has the taint of rotten flesh and
blood. the furniture, what is left of it, has all been swept to one side and there are distinct long bones of discarded limbs scattered
amongst the filth.
============================================================================================================================================''',
                  },
                'the cradle that remembers - foyer' : {
                      'west' : 'hall of the unnumbered trials - south',
                      'south' : 'the cradle that remembers - corridor',
                      'east'  : 'the cradle that remembers - antechamber',
                      'enemy' : 'husk of knowing',
                      'item'  : 'heavy mace',
                      'desc'  : '''
============================================================================================================================================
this foyer has a lilting sadness somehow upon it. lost books litter the floor, as if discarded in a hurry by someone searching for answers 
of the utmost import. to the south is a corridor, and to the east, an antechamber of some kind. to the west lays the long hallway of doors
and forgotten faces.
============================================================================================================================================''',
                },
                'the cradle that remembers - corridor' : {
                      'north' : 'the cradle that remembers - foyer',
                      'east'  : 'the cradle that remembers - cradle',
                      'enemy' : 'husk of knowing',
                      'enemy' : 'vessel of errant insight',
                      'item'  : 'elixir of flesh',
                      'desc'  : '''
============================================================================================================================================
various faded artworks detail the walls, masking some of the faded silken wallpaper. there are indecipherable scrawls along the walls at
intervals that appear to have been written at different times from the shades of the ink, yet strangely all with the same hand. to the east 
the hall opens into a grand library, and to the north the foyer that leads back to the hall.
============================================================================================================================================''',
                },
                'the cradle that remembers - antechamber' : {
                      'west' : 'the cradle that remembers - foyer',
                      'south' : 'the cradle that remembers - cradle',
                      'enemy' : 'husk of knowing',
                      'enemy' : 'vessel of errant insight',
                      'item'  : 'elixir of soul',
                      'desc'  : '''
============================================================================================================================================
old and overused furniture is strewn around the antechamber as if someone had been living here for a very long time. stacks upon stacks of
books surround the various seats like someone had worn out each in turn whilst searching for answers. to the south lays a grand library, and
to the west, the foyer that leads back to the main hall.
============================================================================================================================================''',
                },
                'the cradle that remembers - cradle' : {
                      'west' : 'the cradle that remembers - corridor',
                      'north' : 'the cradle that remembers - antechamber',
                      'boss' : 'lady vestige, the bound echo',
                      'desc'  : '''
============================================================================================================================================
the library houses thousands, if not more, books that once lurked on their many shelves. cobwebs and filth cover most of the room, save for
a corner where there had recently been activity. a solitary desk stands alone, covered in reams of parchment decorated in the same archaic
script that adorns the walls of the corridor to the west. to the north lays the antechamber where someone had clearly been residing.
============================================================================================================================================''',
                  },
                'hall of the unnumbered trials - north' : {
                      'west' : 'vault of the once-whole - foyer',
                      'north' : 'the silent threshold',
                      'south' : 'hall of the unnumbered trials - south',
                      'east'  : 'sepulchre of the unmarked step - foyer',
                      'desc'  : '''
============================================================================================================================================
the north end of the grand hall is as painstakingly decorated as its southern counterpart. the carved reliefs of heroes past continue to
adorn the walls above the familiar dark wainscoting - is that a hint of sadness you see on the faces? there are two doors, one to the west 
and one to the east. back south, you can vaguely make out the same in the darkness.
============================================================================================================================================''',
                },
                'sepulchre of the unmarked step - foyer' : {
                      'west' : 'hall of the unnumbered trials - north',
                      'north' : 'sepulchre of the unmarked step - wasted tomb',
                      'east'  : 'sepulchre of the unmarked step - funerary parlour',
                      'enemy' : 'votary of many tongues',
                      'item'  : 'elixir of soul',
                      'desc'  : '''
============================================================================================================================================
this foyer has an uncanny stillness about it - the stillness of the dead. to the north lies a suspciously empty room, and to the east, a room
with some form of workstation. the west holds the door returning to the hall.
============================================================================================================================================''',
                  },
                'sepulchre of the unmarked step - wasted tomb' : {
                      'south' : 'sepulchre of the unmarked step - foyer',
                      'east'  : 'sepulchre of the unmarked step - undercroft',
                      'enemy' : 'votary of many tongues',
                      'enemy' : 'lamenting vestal',
                      'item'  : 'elixir of flesh',
                      'desc'  : '''
============================================================================================================================================
other than what appears to be an empty stone casket laying on a flagstone floor, there is nothing of note in this dusty room. the foyer is
back to the south, and to the east you can make of the distinctive vaulted appearance of an undercroft.
============================================================================================================================================''',
                  },
                'sepulchre of the unmarked step - funerary parlour' : {
                      'west' : 'sepulchre of the unmarked step - foyer',
                      'north'  : 'sepulchre of the unmarked step - undercroft',
                      'enemy' : 'votary of many tongues',
                      'enemy' : 'lamenting vestal',
                      'item'  : 'elixir of flesh',
                      'desc'  : '''
============================================================================================================================================
what appeared to simply be a workstation seems to actually be a preparation station for... bodies. a large marble slab sits pride of place
in the centre and is covered with blackened red stains. to one side there are shelves, with various dusty containers, and fine tools perhaps
for stripping flesh from bone. there is a painting on the slab, eerily similar to the faces in the reliefs of the grand hallway, almost as 
if to be used as a reference. to the north lays the vaulted arches of an undercroft, and to the west the foyer back to the main hall.
============================================================================================================================================''',
                },
                'sepulchre of the unmarked step - undercroft' : {
                      'west' : 'sepulchre of the unmarked step - wasted tomb',
                      'south'  : 'sepulchre of the unmarked step - funerary parlour',
                      'boss' : 'the choir of one',
                      'desc'  : '''
============================================================================================================================================
you stand in the middle of a grand, vaulted room that houses sacks of materials in the corners. they spill out, seeming to be a cement of
some description. alongside them, there are a couple of skeletons in old ragged armour whose faces have been perfectly preserved as if alive
yet smothered in plaster.
============================================================================================================================================''',
                },
                'vault of the once-whole - foyer' : {
                      'west' : 'vault of the once-whole - gaolers quarters',
                      'north' : 'vault of the once-whole - stockade',
                      'east'  : 'hall of the unnumbered trials - north',
                      'enemy' : 'chained forlorn',
                      'item'  : 'steel warhammer',
                      'desc'  : '''
============================================================================================================================================
the rough cut stone floor of the foyer is marked with scratches and deep gouges, as if a battle had taken place here long before. stale yet
still liquid blood congeals underfoot. to the west is a small room that perhaps once housed a guard, and to the north you see some makeshift
fortifications as if against some threat further inside. back east lays the door to the main hall.
============================================================================================================================================''',
                },
                'vault of the once-whole - gaolers quarters' : {
                      'east' : 'vault of the once-whole - foyer',
                      'north' : 'vault of the once-whole - gaol',
                      'enemy' : 'chained forlorn',
                      'enemy' : 'blood-fettered veteran',
                      'item'  : 'elixir of flesh',
                      'desc'  : '''
============================================================================================================================================
the small guardsman's room must have once been the quarters of a gaoler, with a heavyset barred door to the north. discarded, rusted chains
litter the floor and it looks as if something has broken out of them. away from this, east leads back to the foyer.
============================================================================================================================================''',
                },
                'vault of the once-whole - stockade' : {
                      'west' : 'vault of the once-whole - gaol',
                      'south' : 'vault of the once-whole - foyer',
                      'enemy' : 'chained forlorn',
                      'enemy' : 'blood-fettered veteran',
                      'item'  : 'elixir of soul',
                      'desc'  : '''
============================================================================================================================================
the walls surrounding the stockade are similarly slashed and gouged to the foyer to the south, and the congealing blood is spattered across 
the thick planks that were once used to block something in. there is, however, a way forward to the west.
============================================================================================================================================''',
                },
                'vault of the once-whole - gaol' : {
                      'south' : 'vault of the once-whole - gaolers quarters',
                      'east' : 'vault of the once-whole - stockade',
                      'boss' : 'ser ulthric, burdened of names',
                      'desc'  : '''
============================================================================================================================================
the gaol of an ancient soldier is littered with corpses of would-be adventurers that came before you, their skulls wrenched from their 
shoulders and scattered amongst the broken chains and old weapons.
============================================================================================================================================''',
                },
                'the silent threshold' : {
                      'south' : 'hall of the unnumbered trials - north',
                      'desc'  : '''
============================================================================================================================================
you are alone in a vast, echoic chamber. the air is still, and yet you feel the eyes of previous adventurers upon you. in the centre of the 
room, there stands a lone door - a grand, imposing structure. there is no way to open it, but there seems to be a cavity inside - like a 
mortise. something surely fits in here.
============================================================================================================================================''',
                },
                'the atrium of unmaking' : {
                      'south' : 'the silent threshold',
                      'boss' : 'the child beyond time',
                      'desc'  : '''
============================================================================================================================================

============================================================================================================================================''',
                },
            }
    #hp remnant 2
    enemies = {
                'feral remnant' : {
                      'enemyhp' : 3,
                      'enemyatk'  : 1,
                      'enemyart' : '''
                                                                                                
                                                                                                
                                                                                                
                                                                                                
                                                                                                
                                                                                                
                                                               ;.....+                          
                                                     ...     +;        :                        
                                           :;:;;;::        Xx++;:;:     :                       
                                          +$.::.   .+;.  ..xx++x+x...    x                      
                                        .+. ..: .:    .+.:;+&&x&&x. .... x                      
                                       +... .......:+Xx++x$&&&&;:x&&$:.::                       
                                     :+++.:.  .....&&&$$&&&$&&$&x;&&&XX$+                       
                                 .: .;+xxx;;+;:;:::;&&&&&$$&&&X&&&x+;;Xx.                       
                              ::..++.;$$XXX$$$$&&&&$+.:$&&&&&&XX&&x..+x                         
                           ;...+X;x+xx&&&X&&&$$&$&&&$&$&&&&&&&&$$&&&$;                          
                      :...;.;:+x+XX$+ X$&$&X&&$$&$X$$&&$&&&&&&.$x&&&&++                         
                    :::.;..x;XX$$.    X&XxX$x&&x&&&$&$XX&&&.   :Xx$X&x$;;                       
                   ;x . :x$X           .X&X$xX&$XX&&&$&&&        xX&&&&xxx.                     
                  :;:; ++X.           x&$$&&&&&&&&&&&$X:             +&&&&&$xX.                 
                  .:..xxx          x&X&&&&&&&&&&&&                        +$&&;.;               
                 :+.+:X          :&$&&&&&X&X&&&&&&+                          .&..+;             
                 ...x:           $&&$&&$$X$$&&$&&$&                           +...;;x           
                :..X            x$$$&&&$&&$$&$&$$&&&&&x+:                     ..;;..;;:         
               ...$            X$$&&&&$&$&&&&$$&&&&&&&&&&&&x                 x.x.:&$;:;;        
             . . :x           $&&&&&&&&&$$&&$&$&&&&&x;;;;..&:&X              x;+    &;:+:       
             x...&           XXxxX&&&&XX$XXXX&&&&&&&+;;;::  ..  $:           .X      +;&;;      
            +xX;;:         X$xxX:::$&&&XXX$$&&$&&&&&&&$+; ::. ;  .+                  :X&x:      
          .+x++:.. .       XXX:   :x&$X$XXXX$$&&&&&&&&&&&. .:: ..                    : +:       
         .+::;:.+x.;      X&X:   .::&$X&&&X&&X&&&&&.xX&&&&x..;::.+                              
         ;+:x::x.+xx    :&&&+.  .::$&$x&&&$&$.$&&&&     :$&&&+  . :                             
        +X+x$:+   $x   :&&+++. .::X$&X;&X++&x .&&&$        .&&$+:.::                            
        &$$xx+x   X:  :$  ::; .:.X+&&$X&: ;;x  $:&$          &$&&$$;                            
        ;&$x$$x       x;+$$$::.;+ ;&&&&+   .   X Xx          &&X&&&;                            
          $X +X     .;+X&x$; .&&:  &&&;          +           .&&x&&;.                           
                   ;;X&&&&X;;;x    X&                         &&&&&+X                           
                  +X&&&&&&&&&+      &                         X&&&&xX                           
               .xx&&&&X:            $                          $&&&x$                           
              &&&&&X                ;                           &&&;x                           
             x&&&&                  :                            &&&;:                          
            ;$&&$$                                               +&&X;                          
            x$&$&+                 ..:                            $&x;+                         
           XxXXX$&&&&&&&&&&&&&&&&&&&&&Xxxxxx;;:  .    :::::       X&X:X;                        
      :X&&&+x;;::&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XxXx+xx:    ..:.  .X&X$x;                :      
     +X&&&$X+x;$.+&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$x;;;;       +&X;..:;x         xX;         
          ;$X;          ...::X&&&&&&&$&&&&&&&&&&&&&&&&&&&&&&&+:::.+&&+;  .:.:+x;::              
                                   .:;++++;x$&$Xxxxx++xx&&&&&&&&&&&&&&$+++++;;+:;.              
                                  .                                ....;X$;;&;$+XxX+            
                                                                 .;;+Xx;;:::                    
                                                                                                
                                                                                                
                                                                                                
''',
                    },
                'whispering mistborn' : {
                      'enemyhp' : 5,
                      'enemyatk'  : 1,
                      'enemyart' : '''                                                                                      
                                                                                                
            ..        :..                                                                       
                 .:    .;;;;                                                                    
                          ;;;;           :                   .                                  
                            :;;;.    ...::;:.   .;.    ::..                                     
                               .;;;;;;;.;          .. :+;.:.       :                            
                                                     ;  .;:::  ::  .                            
                                       :: .                .::.  x.. ..                         
                                  ..;+X;.$$$+   ;:    ;   .  ::...x::           .               
                             :x:xxXxX$X&$&&&X$Xxx$X:: ...     .x+x;x;:::....                    
                        :;x&x$X$&$$&$&&&&&&&&&&x&&&X:...........xx;+x::::::.......              
                    :xX$X$$&$&&+;;;;;;        ;X$&&&&&&::....X:xxxXX;xx;:::........             
                x&x$X$$&&&$                        x&&&&X;xxxx;xxX+;;X&;:x...+$+...             
               &X&x$   :&$                        +&&&&$&&X;Xx+;xX;x&+:$$.::$&&+..              
                X &     x:                        X&&&&X$&&&X++;xX;+&&$::.;&&&$:$               
                :  .   X                        .+X&$&&x$&&&&&XXxX;+&&&&:.&&&&&;                
                                           .++;Xx$XX$x$XXx$&&&$++xx+$&XXX.;&&X                  
                                       +&&; Xx$&X&$&&X$X$X$&XXXx+;XXXXX+$&:X                    
                                         ;;X$$$$$$&&&&&&&&&&&&&&$$$&&&&&&&.                     
                     ;;;;;          +:+X&&&&&$$XX&&$&&&&&&&&&X+.    ;&&&&;                      
                  ;+xx&&&xxx++++++xxxX$X+X$$$&&X$X&&$&&&&&&;         $&&&;                      
                 .$&&&&XXxxxxxX$&&&&x+xxxx$&&&&&&&&  .x&&$x          &&&&&+.                    
                &&&&&&XX$&&&&&&&&$XXX$$$&$$&&&&&&&&+xX$$&&+          x&&&$Xx                    
              :&&;          &&&&&&&&&X$&&&&&&&&&&&&&&&&&&&&+          .&&&X+                    
             x;           &&XXXXXX$&&&&&&&&XxxX&&&&&&&&&&&&&+           &&$X:                   
                          x&&&&x;;;&&&&&&$$xxx&&&&&&&&&&&&&&&X           x&$x                   
                        $&&&&      X &&$xxxxxxX&&..&&&&&&&&$x$+.          $&X                   
                       x&x.          &XxxxxxxX&&;  $&&&&&&&Xxx&.          x&XX.                 
                                    +$xxxxxxx&;     x&&&&&&Xxxx+           $&$;                 
                                    $XxxxxxX&      &&&&&&&$xxxx+          $$$X;                 
                                 $&&&$xxxxx;     :X   X$&&$Xxxx+         &&&$$x                 
                               x&&&&&XxxxX;         .&&&&&&Xxxx+;      :&   $$x                 
                              :&&&&&&&&&;      &&&&&&&&&$X$$xxx$        .    $$X                
                              &&&&&&&$        &&&&&&&&$$$$&&&$$              $+&x               
                            .&&&&$+           &&&&:                        .$   +               
                           ;&&&&             X&&&                                               
                          &&&&:       ;     .&&&&                                               
                        ;&&&&x      +        x&&$                                               
             .    :     x&&&       +;                                                           
                 +++:   &&&&      .+;  .                                                        
                   .++ ;&$X$   ;++   .;  :                                                      
                .: ++++x$$$$. +    ++                         +.                                
         ::::+++++++++++++++++++++++++++++xxxxxxxxxxxxxxxxx+++++++xxxxxxxxx+xx;::::          
''',
                    },
                'fallen adventurer' : {
                      'enemyhp' : 7,
                      'enemyatk'  : 3,
                      'enemyart' : '''
                                                                                                
                                                                                                
                                                                                                
                                                                                                
                         :;      ;                                                              
                          x      .$.              :;                                            
                          ;X:     :$x;.         X&X:;;                                          
                           $+.      ;$$X: ;   :&&XX  :..                                        
                            :XxXx.     +&X&X  $&XXx:+ ;+                                        
                      . :     .;&X++     &&&$;&&$&&&&X+;  .                                     
                        .Xxx:.&&$$$$&&&&x.++&&&X&&++X&&+$$+X:                                   
                            X$&X&    ;xXXX&$&&&$$X&+&$X$&;$:Xx;.                                
                                    .x&XXX&X$&&&XX&+&X$&&Xx+  x+;                               
                                    X&&$&&&$&&&&&&X+$$$&$X$XXXxx:;                              
                                  X$$&&&&XX$&&&&&$&&$$$$&X$Xx$&&&$                              
                            X$:  x&&&&&&&&&&&&&&$&$X&+&&&&&&&&$X:&&.                            
                          x$&++X$&&&&&&&&&&&&$&$&&&XXX$$&$&&&&&$+X$X.     .                     
                        .$&$+x&&&&&&&X  .&&&&&&$&+;$&&&&&&XxX&&&&$X+X;  :+x                     
                       +&Xx$XX+&&&&:     X&&&&&$:&&$&&&&&&x   x&&&&$xxx$xxx..                   
                     ;$&xXX++$$XX        :&&&&&&&&&&&&$&&x;     ;&&$&&&$XXxX:.                  
                  +x&&+X;&&&x:           X$&&&&&&&&&&&&&$+         X&&X+xXXxX:                  
               :&&$$$&&&+              x&&&&&&&&&&&&&&&:+           x$&&XXx&+X:.                
              $x&&&&&XX             .X&&&&&&&&&&&&&&&&x$             :xX&&&+X+xX+:              
             x;&&&&Xxx            :$&&xX&&&&&&&$$;+$XX$XX                 ;&&$+xxX+:            
             +$$:X+.+           ;$&&; X$$$$&&&&&$$X$$$XXx$.                 +&&&&&X;;           
               ;  .           +$&&.  X$+;&$X$$&&&&&$&&&&X+ ;                 $++&&&&X:          
                            X&&&.  .X$$&&&&&&$&$&X&X&$X&&&X:X                :x.x$X&&:          
                         :$&&X     &&&&&&&&&$&&$&&&$+xX&&&&&&X;                 +:.XX;          
                       ;$&&+      $&&&$X$&&&$&x$$xxx+x$&&$$&&&&$                                
                     +$&&:      .X&&$Xx&XX&&X&XxXx++xx&&&XX$xxx+;                               
                   $$&$         &&&Xx&XXxX&&X&&x++++xx&&&&&&Xxxxx.:                             
                :$&&X        :$&&$&&&xxxxX&&xX&Xx++xx$&&&&&&&&XXXX++                            
              x&&&x        :$&&&&&&XxxxxX&&$xX&XxxxxX&&&&&&&&&&&$Xx+ :                          
           +$$&$:        ;&&&&&&&$&Xxxxx$&&Xxx$$xxxxX&&&&&&X+&&&&&$xx;                          
          ;+;          X&&&&&&&&&$&xxxxX&&&XXx$$xxxx$&&&&&:  X$$$$&$+;                          
                    .&&&&&&&&&&&$X&XxxX&&&&$&XxxxxxX&&&x&:    &&&&x;+.                          
                 .X&&&$ +&X  $&&&X:&&&+&&&&&&&Xxxxx$&&X $     &&&&&Xx;                          
               :.;           X&&&&$&$&&&&&&&&&&xxx.&&&.       $&$xxXx:.                         
                             &&&&&&&$;X&&&&&&&. x; +x          x&&&Xx;.                         
                           :&&&&&&:   &&$.&&&$  .               ;&&&X+.                         
                          $&&&&&      &. +&;                     +&&$:+                         
                         x&&&&X         ;                         x&&X+.                        
                        x&&&&$                                     &&X;+.                       
                    .  ;&&&&&          :                           &&&&$x.                      
                  ++  +&&$&&x   ...  ;X .;                 ; . :   .&&XXXx+. ;.;.               
                 ;:& x$;&$x&.  +xx.+&$.+$xxxxxxxxxxxxxxxx  x+X:+++..&&&&$X$XxX$;;               
       x&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&+      
                                    .............................                               
                                                                                                
                                                                                                
                                                                                                
''',
                    },
                'chained forlorn' : {
                      'enemyhp' : 7,
                      'enemyatk'  : 3,
                      'enemyart' : '''
                                                                                                
                                                                                                
                                                                                                
                                :;:                                                             
                            ;....x...+.                                                         
                           ;....+......+                                                        
                          &;..;.......+:+                                                       
                         +$&&&&&&&+;.::;++.::.x&x++;;:                                          
                         +&&&&&&&&&&X:x::x$..X&X;......;;                                       
                          &&&&&X&X$&+x:x+;&+.&+$x+++;:.;::                                      
                           $&+X+;.;$;&$:x;$Xx;xXXx$++xX:++;x                                    
                            X&&x::; :XXX+X&X$&x&+$$X+x$:&+:;x;                                  
                           +&&&&$&&&&+x&X;+&&$x&$+&&Xx&&x;+$+..+                                
                          $$&&&&X&&& x&&&xXx&$XX&X&&&x&&&&X;...X.;;   :                         
                         .$X&&&&&&$X&&&&&Xx$&:&+x$$&&&&&&&&&&X+:XXX$XXXx ;                      
                         $X&&&&&&&X&&&&&$&X$;$X+++xX$&&&&&;+&&&&&&&x$Xx++X+                     
                         &$$&&&&&&&xx&&&&X&&++X+++++x$&&&&X   x&&&&&$&&xx$$&&                   
                        .&&&&&&&&&&&x&x$&&xX+&x++++&&&$X$&X      &&&&&$&$xX$&x&&x:              
                        X&&&&&&&  :&&&X$XXX&&&&&&&$XXXX$$X&x      +$&&&&&&&&&&$&XXXXX           
                       $$&&&&&X    &&&&&&&&&&$$XXXXXXXxXX&&$             .$&&&&&+::x+:;x.       
                  ;;+$&X&&&&&&+     x&&&&&&&&&&&XXXXXx$&$&$&.                  &;+&&&&$X++;     
                 $xx$$&&&&&$ $&;      ;&&&&&&&&&&&&&X$&&x&$&&:                 $$$&&&&&&&$x;    
               ;x;XX&&$&&&:  ;x&        ;&&&&&&&&&&&&&$&&&&$&&:                .&+ X&&&&&$$$    
              X$XxX&$&&&&x     $          +&&&&&&&$$$&&&$X$+xX$&                +:    $&&$X     
            ;xX&X&&&x&&&+      $+;        x&&&&&&&&&&&$$$;xxx;;;&x                    $&$&x     
           x$$&$$&X;  X+        +&.      +&x&&&&&&&&&&$&+XX;x+;;&&&.                .x: +       
         ++$xx$&+                x;;x+x:x..&&&&&&&&$x$Xxx&$XXXxXXX&X+                           
       .$Xx&XX;x;                  +  ;; .&&&&&&&$X$&xxXX;$&x;:::::Xx                           
      x+X&&&&&&xx                      :&&&&&$$&&&&XX+x$&&$x+:::::::+X                          
    :x$$&&&&&X $x:                   :&&&&&&&X$X&&x+++&&&&xxx;:::::::x                          
     xXX$&&$.   &                  +&&&&XXx&&X$x$X+++x&&&&$xxX;::::+:::                         
     .X&$X&                       ;xxx+++++&&XX&x$+++&&+&&&&x+;::;;;+$X                         
      X.&: :;                    +x++++++xX&&XX&&$x+X&&+&&&$&x+;:::+&xx                         
                                $x++++xXXxxX&&X&&$xxX&&&&&&&&&x;::::;$x                         
                               Xx+++XX$$$$&&&&X&&&$X$&&+&&&&&&$;::::;$X+                        
                              ++++++xX&&&&&&&&&&&&$X&&&:&&&:&&&;::::+xx$$                       
                             $x++xx&&$x&&&&&& &&&&&&&&&:&&&  &&&XXxx+x&&&&                      
                             &&x$&xx&&&&&&X   &&&&&&&&&:&&x   X&&&&&&&&&&X&                     
                             &&&&&&&&&&&X     &&&&$.+&&:&&&   ;&&&&&&&$$&X&:                    
                             &&&&&&&&&&&x     &&&&$ ;&&:&&&     +&&&&&$&$X$$;                   
                             &&&&&&&&&&&      &X&&$ .&&  $&     ;&&&&&&&&X$$+                   
                              $&&&&&&&x       x X&$   &   $       :$&&&&&&&&&.                  
                              :&&&&&&&        .  +$       :          X&&&&&&&&X                 
                               &&&&&&.            $                    :&&&&&&&:                
                              &&&&&&&                                    ;&&&$&&x               
                            x&&&&&&&&                                    .&&&&&&&               
                         ;$&&&&&&&&&.                                     X&&&$&&$              
                  ;$$$&&&&&&&&&&&&&&$$$$$$$$$$$$$$$$$$$$$$$X$$$$+::::.     &XX++X$;             
                .+..&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&X$X$x$X$&&+.         
''',
                    },
                'blood-fettered veteran' : {
                      'enemyhp' : 6,
                      'enemyatk'  : 3,
                      'enemyart' : '''
............:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.......
.........:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::....
.........::::::::+;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::....
.........::::::::$+++:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::....
.........::::::::+X;+x::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::....
.........:::::::::x$;+x:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::....
.........::::::::::;$+X+::::::::::::::::::Xx;..$;:::::::::::::::::::::::::::::::::::::::::::....
.........:::::::::::;$+;;:::::::::::::::;$+.....:$::::::::::::::::::::::::::::::::::::::::::....
.........::::::::::::;$;+;::::::::::::::;$:....;x&::::::::::::::::::::::::::::::::::::::::::....
.........:::::::::::::;&;+$::::::::::::::&&x:xx:+&&&+:::::::::::::::::::::::::::::::::::::::....
.........::::::::::::::;&:x$::::::::::::X$&&$X&x;&&&&&&$&+::::::::::::::::::::::::::::::::::....
.........:::::::::::::::;&+XX:::::::::X$&&&$;x:$X$&$$$xxx++&x:::::::::::::::::::::::::::::::....
.........::::::::::::::::;$X+X;::;X&&Xx$&&&&&$X&X$&$Xxxx$X$$$&:$X+;:::::::::::::::::::::::::....
.........::::::::::::::::::&XXxX&&&$&XX$&&&&&x:&$$$&xX$$&$x:$&$x+x$x;:::::::::::::::::::::::....
.........::::::::::::::::::+&X&&$&&&&&&&&&&&$$&&X$XXX&&&&;$;;;$x;;;x$X::::::::::::::::::::::....
.........:::::::::::::::XX&X&x&Xx&;+::::;&&&&&&&$&&&&&&&+X;;;;+Xx;;;+&$;::::::::::::::::::::....
.........:::::::::::::::xx::$$;;&x::::::::&&&&&&&&&xX&&x;x;;;;;X+;;;+x&X::::::::::::::::::::....
.........::::::::::::::::::::;X&&x+:::::::&&&&&$&&++X&&+$X.+;;;X;x;;.+$$;:::::::::::::::::::....
.........:::::::::::::::::::::::x$+&::::::&&&&&$&$$$&&&$:X.+;;;+xX;;;;XXx:::::::::::::::::::....
.........::::::::::::::::::::::::;+;::::::$:+x&&&&$&&&&&+&Xx;;;;Xx;;;;x&$:::::::::::::::::::....
.........::::::::::::::::::::::::::::::::::::+&&&&&&&&&&XxX+;;;;x+X;;;;XX+::::::::::::::::::....
.........:::::::::::::::::::::::::::::::::::;&&&$&&&&&&&&:Xx;;;;xxxX;;;x$$::::::::::::::::::....
.........:::::::::::::::::::::::::::::::::::+&$$&X$$xX&&&x&xxx+xXxx$+;;x$$;:::::::::::::::::....
.........:::::::::::::::::::::::::::::::::x&&&&&+x&&&$&$&X:X+xXX$x&$&XxxX$X:::::::::::::::::....
.........:::::::::::::::::::::::::::::+$&$$$$&+X&&XX&&&&&&:&&$xxxX&XXxxxx$X:::::::::::::::::....
.........::::::::::::::::::::::::::;X$$$$$$$$X&&X$&&&&&&&&Xx&&xxxxXXXxxxx$X:::::::::::::::::....
.........::::::::::::::::::::::::;$&$$$$$$$$X$&&X&$$$&&x&&&:&&$xxxx&&xxxx$$;::::::::::::::::....
.........::::::::::::::::::::::;X$&$$$$&&$&$&$&&X&$$&&$$&&&$X$&$$xxxxxxxxx$X::::::::::::::::....
.........:::::::::::::::::::::$X++X&$&&&&&&$&&&$X&$$&&$&&&&&&x&&&$xx&&xxxX$+::::::::::::::::....
.........:::::::::::::::::::::$Xxx$&&&&&&&&&&&&&X&$$&&&&&&&&&&X$&&XxXXxxx$$:::::::::::::::::....
.........:::::::::::::::::::::;$XX&&&&&&:::$&;&&&&$$&&&&&&:+&&&XX&&&xXXxx$$:::::::::::::::::....
.........::::::::::::::::::::::x&&&&&&;::::$+;&&&$&&&&&&&&$:;&&&$X&&$&&xx$X:::::::::::::::::....
.........::::::::::::::::::::::&&&&&&&;:::x&:;&&&$&&&&&&&&&+:x&&&&XX&&XXX$;:::::::::::::::::....
.........::::::::::::::::::::::&XXX$&&::::xX:::&&$&&&&&&&&&&&:;$&&&$X&&Xx&+:::::::::::::::::....
.........::::::::::::::::::::::&&&&&&::::::::::&X$&&&&&&&&&X&:::;&&&&&$X&&&$::::::::::::::::....
.........::::::::::::::::::::::X&&&&&::::::::::::&&&&&&&&&&&;::::::::&&&&&&$;:::::::::::::::....
.........:::::::::::::::::::::::&&&&::::::::::::::+&&x&X;x$&x::::::::&&&&&&&$:::::::::::::::....
.........::::::::::::::::::::::$&&&&::::::::::::::::&:&X;+::::::::::::+&&&&&&;::::::::::::::....
.........::::::::::::::::::::::&&&&X::::::::::::::::::+X:::::::::::::::::x&&&&&;::::::::::::....
.........::::::::::::::::::::X$$&&&&::::::::::::::::::::::::::::::::::::::;&&&&$::::::::::::....
.........:::::::::::::::::;$$$&&&&&&::;;;;+XXXXXXXXXXXXXXXXXXXXXx::::::::::+&&&&&:::::::::::....
.........:::::::::XXX+$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$XX$&$$$$&X:::::::::....
.........:::::::::::::::::::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;::;:::::::;x&&&&&X;::::::::....
.........:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::....
.........:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::....
.........:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::....
''',
                    },
                'lamenting vestal' : {
                      'enemyhp' : 5,
                      'enemyatk'  : 4,
                      'enemyart' : '''
                                                                                                
 ......................................................................:....................... 
 ......................................................:....................................... 
 .........................................:.....::::.::...............................:........ 
 ...............:.............................:;    ;::..............................:......... 
 ................:................:.........:+.    . ::..............................:......... 
 ..............:.................:...........+;; x&&&+x...............:.............::......... 
 ...................::............:.........:$.X+&&&&&X...:...........:.................:..:... 
 .........................................:+Xx.X&&&&&&;.....:.........:.................:...... 
 ....................:.................::;:;+$&X&&$+&X+::.............:.......:.......:........ 
 .:.:.:::.:::::::....................:;     .+;X&Xx++x::+::...............................::... 
 ...................................:&$x.   ..:X$..++x   :;:.........:......................... 
 ..................................::$xxx&X: .+xX..;++: x$::................................... 
 ..................................:+x  X$&&&&&X:.x&x:&&&X.;..........................:........ 
 ...............:..................:x$$$X$&$$xxX&&&&&XXXXXXx:.:................................ 
 ................................::+x$.+$Xxxxx$&&&&&&&&xxxx:;::.....................::::....... 
 .............:...................:;$$$$xxxxX$&&&xx$&&&&XxxxX;:...:.................:.:........ 
 ............::...:.............:.:X$+&Xxxx&&&&xx  xx&&$$xxx$;;.......:........................ 
 ...:.:...........:................X$+&&&&&&&$x.     +x&&&$&$X+.......:........:.............:. 
 .................................:X&+&&&&&&&$+        &&&&&&x;.......:...............:........ 
 ....::..........................:.x$;&&&&&&&&&&&&&&&&X$&&&&&x:.......:...:.::..........:.:::.. 
 ..................................XX+&&&&&&&&$&$X$$&&&&&&&&&x:................................ 
 ..................................X$;&&&&&&$$X&&XX$$&&&&&&&&x:................................ 
 ..................................X&;&&&&$x&$&x:;;;++xx&&&&&x:................................ 
 ..................................X&;&&&&Xx$X&+ .  :;.:&&&&&x:......................:::....... 
 .............:....................$&;&&&&x$$X&+     .. &&&&&x:..........:..........:::::...... 
 .........:::::....................$&;&&&&x&$X&:      . X&&&&x:........:...........:........... 
 ...................:.............;&&;&&&$x&$$&.        x&&&&x:.......:........................ 
 ............:....................;&&;&&&XX&$$&.        x&&&&x:.......:........................ 
 .................................;$&;&&&XX$&$&. :      +&&&&x:..............::.......:...:.... 
 ................................:+$&;&&&xX$&$&. ;    . +&&&&x:.......:.............::..:...... 
 ................................:&$&;&&&xx&&$&. ;    . .&&&&x:................................ 
 ................................:&$&;&&$+x&&&&: .    .  X&&&x:................................ 
 ................................+&X$;&&$+x$$$&:      .  X&&&x:....................:...:....... 
 .............:::................+&X$;&&x++:.X+;         +&&&x:.......:........................ 
 ........::.::::.................$&x$;&&x++  ;;+         ;&&&+;:.:................:.:::........ 
 ..........::.:.................:&&x$+&&xx+ .:;.         :&&&&x:.:....:..........:....:.:...... 
 .....:..........:.............:X&&x$+&&xx+ .:+.         :&&&&;:......:.........:......:....... 
 ..:........:..................:&&&xX+&$x++ .:+.      .  :&&&&;::.....:...............:........ 
 ...............:.............::&&&XX+&$xx+  :+. .:  ..  :&&&&+:...................:...:::::... 
 .............................;&&&X$x+&&&&x: X$;$:; .x$ +x&&&&X:............................... 
 .............................x&&&x$x+&&X$+x ;xxx+;+++$ +X&&&&X:............................... 
 ............................:&&&&X$X+&&&&&&&&&&&&&&&&&&&&&&&&&+:...:.......................... 
 ............................X&&&$&&x&&&$&$XX&&$&&&&$$&$X$&&&&&X:.............................. 
 ...........................+&&&&$$&$&&&$&$xX&$$X$&XxX&$X$&&&&&&::............................. 
 .........................:+&&&&&&&&&&&&$&$xX&$$X$$XxX&$X$&&&&&&&::............................ 
 ......................::.X&&&$&&$&&&&&&&&&&&&&$$$&$$&&&&$&&&&&&&&x:::......................... 
 .................::::X$&&&&&&&$&&&&&&&Xxx$&&&&&&&&&&&&&&XXX$&&&&&&&&&&XX+::.................:. 
 .................::::::::+xxX$&&&&&&&&&&&&&&&&&&&xx;;;;;;;;;;:::::::....::.................... 
 ................................:;++xx++::::.....:.......................................:.... 
 .............................................................................................. 
 ........................................................................:..................... 

''',
                    },
                'votary of many tongues' : {
                      'enemyhp' : 7,
                      'enemyatk'  : 3,
                      'enemyart' : '''
 .................. ..........................................................................  
 .............................................................................................  
 .............................................................................................  
 ....;........................................................................................  
 ...x:;:+.....................................................................................  
 ...;$$$&...+x;+Xx............................................................................  
 .....:XXx:..:x&X$+:..........................................................................  
 ...$;;.xX;x;...+x++..........................................................................  
 ..;:$;.:$&$$.:+x+X...........................................................................  
 ..X&X;...&&$X$$$$:..........................:::..............................................  
 ..+$++x..:X&&&:..........................:;     ;............................................  
 ....$&xx++X:X$;X........................+      .+&...........................................  
 ............X$&$X:......................X .    ::+:..:;;;....................................  
 .............xX$$;......................X+$&&&:+:+X;X ;+&: $X............x&&+;$$&&...........  
 ................$x......................X$&&&&&$xx&+:.+&.+++.x;;$+...x.xX$&&&&&&X............  
 .................$X.................:+  Xx$;+;&&+xx+  XX:X+&X+++;$X$&$X&&&&&&$&x.............  
 ..................xX;..............:.:;:X$X&&X$$XxXX+&xXx$&&&&&&&&&X&Xx......Xx..............  
 ...................X$:.............++X+;xX$$X$XXX+xXx&&&&&&&&&&&$;:..........................  
 ....................x$$X+...;;;++X$X&XX$$$X&X$$X$x$+&&Xx$&&&&x$X$$;x.........................  
 ...................XXxx&&x$$$$Xx$X&XX$&&$&X&X&&&$&+$X+++x&&&;................................  
 ...................;&;X$+&&&&&&&&&$XX&&&&&$+X+&$$xXX+++XxX&&&+...............................  
 .....................Xxx$X..::........x&&&&&&$Xx$&XxxxxxX$$&&$+..............................  
 ........................:&x..............:.:$&&&$$X$X&$$X$&&&&$+.............................  
 .........................:$X................xx&&&&$$$&$$$$$&&&&&X:...........................  
 ..........................:&X.................;&&&&&&&&$$+++X&&&&&x..........................  
 ............................xX:...............&$$XX&$+&&&&&&$x$&&&&&&;.......................  
 .............................X$;............$&&$&&&&&&+..X$&$xx&&&&&&&&&:....................  
 ..............................X$:.........;.xxxx$&&x;+$&&&&xx++xX&&&&&&&&&&&x;;:.............  
 ...............................$$;.....:XxX$xx$$$&XX+$X&&X++;:;;x&&&&&&&&&&&&&&&&&&::........  
 ................................+$+...x&&&&$x$$&X&X$X&x$&X&x:::XX+$&&&&&&&&&&&&&&&&&&&&;;+...  
 .................................+$+;;;+++X&&&X&&&&XXx&X&$x&XX+xx&&$&&&&&&&&&&&&&&&+xx.......  
 ..................................+$x+++++xX&&&&&&&X;Xx$X&X&XxxxxX$&&&&&&&&&&&&&&&$..........  
 .................................;xx$X+++x$&&&&&&&&X;X$X$&&XX++$$&&&&&&&&&&&&&X.++$$.........  
 ................................;+;$$&XX&&&&&&&&&&&Xx+&+x&&&$&&$$&&&&&&&&&&&&&&$..+&&........  
 ................................;$X&&&&&&x$&&&&&&&&X$X&$;X&&X$++++xX&&&&&x..+&&+....$:.......  
 ................................XX&&&&&;..X&&&&&&&&x&&&&&X&&&&++;:++Xx..+&&...:+&:...........  
 ..............................:$:$$&&&&...x&+$&&&&&$$&&&&X$&&&X++::+$X$X...$:....X...........  
 ....................;:........;xx$&$&&X.....;x:&&&&&&&&&x&xX&&&&XX$&X&$X+....................  
 ..................:+..........XX&&&&&x......:+:&$&&&&&&&&&$+$&;+.$&&&&$$&x...................  
 .............................x:$&&&$..........:X..++x&&&&&&&&&;...X&&&&&&&x..................  
 ...........:x.......:.......X:X&&&+.................+;.&&&&&&&&:.....X&&&&&$:................  
 ............x.x........:....+x&&&...................;:...$:.x&&:.......+&&&&&$.......;.......  
 ...............$;....:.....XX$$&:........................$:...&:........:$&&&&;....;.........  
 .........;:...+.$;;.+.....;;$$&;.........................$:..............;&&&&$..:;$.:.......  
 ...........;+.;$x$&x+;::+.xx$$$..++:;+..............................:.;;..X&&&&x.+;$+:::.....  
 .............X$&+$X$$xx;;+X&&$$x.;&$$XX+.......................:+$:+:+x$.;$&&&&&$X$$xX.......  
 .....++;;;;xx&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&x+++:...  
 .............................................................................................  
 .............................................................................................  
 .............................................................................................  
 .............................................................................................  
                                                                                                
''',
                    },
                'grasp of many' : {
                      'enemyhp' : 10,
                      'enemyatk'  : 2,
                      'enemyart' : '''
                                                                                                
 ;XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  
 ;XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  
 ;XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:x+ ::XXXXXXXXXXXXXXXXXXXXXXXXXXXXX  
 ;XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;;XXXXXXXXXXXXXXXXX+ X;;XX$XXXXXXXXXXXXXXXXXXXXXXXXXXXXX  
 ;XXXXXXXXXXXXXXXXXX+xxXXXXXXXXXXXXX.;X$XxXXXXXXXXXXXXXX :X$&$$$;XXXXXXXXXXXXXXXXXXXXXXXXXXXXX  
 ;XXXXXXXXXXXXXXXXX+$X$XXX;XXXXXXX+:+$&$X:$XXXXXXXXXXXX:+$&$$$+X$XXXXXXXXXX.Xx XXXXXXXXXXXXXXX  
 ;XXXXXXXXXXXXXXXXXXx:;:X$;XXXXXX;$;$$x+XXXXXXXXXXXXXx  ;$XXXXXXXXXXXXXXXXx:$x X:XXXXXXXXXXXXX  
 ;XXXXXXXXXXXXXXXXXXx  ;  :XXXXXX&&&&XXXxX;       +XX:  xXXXXXXXXXXXXXXX:XX.$:Xx$x$XXXXXXXXXXX  
 ;XXXXXXXXXXXXXXXXXX$+ :xxXXXXXXXX&xXXXXX         :  +X$$XXXXXXx. XXXXXX:+.;+;XX$XXXXXXXXXXXXX  
 ;XXXXXXXXXXXXXXXXXXXXX+;xXXXXXXXXX: :Xx;        : ;  .+XXXXXXXxXX+XXXXX$. .++x$XXXXXXXXXXXXXX  
 ;XXXXXXXXXXXXXXXXXXXXX; :XXXXXXXXXx.. ;X$. . +X: ;x     :XXXX :X$X$+XXXXX;xxX$$XXXXXXXXXXXXXX  
 ;XXXXXXXXXXXXxXXXXXXXXx.  XXXXXXXXX$Xx$X:++. :::+&&  . .  X+ +XX$$$$XXXXX XxX$XXXXXXXXXXXXXXX  
 ;XXXXXXXXXXxX$XXXXXXXXXx    XXXXXXx&&xX&+$$xX.&&X$...  .   X+$&&XXX$XXXXX .;X$XXXXXXXXXXXXXXX  
 ;XXXXXXXXXX$X$xXxxXXXXX$x:. .XXXXXX;XXX&&&&&&&&&X..:  .    ;&&$XXXXXXXXX  .XXXXXXXXXXXXXXXXXX  
 ;XXXXXXXXX++.:+$xXXXXXXXXX:    x+;;;$X&&XX&X$+&:+.  . .    :++XXXXXXXXx  :XXXXXXXXXXXXXXXXXXX  
 ;XXXXXXXXXXx x. xXXXXXXX$Xxx$    .::+XX&+$x;X.++.X+..       ..+XXXXXXx  :XxXXXXXXxx+XXXXXXXXX  
 ;XXXXXXXXXXxX$$XXXXX++++XX$&&XXX :..Xx$$$$XxXX      :; +  .    X;   :  :xXXXX;$X:$+&;XXXXXXXX  
 ;XXXXXXXXXXXx:;.XXX$&&&&&XX+&&&$x+X$$X;$x$$$: .       X+;++  x+;   ;x+++X$XXX.++.x$X&$XXXXXXX  
 :XXXXxxxxXXXXx  XXXXX$$&$X:XX$&&$$xx;+X$$XxX&$        ;$$x+;$xX$$&&&&&&$$XXXX:..+XX$XXXXXXXxX  
 :xxxxxxxxxxxxxx  ;XXXXXX&&+$$X;++:;;;++;; XX$X++;x&$;;xX$x$xX&&&&&&&XXxxxxxxxX+xX$$Xxxxxxxxxx  
 :xxxxxxxxxxxxxX+   xxXX$&$X;             XX&$:++. x$xX&;+$xxX&&&&$Xxxxxxxxxxx.;X$$xxxxxxxxxxx  
 :xxxxxxxxxxxxxxxX+.;  .+xx.        :  ;;:XX    $&;&X&$& .XX&&&.  :$+;x;;:X;  :xXXxxxxxxxxxxxx  
 :xxxxxxxxxxxxxxx$X$$$xX$X:.        :+;x;XX+;  x &&&X;:  : xx.    ;xXXxX   ;:X$xxxxxxxxxxxxxxx  
 :+++++++++++++xxxxXxX$$&x&x:  :;&+$+;;+.xxX&&&$+ +;:      +: ;xX$&&X&$$&+;$XX++++++++++++++++  
 .+++++++++++.x  x+++++xXxX&&X;;++;X+;.x xX&X$&&x  $X.     +x$$&&&&&&&&&x+x$++++++++++++++++++  
 .+++++++++++x&$X:;x+++x .;.&$$+x&&$x;. ;xX&&&&Xx+. XxX . x ;&&&&$&&&$x.+$&+++++++++++++++++++  
 .++++++++++.X&&$xx. :;xx$&&$&&&xXx+   :+XX$&&&$+x+.    + xX$XX$XXX$xX  ;x++;;;;;;;;;;+;;;;;;;  
 .;;;;;;;;;+xxx++x$X++&&&&&&&XXx+:+:    .XX$XX+;+;. +;   :;xx+&&$$$X:  ++;;;;;;;;;;;;;;;;;;;;;  
  ;;;;;;;;;;;;;;;;xx$&&&&&X&$$xxXx;      :+x          :+;:;     x;.  .x$x;;;;;;;;;;;;;;;;;;;;;  
  ;;;;;;;;;;;;;;;;;;;;;;+XxX$$$x.       ..  ;.       .  ;:++;  ; +;.:X&X$XX+:..::::::::::::::.  
  :::::::::::::::::::::xX$&$&X;   .              .+;..  ;Xx$X$$&&&&&$$&&$&X;:  .:+;;::::.::.    
  :::::::::::::::::;x::XXX$&x++:;.               ::.       $&&&$&$Xxx$&XX$X+X+.X&&$+;::::.      
  ...::.......  .:::::X&XXX&$XX$+::. . :;.          :+x: +;  &&&$$&&$&X+X$X;:+XX$&+x+.          
  .......... ..   ..xXX+$XXx++$&$xxx++xX&$x+::.:;;;;   :X$&$x..xX&&&&+XX$XX::::X xXX.           
  .........       :;x$X$&Xxxx:;x&XX$$x+xX$;:+$$::+xx$&$Xx+;;..$x$$&Xx$xX$&xx;   ..              
             :;. :x$X::.$XX&&X$+xX$&&&&&&&&&&$&&&&x ; xx$$$::.  ;x+Xx;X$$$$&X                   
            ;$&&x;X.  .+&&&.   :$+XX$$X$&&&$+xx;:x.+x+.   +X+;::+$x:+X$&&$$;                    
            x;X;x      X&+      +&$$xxx$$Xx++x++;x+x$       ;$$X;:+X$X&$$$x                     
             :;         :     .xX&&$$$XX$&$XXXX++XXX&x.      x$XX$X$&$$$&$$;                    
                       X.   .x$&&&&&$&&&&&&&&&$$$X$&&$$x+.    X&$$&$X&&&&$$$+..                 
                    .+X;Xx+xx&&&&&&&&&$$$$X$$$$&&&&$&&&&&+.  ;xX$$X&&$&&+x;&$Xx.                
                   :x$&&X&&&&$$&&X&&&&&&&&$$$$&$XX$$&$$$&$&$$&&&$X&$$&&$      $Xx;              
           :      .;+X+     .$&&&&&&&$&&&$&$&&&&&&&$XXX$&&&&&&&$&&&+   +&      +   +            
           :   :.:;+X$&&$&&&&$$$$&&&&$$&&&&&&&&&&&&$$$$&&&&&$&&&&&&$$&$$&&$ : :&X:.:            
      :xX$$&&&&&&&&&&&&&$xXx+++X$&$&&&&&&&&&&&&&&&&&&&&&&$XXx+:X&$X+  ;:  Xxx+x++;xxxx:;;.      
                     .:xxxX$$$$$$&&&&&&&&&&&&&&&&&&&&&&&$$x;..    :: .+                         
                                                     :;+++x$X.$$x.$X:                           
                                                             ..                                 
''',
                    },
                'half-born remnant' : {
                      'enemyhp' : 4,
                      'enemyatk'  : 3,
                      'enemyart' : '''
                                                                                        
                                                                                        
                                                                                        
                               xx                                                       
                              X$.      .                                                
                             ;$&      ..$                                               
                             :X&+:. ;..$+                                               
                              +&&&X&&x+X .;+;::::                                       
                               $&X:::&Xx; ..:      .                                    
                             .X&&&$XX:;:.xx&&.X+;$: ;                                   
                            X&&&&&&&&+&&Xx;;X&&&&&&$                                    
                            +&&&&&&xx&&&;+&+xx&&&&&x.                                   
                            $&&&&&&&&&&&&&.+. &&&&+ &;                                  
                            X&&$;&&&&&$$&X::X+.X$&+  .&+                                
                           .X&$   $&&&&+&X:x$x;&$X;    ;&:                              
                           x&&    .$&&&&&&&$&x;&XX:      $&;                            
                          x&&;      X&&$&&&&&$$X&x       .&&X.                          
                        +&&&&.         &&&&&&&&&&&         &&X;:                        
                       x&&&&;            :&&&&&&&;.          +$;x                       
                      ;&&&$             :$&&&$X&&.  &:         X;:                      
                     ;&&$              &&&$&X+x&&.:&&&x         ;;:                     
                    x&&               $&&&&&&$+&&$&&$$X:         ;x.                    
                   x&&                &&&&$$$$$&$&X&;..X          &.                    
                  x&;                x&&&&&&$$$$$$$x....:         X; ;                  
                 x&X                x&&&&&&&&&X$x&X&X....:       XxX::+                 
                X&&&              .X&&&&&X&&&&&$x&&&&:...:.      X. x:xX                
               X$&&&X            :$&&&&&&&&$&&X$$&&&&$....:      &   x&;&               
              $$&. x$           :&&&&&&&&&$&&$&X&&&$&&;....;         X&x                
             &&&   +$          .$&&&&&&&&&&$&&X&&&&X;&$...:+        +$$.                
             X&&               $&&&&&&$ :&&&&&&&&&X; :&&+..x                            
               $               &&&&&&    &&&&&&& &X    +&+..;                           
                              :&&&&&     &x X&&+ &+     +&..;$+                         
                              &&&&&&&x   &  +&   X+      X&&$+..;                       
                              :&&&&&&&X  x   $    +        &&&;:;                       
                                 :&&&&&x          ;        &&&&+:X                      
                  .                 ;&&&&x                  $&&&xX                      
               +  . +                 &&&&                    $&$x                      
                ;$ :x:               X&&$                      X&x.                     
                 $&&&++++++++++   : X&&$                        &&x                     
            ;+++++&&&&&&&&&&&&&&&$&&&&&&&&&&Xx:                 &$XX                    
                    .XXXX$&&&&&&&$$X&&&&&&&&&&&&&&$$$&+   .     &X+;;   ..              
                           ;+&&&&&&&&&&&&&&&&&&&&x+              &+::.  ;;;             
                    ++++++;.             $&&&&&&&&&&&&&&&&   ;+&&&+;::;&+;+             
                                                  ;;;X&&&&&&&&&&&&;$+X+xX&;             
                                                          ...   x&&:&X;&&&              
                                                                                        
''',
                    },
                'husk of knowing' : {
                      'enemyhp' : 5,
                      'enemyatk'  : 2,
                      'enemyart' : '''
                                                                                        
                                                          x                             
                                                        : .:                            
                            ::....:X+;::::::+.           $X.                            
                            .x+xXX;;X;+:::::::X.      .;x;:x:                           
                                  ..:&X+;:::;$&$:    xx&xXxx$+                          
                                     +x:;++&$$&&$   :;; &+&:.x .                        
                                     xx;;+&&&.$&$    . .x+;: ..                         
                                    +Xx+x&&+ X&&$       x&&.                            
                                   .+$$$$&&+:&&&$       :x:                             
                                 ;X::+++$&$&&&$&x       :x:                             
                                +++x&X;;XXx&&&$&$&:     :X.                             
                               &&$.;++$&X+;$&&$XX&&     ;&.                             
                               $xx$&x++x$&&$xxX$&&$     $&                              
                              .;::XX&&&$X&X$&&xX&&$.    $&.                      .      
                              $:::;X&&Xxx$:xx&x;&&X+  ;&&XX.                            
                             :;:::x&&xx++x::;+::&&$&&:$&++X.                            
                            +;:;+;XxX+x++&:::::;$&&&X&&&&$.                             
                           $xx+++&&.x&Xx+&+x;:::$&&$&&&&$;                              
                           $$$$&$X&.X&&&$XXx+;+$&&&$&&&xx:                              
                            x&X$&&x .&&&X&X$&XX&&x:&&&$;X:                              
                            :&&&$$  $$X$$&x&&&$X$&  $: ;X                               
                             &&&&; ;$X++xx&$$+XX$&+    ;X.                              
                             &&&&..&X+++Xx&$+;$+x&X    ;x                               
                             &&;+;:XX+++Xx&$+;X+x&X    $x                               
                            .X:;;:&X++++Xx$&;&&;+x&:   $X                               
                            .+$X &Xx+++++:;;:&&;++&X   &$                               
                             :$:+&X++;+&&&&&&&&&&&&x  .X$                               
                                x$X++;+x&$$&&&&&$&&x. .X$                               
                                xXx++++$$$X&&&$$$$&x. .X;                               
                               .$Xx++++$XXX&&&$XXX&X. ;x+                               
                               XXx+++++$XX&&&$XXXX&X: +X.                               
                              .$X++++++$XX&&&$$XXX&&+ +$.                               
                              xXX++++++&X&&&&$$XXX&&+ xx                                
                             :XXx+++++$&&&&&&&&$$$&&x.Xx                                
                             xXX+++++x&&&&&&&&&&&&&&X.$x                                
                            .$X++++++x&&&&&&&&&&&&&&X.$+                                
                            ;X&&$&&+xx&&&&&&&&&&&$&&X.$X                                
                             . &&&&+&$&X&; x&&&&+ ;$+.Xx                                
                               $&&&&:      ;&&$&.     X+                                
                               $$$&         $&&X     :X+                                
                              X$&&+         x&$&.    xx+                                
                             .&&$&;        .&&&&$.  XXX                                 
                             ;&$&&..;;;;;;;X&&&&&&X:X&X.                                
                       .;++++&+++$X+++++++++xxx$&$$$$$X+++++;.                          
                        .:;+x&$X$&x++++++++++++++++++++++++:                            
                                                                                        
'''
                    },
                'vessel of errant insight' : {
                      'enemyhp' : 7,
                      'enemyatk'  : 4,
                      'enemyart' : '''
                                                                                        
                                                                                        
                                         x. +                                           
                                       +      +                                         
                                      ;.       ..                                       
                                      x+&&&:    .                                       
                                      x&x&&x&  ..                                       
                                     :X&&&&&& +;;;.                                     
                                   .X$X$&&&&$Xx&x  $X                                   
                                 x+ x;.  $&+;.      :+$                                 
                                x$+   .+..:++.  .;X&XXXx                                
                               +++&&x;x..:.:;$$X$X++++$&X                               
                               $$X&xx$&+$X$X&&++&&xx&XxXXX                              
                               +$&&xxxxx$&$xxx$$X&&&&Xxxx.                              
                               &X$&xxxxX$$$Xxxx$&&&$xX&&&;                              
                               xx$&&xxxxXxXxxxXX$&&&Xxxxx                               
                              +XX$&&xxxx$X$Xxxx$&&&&$XXXxX                              
                             ;x$&&&&&XxxXxXX$$$&&&&&&&&Xxx.                             
                            .+XX$&&&XxxX&&$$XXXX$&&&&$XXX$$                             
                            ::+x&&&&$&&$X$XX&$$&&&&&&X;::;;                             
                            :;:+X$&&&&&&$XXXX&$X$&&&&x..:+X                             
                            +;+X&&&&&&&$$&&XX&&&$&&&&&+::;.                             
                            x;X&&&&&$$$&&$&$&&$$$$&&&&x.:;                              
                           .:x&&&&&xXxxxX.x$&&$xX&&&&&$;;:                              
                            ;;x&&&+xxxxxx&xxxxX&&&X&&+;:xx                              
                           ::+x&&&xxxxxX;&+xxxxxx$&&&++:+x                              
                           :;&x&&&xxxxxX;&$;xxxxxX$&x&&xX$                              
                            XX&&&XxxxxxX$&&xXxxxxX$$&&x$$X                              
                             x&&&Xxxxxxx&&&xXxxxxx$$&&&&&$.                             
                              &&&+xxxxx+&&&&;xxxxxX$$&&&&$:                             
                              &&&+xxxxx;&&&&;xxxxxX$$&&&&$x                             
                             .&&$xxxxxxX&&&&XXxxxxxx$&&&&$X.                            
                             ;&&Xxxxxx;&$&&&&;xxxxXXX$&&&$$;                            
                             X&&&XXXXX$&$&&&&&$$XxXX$&&&&$$+                            
                             X&&&&&&&&&&&&&&&&&&&&&&&&&&&$$$                            
                            .X&&&&&&&&&&&&&&&&&&&&&&&&&&&$$x;                           
                            :$&&&&&&&&&&&&&&&&&&&&&&$&&&&&&$X.                          
                            x$&&$&&&&&&&&&&&&& &&&&&$&&&&&&$$x                          
                            $$&  x&$&&&&&&&&&$  &&&&&&&&&&&$X+                          
                            .&x   .x$&&&&&&&x    &$xXX.&&&&$$.                          
                              x   .x$&&.         X&xXX  x&&X                            
                                  :$$&&           &$XX   +:                             
                                  &&&&&           &&$&.                                 
                                .xX$&&&:          &&$&+                                 
                             .xXX$&&&&&+          &xxX+                                 
                            ;&&&&&;              +$xxX&                                 
                                                  x$$x.                                 
                                                                                                                                                                                                                             
                                                                                                                                       
''',
                    },
    }

    bosses = {
                'the maw of gentle regret' : {
                      'enemyhp' : 45,
                      'enemyatk'  : 3,
                      'bosskey'  : 'tenon of many ends',
                      'bossdesc' : '''[italic]
stitched from ambition and error, this slithering mockery of heroism hungers for meaning.
it wears their armor, their limbs, their hopes - all rotting beneath the weight of shared failure.
so many came seeking purpose. together, they found something worse.

all who enter are remembered. none as themselves. purpose decays. but hunger persists.[/italic]''',
                      'bosskeydesc' : 'knotted bone and glimmering ash. it does not fit cleanly into any shape- but somehow, it belongs.',
                      'bossart' : '''
                                                                                ........                                               
                                                                          ;xx+;;::..........                                           
                                                                       ;$&Xx:..................                                        
                                                                      &&$x++++++++;:..   ..... ;                                       
                                                                  X$&&&&$X++xX$X$$x+;:.   ......:                                      
                                                                X$&&&&&&$$$$&&&&&&$x++::.. ......:                                     
                                                              .X&&&XXX$$&&&&&&&&&&$&X::...........                                     
                       ...                                 :;X&&&&x+::+X&&&&&&XX$&&&&&&&;.........:                                    
                    .+Xxx+;:;.;:. .::                    +$$&&&&&$+;;+&&&&&&&XX&$X$&&&&x&&+...::::.:                                   
                  :$X&&&&&&&&X;+++;:;                   x&&&$X&&&$+:;&&&&&&&&&&&+;;+&&;.:$&$:.;;....+                                  
                  +&&&  X&&&&$&&&&&+.;        XXxx;.x$;:&&&&&&$&&$+:;&&$&&&&&&&&&X:.:x&&&&&&&+Xx&&&&$          ;x+                     
                 x&&X .&&&&&&&&&&&&&x:..    &&&&&&&&&&&&&&&+x&&x&&x:;&&$&&&$&&&&&&&&&X..::;x+:.:$+++         :X$X+:;;;                 
                &&X  :&&&&&&&&&&&&&$$&$     &&&     x&&$&&&&X+X&&+$;+&$&&&&&&&&&&&&&&&&;:;+:x&$X&&$       :XX$&&&&&X&&Xx               
                .&x  .&&X   X$X&&&&&&&+.    &&&x :+$&&&&Xx+;;$&X&&+++X+&&&&&&&&&&&&&&XX;;::.::;+X&+    x&XX&&&&&&&&&&&&X;              
                  :.  &&x   ;  :&&&&&$:;     x&&$&&&&&&&&&&&x;;X++X.:X+&&&$$&&&&$&&&&x++++;;:..;&x    ;&&$$XX$&&&$&&$&&&$+             
                       &x        &&&&+;      :X&&&&&&&&&&&&&&&;;&+X..$x&&&+&X&X&&&&&&&&&XXx&&$+xX:    &&&&&&&&&x  +&&x +&&:            
                       :x        &&&$+;.:   &&&&&&&&&$x;+;+$&&&x;&$:.&+&&&+&+&&&&&&&&&$&&&+&&+x&$+   x&&&&&&&&&;  X&&:  &&;            
                       :x        ;&&$x.... ;&&Xx++X&&&X:x+::&&&&$+&+.&X&&$x&;&&&&&&&&&&&&&&&& ;&+X  +&&&&&& x&+   $x    X&:            
                       :x         &&&X+:...&&&&&&&&X+x&$+&$x;;X&&&X&;x&&&&X&:$&&&&&&&&&&&&&&; :$.: ;XX&&&&X x$    .     X              
                       .+         &&&$x;:..X++&&&&&&&&+X&&&+:..+&&&&$.&&&&xX+&&&&&&&&&&&&&&&. .;  :&xx&&&&. ++                         
                       .+        :&&&&X+:::x&+.:&xx$&$XxX&&X++x+&&&&&+:&&&&+&+X&&&&&&&&&&$$&+&&&XX&$xX&&&X  ++                         
                       .+       &&&&&&&&$$X$&$:. &&+:$&+X:&&XX&&+;;$&&;x&&&&$;X$&$&&&&&xXX+&;&&&&&&Xx$&&&+  ;+                         
                       ;.     x&&&+ X&&&&&&&&+....&&+&;:X;.X&&&&&&+$&&X.   &&$x$Xx&&&&$&xxX&;&&&&&$&&&&&X   ;+                         
                       .     ;&&&: .&&&&&&&&$Xx+++X&&x:..XX..&&&x&xX&&$+:::&&$$x&+&&&&&&$X$&;&&&&&&&&&&$    x+                         
                             +&&&  +&$&&&&&&&&&&&&$&&&$+$&&+..+&+Xx&&&&$Xx+&&&xx&$&&&&&&&x$&X&&&&&&$$&.;     .                         
                             .&&&x$&&&&&&&&&&&&&&&&&&+xXxX&&;:.$&$&&&&X&XXx&&&$x+$&&&&&&&x$x&&&&&    &                                 
            ;+;+x+;;+.:.       &&&&&&&&&&&&&&&&&&&&&&&&&&$X&$+;:$$&&&&&&&&&xx&&;&.$X$$Xx&$X$&&&&&$                                     
          X+X$$&&&&$X&X$$XX.   X&&$&&&&&&&&&&&&&&$$&Xx:+&&Xx&&Xxx&XX+x&&&&&&:;&$+Xxx;+X&&$+&&$&&&X.                       ;.+          
       +Xx$&&&&&&&&&&&x++xXxx +$&&&&&&&&&&&&x$XX&&$$x+++:...  .$&&&$&$&&x;x&$+&$&&+&&&&$&$Xx&$&&&$&&$.         ;$x+;;;:;xx$&&x+++      
       $&&& .$&&&&&&&$x$&&&&$$&&&&&&&&&&&&&&xx;x&&$X;...  ...::::.+&&$X$&x+&++$&x&$X&$.:&&+;&&&&&&&&&&$      .&$++;+&&&&&&&$x&&&$x     
      :&&x :&&&&$&&&&&&&&&&&XXxX&&&&&&&&&&&&x;:&&&&$x;:::..    .:;;:+&&$$&&x$;X&&&&X$X&$$&$&&&&&&&&&&&&;;;;+&&&&&&&&$&&&&&&&&;  $&x    
      x&$  :&&&     &X +&&&&$x++$&&$$&Xx&&&&x::&&&&&$x+;............:..;;x&&XX&&&&&$X&&xX&&&&&&x+&&&&&&&$xxX&&&&&&&&&&&&&X+&&&X   :;   
      X$   :&&x     &X .$X&&$$xx$&&&&&X$&&&&;:$&&&&&&&$x+;:................:..x&&&&&&$&&&&&;..:;+X&&$&&&$$&&&&&&XX&&&&$&&&  &&X        
       :.  .&&x     &X .X  &&&$&&&&&&&&&&&&&;;&&$XXX&&&&&$x+:.. ......  .....:+;:........+X;.:+x$&&&$&&&&&&&&&.   :x    &&X  &X        
           .x .     &X .x ;&&&&&&&&&&&&&&&&&x;&&XX++$x:. X&&Xx+;;;;;.  ..   ......::;+;:;+:+$&&$XXX$&&&&&&&.      .+    &&;  $X        
           .+       &x   ;&&&&&&&$+;&&&x$&&&$;$&&$x$$$x::$&&&X+X$&$$X+;::::.........:::++xx+;::;;;+X&&&&&;              &&;  $x        
                    &x   $&&&&&&&x+;$&&&&&&&&+;xx&&&$+X+$&&&&Xx+.X&&X;;+x;:;;;;::..:..;$&&&&&&&$$$X+++xX&$              &+   $x        
                 +;;&&x;;&&&&&&&$&$&&x$&&X&&&$;+:.;;$&&$&&&&&XXX+&&&;:..$&$XX$$$XxXX$&$+;;+X&&&&&&&Xxx+x$&$             X    Xx        
              +x;:X$&&&&&&&&&&&&$$&xX;;;;+&&&&$xX;.:.x&$;:X&$X&&$$&&&xX$$&&&$&&&$X$&&&&&&&&&&&&XX&$&x;;+$&$                  X+        
            ;x.+&&&&&&&&&&&&&&&&&&$X&&&&&&&&&&&&$X&;.:&x:x+:;;$&$&&&X+:x$&X;;+x;..........:;+xx;:+xxX&X+X&$     XXx+;;++               
           :$;;&:   $: X&&&&&&&&&&;x&$x+:;xX&&&&&&&&X+x&$++++;;:.;&&&&&&+&;:+:::..  .....:::::::+;:;xx&Xx&&&.$&XX$&&&$+:+:             
           &X;;+    $.  $&&&&&&&&&&$x;;xxxXX$&&&&&&&&&$$&&&$$$Xxx+;:....::;;.::........ .....   .:::+x&&X$&&&&&&&&&$XX&;;x:            
           &X+;;    $.  $&&&&&&&&&$XxxX$&&&&&&&&&&&&&&$$X$&&$XXxxxxx+;:...........................:;xx$&$&&&&&&&X     $:;+;            
           X&x;+        X&&&&&&&&&$$&&&&&&&&&&&&&&X&&&&&$x;;+&&&&&&&&&X++X;.::....................:+xx$&X&&&&&:       X.;+;            
           +$x+:+    .$&&&&&&&&&&&&&&&&&&&&&&$;::::+&&&&&$+::..x&&&&&&&&&&&;:x:..;+;:...........:+x+++$&X$&&&X      .x:;xx             
          X&Xxx+:.&&&&&&&&&&&&&&&&&&&&&&&&&&&:.x&&&&&XX&&&&x+;:...   .:&&&&&:;$;+:X+;:..........:++++$&&X&&&&X      x;;X$              
          &&x;+XX::&&&$:+&&&&&&&&&&&&&&&&&&&&+;$XxX&&&.:x&&&$X++;;;::::;x&&&+.+&X:;x++++++::::;+++xX$&&&&&&&&      X;+$&               
          &&x;+&&x:X    ;&&&&&&&&&&&&&&&$XXXXx;$+;+X&&$;+X&&&&&$XXXXxxxxxX&&$:;&&+;&Xx+++++++++++x$$$$&&&&&&&    x$+;+X&               
          &&&XX$&X;X    .&&&&&&&$&&&&&$x++++x$+$xxxX&&&x;$&&&&&&&&&&&$$XXX&&&+:&&xx&&&$Xx++++++x$&$$&&&&&&&&;   ;&x;;+$&               
          +&&&&&&$X&X+;xX&&&&&&&&&&&&$X+;. +xXXXXx$&&&;+&&&&&&&&&&&&&&&&&&&&&x:&&&$&&X&XXxxxxX$&&&&&&&&&&&&&+   $&+..x$&               
           ;&&&&&&$&&&&&&&&&&&&&&&&&&XX+:.+xxxxX$$&&&:x&&&&&&$X++$&&&&&&&&&&&X:&&X$$&&&&&$X&&&&&&&&&&&&&&&&&&&$&&$xxx$$X               
           :;   x+$&&&&&&&&&&&&&&&&&&XXxxxxxxxX$$$&&$.:&&&&$$X+;;x&&$$&&&&&&&X:$x&X&&&&&&&&&&&&X&&&&&&&&&&&&&&&&&$$$$&&X               
                  ;.   ;&&$&&&&&&&&$X+::...+XXX&&&&&&;;+&XXxx++++xX$X$&&&&&&&X;&&&&&&&$X&&&&&&&&&&&&&$&&&&&&&&&&&&&&&&X                
                     :&&&&&&&&&&&&&XXxxXxx+;+xX&&&&&&&$xXxxxxxx++xXXX$$&&&&&&x;$$$&&&&$$XXX$$&X$$$&&&&&&&&&&&&&&&&Xx+                  
                ;xx&&&&&&&&&&&&&&$XXXx+::;++xX&&&&&&&&&&&XXXXXXXXXXX$$X$&&&&&x;+X&&&X$$$$$$XxXx+xx&&&&&&&&&&&&&$x                      
          ;XX$$&&&&&&&&&&&&&&&&&&$x;:..:::xX$&&&&&&&$$&&&&&&&&&&&&&&$XX&&&&&&x;;&&&&&XXX$XX$&&&&&&&&&&&&&&&&&&&&&&&&$.                 
        +$&&&&&&&&&&&&&&&&&&$&&XXx;..;;+x+x&&&&&&&&&&&XXXXXx+++:+XX&&&&&&&&&&Xx+&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&xxx:           
     :+x&&&&&&&&&&&&&&&&&&$&$X+xx;:::+:+&$X&&&&&&&&&&X$&x;::....;x++X$&&&&&&&Xx+&&&&&&&&&$x&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$x;;:      
      ....:;+X$$$&&&X$$xxxX$xx+;;::::xX&&&&&&&&&&&&&&&X+x++;;::::.;X$$&&&&&&&xXx&&&&&&&&&$x&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$XXXx+        
          :;;;+XXx$&&X+x+Xx$&x:..:X$XX&&&&&&&&&&&&&&&&&X+:.....:+xX$$&&&&&&&&Xxx&&&&&&&&&$&&&&&&&&&&&&&&&&&&&&&&&&xxXXX+               
             +xxxX$&&&$$&$&&&&&&$XX&&&&&&&&&&&&&&&&&&&$$X;...;;....+&&&&&&&&&XXX&&&&&&&&&&&&&&&&&&&&XXXXXXXXXXXXXX+                    
           .+&&&&&&&&&&&&&&&X..X&&&&&&&&&&&&&$$$$$&&&$X+:..+;xx+;:;::+&&&&&&$+X$$&&&&$$$&&&&$XXXXX$$$Xxxx+:.;xxxxXxx+;;;;;;;           
           +xxx+++;xX$&&&&&&X;&&&&&&&&$$XXXXXXXXX$&&&&&&&X$x&$$&$X$&X&&&$$&&;+$&X+:;$&$XXXXXXXXXXXXXXXxXXXxxxxX;                       
                      .::;$&&&&&&XXXxxxxx+xxxXXXX&&&X;.+&&&&&&&&&&$;..X&$&Xx$&&&&&&&&&&&&XXXXXXXXXXXXXXXXXXXXXXxxxxx.                  
                           :;:            +XxxXX$&&&;:X&&&&&&&&&&&&&$;.&$$X&&$$XXXXXXXXXXXXXXXXXXx;                                    
                                 .::::::;;;:::+xXX&&$&&&&&&XX$$&&&&&&&X&$$XXXXXXx.                                                     
                                       .:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;                                                           
'''
                    },
                'lady vestige, the bound echo' : {
                      'enemyhp' : 45,
                      'enemyatk'  : 4,
                      'bosskey'  : 'tenon of unspoken shapes',
                      'bossdesc' : '''[italic]
once a seeker of escape through knowledge, she unmade herself word by word.
now bound in thought and thin as parchment, she whispers truths no mind should carry.
she read until there was no more ‘she’ left to read.

she sought the way out, and became the door. in knowing everything, she forgot what she was.[/italic]''',
                      'bosskeydesc' : 'carved with symbols that shift when not observed. cold to the touch, yet burns with withheld meaning.',
                      'bossart' : '''
...................................................................................................................................   
 ++++++++++++++++++++++++++++++++++++++++++++++++++++;;;;;;;;;;;;+x$Xx+++++++++++;;;;;;+++++;;;;;;++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++++++;;;;;;;;;;;xX+XX   ;X++++++++;;;;;;++++++;;;;;++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++++++++;;;;;;;+XX$$$$.    :x++++++++++++++++++++++;++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++++++++;;;;;;++&x$&&&&x  .;++++++++++++++++++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++++++++;;;;;;;+&X&&$XXX&x::++++++++++++++++++++++++++++++++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++++++++++++++++++++;;;;;;;++$&&&&&x&&&&:++++++++++;;;;++++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++++++;;;;;;;;+X&&&X+:$:;x&+;x++++++++++++++++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++++++;;;+++;;x$$&&&&  .&&&;+;x+++++++++++++++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++++++;;++++++X&$&&&&$:X&&&;;;++++++++++++++++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++++++;;;;;++$X&$&&&&&&&&&&;;: X++++++++++++++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++++++;++;;xx&&&&$&&&&&&&&&.++;;+X+++++++++++++;++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++++++;+++&+X&&&&&&&&&&&&&$XX$X;.XX+++++++++++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++;;++++++++;;Xx&&&&&&&&&&&&&&&XX&+X:x   ;x+++++++++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++;;;;;;;+++++++X&&&&&&&&&&&$&$X$Xxx..    . &+++++++++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++;;;++++++++$&&&&&&&&&&&&&&$+;:.....   X+++++++++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++;;;+++++++xx&&&&&&&&&&&&$Xxx+xx:   ;  :x+++++++++;++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++;++++;++++;;;;;;;;+X+$&&&&&&&&$$&$xx++:   +:  .. x+++++++++;++++++++++++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++++++++++;;;;+++;;+$x&&&&&&&$&&&&+&&&$X$x++x+.    ++++++++++++++++++++++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++++++++++;;;++++;+Xx$&&&&&&&&&&&&&&&$xX&&&&&&&$x;xxx++++++++++++++++++++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++++++++++++++++++x&&&&&&&&&&&&&&&&&&&&$X$Xx+;:.. ..+x+++++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++++xX&&&&&&&&&&&&&&&&&&&&&&&X;..;;:..  ++++++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++++&&&&&&&&&&&&&&&&&&&&&&&&&&&&$:  .+xXxxx+++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++xxx&&&&&&&&&&&&&&&&$&&&&&&$&&&&&&&x;;;:::&+++++++++++++;;+++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++++++++++++++X$&&&&&&&&&&&&&&&&&&&$&&&&&&&&&&&&&&&Xxx;.xXx++++++++++++++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++++++++;++++x&&&&&&$$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$x+::;:XX+++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++$&&&&X&&&&&&&&&&&&&&$$xxX$&&&&&&&&&&&&&&XXx:;;X+++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++;+;;;+++xXxx$&$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$xX;&::X+++++++++++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++;;;;;;+++&++&&&$&&&&&&&&&&&&&&&&&+x&$X$&&&&&&&&&&&&&&X$&&+;$x++++++++++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++;;;;++;+++X$X$&&&&&&&&&&&&&&&&&$$$$XxXX&&&xX&&&&&&&&&&&$x&&&x .x+++++++++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++;;++;++XX:+&&&&&&&&&&&&&&&&&&&&&X&&$XXXxx$&&&&&&&&&&&$$&&&&$+;X++++++++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++;++++x&+.$&&&&&&&&&&&&&&&&&&&&&XXxx++xXXx&&&&&&&&&&&&$&&&&&&&;;X+++++++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++++++X$. X&&&&&&&&&&&&&&&&&X&&&$XxxXxx+;+$$x&&&&&&&&&&$&&&&&&&&; x$+++++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++++XX:   x&&&&&&&&&&&&&&&&$++&&$+X+...++&&;+&&&&&&&&&&$&&&&&&&$.  Xx++++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++X+x.:;+;;&&&&&&&&&&&&&$&$&x.$&$X.;xxx$&$+.;;&&&&&&&&&$&&&&&&&$. . ;Xx++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++xxX:X&&Xx$X&&&&&&&&&&&&&$&$$+.+&$xX..;xXx;..;:&&&&&&&&&&&&&&&&&$:&&X;.xX+++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++XX+X&&$++X;&&&&&&&&&&&&&$$&$$+.:$&x:x. ... .+..&&&&&&&&&&&&&&&&&&;++&&&.&+x+++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++;;++x&&$&&+++++&&&&&&&&&&&&&&$$&$X+..x$&;.+:........$&&&&&&&&&&&&&&&&&&x++$&$x&Xx++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++X&$X&x+++++&&&&&&&&&&&&&&$$$xX+..:x&$::;... .. .+&&&&&&&&&&&&&&&&&Xx++xX;$$&x++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++x&$+x+++++&&&&&&&&&&&&&&&$$xX;...;x&+.:.   .. .+$&&&&&&&&&&&&&&&&x++++X$X&$+++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++xX++++++&&&&&&&&&&&&&&&$$xX;..::;$$;......  .;$&&&&&&&&&&&&&&&&x;+++x+XX++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++;+++&&&&&&&&&&&&&&&$XxX;..+::$$X:. .    .;$&&&&&&&&&&&&&&&&x+++++++++++++++++;++++++++++++++++;  
 ++++++++++++++++++++++++++++++;;;+;;;;+++&&&&&&&&&&&&&&&$XxX;..x:.X$$;;.  .. .;X&&&&&&&&&&&&&&&&x++++++++;;+++++++;;+++++++++++++++;  
 ++++++++++++++++++++++++++++++++++;+;;++&&&&&&&&&&&&&&&&$XxXx..X;.x$$;:;. .. .+X$&&&&&&&&&&&&&&&x+++++;;;;+++++;+++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++;;;;+++&&&&&&&&&&&&&&&&$Xx$X;.X+.+$$x.;+;.. .+x$&&&&&&&&&&&&&&&x+++;++;;;;;+++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++;;;;;;;++x&&&&&&&&&&&&&&&&&XX&&&$&&++&$&;.;+;. .+x$&&&&&&&&&&&&$&&x++++++;;;;;+++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++;;;;;;+++&&&&&&&&&&&&&&&&&&&&&&&&&x;&&&X:.++...;+$&&&&&&&&&&&&x&&X+++++++;;;;+++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++;;;;;+++x&&&&&&&&&&&&&&&&&&&&$&&&&$X&&&$;.++..::;X&&&&&&&&&&&&x&&&+++++++;;;;+++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++;;;;;+++X&x&&&X&&&&&&&&&&&&&&$+x&&&&&&&&x.X+..;::x&&&&&&&&&&&$x&&&++++++;;;;;+++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++;;+++x&x&&&x&&&&&&&&&&&&&&; :&&&&&&&&x.X+..+X+x&&&&&&&&&&&++X&&++++++;;;;;+++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++;;;++x&x&&x+&&&&&&&&&&&&&&$:$&&&&&&&&x.X+x;Xx+x&&&&&&&&&&&+++&&++++++;;++;+++++++;;;+++++++++++++;  
 ++++++++++++++++++++++++++++++++++;;;++x++&&x+&X&&&&&&&&&&&&&$&&&&&&&&&&.xX&+&$Xx$&&&&&&&&&&+++&&++++++;;++;;++++++;;;+++++++++++++;  
 +++++++++++++++++++++++++++++++++++;++++++&$++&+&&&&&&&&&&&&&$&&&&&&&&&&;X&&;&&&&X&&&&&&&$&$++x&$++++++++;;;+++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++++++++++&$++$+X&&&&&&&&&&&$$$&&&&&&&&$+&&&X&&&&X&&&&&&&x&x++x&$++++++++++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++++++++++&x++++x&&&&&&&&&&&$X$&&&&&&&&&x&&&X&&&&$&&&&&$&x&x++x&X++++++;;++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++++++++++X+++++x&&x&&&&&&&&$..$&&&&&&&&&&&&$&&&&$&&&&&$X+&x+;x&x++++++;;;;;+++++;+++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++;++++X++;++x&&x&&&&&&&&$..x$&$&&&&&&&&&&&&&&&&&&&&&++&x+;x&x;;++++;;;;;+++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++++;;;+++X++;+++&&+&$&&&X&&$..xX&X&&&&&&&&&&&&&&&&&&&&&++X++;x&x+;++++;+++++++++++++++++++++++++++;  
 ++++++++++++++++++++++++++++++++++++++++++x++;+++$X+&$&&&xX&$..xXxx&&&&&&&&&&&&&&&&&&&$++;+++++X+++++++;;;;;+++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++;;;;+++x++++&++x&&:.xx++$&&&&&&&&&&&&&&X&&$X++;;;;++X++;+++;;;++;+++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++;;;++++;;+++++++x+++&&:.x+++x&&&&x&$x&x$$+$+&&Xx++++;++++++++;;;;;;;;+++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++;;;++++++;;;;+++x+++X&X:x+++x&&&$xx++$+Xx+X+&&++++++;;+++++;;;;;;;;;++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++;;++++++++;;;;+++++++&X;x+++x&&&x++++x+x++++x++++;;;;;++++++;;;;++++++;+++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++;;++x++++;++;;+++;+++&$;x+++X&&x++++;++++;++++++;;;;;;++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++;;++++X++++;;;;;+;;++&$;;x+x&&$+++++++;;;+++++++;+++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++;;;;+++&++++;++++;;++&$x:++&&&$+++++++++++++++;;++++++++++++++++++++++++++++++++++++++++++++;  
 +++++++++++++++++++++++++++++++++++++++++++++++x$Xx+++++++++$&x;++&&&$+++++++;;++++++++++++++++++++++++++++++++++++++++++++++++++++;  
 ;;++;;+++++++++++++++++++++++++++++;+++++++++++++xX&&&&x++++X&:.+X&&&$++++++++++++++++++++xXXxXxxx++;;;++;;+++++;++++++++++++++++++;  
 ;;;+;;;;;++++++++++++++++++++++++++++++xxxX$$$&$x++X&&&&&$++&X..+&&&&&++++++++++++++++x&&Xx+++++++++++++++++++++++++++++++++++++;;;;  
 ;;;;;;++++++++++++++++xxxxxxxxxxxxxXX$&&&&&&&&&&&&&&&&&&&&&&X; :$&&&&&&&&&&&&&&&&&&&&&&&&&&&&$XXxXXXXxxxxxxxxx+++++++++++++++++++;;:  
 ;;;;;+++++xXXXX$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&X:+.+&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XXXXXx++++++;;;:  
 ;;;;;;++++++++++++++++++++++;+++++++++++++++++xXXXXXXXXXXX$$$$X$$$$$$$$Xxxx++++++++++++++++++++++++++++++++++++++++++++++++++++;;;;:  
 ...................................................................................................................................  
''',
                    },
                'the choir of one' : {
                      'enemyhp' : 50,
                      'enemyatk'  : 4,
                      'bosskey'  : 'tenon of hollow praise',
                      'bossdesc' : '''[italic]
a broken cleric who sang to silence until silence sang back.
now a choir of mouths and madness, it praises a god that answers only in echoes.
there were no others to join the hymn. so, it made them.

sing loud enough, and the silence will sing back.[/italic]''',
                      'bosskeydesc' : 'pale and resonant, it hums faintly with voices not your own. some still believe it is listening.',
                      'bossart' : '''
  .................................................................................................................................... 
 .++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 .++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 .+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++xxxx+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 .++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++xx+....:+xx+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 .++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++XX;         ;X++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 .++++++++++++++++++++++++++++x++++++++++x+++++++++++++++++++X$x            Xx++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 .++++++++++++++++++++++++++++++++++++++++++++++++++++++++++x$x+;:        .: $++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 .++++++++++++++++++++++++++++++++++++++++++++++++++++++++++X&X&&&&;    :: : $++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 .++++++++++++++++++++++++++++++++++++++++++++++++++++++++++$&&&&&&&&$.  :.. +x+++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 .++++++++++++++++++++++++++++++++++++++++++++++++++++++++++$&&&&&&&&&&x .; ;.xx++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 .++++++++++++++++++++++++++++++++++++++++++++++++++++++++++$&&&&&x&&&&& .x ::;Xx+++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 .++++++++++++++++++++++++++++++++++++++++++++++++++++++++++$&&&&x&$;x$&X:x :x;.;&x+++++++++++++++++++++++++++++++++++++++++++++++++++ 
 .+++++++++++++++++++++++++++++++++++++++++++++++++++++++x&&&&&&&&xx$&&&X;X.$X:+ &x+Xx++++++++++++++++++++++++++++++++++++++++++++++++ 
 .++++++++++++++++++++++++++++++++++++++++++++++++++++++$&&&&&&&&&&&&+x&:$$& x; &  .;$x+++++++++++++++++++++++++++++++++++++++++++++++ 
 .+++++++++++++++++++++++++++++++++++++++++++++++++++xx&&&&&&&&&&&&&$&&&&&X+;.$X . ;xX:+x+++++++++++++++++++++++++++++++++++++++++++++ 
 .+++++++++++++++++++++++++++++++++++++++++++++++++++$&&&&&&&&&&&&&&&&$&&X; :+::.;x&xx;;;X++++++++++++++++++++++++++++++++++++++++++++ 
 .;;;;;;;;;+;;;;;;;;;;+;;;;;;;;;;;;;;;;;;;;;;++;;;;++&&&&&&&&&&&&&&&&&&$+.;; .:;X$&X::&XxX+;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
 .;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+&&&&&&&&&&&&&&&&x:XX.+X+;&&&;.;&X+++;x+;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
 .;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;$&&&&&&&&&&&&&&&&&.:x::+$&&+;X&&X+++xx$x;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;&&&&&&&&&&&&&&&&&$X$$X&&&&$&$XX$$XX$&&&+;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;&&&&&&&&&&&&&&&&&&&&&&&&&&XX$X&&&&&X;xX;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;x$&&&&&&&&&&&&&&&&&&&&&$&&$Xx+&x&&$x;:::x;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;$&&&&&&&&&&&&&&&&&&$$&&$&X&xXXx+&&xx::+&&+;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;x&&&&&&&&&&&&&&&&&&$$&&;.&.+Xxx+&&xx+$&&&X;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;$&&&&&&&&&&X&X$$&$$X$&&+.&.+Xxx+$&+&&&&&&X;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;x&&&&&&&&&$X;x;&&+;XX$&&&$XX$X&xx&&&&&&&Xx&+;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;$&&&&&&&&&&&x&&&+xXx.&&&$XX&X&&&X&&&&&&&&X+x;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+&&&&&&&&&&&&&&$&:.;.;$$&$X&&&&&&&&&&&&&&X;..++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;&&&&&&&&&&&&&&&&&&&X&$&&&&&&&&&&&&&&&&&&&Xxxx$x;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&x&&&&&&&&&&&x;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;x&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$&&&&&&&$XxXX;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::: 
  :::::::;;::::;::::::::::::::::::::;;::::::::;X&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&+$&&&&&&&&&$;;;;;::::::::;;;;;;;::::;;;::::::::::: 
  ::::::;;;;;:::::::::::::::::::::;;;;:::::::::$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&+;&&&&&&&&$X;::::::::::::;;;;;;;;::::::::::::::::: 
  :::::::::::::::::::::::::::::::::::::::::::::&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$;;&&&&&&$&x:::::::::::::::::::::::::::::::::::::: 
  ::::::::::::::::::::::::::::::::::::::::::::+&&&&&&&&x$&&&&&&&&&&&$$$&::..&&&X$&&&&+;+&&&&&&&x:::::::::::::::::::::::::::::::::::::: 
  ::::::::::::::::::::::::::::::::::::::::::::X&&&&&&&;x&&&&&&&&&&&$$&&&:&&x;&&XX&&&&X:;X&&&&&$x:::::::::::::::::::::::::::::::::::::: 
  :::::::::::::::::::::::::::::::::::::::::::+&&&&&&&+;&&$$x&&&&&xx$$&&&xx+:&&&XX$&&&&::x&&&&&&X:::::::::::::::::::::::::::::::::::::: 
  :::::::::::::::::::::::::::::::::::::::::::x&&&&&&&;+&X$&X;$&&:+&;+&$&&&&&&&&X&x&&&&+:x&&&&&&x:::::::::::::::::::::::::::::::::::::: 
  :::::::::::::::::::::::::::::::::::::::::::x&&&&&&&;$&;&&&xx&x&&&&x&$$$&&&&x$$&+&&&&&;&&&&&&&X:::::::::::::::::::::::::::::::::::::: 
  ..........................................:x&&&&&&X;&&xx$;+&&$::$::&$$&&&+$&;;&+&$&$&&&&&&&&&x:::................................... 
  ..........................................:x&&&&&&;x&&&&&&&&&&&&X&&$xxx&&+x$;.$$&X$&&&&&&&&&&x:..................................... 
  ...........................................x&&&&$&+$&&&&&&&&&&&&&&&$xX&&&&&XxX$&&XX&&&$:&&&&&x:..................................... 
  ............................................$&&&::.$&&&&&&&&&$$&&$&$xxX&&$&;xXX$&XX&&&&.$&&&X:...................................... 
  ............................................;$&&$x.$&&&&&&&&&XxX&X$&&$&&&$&$XXX$&XX&&&X$&&&&:..................................      
  ..............................................X&&&+$&&&&&&&&$XxX&Xx&&&&&&$$XxxxX&XX&&&&&&&x.....................................     
                   ...................         ....:&&&&&&&&&&&&X$&Xx&&&&&&$X::;;;XXxx&&&&:..     ...............................      
                                                   :$&&&&&&&&$&&$$&xx$&&&&&$$::;;;;xxx&&&&;                                            
                                                   +$&&&&&&&&&$XX$&&x&&&&&$$X::;;;:x+xx&&&&.                                           
                                                  .+&&&&&&&&&&$XX&&&&&&&&&$$+::;+::;++x&&&&.                                           
                                                  :&&&&$XXX&&$XxX&&&&&&&&&$$+::;;:::;+X$&&X+                                           
                                                  ;&&&XXXXX&$XXX$&X&&&&&&&&$x::;;;:.;;&X&&$&                                           
                                                  ;&&&$$X$$&$XXX&$$&&&&&&&&$X;;;++;:;;X&&&$$.                                          
                                                  x&&&$$$&&&&$$X&$X$&&&&&&&$&;;;+++:;;;&&&$X;                                          
                                                 :&&&&$&$$&&&$$X&$XX$$&&&&&&&+;+++x+;;;X&&$$&                                          
                                                 ;&&&&&&&&&&&$$X&$$XX$X&&&&&&+++++X&++x$X&&$$                                          
                                                 ;&&&&&&&&&&&$$&&$XXX$X&&&&&&++++x$&xxxX$&&$x+                                         
                                                .&&&&&&&&&&&&&$&$$XXXXX&&&&&&$XxX+xXxxxxX&&$$x.                                        
                                                &X&&&&&&&&&&&&$&&&$XXXXX&&&&&&$&&&X$$xxX$&&&$$+                                        
                                                &&&&&&&&&&&&&$&&&&$X&XXX$&&&&&&&&&&$&&&&&&&&&X+.                                       
                                      .+       x&&&&&&&&&&&&&$&&&&$X&XXXXX$&&&&&&&&&&&&&&&&&&&&x             ;:                        
                                      .$.     .&&&&&&&&&&&&&&&&&&&$X$XXXX&&&&&&&&&&&&&&&&&&&&&&$$           ::                         
                   .            ;      ;+;   ;&&&&&&&&&&&&&&&&&&&&$&&$$$&&&&&&&&&&&&&&&&&&&&&&&&$&;        :; .                        
                   ..         .;.     x.;$X;&&&&&&&&&&&&&&&&&&&$&&$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$xxx+: x&.;.     ;. ;               
                    +X ::  ..$+X;.....;&&&&&&&&&&&&&$XXXXX$&&$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$$$$$Xx.   ;;$::                
           ;&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&X$&&&&&&&&&&&&&&&&&&&&&&&&&$&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$$$&&&&&&&&&&&$         
         .......&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&X$&&X&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$+;;;;;;:     
                        .xXXXXXXXXX$&&&$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&X$xx&$$XXXXXXx++++;:             
                             ;;;;;+x+:  .          ....XXXXX+++++++;+xxxxxxxx$&&.    . :.:++XX;     ..     +x+;;                       
                                             ++xxxxx+++:        &X$$+::::::::::;:::::::         +$$;                                   
                                                                                                                                       
''',
                    },
                'ser ulthric, burdened of names' : {
                      'enemyhp' : 50,
                      'enemyatk'  : 5,
                      'bosskey'  : 'tenon of broken oaths',
                      'bossdesc' : '''[italic]
once a proud champion entombed by his own honours, ulthric was left to rot in chains he forged with valour.
now, a beast of instinct, he swings in defiance of a past no longer his.
they built walls to keep him safe. or was it to keep him in?

chains may break. but the burden remains. he remembers only the oath. not who he swore it to.[/italic]''',
                      'bosskeydesc' : 'a heavy shard of forged steel, stained and splintered. it bears the weight of forgotten vows.',
                      'bossart' : '''
.......................................................................................................................................
.......................................................................................................................................
..............................................................;X$xXx+..................................................................
............................................................+$$$+x++xxx................................................................
...........................................................X$$XX;x;;+xXX:..............................................................
..........................................................+$$XXX;x;;xXXX+..........;+..................................................
..........................................................X&$XXXxX+++XXXx:......;xX$$:.................................................
..................................................;xxxx...X$$XXX+Xx++XXX$;.....xx$$$$$.................................................
.................................................Xx$&&$+..X$$&&XxXX&$xXX$X;...;+XX$XXXXx:..............................................
..............................................;X$+$&&&&&XX&$$&&XX$$$xXX$$XX&X$xXXXxxxxXXXXx:..........................................:
...........................................;X$$$$x&&&&$$$&&&$$$$$&$$xXX$$$XX$XXXXxx+xxxxxxXXX;........................................:
.........................................;X$$$$&$+X$$$&$$$&&&&&$&&$XX$$$Xx$$$xXXx++::;;;;;+XXXx:......................................:
.......................................:x$$$$$$&&xx$$$&&$$Xx$&&&&&$$XxxX$$$&XxXXxx+++;:::;+xxxXX:.....................................:
......................................:X$$$$XX$$&Xx$$$&$&&$$$XxxxxxXX$$$$$$&x$XXxxxxx+++++xxxXXXX.....................................:
......................................x$$$$$XXX$&$XX$$&&$$$&$$$XXX$$X$$XX$X&+xXXxxxxxxxXxxxXXx+++xX:..................................:
...................................:;x$$$$$XXXXX&&$$$$$&&$$$$$XXXXXXXXX$$$$&$X+XXxxXXxxXx+xX$$$&&&&x..................................:
...................................:$$$$XXXX$X$XX$$$&$X$$&$XX$$$XXXX$$XXXXX$X$$X+xXXx+x$&&&&&&&&$+;...................................:
.....................................:++X&$XXX$$X$$$$$$$X$$&$XXXXXXXXXX$x++xXX$&&$$$$$&$XXX$$$$&;.....................................:
........................................+$$&&$$$&&$$$$$$$$XX$&&$&$XxX$Xxx+++++x&$&&&&&&&$xXXXXXXx.....................................:
.......................................;$$$&&&$$$&$$$XXXX$$$XXXXXX$Xxx++++xXxxX$&$&&$$$&$$$$$$&&X.....................................:
........................................:X&&$&&$&&$$$$XXXXXX$$$$XxxxxxxxxxxxxX$X$&&$$$X$XX$$$X$$X.....................................:
.......................................:X&$$$$$$&&$$$$$XXXXX$$$$$$$XxxxxxxxX$$$XX$&&&&&$XXXX$$$$$:....................................:
........................................+$$XX$$$&&$$&&$$$$$$XXXXXXXXXX$$$$XXXX$$$$&&&&&X$$$XXXXXXX:..:;...............................:
.......................................:$&&$$&$&&&&$$$$$$$XX$$$$$$$XXxxXXXXXXXX$$$&&xX$&$XXXX$$$X$X+:+Xx:.............................:
...................................:x;:X$$$$XX$&&&$xX$&$$&$$$XXXXXXXXX$$$XXXXX$$$&$;..x&$$$$$$$$$$$&XXXXX;............................:
..................................+$$$x&$$$$X$$&&&x.;X$&&$$$XXXXXXXXXXXXXX$&&$$$&&+....x&$$&&&$$$X$XXXXXX;............................:
.................................;$X$&&$&$$$&$&&$:....$&&$$$XXXXXXXXXXXXX$$XXX$$$.......;$$$$$$X$xXxxxXxX+............................:
................................;$$$X$$&$$$&&$&$;....;$&$$$$$$XXXXXXXXXXX$$$$$$&X;.......:$&$$$$$$Xx+xxXXx:...........................:
...............................:$$X$XX$$$$$$&&$;....;$$$$&&$$$$XXxXXxXX$$$&$$$$$$&X:.....:$&$XXXX&XxxxXXXX;...........................:
...............................x$XXXx$$X$$$$$$x.....+$$$$$$$$X$$$$XxX$XX$$XXXX$$X$$:.....;$$$$$$$$$xxxxXX$;...........................:
..............................:X$XXX$X$$$$X$&&&;....X&$X$$$&&$$$$$X$$&&$$$XXxX$$X$$+......x&&&$$$$&$xxxXX$;...........................:
..............................:XXXX$$$$$$$$&&X:..;:x&&&$X$$$x$XX$$$XXXXXXX$XX$$&&&X........x&&$$&XX$$xxXX$;...........................:
..............................+$XXX$$$$$$&&&X:...++$$&&$$&&$&XxX$Xx$&$&&&$XXxxXXXX$x:.......:$&&&X$$$xxxXX+...........................:
.............................:X$XX$$$$$$&$X:.....X$$$$&$X$Xx$$&$$$X$$X$&$XXXXXXXXXX$$&........+$&$$$$XxxxXX:..........................:
............................:X$$XX$$XX$&X:......+&$$$$&$$$XXxX&XxxxX$$$&$$XXXX$$$$$$$$.........;$&$$$XXxxXXX:.........................:
...........................;X$$$XXXX$&$+.......x$$$&$$X$$&$X$XXXXX$XX$$$$$$$$XxxxX$$$$..........:&$$$xXXXX$XX.........................:
...........................x$$X$$$XX$$:........X$$&$$$$$$&Xxx$XXXxxx+X$$&XXXXxx+xxxXX$;.........:&$XX$$$XxX+:.........................:
...........................x$$$XX$X$$$:.......+$$$$$$$$X&&XxXxxxxxx++x$X$$XXXxx++XXxXX&........;$$$$$&xXXXX$X.........................:
..........................:$$$Xx$$$XXXx:.....:x$$$$$$X$X&&Xx+x++xx++x+XX$&xXXxx++++xXX$+......:xXXX$$$XxXXxXX;........................:
..........................:$$$Xx&$$XXXXx:....;x$$&$$$X$$$$$+++x+x+++x++X$$XXXXxx++xXXXX$:....:xXXXX$$$$xX$XXX;........................:
..........................:$$$Xx$$$$$XX$x:...;$$$$$$$$X&$&$+++x++;+x+++X&$$Xxxxx+xxX$$$$x....;$$$$$&$$&xXX$$$;........................:
...........................X$$X$$$X:X$Xxx:....+$&&&$$$X&$&$+++xx+++++xxx&&&$$$$$XXXXX$$$:....+$XX&;:X$$XxXX$;.........................:
...........................x$&$XXX+:.XXx;.....x$&$$X$$$&&&$++x+xx;;;+++x&&&$X$$XxxxxXXXX......+xX:;:x$$X$&$$:.........................:
...........................:X$$XXX&$xxxxXX:..:x$&$$X$$X&&&$x+x+xx++;;;;X&&$&xXXX$$xxXXX$x..:XxX+X&&&&$XXX$$:..........................:
...........................;x;x$X$$$$$X..;x++xX$&$$$$X&&&&$x+x+xxx;;;;+X&$&&$xXXXXXX$$$$XXXXx:..x$$$$$XXXXx:..........................:
...........................;x:.+$$$$$+.....:+X$$&$$$$x&&&&$Xx$++xx+++;&X&&&$$xXXXXXXXX$X$+......:x$$$$&X+xX:..........................:
...........................;x;...:xXxx;......;$$&$$$Xx&&&&$x$$x++x+Xx+&$&&&$&XxXXXXXX$$X:......+X+x&Xx:.:xX:..........................:
...........................;X:....+x;+x......+x::&&$$$&&&&$$&$xx;++$x+&$&&$$&&&$XxxxX$$.......;X;.;$+....++...........................:
...........................;x;....;+.:Xx....;$+:$&$&&&&&&&&&&$x$$;x&X+&&&&&$&$XXXxxxxXXX:....+$x...;:...:x+...........................:
...........................;X:....+x:.:X;...;X;X$$$$$$$$&&&&&$x$&+x&$x$&&&&&&$$Xx+++xXXXx:;XX+:...:X;...:x+...........................:
...........................;X;....+x...+x;.:X+.+$&&&&&&&&&&&&$x$&+x&$x&&&&&$$$&$Xx+xxXXXX++:.......+;...:x+...........................:
...........................;x:....;X:...+X;.X:.+$&&&&&&&&&&&&$x$&xX&&x&&&&&&&$&&$XXXXXX$$x:.......:x+...:x+...........................:
...........................;x:....:x:.....X+x..:$&&&&&&&&&&&&&X$&x&&&X&&&&$X&$&&$$XXX$&$$+........:X+....x;...........................:
...........................;x;....;X:.....:$xx;.x$&&&&$$&&&&&&$$&x&&&&&&&&;:$&&$$&&&$$$$$$x.......:X:...:x;...........................:
...........................;X;....:+:....:x$..:+X&$$$&&&&&&&&&&&&X&&&&&;&&;.&$&&&&&&$$$$XXX:......:x+...:x;...........................:
...........................;x+....;X:....:x.....X$&&&&&&&&&&&&&&&&&&&xx:&x.;$&&&$$$&&$XXXXx:......:x:...:x;...........................:
...........................:+;....:;......:.....X$&&&&&&&&&&&&&&&&&&X:x:$;.x$&&&&$$$XXX$$&;.......:X+...:x;...........................:
............................++:...+x:....:+......x&$$&$$&&&&$+$&&&&X;.+:X:..:&&$$$$$$$XX$$:.......;x:...;$;...........................:
............................:x:..:x:......+......;$&&&$&&&&&;;$$&&X:..+:x....x&&&&$$$$$$$x........X+;...:+:...........................:
.............................;xX+$+....;:........:&&$&&&&&&:.;x+$&x...+.......:$&&$$$$$$$+........:;....:X;...........................:
.................................................;&&&&$&&&$...::$&X...+........;$&$$$$$$$X:.......Xx....:X;...........................:
................................................:&&&&&&&&$:.....;&X.............X&$$$$$$$+........x;....:X;...........................:
...............................................;$$$&$$&&&&X......$X.............+&&$$$XX$x:......:X;....:x;...........................:
..............................................+$$$&&&&$&&&x......$+.............:$$$$XXXXXX:.....:x;....:X;...........................:
........................................:+::;X$&&&&&$&&&&&&;.....$..............+&$XXx++xxxX:.....X+....;$;...........................:
..............................;::+......:X$$&&$XXX$&&&$&&&&+....::.............;$&$X$&$$$$&$$:;:..xx...:X;............................:
...............................:+;+:+.;x$$$$$$$$&XXX$&&&&&X....;...............x&$&$$$XXXX$&$:+:;..+x+:$x;............................:
........................::::;:;xxxXXXXXX$$$X&$$$$$$$$&&&&&$::+x&+x;+;::::::::..:$&$$$$$$$$$XXX++;+::;xX;:::............................
......................:+XX$&$$$&&$&$$XX$X$$XXX$$$$$&$$$$&&&&&&&&&&&&&&&&&&$$$$$$$&$$$$&$$$$$$$$Xxx+xXXXxxx+;;:.........................
..........:::::++++++++xxxXXxXxXXxXxXXXXxxXXxxxXXxXXxXXXXXXXXX$$$$&&&&&&&&&&&&&&$&$XxXX&$$X+xX$$xxxXXXXXxxxxxxxxxx+++++++;:............
..................................................................:...:::;xxxXXX$&$XXXX$$$$XXX$Xxx+++xxxxxxxxxxxxxxx+;:................
...............................;++++++::......................;++++++++++++xxxxxxxxxxxxxx++++++xxxxxxxxxx+++++:........................
.......................................................................................................................................
..........:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..........
''',
                    },
                'the child beyond time' : {
                      'enemyhp' : 120,
                      'enemyatk'  : 6,
                      'bossdesc'  :'''
the lock turns not with a key, but with surrender. you are not the first. you were simply next.

you step forward into nothing- a formless, infinite void that swallows all sound, all light, all meaning.

there is no floor, yet you do not fall.
there are no walls, yet something watches.

the air shimmers faintly with the echo of voices you don’t remember having,
names you’ve almost spoken, and faces you’ve almost known.

far ahead, a figure stands- not tall, not grand, but small.
a silhouette of something childlike, flickering between shapes like a stuttering memory.
one moment draped in rags, the next in ruined armour, then nothing at all.
it doesn’t look at you- but you know it knows you’re here.

fragments of past rooms briefly coalesce in the distance-
a broken chain, a plaster face, a discarded helm, a singed page
and are gone again.

this is the place the maze was built to hide.

this is where it ends.
[bold]or begins.[/bold]
    ''',
                      'bossart' : '''
                                                        ?    ???
                                                      ?????? ????    ??
                                                    ??????   ????? ??
                                                  ????      ????   ?
                                                ? ????      ????    
                                                  ????   ?  ????     
                                                    ???      ???   ?
                                                ?? ???  ?   ???      
                                                ?   ???      ???     
                                                  ????  ?   ????    
                                                  ????      ????  ?
                                                ?  ????      ????    
                                                  ????   ?  ????    
                                                ?? ????      ????    
                                                  ????      ????  ?
                                                    ???   ?  ???     
                                                ?   ???      ???  ??
                                                    ???  ?   ???     
                                                    ???      ???  ?
                                                ? ????      ????    
                                                ? ????   ?  ????     
                                                    ???      ???     
                                                    ???      ???   ?
                                                    ???      ???     
                                                  ?? ???  ?  ???     
                                                    ?????  ????  ??
                                                  ?  ?????????
                                                        ??????  ?
                                                        ?????
''',

                    },
    }

    weapons = {
                'broken sword' : {
                      'weapondamage' : 1,
                    },
                'rusted axe' : {
                      'weapondamage' : 2,
                    },
                'steel greatsword' : {
                      'weapondamage' : 3,
                    },
                'heavy mace' : {
                      'weapondamage' : 4,
                    },
                'steel warhammer' : {
                      'weapondamage' : 5,
                    },
    }

    finalbosstext = {
                1 : '''"you have come far. or rather, you have come again."''',
                2 : '''"you were always meant to arrive. that is why they were chosen. do you recognize them? no… you wouldn’t yet.”''',
                3 : '''“we’ve done this before. we’ll do it again. one of us must be free.”''',
    }
    #spawn area is cave cell; change to wherever you need to go for debugging :)))
    currentroom = 'cave cell'

    validactions = ['feral remnant','whispering mistborn','fallen adventurer','chained forlorn','blood-fettered veteran','lamenting vestal','votary of many tongues','grasp of many','half-born remnant','husk of knowing','vessel of errant insight','the maw of gentle regret','lady vestige, the bound echo','the choir of one','ser ulthric, burdened of names','the child beyond time','broken sword','rusted axe','steel greatsword','heavy mace','steel warhammer','north','south','east','west','map','commands','elixir of soul','elixir of flesh',]
    showinstructions()

    #loop forever
    while True:
      playeratk = (playerstr * weapondamage) + playerlck
      showstatus()
      if playerhp <= 0:
        print('''
                            
                ███   ██    █████    ████    ███      ████████     ████  ████████  ████████             
                ███   █   ███   ███   ███    ██        ██    ███   ███   ███    ██  ██    ███           
                 ███ ██  ███     ███  ██      █        ██     ███  ███   ███  █     ██     ██           
                  ████   ███      ██  ██      █        ██     ███  ███   ███  █     ██     ███          
                  ███    ██       ██  ██      █        ██     ███  ███   ██████     ██     ███          
                  ██    ███      ██  ███     █        ██     ███  ███   ███  █     ██     ███          
                  ██     ██     ██   ███    ██        ██     ██   ███   ███     █  ██    ███           
                  ██      ███ ███     ███████         ███ ████    ███   ████████  ███  ████            
                              █           █                                                             
                                                                                                        
                            ''')
        restart = str(input("Would you like to restart? y or n:  "))
        if restart == "y":
            pygame.mixer.stop()
            script()
        else:
            print("Farewell, be stronger next time")
            time.sleep(2)
            credits()
            time.sleep(5)
            pygame.mixer.stop()
            quit()
            break
      #get the player's next 'action' as a list array (verb, noun)
      action = input('>').strip()      
      action = action.split(" ", 1)

      if len(action) < 2:
          print("please enter a valid command, use \"show commands\" for help")
          continue
      
      if validactions.count(action[1]) == 0:
          print("please enter a valid command, use \"show commands\" for help")
          continue
          
      
      #if they type 'go' first
      if action[0] == 'go':
        #prevent running from boss
        if "boss" in rooms[currentroom]:
           print("can\'t run from a boss!")
        #check that they are allowed wherever they want to go
        elif action[1] in rooms[currentroom]:
          #set the current room to the new room
          currentroom = rooms[currentroom][action[1]]

        #there is no door (link) to the new room
        else:
            print('you can\'t go that way!')

      #if they type 'commands'
      elif action[1] == "commands":
         showinstructions()
         

      #if they type 'get' first
      elif action[0] == 'get' :
        if "item" in rooms[currentroom] and action[1] in rooms[currentroom]['item']:
          inventory.append(action[1])
          print(action[1] + ' acquired.')
          del rooms[currentroom]['item']
        else:
          print('can\'t get ' + action[1] + '!')


      #to use an item
      elif action[0] == 'use' :
        if "item" in rooms[currentroom] and action[1] in rooms[currentroom]['item']:
          print(action[1] + ' must be picked up first!')
        elif action[1] in inventory and action[1] == 'elixir of soul':
          maxhp += 2
          playerhp = maxhp
          print("you feel sturdier! max hp increased.")
          inventory.remove('elixir of soul')
        elif action[1] in inventory and action[1] == 'elixir of flesh':
          playerstr += 1
          print("you feel stronger! strength increased.")
          inventory.remove('elixir of flesh')
        elif action[1] in weapons and action[1] in inventory:
          inventory.append(equipment[0])
          equipment.clear()
          equipment.append(action[1])
          inventory.remove(action[1])
          weapondamage = weapons[action[1]]['weapondamage']
        else:
          print('can\'t use ' + action[1] + '!')
          
      #show map
      elif action[1] == 'map' :
        print('''
              
map:
              □
              |
    □ __ □    □    □ __ □             x = start
    |    |    |    |    |
    □ __ □ __ □ __ □ __ □
              |   
    □ __ □ __ □ __ □ __ □
          |    |    |    |
    □ __ □    □    □ __ □
    |         |
x    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □
          
              '''
    )


      #attacking a normal enemy
      elif action[0] == 'attack' and len(action) > 1:
          if "enemy" in rooms[currentroom] and action[1] in rooms[currentroom]['enemy']:
              print(action[1] + ' has '+ str(enemies[action[1]]['enemyhp']) +' hp and ' + str(enemies[action[1]]['enemyatk']) + ' attack.')
              if playerlck == 0:
                  hitchance = random.randint(0,3)
                  enemyhitchance = random.randint(0,4)
              elif playerlck == 2:
                  hitchance = random.randint(0,5)
                  enemyhitchance = random.randint(0,3)
              elif playerlck >= 5:
                  hitchance = random.randint(0,10)
                  enemyhitchance = random.randint(0,2)

              if enemies[action[1]]['enemyhp'] <= playeratk:
                  print(action[1] + ' defeated!')
                  del rooms[currentroom]['enemy']
                  playerhp -= enemies[action[1]]['enemyatk'] 
                  playerhp -= enemyhitchance
                  maxhp += 1
                  print('health decreased by ' + str(enemies[action[1]]['enemyatk']) + ' with ' + str(enemyhitchance) + ' bonus damage!')
              if playerhp <= 0:
                  print('''
                            
                ███   ██    █████    ████    ███      ████████     ████  ████████  ████████             
                ███   █   ███   ███   ███    ██        ██    ███   ███   ███    ██  ██    ███           
                 ███ ██  ███     ███  ██      █        ██     ███  ███   ███  █     ██     ██           
                  ████   ███      ██  ██      █        ██     ███  ███   ███  █     ██     ███          
                  ███    ██       ██  ██      █        ██     ███  ███   ██████     ██     ███          
                  ██    ███      ██  ███     █        ██     ███  ███   ███  █     ██     ███          
                  ██     ██     ██   ███    ██        ██     ██   ███   ███     █  ██    ███           
                  ██      ███ ███     ███████         ███ ████    ███   ████████  ███  ████            
                              █           █                                                             
                                                                                                        
                            ''')
                  restart = str(input("Would you like to restart? y or n:  "))
                  if restart == "y":
                     pygame.mixer.stop()
                     script()
                  else:
                      print("Farewell, be stronger next time")
                      time.sleep(2)
                      credits()
                      time.sleep(5)
                      pygame.mixer.stop()
                      quit()
                      break
                  
              elif enemies[action[1]]['enemyhp'] > playeratk:
                  enemies[action[1]]['enemyhp'] -= playeratk
                  enemies[action[1]]['enemyhp'] -= hitchance
                  print(action[1] + ' health decreased by ' + str(playeratk))
                  playerhp -= enemies[action[1]]['enemyatk']
                  playerhp -= enemyhitchance
                  print('health decreased by ' + str(enemies[action[1]]['enemyatk']) + ' with ' + str(enemyhitchance) + ' bonus damage!')
                  if playerhp <= 0:
                      print('''
                            
                ███   ██    █████    ████    ███      ████████     ████  ████████  ████████             
                ███   █   ███   ███   ███    ██        ██    ███   ███   ███    ██  ██    ███           
                 ███ ██  ███     ███  ██      █        ██     ███  ███   ███  █     ██     ██           
                  ████   ███      ██  ██      █        ██     ███  ███   ███  █     ██     ███          
                  ███    ██       ██  ██      █        ██     ███  ███   ██████     ██     ███          
                  ██    ███      ██  ███     █        ██     ███  ███   ███  █     ██     ███          
                  ██     ██     ██   ███    ██        ██     ██   ███   ███     █  ██    ███           
                  ██      ███ ███     ███████         ███ ████    ███   ████████  ███  ████            
                              █           █                                                             
                                                                                                        
                            ''')
                      restart = str(input("Would you like to restart? y or n:  "))
                      if restart == "y":
                        pygame.mixer.stop()
                        script()
                      else:
                        print("Farewell, be stronger next time")
                        time.sleep(2)
                        credits()
                        time.sleep(5)
                        pygame.mixer.stop()
                        quit()
                        break
                      
          elif playerhp <= 0:
              print('''
                            
                ███   ██    █████    ████    ███      ████████     ████  ████████  ████████             
                ███   █   ███   ███   ███    ██        ██    ███   ███   ███    ██  ██    ███           
                 ███ ██  ███     ███  ██      █        ██     ███  ███   ███  █     ██     ██           
                  ████   ███      ██  ██      █        ██     ███  ███   ███  █     ██     ███          
                  ███    ██       ██  ██      █        ██     ███  ███   ██████     ██     ███          
                  ██    ███      ██  ███     █        ██     ███  ███   ███  █     ██     ███          
                  ██     ██     ██   ███    ██        ██     ██   ███   ███     █  ██    ███           
                  ██      ███ ███     ███████         ███ ████    ███   ████████  ███  ████            
                              █           █                                                             
                                                                                                        
                            ''')
              restart = str(input("Would you like to restart? y or n:  "))
              if restart == "y":
                  pygame.mixer.stop()
                  script()
              else:
                  print("Farewell, be stronger next time")
                  time.sleep(2)
                  credits()
                  time.sleep(5)
                  pygame.mixer.stop()
                  quit()
                  break
          



    #attacking a boss that is not final boss
          elif "boss" in rooms[currentroom] and action[1] in rooms[currentroom]['boss'] and rooms[currentroom]['boss'] != "the child beyond time":
              print(action[1] + ' has '+ str(bosses[action[1]]['enemyhp']) +' hp and ' + str(bosses[action[1]]['enemyatk']) + ' attack.')
              if playerlck == 0:
                  hitchance = random.randint(0,3)
                  enemyhitchance = random.randint(0,4)
              elif playerlck == 2:
                  hitchance = random.randint(0,5)
                  enemyhitchance = random.randint(0,3)
              elif playerlck >= 5:
                  hitchance = random.randint(0,10)
                  enemyhitchance = random.randint(0,2)
              if bosses[action[1]]['enemyhp'] <= playeratk:
                  print(action[1] + ' defeated!')
                  del rooms[currentroom]['boss']
                  inventory.append(bosses[action[1]]['bosskey'])
                  print(bosses[action[1]]['bosskey'] + ' added to inventory!')
                  print(bosses[action[1]]['bosskeydesc'])
                  playerhp -= bosses[action[1]]['enemyatk']
                  playerhp -= enemyhitchance
                  playerstr += 1
                  print('health decreased by ' + str(bosses[action[1]]['enemyatk']) + '!')
              if bosses[action[1]]['enemyhp'] == 0:
                  inventory.append(bosses[action[1]]['bosskey'])
                  print(bosses[action[1]]['bosskeydesc'])
                  if playerhp <= 0:
                      print('''
                            
                ███   ██    █████    ████    ███      ████████     ████  ████████  ████████             
                ███   █   ███   ███   ███    ██        ██    ███   ███   ███    ██  ██    ███           
                 ███ ██  ███     ███  ██      █        ██     ███  ███   ███  █     ██     ██           
                  ████   ███      ██  ██      █        ██     ███  ███   ███  █     ██     ███          
                  ███    ██       ██  ██      █        ██     ███  ███   ██████     ██     ███          
                  ██    ███      ██  ███     █        ██     ███  ███   ███  █     ██     ███          
                  ██     ██     ██   ███    ██        ██     ██   ███   ███     █  ██    ███           
                  ██      ███ ███     ███████         ███ ████    ███   ████████  ███  ████            
                              █           █                                                             
                                                                                                        
                            ''')
                      restart = str(input("Would you like to restart? y or n:  "))
                      if restart == "y":
                          pygame.mixer.stop()
                          script()
                      else:
                        print("Farewell, be stronger next time")
                        time.sleep(2)
                        credits()
                        time.sleep(5)
                        pygame.mixer.stop()
                        quit()
                        break
                  del rooms[currentroom]['boss']
              elif bosses[action[1]]['enemyhp'] > playeratk:
                  bosses[action[1]]['enemyhp'] -= playeratk
                  bosses[action[1]]['enemyhp'] -= hitchance
                  print(action[1] + ' health decreased by ' + str(playeratk))
                  playerhp -= bosses[action[1]]['enemyatk']
                  playerhp -= enemyhitchance
                  print('health decreased by ' + str(bosses[action[1]]['enemyatk'])  + ' with ' + str(enemyhitchance) + ' bonus damage!')
                  if playerhp <= 0:
                      print('''
                            
                ███   ██    █████    ████    ███      ████████     ████  ████████  ████████             
                ███   █   ███   ███   ███    ██        ██    ███   ███   ███    ██  ██    ███           
                 ███ ██  ███     ███  ██      █        ██     ███  ███   ███  █     ██     ██           
                  ████   ███      ██  ██      █        ██     ███  ███   ███  █     ██     ███          
                  ███    ██       ██  ██      █        ██     ███  ███   ██████     ██     ███          
                  ██    ███      ██  ███     █        ██     ███  ███   ███  █     ██     ███          
                  ██     ██     ██   ███    ██        ██     ██   ███   ███     █  ██    ███           
                  ██      ███ ███     ███████         ███ ████    ███   ████████  ███  ████            
                              █           █                                                             
                                                                                                        
                            ''')
                      restart = str(input("Would you like to restart? y or n:  "))
                      if restart == "y":
                          pygame.mixer.stop()
                          script()
                      else:
                        print("Farewell, be stronger next time")
                        time.sleep(2)
                        credits()
                        time.sleep(5)
                        pygame.mixer.stop()
                        quit()
                        break


    #attacking final boss
          elif "boss" in rooms[currentroom] and action[1] in rooms[currentroom]['boss'] and rooms[currentroom]['boss'] == "the child beyond time":
              print(action[1] + ' has '+ str(bosses[action[1]]['enemyhp']) +' hp and ' + str(bosses[action[1]]['enemyatk']) + ' attack.')
              if playerlck == 0:
                  hitchance = random.randint(0,3)
                  enemyhitchance = random.randint(0,4)
              elif playerlck == 2:
                  hitchance = random.randint(0,5)
                  enemyhitchance = random.randint(0,3)
              elif playerlck >= 5:
                  hitchance = random.randint(0,10)
                  enemyhitchance = random.randint(0,2)
              if finalbossturn == 1:
                print(finalbosstext[1])
              if finalbossturn == 2:
                print(finalbosstext[2])
              if finalbossturn == 3:
                print(finalbosstext[3])
              if finalbossturn >= 4:
                print("")
              if bosses[action[1]]['enemyhp'] <= playeratk:
                  console.print(action[1] + '''[italic] has been defeated... for now.
a voice whispers in the darkness:
                
“you’ll need new guards.”
                
“find others. from other whens. make them strong.”
                
“soon... you’ll forget this was you.”
                                

                        [/italic]''')
                  time.sleep(3)
                  print('''
                                                                 
                                                            ███                                                                  
                                              ████████  ██████████    ███████                                                    
                                               ██      ███       ███   ██                                                        
                                               ██     ███         ███  ██                                                        
                                               ██████ ███          ██  ██████                                                    
                                               ██     ███          ██  ██                                                        
                                               ██      ███        ██   ██                                                        
                                               ██       ████    ███    ███  ██                                                   
                                              ████         ██████     ████████                                                   
                                                                                                                                                                                                   
                                                                                                                                 
                                                      ██                                                                         
  █████      ████      ██        ███      █████  ███████████   ████     ████ ████  ██████ ████     █████ ████████ ███████████    
    ███      ██       ████       ████       ██  ██        ███   ██       ██   ██  ███   █  ███       ██   ███      ██      ████  
     ███    ██        ████       ██████     ██ ██          ███  ██       ██   ██  ████     ███       ██   ███      ██        ███ 
      ███  ██        ██  ██      ██  ████   ██ ██          ███  ██       ██   ██    ████   ████████████   ███████  ██        ███ 
      ███  ██       ████████     ██    ███  ██ ███         ███  ██       ██   ██      ███  ███       ██   ███      ██        ███ 
       █████        ██    ███    ██     ██████  ███       ███   ██       ██   ██       ███ ███       ██   ███      ██        ██  
        ███        ██      ███   ██       ████   █████  ████     ██     ██    ██  ██   ██  ███      ███   ███   █  ███     ███   
         █        ███      ████ ████        █      ███████████    ███████    ████ ██████   ███      ████  ███████ ██████████     
                                                            █████████████                                                        
                                                                  █████                                                          
                        ''')
                  time.sleep(3)
                  print('''
the child in time is silent. not slain, but emptied.
its echoes scatter like dust across the void.

you stand alone, yet not alone.
the faces return; not as memory, but as design.
each one, a guardian you once called friend.
each one, drawn here by your hand
                        
                        ''')
                  time.sleep(6)
                  console.print('''[italic]The courtyard crackles with frost as Ulthric nudges your shoulder with his elbow.
\"First one to lose a gauntlet buys the next round,\" he grins.
Together, you gaze up at the castle—its spires hollow, its silence too loud.
\"No one comes out,\" he says, tightening his helm. \"So we go in. You know I'll always protect you.\"
You nod. You always nodded when he looked that sure.
You don’t see him look back at you, just once, before the gates open.[/italic]
                                
                                ''')
                  time.sleep(8)
                  console.print('''[italic]You sit beside Countess Isolde beneath the dim light of enchanted lanterns, books piled high.
Her hand lingers over yours. \"You read that one backwards,\" she teases softly.
A scroll glows faintly near her desk, sealed in three kinds of wax.
\"Promise me you won’t try it,\" she whispers. \"No one knows what it does.\"
She leans in, lips brushing your ear.
\"And I’d rather not lose you to another riddle.\"[/italic]
                                
                                ''')
                  time.sleep(8)
                  console.print('''[italic]The undercroft smells of incense and dust. You shiver as he offers you a seat.
\"There are things that follow, even between dreams,\" he murmurs. \"You’re not mad.\"
He draws a sigil on the stone floor with chalk, steady and slow.
\"It won’t stop it, but it will forget you - for now.\"
You say you'll never forget him. He only smiles.
\"Good,\" he says. \"Then I won’t be alone.\"[/italic]
                                
                                ''')
                  time.sleep(8)
                  console.print('''[italic]You all patiently wait in the dining room of the grand castle, waiting for the sign.
Someone makes a joke about cursed bricks. Everyone laughs, even you.
One of your compatriots grips your elbow. \"When we’re done, drinks and women on me!\"
The signal never comes. You're nervous, and decide to venture out into the hall to check, stepping over the slain creatures.
Behind you, the doors slam shut. Screaming, then silence.
You run. You always regretted running.[/italic]
                                
                                ''')
                  time.sleep(8)
                  print('''the tenons twist within the mortise behind you.
a perfect fit.
a perfect seal.

the door closes.
the maze shifts.
the next you will come.

and they will find a gaol.
and a hymn.
and a corpse that still remembers.
and a whisper in the dark:

"one must judge. one must suffer. one must remain."

you remain.
                        

''')
                  time.sleep(6)
                  credits()
                  time.sleep(4)
                  restart = str(input("Would you like to restart? y or n:  "))
                  if restart == "y":
                      pygame.mixer.stop()
                      script()
                  else:
                      print("Farwell, for now...")
                      time.sleep(2)
                      quit()
                      break


                  if playerhp <= 0:
                      print('''
                            
                ███   ██    █████    ████    ███      ████████     ████  ████████  ████████             
                ███   █   ███   ███   ███    ██        ██    ███   ███   ███    ██  ██    ███           
                 ███ ██  ███     ███  ██      █        ██     ███  ███   ███  █     ██     ██           
                  ████   ███      ██  ██      █        ██     ███  ███   ███  █     ██     ███          
                  ███    ██       ██  ██      █        ██     ███  ███   ██████     ██     ███          
                  ██    ███      ██  ███     █        ██     ███  ███   ███  █     ██     ███          
                  ██     ██     ██   ███    ██        ██     ██   ███   ███     █  ██    ███           
                  ██      ███ ███     ███████         ███ ████    ███   ████████  ███  ████            
                              █           █                                                             
                                                                                                        
                            ''')
                      restart = str(input("Would you like to restart? y or n:  "))
                      if restart == "y":
                          pygame.mixer.stop()
                          script()
                      else:
                        print("Farewell, be stronger next time")
                        time.sleep(2)
                        credits()
                        time.sleep(5)
                        pygame.mixer.stop()
                        break
                  del rooms[currentroom]['boss']
              elif bosses[action[1]]['enemyhp'] > playeratk:
                  bosses[action[1]]['enemyhp'] -= playeratk
                  bosses[action[1]]['enemyhp'] -= hitchance
                  print(action[1] + ' health decreased by ' + str(playeratk))
                  playerhp -= bosses[action[1]]['enemyatk']
                  playerhp -= enemyhitchance
                  print('health decreased by ' + str(bosses[action[1]]['enemyatk'])  + ' with ' + str(enemyhitchance) + ' bonus damage!')
                  finalbossturn += 1
                  if playerhp <= 0:
                      print('''
                            
                ███   ██    █████    ████    ███      ████████     ████  ████████  ████████             
                ███   █   ███   ███   ███    ██        ██    ███   ███   ███    ██  ██    ███           
                 ███ ██  ███     ███  ██      █        ██     ███  ███   ███  █     ██     ██           
                  ████   ███      ██  ██      █        ██     ███  ███   ███  █     ██     ███          
                  ███    ██       ██  ██      █        ██     ███  ███   ██████     ██     ███          
                  ██    ███      ██  ███     █        ██     ███  ███   ███  █     ██     ███          
                  ██     ██     ██   ███    ██        ██     ██   ███   ███     █  ██    ███           
                  ██      ███ ███     ███████         ███ ████    ███   ████████  ███  ████            
                              █           █                                                             
                                                                                                        
                            ''')
                      restart = str(input("Would you like to restart? y or n:  "))
                      if restart == "y":
                          pygame.mixer.stop()
                          script()
                      else:
                        print("Farewell, be stronger next time")
                        time.sleep(2)
                        credits()
                        time.sleep(5)
                        pygame.mixer.stop()
                        break


          else:
            print('can\'t do ' + action[1] + '!')
      else:
            print('please enter a valid command')

      #if a player has defeated all four bosses, going to the silent threshold with all the keys will send them into final boss room
      if currentroom == 'the silent threshold' and 'tenon of many ends' in inventory and 'tenon of unspoken shapes' in inventory and 'tenon of hollow praise' in inventory and 'tenon of broken oaths' in inventory:
        console.print('''[italic]
============================================================================================================================================
the tenon pieces in your inventory seem to resonate with the grand door, and you pull them out and slot them into
the mortise. the door opens slowly without a sound, and your breath catches in your throat as you step through.
============================================================================================================================================[/italic]''')
        currentroom = 'the atrium of unmaking'
        showstatus()


try:
    script()
except Exception as e:
    crash=["Error on line {}".format(sys.exc_info()[-1].tb_lineno),"\n",e]
    timeX=str(time.time())
    print(crash)
    with open("FALSE-SOULS-CRASH.txt","w") as crashLog:
        for i in crash:
            i=str(i)
            crashLog.write(datetime.datetime.now())
            crashLog.write(i)


