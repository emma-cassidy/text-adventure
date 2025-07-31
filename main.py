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
===============================================
Select your starting character:
  Cleric - 8HP, 2 Strength, 2 Luck 
  Warrior - 5HP, 5 Strength, 0 Luck
  Rogue - 5HP, 2 Strength, 5 Luck
        
  Attack = (Strength x Weapon Damage) + Luck
===============================================
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
===============================================
Commands:
  go [direction] (north, south, east, west)
  get [item]     (item name)
  use [item]     (item name)
  attack [enemy]
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
  #show an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  #show an enemy if there is one
  if "enemy" in rooms[currentRoom]:
    print('There is a ' + rooms[currentRoom]['enemy'] + ' in here!')
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
                },

            'Cave Tunnel' : {
                  'north' : 'Cave Cell',
                  'south' : 'Cave Mouth - South',
                  'east'  : 'Cave Mouth - East',
                },
            'Cave Mouth South' : {
                  'south': 'Cliff Edge - West',
                  'north' : 'Cave Tunnel',
               },
            'Cave Mouth - East' : {
                  'west' : 'Cave Tunnel',
                  'north' : 'Cliff Ledge',
                  'south' : 'Cliff Edge - East',
               },
            'Cliff Edge - West' : {
                  'north' : 'Cave Mouth - South',
                  'east'  : 'Cliff Edge - East',
            },
            'Cliff Edge - East' : {
                  'west' : 'Cliff Edge - West',
                  'north' : 'Cave Mouth - East'
                },
            'Cliff Ledge' : {
                  'north' : 'Crack in the wall',
                  'south' : 'Cave Mouth - East',
                  'east'  : 'Wrought Iron Fence',
                },
            'Cave Mouth - South' : {
                  'south': 'Cliff Edge - West',
                  'north' : 'Cave Tunnel',
               },
            'Crack in the wall' : {
                  'south' : 'Cliff Ledge',
                  'east'  : 'The Maw Between Hours - Corridor',
            },
            'Wrought Iron Fence' : {
                  'west' : 'Cliff Ledge',
                  'south' : 'Graveyard',
                  'east'  : 'Garden',
               },
            'Graveyard' : {
                  'north' : 'Wrought Iron Fence',
                  'east'  : 'Disused Training Yard',
            },
            'Garden' : {
                  'west' : 'Wrought Iron Fence',
                  'north' : 'Foyer',
                  'south' : 'Disused Training Yard',
                  'east'  : 'Carriage House',
               },
            'Disused Training Yard' : {
                  'west' : 'Graveyard',
                  'north' : 'The Garden',
                  'east'  : 'Worn Barracks',
            },
            'Carriage House' : {
                  'west' : 'The Garden',
                  'south' : 'Worn Barracks',
               },
            'Worn Barracks' : {
                  'west' : 'Disused Training Yard',
                  'north' : 'Carriage House',
            },
            'Main Foyer' : {
                  'north' : 'Hall of the Unnumbered Trials - South',
                  'south' : 'The Garden',
               },
            'Hall of the Unnumbered Trials - South' : {
                  'west' : 'The Maw Between Hours - Foyer',
                  'north' : 'Hall of the Unnumbered Trials - North',
                  'south' : 'Main Foyer',
                  'east'  : 'The Cradle That Remembers - Foyer',
            },
            'The Maw Between Hours - Corridor' : {
                  'west' : 'Crack in the wall',
                  'north' : 'The Maw Between Hours - Foyer',
               },
            'The Maw Between Hours - Foyer' : {
                  'west' : 'The Maw Between Hours - Hall',
                  'south' : 'The Maw Between Hours - Corridor',
                  'east'  : 'Hall of the Unnumbered Trials - South',
               },
            'The Maw Between Hours - Hall' : {
                  'east'  : 'The Maw Between Hours - Foyer',
               },
            'The Cradle That Remembers - Foyer' : {
                  'west' : 'Hall of the Unnumbered Trials - South',
                  'south' : 'The Cradle That Remembers - Corridor',
                  'east'  : 'The Cradle That Remembers - Antechamber',
            },
            'The Cradle That Remembers - Corridor' : {
                  'north' : 'The Cradle That Remembers - Foyer',
                  'east'  : 'The Cradle That Remembers - Cradle',
            },
            'The Cradle That Remembers - Antechamber' : {
                  'west' : 'The Cradle That Remembers - Foyer',
                  'south' : 'The Cradle That Remembers - Cradle',
            },
            'The Cradle That Remembers - Cradle' : {
                  'west' : 'The Cradle That Remembers - Corridor',
                  'north' : 'The Cradle That Remembers - Antechamber',
               },
            'Hall of the Unnumbered Trials - North' : {
                  'west' : 'Vault of the Once-Whole - Foyer',
                  'north' : 'The Silent Threshold',
                  'south' : 'Hall of the Unnumbered Trials - South',
                  'east'  : 'Sepulchre of the Unmarked Step - Foyer',
            },
            'Sepulchre of the Unmarked Step - Foyer' : {
                  'west' : 'Hall of the Unnumbered Trials - North',
                  'north' : 'Sepulchre of the Unmarked Step - Wasted Tomb',
                  'east'  : 'Sepulchre of the Unmarked Step - Funerary Parlour',
               },
            'Sepulchre of the Unmarked Step - Wasted Tomb' : {
                  'south' : 'Sepulchre of the Unmarked Step - Foyer',
                  'east'  : 'Sepulchre of the Unmarked Step - Undercroft',
               },
            'Sepulchre of the Unmarked Step - Funerary Parlour' : {
                  'west' : 'Sepulchre of the Unmarked Step - Foyer',
                  'north'  : 'Sepulchre of the Unmarked Step - Undercroft',
            },
            'Sepulchre of the Unmarked Step - Undercroft' : {
                  'west' : 'Sepulchre of the Unmarked Step - Wasted Tomb',
                  'south'  : 'Sepulchre of the Unmarked Step - Funerary Parlour',
            },
            'Vault of the Once-Whole - Foyer' : {
                  'west' : 'Vault of the Once-Whole - Gaolers Quarters',
                  'north' : 'Vault of the Once-Whole - Stockade',
                  'east'  : 'Hall of the Unnumbered Trials - North',
            },
            'Vault of the Once-Whole - Gaolers Quarters' : {
                  'east' : 'Vault of the Once-Whole - Foyer',
                  'north' : 'Vault of the Once-Whole - Gaol',
            },
            'Vault of the Once-Whole - Stockade' : {
                  'west' : 'Vault of the Once-Whole - Gaol',
                  'south' : 'Vault of the Once-Whole - Foyer',
            },
            'Vault of the Once-Whole - Gaol' : {
                  'south' : 'Vault of the Once-Whole - Gaolers Quarters',
                  'east' : 'Vault of the Once-Whole - Stockade',
            },
            'The Silent Threshold' : {
                  'north' : 'The Atrium of Unmaking',
                  'south' : 'Hall of the Unnumbered Trials - North',
            },
            'The Atrium of Unmaking' : {
                  'south' : 'The Silent Threshold',
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
            'Acolyte of Many Tongues' : {
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
#start the player in the spawn area 
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