#My baby RPG lol

playerHP = 0
playerSTR = 0
playerLCK = 0
playerATK = 0
char_name = ""
char_class = ""
weapondamage = 1
finalbossturn = 1

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
placeholder = ""
maxHP = playerHP

def showInstructions():
  print(f'''
Welcome to EMMA RING, {char_class} {char_name}!
============================================================================================================================================
Commands:
  go [direction]       (north, south, east, west)
  get [item]           (item name)
  use [item]           (item name)
  map                  (shows map)
  attack [enemy]       (initiates combat)
============================================================================================================================================
''')

def showStatus():
    #print the player's current status
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('You are in the ' + currentRoom)
    #show current stats
    print(f'You have {playerHP} HP of a maximum {maxHP}, {playerSTR} strength, and {playerLCK} luck.')
    print(f'Your attack stat is {playerATK}.')
    #show the current inventory and equipment
    print('Inventory : ' + str(inventory))
    print('Equipment : ' + str(equipment))
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
        placeholder = rooms[currentRoom]['boss']
    if "boss" in rooms[currentRoom] and bosses[placeholder]['enemyHP'] > 20:
        print((bosses[placeholder]['bossdesc']))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


inventory = []
equipment = ["Bare Hands"]

rooms = {

            'Cave Cell' : {
                  'south' : 'Cave Tunnel',
                  'item'  : 'Broken Sword',
                  'desc'  : '''
============================================================================================================================================
You are in a dank, dark cave, with a broken chain at your feet. Your neck is sore, as if you were restrained by it. The only way to go 
is through the cave tunnel you see to your south.

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

============================================================================================================================================''',
                },
            'Cave Mouth - South' : {
                  'north' : 'Cave Tunnel',
                  'east'  : 'Cliff Edge - East',
                  'enemy' : 'Feral Remnant',
                  'desc'  : '''
============================================================================================================================================
The cave mouth faces out onto a sheer cliff opening. You see dark, cloudy skies for a few miles with crashing - yet silent - waves below.
In the distance beyond the cloud and waves you see an endless abyss of darkness, as if you the land on which you stand has been plucked from
elsewhere. To your north is the cave tunnel.

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

============================================================================================================================================''',
               },
            'Cliff Edge - East' : {
                  'north' : 'Cave Mouth - East',
                  'west'  : 'Cave Mouth - South',
                  'enemy' : 'Whispering Mistborn',
                  'desc'  : '''
============================================================================================================================================
You stand on the precipice, staring out into the silent darkness. There is no other way forward except back north to the cave mouth.

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

============================================================================================================================================''',
                },
            'Crack in the wall' : {
                  'south' : 'Cliff Ledge',
                  'east'  : 'The Maw Between Hours - Corridor',
                  'enemy' : 'Half-Born Remnant',
                  'item'  : 'Elixir of Flesh',
                  'desc'  : '''
============================================================================================================================================
From your location in the crevice of the thick stone wall, you notice what seems to be a grand corridor to your east. The air is pungent 
with rot and decay, punctured only by the fresh air flowing from the cliff ledge to your south. You hear movement in the building to your
east. 

============================================================================================================================================''',
            },
            'Wrought Iron Fence' : {
                  'west' : 'Cliff Ledge',
                  'south' : 'Graveyard',
                  'east'  : 'The Garden',
                  'desc'  : '''
============================================================================================================================================
From your position atop the wrought iron fence, to the east you spy what seems to be a derelict yet once loved garden, with a dried fountain, 
barren soil and withered trees. To your south there are unmistakeably graves whose inhabitants' names have been lost to time.

============================================================================================================================================''',
               },
            'Graveyard' : {
                  'north' : 'Wrought Iron Fence',
                  'east'  : 'Disused Training Yard',
                  'enemy' : 'Whispering Mistborn',
                  'item'  : 'Elixir of Flesh',
                  'desc'  : '''
============================================================================================================================================
The graveyard is full of tombstones of varying shapes and sizes, with some modern black marble and others crumbling sandstone and lime. They
have one thing in common - all have clearly been forgotten - but appear to be those of heroes, judging from the decayed and rusted weapons
and shields littered around them in tribute. The iron fence is to your north, and to your east you see a disused training yard.

============================================================================================================================================''',
            },
            'The Garden' : {
                  'west' : 'Wrought Iron Fence',
                  'north' : 'Main Foyer',
                  'south' : 'Disused Training Yard',
                  'east'  : 'Carriage House',
                  'enemy' : 'Whispering Mistborn',
                  'desc'  : '''
============================================================================================================================================
You stand in the remains of a once-loved garden, evidenced by the dried earth of the former flower beds that garnished the mossy cobble path and
surround the bases of the corpses of trees. West is the iron fence, south is an old training yard, and east appears to be a derelict carriage
house. Directly north is a grand entryway into what appears to be some kind of manor or castle. The arched ironwood door is an anomaly among 
the blatant disrepair, standing tall and imposing, as sound and polished as the day it was made. The carvings of the tympanum above are
unintelligble, however.

============================================================================================================================================''',
               },
            'Disused Training Yard' : {
                  'west' : 'Graveyard',
                  'north' : 'The Garden',
                  'east'  : 'Worn Barracks',
                  'enemy' : 'Fallen Adventurer',
                  'item'  : 'Rusted Axe',
                  'desc'  : '''
============================================================================================================================================
Rotten straw men lay strewn across the ground, clearly having been target practice in the past, surrounded by an assortment of old weapons.
To the west lays the graveyard, and to the east, an old barracks building. North is the garden.

============================================================================================================================================''',
            },
            'Carriage House' : {
                  'west' : 'The Garden',
                  'south' : 'Worn Barracks',
                  'item'  : 'Elixir of Soul',
                  'desc'  : '''
============================================================================================================================================
The carriage house must have been a grand affair once, its simple design disguising the use of elegant woods in its construction. Rusted
troughs lay to one side where horses must have been fed and watered by their coachmen. There are no signs of any vehicle or animal now save
for a bent old wheel to one side in the dusty building. Looking out west, you see the garden and to the south, a similarly dusty barracks.

============================================================================================================================================''',
               },
            'Worn Barracks' : {
                  'west' : 'Disused Training Yard',
                  'north' : 'Carriage House',
                  'enemy' : 'Feral Remnant',
                  'item'  : 'Steel Greatsword',
                  'desc'  : '''
============================================================================================================================================
You step through the splinters that were once a door into a musty old barracks. Its a relatively small affair, with space and lodgings for
no more than ten guards. There are still a few mouldy hay mattresses dotted around, and an assortment of old weaponry. West lays the training
yard, and to the north is the carriage house.

============================================================================================================================================''',
            },
            'Main Foyer' : {
                  'north' : 'Hall of the Unnumbered Trials - South',
                  'south' : 'The Garden',
                  'enemy' : 'Whispering Mistborn',
                  'desc'  : '''
============================================================================================================================================
The foyer seems out of place compared to outside - barring a little dust, it looks relatively modern, with ornate wainscoting in a lush dark
wood with lighter appliques surrounding the doorway to the garden in the south and a similar doorway to the north. 

============================================================================================================================================''',
               },
            'Hall of the Unnumbered Trials - South' : {
                  'west' : 'The Maw Between Hours - Foyer',
                  'north' : 'Hall of the Unnumbered Trials - North',
                  'south' : 'Main Foyer',
                  'east'  : 'The Cradle That Remembers - Foyer',
                  'desc'  : '''
============================================================================================================================================
The wainscoting of the main foyer continues in to a grand hall, so large you are almost unable to see the northern end. Along the walls above the
wooden pannelling are stonecarved reliefs of figures, each wearing distinct attire and armour - as if in rememberance of previous heroes to tread
the same path you are on. There is an empty space, waiting for its next inhabitant. There are two doors, one to the west and one to the east.
To the north, there seem to be two more, similarly on each side.

============================================================================================================================================''',
            },
            'The Maw Between Hours - Corridor' : {
                  'west' : 'Crack in the wall',
                  'north' : 'The Maw Between Hours - Foyer',
                  'enemy' : 'Half-Born Remnant',
                  'item'  : 'Elixir of Soul',
                  'desc'  : '''
============================================================================================================================================
The thick miasma of stench tainted by decay almost overwhelms you, but the gentle breeze through the crack in the west wall aids in your
resolve. The otherwise fine hallway leads north to the foyer.

============================================================================================================================================''',
               },
            'The Maw Between Hours - Foyer' : {
                  'west' : 'The Maw Between Hours - Hall',
                  'south' : 'The Maw Between Hours - Corridor',
                  'east'  : 'Hall of the Unnumbered Trials - South',
                  'enemy' : 'Grasp of Many',
                  'desc'  : '''
============================================================================================================================================
The repugnant stench of decay and despair becomes suffocating as you near its source. To the east, you see the door back to the vast hall of
other doors, and to your south, the corridor with a crack in the wall to the outside. West lays a grand hall, where the source of the
miasma appears to be.

============================================================================================================================================''',
               },
            'The Maw Between Hours - Hall' : {
                  'east'  : 'The Maw Between Hours - Foyer',
                  'boss' : 'The Maw of Gentle Regret',
                  'desc'  : '''
============================================================================================================================================
The hall must once have been a grand dining room, the polished marbled floor thick with a sludge that has the taint of rotten flesh and
blood. The furniture, what is left of it, has all been swept to one side and there are distinct long bones of discarded limbs scattered
amongst the filth.

============================================================================================================================================''',
               },
            'The Cradle That Remembers - Foyer' : {
                  'west' : 'Hall of the Unnumbered Trials - South',
                  'south' : 'The Cradle That Remembers - Corridor',
                  'east'  : 'The Cradle That Remembers - Antechamber',
                  'enemy' : 'Husk of Knowing',
                  'item'  : 'Heavy Mace',
                  'desc'  : '''
============================================================================================================================================
This foyer has a lilting sadness somehow upon it. Lost books litter the floor, as if discarded in a hurry by someone searching for answers 
of the utmost import. To the south is a corridor, and to the east, an antechamber of some kind. To the west lays the long hallway of doors
and forgotten faces.

============================================================================================================================================''',
            },
            'The Cradle That Remembers - Corridor' : {
                  'north' : 'The Cradle That Remembers - Foyer',
                  'east'  : 'The Cradle That Remembers - Cradle',
                  'enemy' : 'Husk of Knowing',
                  'enemy' : 'Vessel of Errant Insight',
                  'item'  : 'Elixir of Flesh',
                  'desc'  : '''
============================================================================================================================================
Various faded artworks detail the walls, masking some of the faded silken wallpaper. There are indecipherable scrawls along the walls at
intervals that appear to have been written at different times from the shades of the ink, yet strangely all with the same hand. To the east 
the hall opens into a grand library, and to the north the foyer that leads back to the hall.

============================================================================================================================================''',
            },
            'The Cradle That Remembers - Antechamber' : {
                  'west' : 'The Cradle That Remembers - Foyer',
                  'south' : 'The Cradle That Remembers - Cradle',
                  'enemy' : 'Husk of Knowing',
                  'enemy' : 'Vessel of Errant Insight',
                  'item'  : 'Elixir of Soul',
                  'desc'  : '''
============================================================================================================================================
Old and overused furniture is strewn around the antechamber as if someone had been living here for a very long time. Stacks upon stacks of
books surround the various seats like someone had worn out each in turn whilst searching for answers. To the south lays a grand library, and
to the west, the foyer that leads back to the main hall.

============================================================================================================================================''',
            },
            'The Cradle That Remembers - Cradle' : {
                  'west' : 'The Cradle That Remembers - Corridor',
                  'north' : 'The Cradle That Remembers - Antechamber',
                  'boss' : 'Lady Vestige, the Bound Echo',
                  'desc'  : '''
============================================================================================================================================
The library houses thousands, if not more, books that once lurked on their many shelves. Cobwebs and filth cover most of the room, save for
a corner where there had recently been activity. A solitary desk stands alone, covered in reams of parchment decorated in the same archaic
script that adorns the walls of the corridor to the west. To the north lays the antechamber where someone had clearly been residing.

============================================================================================================================================''',
               },
            'Hall of the Unnumbered Trials - North' : {
                  'west' : 'Vault of the Once-Whole - Foyer',
                  'north' : 'The Silent Threshold',
                  'south' : 'Hall of the Unnumbered Trials - South',
                  'east'  : 'Sepulchre of the Unmarked Step - Foyer',
                  'desc'  : '''
============================================================================================================================================
The north end of the grand hall is as painstakingly decorated as its southern counterpart. The carved reliefs of heroes past continue to
adorn the walls above the familiar dark wainscoting - is that a hint of sadness you see on the faces? There are two doors, one to the west 
and one to the east. Back south, you can vaguely make out the same in the darkness.

============================================================================================================================================''',
            },
            'Sepulchre of the Unmarked Step - Foyer' : {
                  'west' : 'Hall of the Unnumbered Trials - North',
                  'north' : 'Sepulchre of the Unmarked Step - Wasted Tomb',
                  'east'  : 'Sepulchre of the Unmarked Step - Funerary Parlour',
                  'enemy' : 'Votary of Many Tongues',
                  'desc'  : '''
============================================================================================================================================
This foyer has an uncanny stillness about it - the stillness of the dead. To the north lies a suspciously empty room, and to the east, a room
with some form of workstation. The west holds the door returning to the hall.

============================================================================================================================================''',
               },
            'Sepulchre of the Unmarked Step - Wasted Tomb' : {
                  'south' : 'Sepulchre of the Unmarked Step - Foyer',
                  'east'  : 'Sepulchre of the Unmarked Step - Undercroft',
                  'enemy' : 'Votary of Many Tongues',
                  'enemy' : 'Lamenting Vestal',
                  'item'  : 'Elixir of Flesh',
                  'desc'  : '''
============================================================================================================================================
Other than what appears to be an empty stone casket laying on a flagstone floor, there is nothing of note in this dusty room. The foyer is
back to the south, and to the east you can make of the distinctive vaulted appearance of an undercroft.

============================================================================================================================================''',
               },
            'Sepulchre of the Unmarked Step - Funerary Parlour' : {
                  'west' : 'Sepulchre of the Unmarked Step - Foyer',
                  'north'  : 'Sepulchre of the Unmarked Step - Undercroft',
                  'enemy' : 'Votary of Many Tongues',
                  'enemy' : 'Lamenting Vestal',
                  'item'  : 'Elixir of Flesh',
                  'desc'  : '''
============================================================================================================================================
What appeared to simply be a workstation seems to actually be a preparation station for... bodies. A large marble slab sits pride of place
in the centre and is covered with blackened red stains. To one side there are shelves, with various dusty containers, and fine tools perhaps
for stripping flesh from bone. There is a painting on the slab, eerily similar to the faces in the reliefs of the grand hallway, almost as 
if to be used as a reference. To the north lays the vaulted arches of an undercroft, and to the west the foyer back to the main hall.

============================================================================================================================================''',
            },
            'Sepulchre of the Unmarked Step - Undercroft' : {
                  'west' : 'Sepulchre of the Unmarked Step - Wasted Tomb',
                  'south'  : 'Sepulchre of the Unmarked Step - Funerary Parlour',
                  'boss' : 'The Choir of One',
                  'desc'  : '''
============================================================================================================================================
You stand in the middle of a grand, vaulted room that houses sacks of materials in the corners. They spill out, seeming to be a cement of
some description. Alongside them, there are a couple of skeletons in old ragged armour whose faces have been perfectly preserved as if alive
yet smothered in plaster.

============================================================================================================================================''',
            },
            'Vault of the Once-Whole - Foyer' : {
                  'west' : 'Vault of the Once-Whole - Gaolers Quarters',
                  'north' : 'Vault of the Once-Whole - Stockade',
                  'east'  : 'Hall of the Unnumbered Trials - North',
                  'enemy' : 'Chained Forlorn',
                  'item'  : 'Steel Warhammer',
                  'desc'  : '''
============================================================================================================================================
The rough cut stone floor of the foyer is marked with scratches and deep gouges, as if a battle had taken place here long before. Stale yet
still liquid blood congeals underfoot. To the west is a small room that perhaps once housed a guard, and to the north you see some makeshift
fortifications as if against some threat further inside. Back east lays the door to the main hall.

============================================================================================================================================''',
            },
            'Vault of the Once-Whole - Gaolers Quarters' : {
                  'east' : 'Vault of the Once-Whole - Foyer',
                  'north' : 'Vault of the Once-Whole - Gaol',
                  'enemy' : 'Chained Forlorn',
                  'enemy' : 'Blood-Fettered Veteran',
                  'item'  : 'Elixir of Flesh',
                  'desc'  : '''
============================================================================================================================================
The small guardsman's room must have once been the quarters of a gaoler, with a heavyset barred door to the north. Discarded, rusted chains
litter the floor and it looks as if something has broken out of them. Away from this, east leads back to the foyer.

============================================================================================================================================''',
            },
            'Vault of the Once-Whole - Stockade' : {
                  'west' : 'Vault of the Once-Whole - Gaol',
                  'south' : 'Vault of the Once-Whole - Foyer',
                  'enemy' : 'Chained Forlorn',
                  'enemy' : 'Blood-Fettered Veteran',
                  'item'  : 'Elixir of Soul',
                  'desc'  : '''
============================================================================================================================================
The walls surrounding the stockade are similarly slashed and gouged to the foyer to the south, and the congealing blood is spattered across 
the thick planks that were once used to block something in. There is, however, a way forward to the west.

============================================================================================================================================''',
            },
            'Vault of the Once-Whole - Gaol' : {
                  'south' : 'Vault of the Once-Whole - Gaolers Quarters',
                  'east' : 'Vault of the Once-Whole - Stockade',
                  'boss' : 'Ser Ulthric, Burdened of Names',
                  'desc'  : '''
============================================================================================================================================
The gaol of an ancient soldier is littered with corpses of would-be adventurers that came before you, their skulls wrenched from their 
shoulders and scattered amongst the broken chains and old weapons.

============================================================================================================================================''',
            },
            'The Silent Threshold' : {
                  'south' : 'Hall of the Unnumbered Trials - North',
                  'desc'  : '''
============================================================================================================================================
You are alone in a vast, echoic chamber. The air is still, and yet you feel the eyes of previous adventurers upon you. In the centre of the 
room, there stands a lone door - a grand, imposing structure. There is no way to open it, but there seems to be a cavity inside - like a 
mortise. Something surely fits in here.

============================================================================================================================================''',
            },
            'The Atrium of Unmaking' : {
                  'south' : 'The Silent Threshold',
                  'boss' : 'The Child Beyond Time',
                  'desc'  : '''
============================================================================================================================================

============================================================================================================================================''',
            },
         }
#HP remnant 2
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
                  'enemyHP' : 21,
                  'enemyATK'  : 2,
                  'bosskey'  : 'Tenon of Many Ends',
                  'bossdesc' : '''
Stitched from ambition and error, this slithering mockery of heroism hungers for meaning.
It wears their armor, their limbs, their hopes - all rotting beneath the weight of shared failure.
So many came seeking purpose. Together, they found something worse.

All who enter are remembered. None as themselves. Purpose decays. But hunger persists.''',
                  'bosskeydesc' : 'Knotted bone and glimmering ash. It does not fit cleanly into any shape- but somehow, it belongs.',
                },
            'Lady Vestige, the Bound Echo' : {
                  'enemyHP' : 20,
                  'enemyATK'  : 3,
                  'bosskey'  : 'Tenon of Unspoken Shapes',
                  'bossdesc' : '''
Once a seeker of escape through knowledge, she unmade herself word by word.
Now bound in thought and thin as parchment, she whispers truths no mind should carry.
She read until there was no more ‘she’ left to read.

She sought the way out, and became the door. In knowing everything, she forgot what she was.''',
                  'bosskeydesc' : 'Carved with symbols that shift when not observed. Cold to the touch, yet burns with withheld meaning.',
                },
            'The Choir of One' : {
                  'enemyHP' : 35,
                  'enemyATK'  : 5,
                  'bosskey'  : 'Tenon of Hollow Praise',
                  'bossdesc' : '''
A broken cleric who sang to silence until silence sang back.
Now a choir of mouths and madness, it praises a god that answers only in echoes.
There were no others to join the hymn. So, it made them.

Sing loud enough, and the silence will sing back.''',
                  'bosskeydesc' : 'Pale and resonant, it hums faintly with voices not your own. Some still believe it is listening.',
                },
            'Ser Ulthric, Burdened of Names' : {
                  'enemyHP' : 35,
                  'enemyATK'  : 5,
                  'bosskey'  : 'Tenon of Broken Oaths',
                  'bossdesc' : '''
Once a proud champion entombed by his own honours, Ulthric was left to rot in chains he forged with valour.
Now, a beast of instinct, he swings in defiance of a past no longer his.
They built walls to keep him safe. Or was it to keep him in?

Chains may break. But the burden remains. He remembers only the oath. Not who he swore it to.''',
                  'bosskeydesc' : 'A heavy shard of forged steel, stained and splintered. It bears the weight of forgotten vows.',
                },
            'The Child Beyond Time' : {
                  'enemyHP' : 40,
                  'enemyATK'  : 6,
                  'bossdesc'  :'''
The lock turns not with a key, but with surrender. You are not the first. You were simply next.

You step forward into nothing- a formless, infinite void that swallows all sound, all light, all meaning.

There is no floor, yet you do not fall.
There are no walls, yet something watches.

The air shimmers faintly with the echo of voices you don’t remember having,
names you’ve almost spoken, and faces you’ve almost known.

Far ahead, a figure stands- not tall, not grand, but small.
A silhouette of something childlike, flickering between shapes like a stuttering memory.
One moment draped in rags, the next in ruined armour, then nothing at all.
It doesn’t look at you—but you know it knows you’re here.

Fragments of past rooms briefly coalesce in the distance-
a broken chain, a plaster face, a discarded helm, a singed page
and are gone again.

This is the place the maze was built to hide.

This is where it ends.
Or begins.
'''
                },
}

weapons = {
            'Broken Sword' : {
                  'weapondamage' : 2,
                },
            'Rusted Axe' : {
                  'weapondamage' : 3,
                },
            'Steel Greatsword' : {
                  'weapondamage' : 4,
                },
            'Heavy Mace' : {
                  'weapondamage' : 5,
                },
            'Steel Warhammer' : {
                  'weapondamage' : 6,
                },
}

finalbosstext = {
            1 : '''"You have come far. Or rather, you have come again."''',
            2 : '''"You were always meant to arrive. That is why they were chosen. Do you recognize them? No… you wouldn’t yet.”''',
            3 : '''“We’ve done this before. We’ll do it again. One of us must be free.”''',
}
#spawn area is cave cell; change to wherever you need to go for debugging :)))
currentRoom = 'The Maw Between Hours - Foyer'

showInstructions()

#loop forever
while True:
  playerATK = (playerSTR * weapondamage) + playerLCK
  showStatus()

  #get the player's next 'action'
  #.split() breaks it up into a list array
  #eg typing 'go east' would give the list:
  #['go','east']
  action = ''
  while action == '':
    action = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  action = action.split(" ", 1)

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


  #to use an item
  if action[0] == 'use' :
    if "item" in rooms[currentRoom] and action[1] in rooms[currentRoom]['item']:
      print(action[1] + ' must be picked up first!')
    elif action[1] in inventory and action[1] == 'Elixir of Soul':
      maxHP += 2
      playerHP = maxHP
      inventory.remove('Elixir of Soul')
    elif action[1] in inventory and action[1] == 'Elixir of Flesh':
      playerSTR += 1
      inventory.remove('Elixir of Flesh')
    elif action[1] in weapons and action[1] in inventory:
      inventory.append(equipment[0])
      equipment.clear()
      equipment.append(action[1])
      inventory.remove(action[1])
      weapondamage = weapons[action[1]]['weapondamage']
    else:
      print('Can\'t use ' + action[1] + '!')
      
  #show map
  if action[0] == 'map' :
    print('''
          
MAP:
               □
               |
     □ __ □    □    □ __ □             X = Start
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
          
          '''
)


  #if they type 'attack'
  if action[0] == 'attack' :
      if "enemy" in rooms[currentRoom] and action[1] in rooms[currentRoom]['enemy']:
          print(action[1] + ' has '+ str(enemies[action[1]]['enemyHP']) +' HP and ' + str(enemies[action[1]]['enemyATK']) + ' attack.')
          if enemies[action[1]]['enemyHP'] <= playerATK:
              print(action[1] + ' defeated!')
              del rooms[currentRoom]['enemy']
              playerHP -= enemies[action[1]]['enemyATK']
              print('Health decreased by ' + str(enemies[action[1]]['enemyATK']) + '!')
          if playerHP <= 0:
              print("YOU DIED.")
              break
          elif enemies[action[1]]['enemyHP'] > playerATK:
              enemies[action[1]]['enemyHP'] -= playerATK
              print(action[1] + ' health decreased by ' + str(playerATK))
              playerHP -= enemies[action[1]]['enemyATK']
              print('Health decreased by ' + str(enemies[action[1]]['enemyATK']) + '!')
              if playerHP <= 0:
                  print("YOU DIED.")
                  break
      elif playerHP <= 0:
          print("YOU DIED.") 
          break
      elif "boss" in rooms[currentRoom] and action[1] in rooms[currentRoom]['boss']:
          print(action[1] + ' has '+ str(bosses[action[1]]['enemyHP']) +' HP and ' + str(bosses[action[1]]['enemyATK']) + ' attack.')
          if bosses[action[1]]['enemyHP'] <= playerATK:
              print(action[1] + ' defeated!')
              del rooms[currentRoom]['boss']
              inventory.append(bosses[action[1]]['bosskey'])
              print(bosses[action[1]]['bosskey'] + ' added to inventory!')
              print(bosses[action[1]]['bosskeydesc'])
              playerHP -= bosses[action[1]]['enemyATK']
              print('Health decreased by ' + str(bosses[action[1]]['enemyATK']) + '!')
          if bosses[action[1]]['enemyHP'] == 0:
              inventory.append(bosses[action[1]]['bosskey'])
              print(bosses[action[1]]['bosskeydesc'])
              if playerHP <= 0:
                  print("YOU DIED.")
                  break
              del rooms[currentRoom]['boss']
          elif bosses[action[1]]['enemyHP'] > playerATK:
              bosses[action[1]]['enemyHP'] -= playerATK
              print(action[1] + ' health decreased by ' + str(playerATK))
              playerHP -= bosses[action[1]]['enemyATK']
              print('Health decreased by ' + str(bosses[action[1]]['enemyATK']) + '!')
              if playerHP <= 0:
                  print("YOU DIED.")
                  break
      elif "boss" in rooms[currentRoom] == "The Child Beyond Time":
          print(action[1] + ' has '+ str(bosses[action[1]]['enemyHP']) +' HP and ' + str(bosses[action[1]]['enemyATK']) + ' attack.')
          if finalbossturn == 1:
             print(finalbosstext[1])
          if finalbossturn == 2:
             print(finalbosstext[2])
          if finalbossturn == 3:
             print(finalbosstext[3])
          if finalbossturn >= 4:
             print("")
          if bosses[action[1]]['enemyHP'] <= playerATK:
              print(action[1] + ''' has been defeated... for now.
A voice whispers in the darkness:
                    
“You’ll need new guards.”
                    
“Find others. From other whens. Make them strong.”
                    
“Soon... you’ll forget this was you.”
                    ''')
              del rooms[currentRoom]['boss']
              playerHP -= bosses[action[1]]['enemyATK']
              print('Health decreased by ' + str(bosses[action[1]]['enemyATK']) + '!')
              if playerHP <= 0:
                  print("YOU DIED.")
                  break
              del rooms[currentRoom]['boss']
          elif bosses[action[1]]['enemyHP'] > playerATK:
              bosses[action[1]]['enemyHP'] -= playerATK
              print(action[1] + ' health decreased by ' + str(playerATK))
              playerHP -= bosses[action[1]]['enemyATK']
              print('Health decreased by ' + str(bosses[action[1]]['enemyATK']) + '!')
              finalbossturn += 1
              if playerHP <= 0:
                  print("YOU DIED.")
                  break
      else:
        print('Can\'t do ' + action[1] + '!')


  
  #   #gain items to progress from the bosses
  # if action[0] == 'attack' :
  #   if "boss" in rooms[currentRoom] and action[1] in rooms[currentRoom]['boss']:
  #     if bosses[action[1]]['enemyHP'] == 0:
  #       inventory.append(bosses[action[1]]['bosskey'])
  #       print(bosses[action[1]]['bosskeydesc'])


      
  # ## Define how a player can win
  # if currentRoom == 'The Silent Threshold' and 'key' in inventory and 'potion' in inventory:
  #   print('''
  # ============================================================================================================================================
# The tenon pieces in your inventory seem to resonate with the grand door, and you pull them out and slot them into
# the mortise. The door opens slowly without a sound, and your breath catches in your throat as you tep through.
# ============================================================================================================================================'''
#   #   break

#   # ## If a player enters a room with a monster
#   # elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
#   # #   print('A monster has got you... GAME OVER!')
#   #   break