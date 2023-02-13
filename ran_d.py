import random

def create_player(player_name):
    player_odds = [random.uniform(1, 10) for _ in range(7)]
    return {player_name: player_odds}

odds = {}
players = ['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10']

for player in players:
    odds.update(create_player(player))

def update_odds(odds):
    for player in odds:
        # Generate new odds for each player
        new_odd = [random.uniform(1, 10) for _ in range(3)]
        odds[player] += new_odd
    return odds

while True:
    # Call the update_odds function to add new odds for each player
    odds = update_odds(odds)
    # Check if the user wants to exit
    exit = input("Press 'q' to exit or any other key to continue: ")
    if exit == 'q':
        break

