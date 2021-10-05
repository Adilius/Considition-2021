from greedy_solver import GreedySolver
from binpacking import BinPacker
import api
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('APIKEY')
# The different map names can be found on considition.com/rules
# TODO: You map choice here. Unless changed, the map "training1" will be selected.
map_name = "training2"


def main():
	print("Starting game...")
	response = api.new_game(api_key, map_name)
	#print(json.dumps(response, indent=4, sort_keys=True))

	print('Solving game..')
	#greedy = GreedySolver(game_info=response)
	#order = list(range(0,60))
	#solution = greedy.SolveList(order)
	#solution = greedy.Solve()

	binpacking = BinPacker(game_info=response)
	solution = binpacking.Solve()

	print('Submitting game...')
	submit_game_response = api.submit_game(api_key, map_name, solution)
	print(submit_game_response)
if __name__ == "__main__":
    main()
