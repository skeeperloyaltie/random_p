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

def simulate_round(odds):
    round_results = {}
    for player in odds:
        # Simulate a choice made by each player in the round
        choice = random.choice(odds[player])
        round_results[player] = choice
    return round_results

def determine_winner(round_results):
    # Determine the player with the highest number in the round
    winner = max(round_results, key=round_results.get)
    return winner

while True:
    # Call the update_odds function to add new odds for each player
    odds = update_odds(odds)
    # Simulate a round
    round_results = simulate_round(odds)
    # Determine the winner of the round
    winner = determine_winner(round_results)
    print(f"Round One:")
    for player in round_results:
        print(f"{player} - {round_results[player]}")
    print(f"{winner} won the round\n")
    # Check if the user wants to exit
    exit = input("Press 'q' to exit or any other key to continue: ")
    if exit == 'q':
        break
