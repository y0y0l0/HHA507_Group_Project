import pandas as pd
import numpy as np

## Load the dataset
df_metrics = pd.read_csv('output/3.2-2_matched_metrics_by_date_wide_format.csv')


## Identify players with torque or max force asymmetry >= 10%

flagged_asymmetry_records = []

for index, row in df_metrics.iterrows():
    # Check for High Max Force Asymmetry
    if abs(row['avg_max_force_asymmetry']) >= 10:
        flagged_asymmetry_records.append({
            'playername': row['playername'],
            'team': row['team'],
            'flag_reason': 'High Max Force Asymmetry',
            'metric_value': row['avg_max_force_asymmetry'],
            'test_date': row['test_date']
        })

    # Check for High Torque Asymmetry
    if abs(row['avg_torque_asymmetry']) >= 10:
        flagged_asymmetry_records.append({
            'playername': row['playername'],
            'team': row['team'],
            'flag_reason': 'High Torque Asymmetry',
            'metric_value': row['avg_torque_asymmetry'],
            'test_date': row['test_date']
        })

flagged_asymmetry_players_df = pd.DataFrame(flagged_asymmetry_records)

flagged_asymmetry_players_df.head()


## Identify players whose last test date is more than 30 days from the latest test date in the dataset

# Ensure 'test_date' is datetime
df_metrics['test_date'] = pd.to_datetime(df_metrics['test_date'])

# Find the latest test date in the dataset and per-player last test date
latest_test_date = df_metrics['test_date'].max()
last_test_dates = (
    df_metrics
    .dropna(subset=['test_date'])
    .groupby('playername', as_index=False)['test_date']
    .max()
    .rename(columns={'test_date': 'last_test_date'})
)

# Flag players whose last test is older than 30 days
cutoff = latest_test_date - pd.Timedelta(days=30)
inactive_players = last_test_dates[last_test_dates['last_test_date'] < cutoff].copy()
inactive_players['days_since_last_test'] = (latest_test_date - inactive_players['last_test_date']).dt.days

# Get the team for each player from df_metrics
player_team_mapping = df_metrics[['playername', 'team']].drop_duplicates().set_index('playername')['team']

# Add team information to inactive_players
inactive_players_with_team = inactive_players.set_index('playername').join(player_team_mapping).reset_index()

# Create the flagged_asymmetry_players_df for inactive players
inactive_players_df = pd.DataFrame({
    'playername': inactive_players_with_team['playername'],
    'team': inactive_players_with_team['team'],
    'flag_reason': 'Not Tested in > 30 days',
    'metric_value': np.nan,
    'test_date': inactive_players_with_team['last_test_date']
})

inactive_players_df.head()

## Combine both flagged datasets

flagged_asymmetry_players_df_renamed = flagged_asymmetry_players_df.rename(columns={'test_date': 'last_test_date'})

all_flagged_players_df = pd.concat([
    flagged_asymmetry_players_df_renamed,
    inactive_players_df
], ignore_index=True)

all_flagged_players_df = all_flagged_players_df.sort_values(by=['playername', 'last_test_date']).reset_index(drop=True)

all_flagged_players_df.head()

print(f"Total flagged instances: {len(all_flagged_players_df)}")
print(f"Unique players flagged: {all_flagged_players_df['playername'].nunique()}")

## Output flagged players to CSV
all_flagged_players_df.to_csv('output/part4_flag_system_draft.csv', index=False)