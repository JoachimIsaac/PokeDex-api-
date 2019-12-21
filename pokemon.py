# What is an API (A way to communicated between different divices different broswers between databses to get that info(data) to your aplication) (different types of requests get , post, delete and put but put and delete are post also)  but put is more updating and delete is removing one while post is just adding one .

import requests
# json libary already in python
import json

print("Welcome to the pokedex!!!")
pokemon_name = input("What Pokemon do you want to search? ")


# Response of 200 means everything went well when you make a get request to a sever.
data = requests.get(
    f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")


# (i = info, s = stats)
# name, id, wieght , height, types of pokemon
# Turns it into a dictionary of strings.
if data.status_code == 200:
    data = json.loads(data.text)

    print(f"You chose {data['name']}")
    action = input(
        "What information would you like to see?\n(i = info, s = stats)")

    if action == "i" or action == "info":
        print(f"\nID: {data['id']}\n")
        print(f"Name: {data['name']}\n")
        print(f"Height: {data['height']}\n")
        print(f"Weight: {data['weight']}lbs\n")
        pokemon_type = ""
        for type in data['types']:
            if data["types"].index(type) == (len(data["types"]) - 1):
                pokemon_type += f"{type['type']['name']}"
            else:
                pokemon_type += f"{type['type']['name']}, "
        print(f"type: {pokemon_type}\n")

    elif action == "s" or action == "stats":
        print(f"HP: {data['stats'][5]['base_stat']}")
        print(f"Attack: {data['stats'][4]['base_stat']}")
        print(f"Defense: {data['stats'][3]['base_stat']}")
        print(f"Speed: {data['stats'][0]['base_stat']}")
        print(f"Special attack: {data['stats'][2]['base_stat']}")
        print(f"Special defense: {data['stats'][1]['base_stat']}")

    else:
        print("Sorry we don't recognize that command!")
else:
    print("Sorry that's not a valid pokemon!")
