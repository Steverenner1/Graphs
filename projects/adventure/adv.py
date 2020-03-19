from room import Room
from player import Player
from world import World
from graph import Graph
from utils import Stack
from utils import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
reversed_traversal_path = []
# path = []
# rooms_past = {}

# rooms_past[0] = player.current_room
# rooms_past[player.current_room.id] = player.current_room

# while len(rooms_past) < len(room_graph) - 1:
#     if player.current_room.id not in rooms_past:
#         rooms_past[player.current_room.id] = player.current_room
#         next_direction = path[-1]
#         rooms_past[player.current_room.id].remove(next_direction)

#     while len(rooms_past[player.current_room.id]) < 1:
#         next_direction = path.pop()
#         traversal_path.append(next_direction)
#         player.travel(next_direction)

#     move_forward = rooms_past[player.current_room.id].pop(0)
#     traversal_path.append(move_forward)
#     path.append(directions[move_forward])
#     player.travel(move_forward)


# def path_traverse():
#     visited = {}
#     totalRooms = len(room_graph)
#     rooms_visited = 0

#     while rooms_visited < totalRooms:
#         current_room = player.current_room.id

#         exits = player.current_room.get_exits()
#         for e in exits:
#             visited[current_room] = { dir:"?"}

#         rooms_visited += 1

# path_traverse()
opposite_direction = {"n":"s", "s":"n", "e":"w", "w":"e"}

# Start with empty list
# Iterate through current rooms and find valid exits
# Make sure there are no duplicates
# Append valid exits
# Use exits function in traversal function

def find_exits(current_room, visited):
    valid_exits = []
    for exit in current_room.get_exits():
        if exit in room_graph[current_room.id][1]:
            if room_graph[current_room.id][1][exit] not in visited:
                valid_exits.append(exit)
    return valid_exits


# Add first room to visited category
# Count variable declaration
# Grab the reversed traversal
# Get copy of current room and loop through room ID's
# Iterate over directions in current rooms that have valid exits
# Append to visited list
# Handle opposite direction (reverse traversal)
# Player moves to current room
# Invoke function

def traverse_maze():
    visited = set()
    visited.add(player.current_room.id)
    reversed_traversal_path = []
    
    while len(visited) < len(room_graph.keys()):
        current_room = player.current_room.id        
        valid_exits = find_exits(player.current_room, visited)
        print(valid_exits)

        if len(valid_exits) > 0:
            for direction in valid_exits:
                visited.add(room_graph[current_room][1][direction])
                traversal_path.append(direction)
                reversed_traversal_path.append(opposite_direction[direction])
                player.travel(direction)
                # skip else statement if one is found
                break
        else:
            print(reversed_traversal_path)
            direction = reversed_traversal_path.pop()
            player.travel(direction)
            traversal_path.append(direction)
traverse_maze()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)



for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
