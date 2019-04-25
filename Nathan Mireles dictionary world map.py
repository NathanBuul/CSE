world_map = {
    'PARK': {
        'NAME': "A Parking Lot",
        'DESCRIPTION': "There are 2 cars parked here",
        'PATHS': {
            'WEST': "ENTRANCE"
        }
    },
    'ENTRANCE': {
        'NAME': "Entrance To House",
        'DESCRIPTION': "This is the entrance to the house",
        'PATHS': {
            'WEST': 'HALLWAY',
            "EAST": "PARK"

        }
    },
    'HALLWAY': {
        'NAME': "Hallway",
        'DESCRIPTION': "This leads to a bathroom",
        'PATHS': {
            'WEST': 'BATHROOM',
            'EAST': 'ENTRANCE'
        }
    },
    'BATHROOM': {
        'NAME': "Bathroom",
        'DESCRIPTION': "This is a bathroom that could possibly have a weapon",
        'PATHS': {
            'EAST': 'HALLWAY',

        }
    },
    'KITCHEN': {
        'NAME': "Kitchen",
        'DESCRIPTION': "This is where they keep their food. They also store knives here",
        'PATHS': {
            'EAST': 'BEDROOM',
            'WEST': 'DINING ROOM',
            'NORTH': 'BACKYARD'
        }
    },
    'BEDROOM': {
        'NAME': "Bedroom 1",
        'DESCRIPTION': 'There is nothing but a toilet, sink, and shower in here. There might be weapons here',
        'PATHS': {
            'NORTH': 'UPSTAIRS',
            'WEST': 'KITCHEN'
        }
    },
    'UPSTAIRS': {
        'NAME': "Upstairs",
        'DESCRIPTION': "These stairs go up",
        'PATHS': {
            'NORTH': 'CORNER',
            'SOUTH': 'UPSTAIRS'

        }
    },
    'CORNER': {
        'NAME': "Corner",
        'DESCRIPTION': "There is a weapon in here",
        'PATHS': {
            'WEST': 'BEDROOM 2',
            'SOUTH': 'UPSTAIRS'
        }
    },
    'BEDROOM 2': {
        'NAME': "Bedroom 2",
        'DESCRIPTION': "This is the second bedroom of the house",
        'PATHS': {
            'EAST': 'CORNER',
            'NORTH': 'BATHROOM 2'
        }
    },
    'BATHROOM 2': {
        'NAME': "Bathroom",
        'DESCRIPTION': "This is the second bathroom of the house. There are no weapons here",
        'PATHS': {
            'SOUTH': 'BEDROOM 2'
        }
    },
    'GARDEN': {
        'NAME': "Garden",
        'DESCRIPTION': "This is a garden",
        'PATHS': {
            'NORTH': 'POOL',
            'SOUTH': 'GARDEN',
            'EAST': 'SHED'

        }
    },
    'POOL': {
        'NAME': "Pool",
        'DESCRIPTION': "This is a pool",
        'PATHS': {
            'SOUTH': 'GARDEN'
        }
    },
    'SHED': {
        'NAME': 'Shed',
        'DESCRIPTION': 'This is a shed with weapons in it',
        'PATHS': {
            'WEST': 'GARDEN'
        }
    },
    'BATHROOM_3': {
        'NAME': "Bathroom",
        'DESCRIPTION': "This is the first bathroom of the house",
        'PATHS': {
            'EAST': 'HALLWAY'
        }
    },
    'BACKYARD': {
        'NAME': "Bathroom",
        'DESCRIPTION': "This is the backyard, and it's huge!!",
        'PATHS': {
            'SOUTH': 'KITCHEN',
            'NORTH': 'GARDEN'
        }
    }

},

# other variables
directions = {"NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"}
current_node = world_map["PARK"]   # this is your current location
playing = True


while playing:
    print(current_node['NAME'])
    command = input(">_")
    if command in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I cannot go that way.")

    else:
        print("Command not recognized.")
