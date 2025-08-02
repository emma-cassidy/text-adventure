#my baby rpg lol

import time
import random
import pygame
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("False Souls")

def script():
    pygame.init()
    my_sound = pygame.mixer.Sound('c:/users/emmac/python/text-adventure/bgmv3.mp3')
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
          ███   ██   ██  █████ ██     ██████  █████    █      █  █████    █   ██   █  █████                                               
           ██  ████  ██  ██    ██   ███    ███     ██  ██    ██   ██          ██    ██    ███                                             
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
        char_class = input("choose your class. enter cleric, warrior or rogue: ").lower()
        if char_class in ["cleric", "warrior", "rogue", "altmer",]:
            break
        else:
            print("please choose a valid class.")
      char_name = input("name your character: ")

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
  map                  (shows map)
  attack [enemy]       (initiates combat)
  command              (show commands)

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
            print('you see a ' + rooms[currentroom]['item'])
        #show an enemy if there is one
        if "enemy" in rooms[currentroom]:
            print('there is a ' + rooms[currentroom]['enemy'] + ' enemy in here!')
        if "boss" in rooms[currentroom]:
            print('the boss ' + rooms[currentroom]['boss'] + ' prepares to attack!')
            placeholder = rooms[currentroom]['boss']
            if bosses[placeholder]['enemyhp'] >= 30:
                print((bosses[placeholder]['bossdesc']))
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
                      'enemyhp' : 2,
                      'enemyatk'  : 1,
                    },
                'whispering mistborn' : {
                      'enemyhp' : 4,
                      'enemyatk'  : 1,
                    },
                'fallen adventurer' : {
                      'enemyhp' : 5,
                      'enemyatk'  : 3,
                    },
                'chained forlorn' : {
                      'enemyhp' : 5,
                      'enemyatk'  : 3,
                    },
                'blood-fettered veteran' : {
                      'enemyhp' : 4,
                      'enemyatk'  : 3,
                    },
                'lamenting vestal' : {
                      'enemyhp' : 3,
                      'enemyatk'  : 4,
                    },
                'votary of many tongues' : {
                      'enemyhp' : 5,
                      'enemyatk'  : 3,
                    },
                'grasp of many' : {
                      'enemyhp' : 8,
                      'enemyatk'  : 2,
                    },
                'half-born remnant' : {
                      'enemyhp' : 2,
                      'enemyatk'  : 3,
                    },
                'husk of knowing' : {
                      'enemyhp' : 3,
                      'enemyatk'  : 2,
                    },
                'vessel of errant insight' : {
                      'enemyhp' : 5,
                      'enemyatk'  : 4,
                    },
    }

    bosses = {
                'the maw of gentle regret' : {
                      'enemyhp' : 30,
                      'enemyatk'  : 45,
                      'bosskey'  : 'tenon of many ends',
                      'bossdesc' : '''
stitched from ambition and error, this slithering mockery of heroism hungers for meaning.
it wears their armor, their limbs, their hopes - all rotting beneath the weight of shared failure.
so many came seeking purpose. together, they found something worse.

all who enter are remembered. none as themselves. purpose decays. but hunger persists.''',
                      'bosskeydesc' : 'knotted bone and glimmering ash. it does not fit cleanly into any shape- but somehow, it belongs.',
                    },
                'lady vestige, the bound echo' : {
                      'enemyhp' : 30,
                      'enemyatk'  : 3,
                      'bosskey'  : 'tenon of unspoken shapes',
                      'bossdesc' : '''
once a seeker of escape through knowledge, she unmade herself word by word.
now bound in thought and thin as parchment, she whispers truths no mind should carry.
she read until there was no more ‘she’ left to read.

she sought the way out, and became the door. in knowing everything, she forgot what she was.''',
                      'bosskeydesc' : 'carved with symbols that shift when not observed. cold to the touch, yet burns with withheld meaning.',
                    },
                'the choir of one' : {
                      'enemyhp' : 35,
                      'enemyatk'  : 5,
                      'bosskey'  : 'tenon of hollow praise',
                      'bossdesc' : '''
a broken cleric who sang to silence until silence sang back.
now a choir of mouths and madness, it praises a god that answers only in echoes.
there were no others to join the hymn. so, it made them.

sing loud enough, and the silence will sing back.''',
                      'bosskeydesc' : 'pale and resonant, it hums faintly with voices not your own. some still believe it is listening.',
                    },
                'ser ulthric, burdened of names' : {
                      'enemyhp' : 35,
                      'enemyatk'  : 5,
                      'bosskey'  : 'tenon of broken oaths',
                      'bossdesc' : '''
once a proud champion entombed by his own honours, ulthric was left to rot in chains he forged with valour.
now, a beast of instinct, he swings in defiance of a past no longer his.
they built walls to keep him safe. or was it to keep him in?

chains may break. but the burden remains. he remembers only the oath. not who he swore it to.''',
                      'bosskeydesc' : 'a heavy shard of forged steel, stained and splintered. it bears the weight of forgotten vows.',
                    },
                'the child beyond time' : {
                      'enemyhp' : 50,
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
it doesn’t look at you—but you know it knows you’re here.

fragments of past rooms briefly coalesce in the distance-
a broken chain, a plaster face, a discarded helm, a singed page
and are gone again.

this is the place the maze was built to hide.

this is where it ends.
or begins.
    '''
                    },
    }

    weapons = {
                'broken sword' : {
                      'weapondamage' : 2,
                    },
                'rusted axe' : {
                      'weapondamage' : 3,
                    },
                'steel greatsword' : {
                      'weapondamage' : 4,
                    },
                'heavy mace' : {
                      'weapondamage' : 5,
                    },
                'steel warhammer' : {
                      'weapondamage' : 6,
                    },
    }

    finalbosstext = {
                1 : '''"you have come far. or rather, you have come again."''',
                2 : '''"you were always meant to arrive. that is why they were chosen. do you recognize them? no… you wouldn’t yet.”''',
                3 : '''“we’ve done this before. we’ll do it again. one of us must be free.”''',
    }
    #spawn area is cave cell; change to wherever you need to go for debugging :)))
    currentroom = 'the maw between hours - corridor'

    showinstructions()

    #loop forever
    while True:
      playeratk = (playerstr * weapondamage) + playerlck
      showstatus()

      #get the player's next 'action' as a list array (verb, noun)
      action = ''
      while action == '':
        action = input('>')       
      action = action.split(" ", 1)

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
      if action[0] == 'command' or action[0] == "commands":
         showinstructions()
         

      #if they type 'get' first
      if action[0] == 'get' :
        if "item" in rooms[currentroom] and action[1] in rooms[currentroom]['item']:
          inventory.append(action[1])
          print(action[1] + ' acquired.')
          del rooms[currentroom]['item']
        else:
          print('can\'t get ' + action[1] + '!')


      #to use an item
      if action[0] == 'use' :
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
      if action[0] == 'map' :
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
      if action[0] == 'attack' :
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
                     script()
                  else:
                      print("Farwell, be stronger next time")
                      time.sleep(2)
                      credits()
                      time.sleep(5)
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
                        script()
                      else:
                        print("Farwell, be stronger next time")
                        time.sleep(2)
                        credits()
                        time.sleep(5)
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
                  script()
              else:
                  print("Farwell, be stronger next time")
                  time.sleep(2)
                  credits()
                  time.sleep(5)
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
                          script()
                      else:
                        print("Farwell, be stronger next time")
                        time.sleep(2)
                        credits()
                        time.sleep(5)
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
                          script()
                      else:
                        print("Farwell, be stronger next time")
                        time.sleep(2)
                        credits()
                        time.sleep(5)
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
                  print(action[1] + ''' has been defeated... for now.
a voice whispers in the darkness:
                
“you’ll need new guards.”
                
“find others. from other whens. make them strong.”
                
“soon... you’ll forget this was you.”
                        ''')
                  playerhp -= bosses[action[1]]['enemyatk']
                  print('health decreased by ' + str(bosses[action[1]]['enemyatk']) + '!')
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
                          script()
                      else:
                        print("Farwell, be stronger next time")
                        time.sleep(2)
                        credits()
                        time.sleep(5)
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
                          script()
                      else:
                        print("Farwell, be stronger next time")
                        time.sleep(2)
                        credits()
                        time.sleep(5)
                        break


          else:
            print('can\'t do ' + action[1] + '!')

      #if a player has defeated all four bosses, going to the silent threshold with all the keys will send them into final boss room
      if currentroom == 'the silent threshold' and 'tenon of many ends' in inventory and 'tenon of unspoken shapes' in inventory and 'tenon of hollow praise' in inventory and 'tenon of broken oaths' in inventory:
        print('''
============================================================================================================================================
the tenon pieces in your inventory seem to resonate with the grand door, and you pull them out and slot them into
the mortise. the door opens slowly without a sound, and your breath catches in your throat as you step through.
============================================================================================================================================''')
        currentroom = 'the atrium of unmaking'
        showstatus()

script()
