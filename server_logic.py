import random
from typing import List, Dict
import math

"""
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""


def avoid_my_neck(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:
    """
    my_head: Dictionary of x/y coordinates of the Battlesnake head.
            e.g. {"x": 0, "y": 0}
    my_body: List of dictionaries of x/y coordinates for every segment of a Battlesnake.
            e.g. [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]
    possible_moves: List of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]

    return: The list of remaining possible_moves, with the 'neck' direction removed
    """
    my_neck = my_body[1]  # The segment of body right after the head is the 'neck'

    if my_neck["x"] < my_head["x"]:  # my neck is left of my head
        possible_moves.remove("left")
    elif my_neck["x"] > my_head["x"]:  # my neck is right of my head
        possible_moves.remove("right")
    elif my_neck["y"] < my_head["y"]:  # my neck is below my head
        possible_moves.remove("down")
    elif my_neck["y"] > my_head["y"]:  # my neck is above my head
        possible_moves.remove("up")

    return possible_moves




def choose_move(data: dict) -> str:
    """
    data: Dictionary of all Game Board data as received from the Battlesnake Engine.
    For a full example of 'data', see https://docs.battlesnake.com/references/api/sample-move-request

    return: A String, the single move to make. One of "up", "down", "left" or "right".

    Use the information in 'data' to decide your next move. The 'data' variable can be interacted
    with as a Python Dictionary, and contains all of the information about the Battlesnake board
    for each move of the game.

    
    """
    my_head = data["you"]["head"]  # A dictionary of x/y coordinates like {"x": 0, "y": 0}
    my_body = data["you"]["body"]  # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]

    # TODO: uncomment the lines below so you can see what this data looks like in your output!
    # print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    # print(f"All board data this turn: {data}")
    # print(f"My Battlesnakes head this turn is: {my_head}")
    # print(f"My Battlesnakes body this turn is: {my_body}")

    possible_moves = ["up", "down", "left", "right"]

    # Don't allow your Battlesnake to move back in on it's own neck
    possible_moves = avoid_my_neck(my_head, my_body, possible_moves)

    # TODO: Using information from 'data', find the edges of the board and don't let your Battlesnake move beyond them
    # board_height = ?
    # board_width = ?

    # TODO Using information from 'data', don't let your Battlesnake pick a move that would hit its own body

    # TODO: Using information from 'data', don't let your Battlesnake pick a move that would collide with another Battlesnake

    # TODO: Using information from 'data', make your Battlesnake move towards a piece of food on the board
    
    # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]
    
    tail = my_body[-1]
    # TODO: uncomment the lines below so you can see what this data looks like in your output!
    # print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    # print(f"All board data this turn: {data}")
    # print(f"My Battlesnakes head this turn is: {my_head}")
    # print(f"My Battlesnakes body this turn is: {my_body}")

    possible_moves = ["up", "down", "left", "right"]

    # Don't allow your Battlesnake to move back in on it's own neck
    possible_moves = avoid_my_neck(my_head, my_body, possible_moves)
    

    
    # TODO: Using information from 'data', find the edges of the board and don't let your Battlesnake move beyond them

    board_height = data['board']['height']
    board_width = data['board']['height']

    if my_head['x'] == board_width-1: 
        possible_moves.remove('right')
    if my_head['x'] - 1 < 0:
        possible_moves.remove('left')
    if my_head['y'] == board_height-1:
        possible_moves.remove('up')
    if my_head['y'] - 1 < 0:
        possible_moves.remove('down')
    
     # TODO Using information from 'data', don't let your Battlesnake pick a move that would hit its own body

    for bite in my_body:
        
        if (my_head['x'] + 1 == bite['x'] and my_head['y'] == bite['y']):
            if 'right' in possible_moves: possible_moves.remove('right')
        if (my_head['x'] - 1 == bite['x'] and my_head['y'] == bite['y']):
            if 'left' in possible_moves: possible_moves.remove('left')
        if (my_head['x'] == bite['x'] and my_head['y'] + 1 == bite['y']):
            if 'up' in possible_moves: possible_moves.remove('up')
        if (my_head['x'] == bite['x'] and my_head['y'] - 1 == bite['y']):
            if 'down' in possible_moves: possible_moves.remove('down')


     # TODO: Using information from 'data', don't let your Battlesnake pick a move that would collide with another Battlesnake

    for snake in data['board']['snakes']:
        for block in snake['body']:
            if (my_head['x'] + 1 == block['x'] and my_head['y'] == block['y']):
                if 'right' in possible_moves: possible_moves.remove('right')
            if (my_head['x'] - 1 == block['x'] and my_head['y'] == block['y']):
                if 'left' in possible_moves: possible_moves.remove('left')
            if (my_head['x'] == block['x'] and my_head['y'] + 1 == block['y']):
                if 'up' in possible_moves: possible_moves.remove('up')
            if (my_head['x'] == block['x'] and my_head['y'] - 1 == block['y']):
                if 'down' in possible_moves: possible_moves.remove('down')
        block = snake['head']
        if (my_head['x'] + 1 == block['x'] and my_head['y'] == block['y']):
            if 'right' in possible_moves: possible_moves.remove('right')
        if (my_head['x'] - 1 == block['x'] and my_head['y'] == block['y']):
            if 'left' in possible_moves: possible_moves.remove('left')
        if (my_head['x'] == block['x'] and my_head['y'] + 1 == block['y']):
            if 'up' in possible_moves: possible_moves.remove('up')
        if (my_head['x'] == block['x'] and my_head['y'] - 1 == block['y']):
            if 'down' in possible_moves: possible_moves.remove('down')
   
    # Choose a random direction from the remaining possible_moves to move in, and then return that move
    

    ideal_moves = possible_moves.copy()
    if len(data['board']['food']) > 0:
        closest_food = data['board']['food'][0]
        food_distance = lambda head, food: math.sqrt((head['x'] - tail['x'])**2 + (head['y'] - tail['y'])**2)



    min_distance = food_distance(my_head, closest_food)



    for move in ideal_moves:
                if move == 'up':
                    temp_head = my_head
                    temp_head["y"] += 1
                    if (food_distance(temp_head, closest_food) > min_distance):
                        if 'up' in ideal_moves: ideal_moves.remove('up')
                elif move == 'right':
                    temp_head = my_head.copy()
                    temp_head["x"] += 1
                    if (food_distance(temp_head, closest_food) > min_distance):
                        if 'right' in ideal_moves: ideal_moves.remove('right')
                elif move == 'down':
                    temp_head = my_head.copy()
                    temp_head["y"] -= 1
                    if (food_distance(temp_head, closest_food) > min_distance):
                        if 'down' in ideal_moves: ideal_moves.remove('down')
                else:
                    temp_head = my_head.copy()
                    temp_head["x"] -= 1
                    if (food_distance(temp_head, closest_food) > min_distance):
                        if 'left' in ideal_moves: ideal_moves.remove('left')

    

    

    

    return possible_moves

        

# TODO: Explore new strategies for picking a move that are better than random

    

    
    
#global food_target
 #   food_target = []
  #  if data['board']['food']:
   #   food_target = [food for food in data['board']['food'] if food not in data['board']['hazards']]

    # TODO - look at the server_logic.py file to see how we decide what move to return!

#def best_food():
  
  



   #     min_distance=[]    
    #    for fd in food_target:
     #     dist = math.hypot(my_head['x'],my_head['y'], fd['x'],fd['y'])
      #    min_distance.append(dist)
                  
      #  index_min = min(range(len(min_distance)), key=min_distance.__getitem__)
              
              
       # return food_target[index_min]



      #def nextmoves(head_pos):
       # directions = {"up": [0,1],
        #                      "down": [0,-1],
         #                     "left": [-1,0],
          #                    "right": [1,0],
           #                   "center": [0,0]}
        #moves = ["up", "down", "left", "right"]
        #outlist = []
        #for mov in moves:
         # next_move = [directions[mov][0]+my_head['x'],directions[mov][1]+my_head['y']]
          #outlist.append([mov,next_move])
        #return outlist

      #def find_food():
       #   moves_ideal=nextmoves(my_head)
        #  fdb=best_food()
            
         # min_food=[]
          #for m in moves_ideal:
           #   dista = math.hypot(fdb['x'],fdb['y'], my_head['x'],my_head['y'])
            #  min_food.append(dista)
            
          #index_min2 = min(range(len(min_food)), key=min_food.__getitem__)
            
          #move_food=moves_ideal[index_min2][0]
                
          #return move_food

          
          

      #move_food=find_food()

      #if move_food in possible_moves:
       # move=move_food
