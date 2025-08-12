import json
import random 

user_team = []
#show list of available players to draft in main menu 
def load_players(filepath="data/teams.json"):
    with open(filepath, "r") as f:
        teams = json.load(f)

    player_pool = []
    for team in teams:
        for player in team["players"]:
            player_copy = player.copy()
            player_copy["team"] = team["team"]
            player_copy["conference"] = team["conference"]
            player_pool.append(player_copy)
    return player_pool

#store drafted players
def draft_team(players, team_size =5):
    drafted = [] 
    while len(drafted) < team_size:
        print(f"\nDrafting Player... {len(drafted) + 1} of {team_size}")
        for idx, player in enumerate(players):
            print(f"{idx + 1}. {player['name']} {player['team']} - {player['ppg']} PPG")
        try:
            choice = int(input("Pick a player by number: ")) - 1
            if choice < 0 or choice >= len(players):
                print("Invalid entry. Try again.")
                continue
        
        #removed selected player from pool 
            selected_player = players.pop(choice)
            drafted.append(selected_player)
            print(f"✅ {selected_player['name']} added to your team.")

        except ValueError:
            print("Enter a valid number.")

    return drafted

    #logic for simulating matches
def simulate_match(user_team):
    players_pool = load_players()

    drafted_names = {player['name'] for player in user_team}
    available_players = [p for p in players_pool if p['name'] not in drafted_names]
    cpu_team = random.sample(available_players, len(user_team))

    print("\n CPU Team Drafted:")
    for idx, player in enumerate(cpu_team, start=1):
        print(f"{idx}. {player['name']} {player['team']} - {player['position']} - {player['ppg']} PPG")

    #calulating score between User and CPU
    def simulate_player_stats(team):
        stats = []

        for player in team:
            points = round(player['ppg'] + random.uniform(-5, 5))
            rebounds = random.randint(2, 12)
            assists = random.randint(1, 11)

            stats.append({
                'name': player['name'],
                'team': player['team'],
                'points': points,
                'rebounds': rebounds,
                'assists': assists
            })
        return stats

#Team box score
    def print_stats(title, stats):
        print(f"\n {title}")
        for idx, player in enumerate(stats, start=1):
            print(f"{idx}. {player['name']} - {player['points']} PTS, {player['rebounds']} REB, {player['assists']} AST")
    
    #Sim CPU and User players stats
    user_stats = simulate_player_stats(user_team)
    cpu_stats = simulate_player_stats(cpu_team)

    #calculating total score
    user_score = sum(p['points'] for p in user_stats)
    cpu_score = sum(p['points'] for p in cpu_stats)

    
    # overtime logic
    while round(user_score, 1) == round(cpu_score, 1):
        print("Heading to OVERTIME...")
        user_overtime = random.uniform(5, 15)
        cpu_overtime = random.uniform(5, 15)
        user_score += user_overtime
        cpu_score += cpu_overtime
        print(f"Overtime: You scored +{user_overtime:.1f}, CPU scored +{cpu_overtime:.1f}")
    
    print("\n Final Score:")
    print(f"Your Team Score: {user_score:.1f}")
    print(f"CPU Team Score: {cpu_score:.1f}")
    
    if user_score > cpu_score:
        print("You win!")
    elif cpu_score > user_score:
        print('CPU wins!')

def main_menu():
    while True:
        print("\n🏀 Fantasy Basketball Sim")
        print("1. Draft a team")
        print("2. View your team")
        print("3. Simulate a match")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            players = load_players()
            global user_team
            user_team = draft_team(players)
            print("\nYour team has been drafted!")
        elif choice == "2":
            if not user_team:
                print("You haven't drafted a team yet.")
            else:
                print("\n Your Drafted Team:")
                for idx, player in enumerate(user_team, start=1):
                    print(f"{idx}. {player['name']} {player['team']} - {player['position']} - {player['ppg']} PPG")
        elif choice == "3":
            if not user_team:
                print("You haven't drafted a team yet.")
            else:
                simulate_match(user_team)


        elif choice == "4":
            print("Goodbye...")
            break    
        else:
            print("Invalid, Please choose another option.")









if __name__ == "__main__":
    main_menu()