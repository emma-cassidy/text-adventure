#My baby RPG lol

playerHP = 0
playerSTR = 0
playerLCK = 0
playerATK = 0
char_name = ""
char_class = ""
weapondamage = 1


def characterSelect():
  print('''
Welcome to EMMA RING
============================================================================================================================================
Select your starting character:
  Cleric - 8HP, 2 Strength, 2 Luck 
  Warrior - 5HP, 5 Strength, 0 Luck
  Rogue - 5HP, 2 Strength, 5 Luck
        
  Attack = (Strength x Weapon Damage) + Luck
============================================================================================================================================
''')
  while True:
    char_class = input("Choose your class. Enter Cleric, Warrior or Rogue: ").lower()
    if char_class in ["cleric", "warrior", "rogue"]:
        break
    else:
        print("Please choose a valid class.")
  char_name = input("Name your character: ")

  if char_class == "cleric":
    playerHP = 8
    playerSTR = 2
    playerLCK = 2
  elif char_class == "warrior":
    playerHP = 5
    playerSTR = 5
    playerLCK = 0
  else:
    playerHP = 5
    playerSTR = 2
    playerLCK = 5
  return char_name, char_class, playerHP, playerSTR, playerLCK


char_name, char_class, playerHP, playerSTR, playerLCK = characterSelect()
playerATK = (playerSTR * weapondamage) + playerLCK

def showInstructions():
  print(f'''
Welcome to EMMA RING, {char_class} {char_name}!
============================================================================================================================================
Commands:
  go [direction] (north, south, east, west)
  get [item]     (item name)
  use [item]     (item name)
  attack [enemy]
============================================================================================================================================
''')

def showStatus():
  #print the player's current status
  print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
  print('You are in the ' + currentRoom)
  #show current stats
  print(f'You have {playerHP} HP, {playerSTR} strength, and {playerLCK} luck.')
  print(f'Your attack stat is {playerATK}.')
  #show the current inventory
  print('Inventory : ' + str(inventory))
  #print description if there is one
  if "desc" in rooms[currentRoom]:
    print((rooms[currentRoom]['desc']))
  #show an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  #show an enemy if there is one
  if "enemy" in rooms[currentRoom]:
    print('There is a ' + rooms[currentRoom]['enemy'] + ' enemy in here!')
  if "boss" in rooms[currentRoom]:
    print('The boss ' + rooms[currentRoom]['boss'] + ' prepares to attack!')
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# def startCombat():
#   if rooms[currentRoom]['enemy'] == "Fallen Adventurer":


inventory = []

rooms = {

            'Cave Cell' : {
                  'south' : 'Cave Tunnel',
                  'item'  : 'Broken Sword',
                  'desc'  : '''
============================================================================================================================================
You are in a dank, dark cave, with a broken chain at your feet. Your neck is sore, as if you were restrained by it. The only way to go 
is through the cave tunnel you see to your south.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
X    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
                },

            'Cave Tunnel' : {
                  'north' : 'Cave Cell',
                  'south' : 'Cave Mouth - South',
                  'east'  : 'Cave Mouth - East',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
X __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
                },
            'Cave Mouth - South' : {
                  'north' : 'Cave Tunnel',
                  'enemy' : 'Feral Remnant',
                  'desc'  : '''
============================================================================================================================================
The cave mouth faces out onto a sheer cliff opening. You see dark, cloudy skies for a few miles with crashing - yet silent - waves below.
In the distance beyond the cloud and waves you see an endless abyss of darkness, as if you the land on which you stand has been plucked from
elsewhere. To your north is the cave tunnel.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
X __ □

============================================================================================================================================''',
               },
            'Cave Mouth - East' : {
                  'west' : 'Cave Tunnel',
                  'north' : 'Cliff Ledge',
                  'south' : 'Cliff Edge - East',
                  'enemy' : 'Feral Remnant',
                  'desc'  : '''
============================================================================================================================================
The cave mouth faces out onto a sheer cliff opening. You see dark, cloudy skies for a few miles with crashing - yet silent - waves below.
In the distance beyond the cloud and waves you see an endless abyss of darkness, as if you the land on which you stand has been plucked from
elsewhere. To your west is the cave tunnel. To your south is the cliff edge, where you can hear a faint moaning. To your north, there seems
to be a ledge you could climb.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ X    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
               },
            'Cliff Edge - East' : {
                  'north' : 'Cave Mouth - East',
                  'enemy' : 'Whispering Mistborn',
                  'desc'  : '''
============================================================================================================================================
You stand on the precipice, staring out into the silent darkness. There is no other way forward except back north to the cave mouth.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ X

============================================================================================================================================''',
                },
            'Cliff Ledge' : {
                  'north' : 'Crack in the wall',
                  'south' : 'Cave Mouth - East',
                  'east'  : 'Wrought Iron Fence',
                  'desc'  : '''
============================================================================================================================================
You scramble onto the ledge, and to your east notice a wrought iron fence you could climb. To your north, there is a crack in a large stone
wall, large enough for you to squeeze into. To your south below you lies the cave mouth.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    X __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
                },
            'Crack in the wall' : {
                  'south' : 'Cliff Ledge',
                  'east'  : 'The Maw Between Hours - Corridor',
                  'enemy' : 'Half-Born Remnant',
                  'desc'  : '''
============================================================================================================================================
From your location in the crevice of the thick stone wall, you notice what seems to be a grand corridor to your east. The air is pungent 
with rot and decay, punctured only by the fresh air flowing from the cliff ledge to your south. You hear movement in the building to your
east. 

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     X __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'Wrought Iron Fence' : {
                  'west' : 'Cliff Ledge',
                  'south' : 'Graveyard',
                  'east'  : 'Garden',
                  'desc'  : '''
============================================================================================================================================
From your position atop the wrought iron fence, to the east you spy what seems to be a derelict yet once loved garden, with a dried fountain, 
barren soil and withered trees. To your south there are unmistakeably graves whose inhabitants' names have been lost to time.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ X __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
               },
            'Graveyard' : {
                  'north' : 'Wrought Iron Fence',
                  'east'  : 'Disused Training Yard',
                  'enemy' : 'Whispering Mistborn',
                  'desc'  : '''
============================================================================================================================================
The graveyard is full of tombstones of varying shapes and sizes, with some modern black marble and others crumbling sandstone and lime. They
have one thing in common - all have clearly been forgotten - but appear to be those of heroes, judging from the decayed and rusted weapons
and shields littered around them in tribute. The iron fence is to your north, and to your east you see a disused training yard.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    X __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'Garden' : {
                  'west' : 'Wrought Iron Fence',
                  'north' : 'Main Foyer',
                  'south' : 'Disused Training Yard',
                  'east'  : 'Carriage House',
                  'enemy' : 'Whispering Mistborn',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ X __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
               },
            'Disused Training Yard' : {
                  'west' : 'Graveyard',
                  'north' : 'The Garden',
                  'east'  : 'Worn Barracks',
                  'enemy' : 'Fallen Adventurer',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ X __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'Carriage House' : {
                  'west' : 'The Garden',
                  'south' : 'Worn Barracks',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ X
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
               },
            'Worn Barracks' : {
                  'west' : 'Disused Training Yard',
                  'north' : 'Carriage House',
                  'enemy' : 'Feral Remnant',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ X   
|    |
□ __ □

============================================================================================================================================''',
            },
            'Main Foyer' : {
                  'north' : 'Hall of the Unnumbered Trials - South',
                  'south' : 'The Garden',
                  'enemy' : 'Whispering Mistborn',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    X    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
               },
            'Hall of the Unnumbered Trials - South' : {
                  'west' : 'The Maw Between Hours - Foyer',
                  'north' : 'Hall of the Unnumbered Trials - North',
                  'south' : 'Main Foyer',
                  'east'  : 'The Cradle That Remembers - Foyer',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ X __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'The Maw Between Hours - Corridor' : {
                  'west' : 'Crack in the wall',
                  'north' : 'The Maw Between Hours - Foyer',
                  'enemy' : 'Half-Born Remnant',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ X    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
               },
            'The Maw Between Hours - Foyer' : {
                  'west' : 'The Maw Between Hours - Hall',
                  'south' : 'The Maw Between Hours - Corridor',
                  'east'  : 'Hall of the Unnumbered Trials - South',
                  'enemy' : 'Grasp of Many',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ X __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
               },
            'The Maw Between Hours - Hall' : {
                  'east'  : 'The Maw Between Hours - Foyer',
                  'boss' : 'The Maw of Gentle Regret',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     X __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
               },
            'The Cradle That Remembers - Foyer' : {
                  'west' : 'Hall of the Unnumbered Trials - South',
                  'south' : 'The Cradle That Remembers - Corridor',
                  'east'  : 'The Cradle That Remembers - Antechamber',
                  'enemy' : 'Husk of Knowing',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ X __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'The Cradle That Remembers - Corridor' : {
                  'north' : 'The Cradle That Remembers - Foyer',
                  'east'  : 'The Cradle That Remembers - Cradle',
                  'enemy' : 'Husk of Knowing',
                  'enemy' : 'Vessel of Errant Insight',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    X __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'The Cradle That Remembers - Antechamber' : {
                  'west' : 'The Cradle That Remembers - Foyer',
                  'south' : 'The Cradle That Remembers - Cradle',
                  'enemy' : 'Husk of Knowing',
                  'enemy' : 'Vessel of Errant Insight',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ X
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'The Cradle That Remembers - Cradle' : {
                  'west' : 'The Cradle That Remembers - Corridor',
                  'north' : 'The Cradle That Remembers - Antechamber',
                  'boss' : 'Lady Vestige, the Bound Echo',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ X
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
               },
            'Hall of the Unnumbered Trials - North' : {
                  'west' : 'Vault of the Once-Whole - Foyer',
                  'north' : 'The Silent Threshold',
                  'south' : 'Hall of the Unnumbered Trials - South',
                  'east'  : 'Sepulchre of the Unmarked Step - Foyer',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ X __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'Sepulchre of the Unmarked Step - Foyer' : {
                  'west' : 'Hall of the Unnumbered Trials - North',
                  'north' : 'Sepulchre of the Unmarked Step - Wasted Tomb',
                  'east'  : 'Sepulchre of the Unmarked Step - Funerary Parlour',
                  'enemy' : 'Votary of Many Tongues',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ X __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
               },
            'Sepulchre of the Unmarked Step - Wasted Tomb' : {
                  'south' : 'Sepulchre of the Unmarked Step - Foyer',
                  'east'  : 'Sepulchre of the Unmarked Step - Undercroft',
                  'enemy' : 'Votary of Many Tongues',
                  'enemy' : 'Lamenting Vestal',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    X __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
               },
            'Sepulchre of the Unmarked Step - Funerary Parlour' : {
                  'west' : 'Sepulchre of the Unmarked Step - Foyer',
                  'north'  : 'Sepulchre of the Unmarked Step - Undercroft',
                  'enemy' : 'Votary of Many Tongues',
                  'enemy' : 'Lamenting Vestal',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ X
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'Sepulchre of the Unmarked Step - Undercroft' : {
                  'west' : 'Sepulchre of the Unmarked Step - Wasted Tomb',
                  'south'  : 'Sepulchre of the Unmarked Step - Funerary Parlour',
                  'boss' : 'The Choir of One',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ X
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'Vault of the Once-Whole - Foyer' : {
                  'west' : 'Vault of the Once-Whole - Gaolers Quarters',
                  'north' : 'Vault of the Once-Whole - Stockade',
                  'east'  : 'Hall of the Unnumbered Trials - North',
                  'enemy' : 'Chained Forlorn',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ X __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'Vault of the Once-Whole - Gaolers Quarters' : {
                  'east' : 'Vault of the Once-Whole - Foyer',
                  'north' : 'Vault of the Once-Whole - Gaol',
                  'enemy' : 'Chained Forlorn',
                  'enemy' : 'Blood-Fettered Veteran',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     X __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'Vault of the Once-Whole - Stockade' : {
                  'west' : 'Vault of the Once-Whole - Gaol',
                  'south' : 'Vault of the Once-Whole - Foyer',
                  'enemy' : 'Chained Forlorn',
                  'enemy' : 'Blood-Fettered Veteran',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     □ __ X    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'Vault of the Once-Whole - Gaol' : {
                  'south' : 'Vault of the Once-Whole - Gaolers Quarters',
                  'east' : 'Vault of the Once-Whole - Stockade',
                  'boss' : 'Ser Ulthric, Burdened of Names',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               □
               |
     X __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'The Silent Threshold' : {
                  'north' : 'The Atrium of Unmaking',
                  'south' : 'Hall of the Unnumbered Trials - North',
                  'desc'  : '''
============================================================================================================================================
You are alone in a vast, echoic chamber. The air is still, and yet you feel the eyes of previous adventurers upon you. In the centre of the 
room, there stands a lone door - a grand, imposing structure. There is no way to open it, but there seems to be a cavity inside - like a 
mortise. Something surely fits in here.

MAP:
               □
               |
     □ __ □    X    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
            'The Atrium of Unmaking' : {
                  'south' : 'The Silent Threshold',
                  'boss' : 'The Child Beyond Time',
                  'desc'  : '''
============================================================================================================================================
You are in a cave tunnel as fetid as the cell you just came from. There are two cave mouths. One to your east, and one to your south.
There are shuffling, moaning sounds coming from both directions.

MAP:
               X
               |
     □ __ □    □    □ __ □
     |    |    |    |    |
     □ __ □ __ □ __ □ __ □
               |   
     □ __ □ __ □ __ □ __ □
          |    |    |    |
     □ __ □    □    □ __ □
     |         |
□    □ __ □ __ □ __ □
|    |    |    |    |
□ __ □    □ __ □ __ □   
|    |
□ __ □

============================================================================================================================================''',
            },
         }

enemies = {
            'Feral Remnant' : {
                  'enemyHP' : 2,
                  'enemyATK'  : 3,
                },
            'Whispering Mistborn' : {
                  'enemyHP' : 4,
                  'enemyATK'  : 2,
                },
            'Fallen Adventurer' : {
                  'enemyHP' : 5,
                  'enemyATK'  : 4,
                },
            'Chained Forlorn' : {
                  'enemyHP' : 5,
                  'enemyATK'  : 3,
                },
            'Blood-Fettered Veteran' : {
                  'enemyHP' : 4,
                  'enemyATK'  : 6,
                },
            'Lamenting Vestal' : {
                  'enemyHP' : 3,
                  'enemyATK'  : 5,
                },
            'Votary of Many Tongues' : {
                  'enemyHP' : 5,
                  'enemyATK'  : 3,
                },
            'Grasp of Many' : {
                  'enemyHP' : 8,
                  'enemyATK'  : 2,
                },
            'Half-Born Remnant' : {
                  'enemyHP' : 2,
                  'enemyATK'  : 3,
                },
            'Husk of Knowing' : {
                  'enemyHP' : 3,
                  'enemyATK'  : 2,
                },
            'Vessel of Errant Insight' : {
                  'enemyHP' : 5,
                  'enemyATK'  : 4,
                },
}

bosses = {
            'The Maw of Gentle Regret' : {
                  'enemyHP' : 15,
                  'enemyATK'  : 4,
                },
            'Lady Vestige, the Bound Echo' : {
                  'enemyHP' : 4,
                  'enemyATK'  : 2,
                },
            'The Choir of One' : {
                  'enemyHP' : 5,
                  'enemyATK'  : 4,
                },
            'Ser Ulthric, Burdened of Names' : {
                  'enemyHP' : 5,
                  'enemyATK'  : 3,
                },
            'The Child Beyond Time' : {
                  'enemyHP' : 5,
                  'enemyATK'  : 4,
                },
}

weapons = {
            'Broken Sword' : {
                  'weapondamage' : 2,
                },
            'Whispering Mistborn' : {
                  'weapondamage' : 4,
                  'enemyATK'  : 2,
                },
            'Fallen Adventurer' : {
                  'weapondamage' : 5,
                  'enemyATK'  : 4,
                },
            'Chained Forlorn' : {
                  'weapondamage' : 5,
                  'enemyATK'  : 3,
                },
            'Blood-Fettered Veteran' : {
                  'weapondamage' : 4,
                  'enemyATK'  : 6,
                },
            'Lamenting Vestal' : {
                  'weapondamage' : 3,
                  'enemyATK'  : 5,
                },
            'Acolyte of Many Tongues' : {
                  'weapondamage' : 5,
                  'enemyATK'  : 3,
                },
            'Grasp of Many' : {
                  'weapondamage' : 8,
                  'enemyATK'  : 2,
                },
            'Half-Born Remnant' : {
                  'weapondamage' : 2,
                  'enemyATK'  : 3,
                },
}


#spawn area
currentRoom = 'Cave Cell'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'action'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  action = ''
  while action == '':
    action = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  action = action.lower().split(" ", 1)

  #if they type 'go' first
  if action[0] == 'go':
    #check that they are allowed wherever they want to go
    if action[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][action[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if action[0] == 'get' :
    if "item" in rooms[currentRoom] and action[1] in rooms[currentRoom]['item']:
      inventory.append(action[1])
      print(action[1] + ' acquired.')
      del rooms[currentRoom]['item']
    else:
      print('Can\'t get ' + action[1] + '!')

  #if they type 'attack' first
  if action[0] == 'attack' :
    if "enemy" in rooms[currentRoom] and action[1] in rooms[currentRoom]['enemy']:
    #   startCombat()
      print(action[1] + ' defeated!')
      del rooms[currentRoom]['enemy']
    else:
      print('Can\'t do ' + action[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break