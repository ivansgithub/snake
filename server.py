import logging
import os
import random
from flask import Flask
from flask import request
import math
import server_logic


app = Flask(__name__)


@app.get("/")
def handle_info():
    """
    This function is called when you register your Battlesnake on play.battlesnake.com
    See https://docs.battlesnake.com/guides/getting-started#step-4-register-your-battlesnake

    It controls your Battlesnake appearance and author permissions.
    For customization options, see https://docs.battlesnake.com/references/personalization

    TIP: If you open your Battlesnake URL in browser you should see this data.
    """
    print("INFO")
    return {
        "apiversion": "1",
        "author": "",  # TODO: Your Battlesnake Username
        "color": "#00ff00",  # TODO: Personalize
        "head": "silly",  # TODO: Personalize
        "tail": "mouse",  # TODO: Personalize
    }


@app.post("/start")
def handle_start():
    """
    This function is called everytime your snake is entered into a game.
    request.json contains information about the game that's about to be played.
    """
    data = request.get_json()

    print(f"{data['game']['id']} START")
    return "ok"


@app.post("/move")
def handle_move():
    """
    This function is called on every turn of a game. It's how your snake decides where to move.
    Valid moves are "up", "down", "left", or "right".
    """
    data = request.get_json()

    my_head = data["you"]["head"]

    
    possible_moves = server_logic.choose_move(data)

    choice=possible_moves
    def chicken():
      
      k= choice.pop(0)
      choice.append(k)

      return k
    
    move=chicken()
    
    if data['you']['health'] < 20:
      def best_food():

        food_target = []
        if data['board']['food']:
          food_target = [food for food in data['board']['food'] if food not in data['board']['hazards']]




        min_distance=[]    
        for fd in food_target:
          dist = math.hypot(my_head['x'],my_head['y'], fd['x'],fd['y'])
          min_distance.append(dist)
                  
        index_min = min(range(len(min_distance)), key=min_distance.__getitem__)
              
              
        return food_target[index_min]

      if math.hypot( my_head['x']+best_food()['x']) < math.hypot(my_head['y']+best_food()['y']):
          if 'left' in possible_moves:
              move='left'
          elif 'right' in possible_moves:
              move='right'
          elif 'up' in possible_moves:
              move='up'
          else:
              move='down'
              
      else:
          if 'up' in possible_moves:
              move='up'
          elif 'down' in possible_moves:
              move='down'
          elif 'left' in possible_moves:
              move='left'
          else:
              move='right'

      
      
      
      
      #if 'up' in possible_moves:
       # move='up'
      
      
      

    if data['you']['health'] > 20:
       move=chicken()

    if data['you']['length'] > 18:
      move=random.choice(possible_moves)
      
    return {"move": move}


@app.post("/end")
def end():
    """
    This function is called when a game your snake was in ends.
    It's purely for informational purposes, you don't have to make any decisions here.
    """
    data = request.get_json()

    print(f"{data['game']['id']} END")
    return "ok"


if __name__ == "__main__":
    logging.getLogger("werkzeug").setLevel(logging.ERROR)

    print("Starting Battlesnake Server...")
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port, debug=True)
