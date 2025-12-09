import pandas as pd

all_clean_metrics = pd.read_csv("output/2.1-1_all_clean_metrics_records.csv")   

duplicated_players = all_clean_metrics.groupby('playername')['team'].nunique()
duplicated_players = duplicated_players[duplicated_players > 1].index.tolist()


print(f"\nTotal number of playernames with more than one team: {len(duplicated_players)}")

print("\nDetails for playernames with more than one team:")
for player in duplicated_players:
    teams = all_clean_metrics[all_clean_metrics['playername'] == player]['team'].unique().tolist()
    print(f"- {player}: {teams}")

# output results to a csv file with playername and teams
duplicated_players_details = []
for player in duplicated_players:
    teams = all_clean_metrics[all_clean_metrics['playername'] == player]['team'].unique().tolist()
    duplicated_players_details.append({'playername': player, 'teams': ', '.join(teams)})

duplicated_players_df = pd.DataFrame(duplicated_players_details)
duplicated_players_df.to_csv("output/duplicate_players_draft.csv", index=False)