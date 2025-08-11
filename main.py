import json

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
            print(f"✅ {selected_player['name']} addted to your team.")

        except ValueError:
            print("Enter a valid number.")

    return drafted




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
            print("Simulating season...")
        elif choice == "4":
            print("Goodbye...")
            break    
        else:
            print("Invalid, Please choose another option.")









if __name__ == "__main__":
    main_menu()