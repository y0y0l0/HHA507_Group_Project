from datetime import timedelta, datetime
import pandas as pd
from common_functions import run_sport_data_query,get_unique_athletes

def get_metric_with_most_missing_records() -> int:
    """Get a metric with the most missing records.
    Returns:
        int: The number of records retrieved.
        csv: A CSV file containing all records.
    """
    ## Identify which of your selected metrics have the most NULL or zero values?
    sql_test_query = "SELECT COUNT(*) AS count," \
                     " metric, " \
                     " data_source " \
                     "FROM research_experiment_refactor_test " \
                     "WHERE " \
                        "metric " \
                        "IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                        "AND (team " \
                        "IN ('Unknown', 'Player Not Found', 'Graduated (No longer enrolled)') " \
                        "OR (value IS NULL OR value = 0.0) ) " \
                     "GROUP BY metric, data_source " \
                     "ORDER BY COUNT(*) DESC;"
    response = run_sport_data_query(sql_test_query)
    if not response.empty:
        response.to_csv('output/2.1-1_metric_with_most_missing_records.csv')
    return response

def get_athletes_with_at_least_5_measurements_in_selected_metrics() -> int:
    """Get the percentage of athletes with at least 5 measurements per team.
    Returns:
        pd.DataFrame: DataFrame with team, athlete counts, and percentages.
        csv: A CSV file containing results per team.
    """
    ## For each sport/team, calculate what percentage of athletes have at least 5 measurements for your selected metrics?
    sql_test_query = "SELECT REPLACE(t.team, '\\'', '') AS team, " \
                     "COUNT(DISTINCT CASE WHEN cnt >= 5 THEN playername END) AS athletes_with_5_plus, " \
                     "COUNT(DISTINCT playername) AS total_athletes_in_team, " \
                     "ROUND(COUNT(DISTINCT CASE WHEN cnt >= 5 THEN playername END) / " \
                     "COUNT(DISTINCT playername) * 100, 2) AS percentage " \
                     "FROM (SELECT REPLACE(team, '\\'', '') AS team, playername, COUNT(*) AS cnt " \
                     "FROM research_experiment_refactor_test " \
                     "WHERE value IS NOT NULL AND value > 0.0 " \
                     "AND metric IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                     "AND REPLACE(team, '\\'', '') NOT IN ('Unknown', 'Player Not Found', 'Graduated (No longer enrolled)') " \
                     "GROUP BY REPLACE(team, '\\'', ''), playername) t " \
                     "GROUP BY REPLACE(t.team, '\\'', '') " \
                     "ORDER BY percentage DESC;"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        response.to_csv('output/2.1-2_athletes_with_at_least_5_measurements_in_selected_metrics.csv', index=False)
        print(f"Percentage of athletes with at least 5 measurements per team:")
        for index, row in response.iterrows():
            print(f"  {row['team']}: {row['percentage']}% ({row['athletes_with_5_plus']}/{row['total_athletes_in_team']})")
    return response

def get_athletes_with_5_measurements_not_in_selected_metrics() -> int:
    """Get the percentage of athletes with at least 5 measurements per team for non-selected metrics.
    Returns:
        pd.DataFrame: DataFrame with team, athlete counts, and percentages.
        csv: A CSV file containing results per team.
    """
    ## For each sport/team, calculate what percentage of athletes have at least 5 measurements not in your selected metrics?
    sql_test_query = "SELECT REPLACE(t.team, '\\'', '') AS team, " \
                     "COUNT(DISTINCT CASE WHEN cnt >= 5 THEN playername END) AS athletes_with_5_plus, " \
                     "COUNT(DISTINCT playername) AS total_athletes_in_team, " \
                     "ROUND(COUNT(DISTINCT CASE WHEN cnt >= 5 THEN playername END) / " \
                     "COUNT(DISTINCT playername) * 100, 2) AS percentage " \
                     "FROM (SELECT REPLACE(team, '\\'', '') AS team, playername, COUNT(*) AS cnt " \
                     "FROM research_experiment_refactor_test " \
                     "WHERE value IS NOT NULL AND value > 0.0 " \
                     "AND metric NOT IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                     "AND REPLACE(team, '\\'', '') NOT IN ('Unknown', 'Player Not Found', 'Graduated (No longer enrolled)') " \
                     "GROUP BY REPLACE(team, '\\'', ''), playername) t " \
                     "GROUP BY REPLACE(t.team, '\\'', '') " \
                     "ORDER BY percentage DESC;"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        response.to_csv('output/2.1-2_athletes_with_5_measurements_not_in_metric.csv', index=False)
        print(f"Percentage of athletes with at least 5 measurements in NON-selected metrics per team:")
        for index, row in response.iterrows():
            print(f"  {row['team']}: {row['percentage']}% ({row['athletes_with_5_plus']}/{row['total_athletes_in_team']})")
    return response

def get_team_percentages_with_athletes_with_at_least_5_measurements() -> int:
    """Get the percentage of athletes with at least 5 measurements for each sport/team.
    Returns:
        int: The percentage of athletes with at least 5 measurements.
        csv: A CSV file containing the results per team.
    """
    ## For each sport/team, calculate what percentage of athletes have at least 5 measurements for your selected metrics?
    sql_test_query = "SELECT REPLACE(t.team, '\\'', '') AS team, " \
                     "COUNT(DISTINCT CASE WHEN cnt >= 5 THEN playername END) AS athletes_with_5_plus, " \
                     "COUNT(DISTINCT playername) AS total_athletes_in_team, " \
                     "ROUND(COUNT(DISTINCT CASE WHEN cnt >= 5 THEN playername END) / " \
                     "COUNT(DISTINCT playername) * 100, 2) AS percentage " \
                     "FROM (SELECT REPLACE(team, '\\'', '') AS team, playername, COUNT(*) AS cnt " \
                     "FROM research_experiment_refactor_test " \
                     "WHERE value IS NOT NULL AND value > 0.0 " \
                     "AND metric IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                     "AND REPLACE(team, '\\'', '') NOT IN ('Unknown', 'Player Not Found', 'Graduated (No longer enrolled)') " \
                     "GROUP BY REPLACE(team, '\\'', ''), playername) t " \
                     "GROUP BY REPLACE(t.team, '\\'', '') " \
                     "ORDER BY percentage DESC;"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        response.to_csv('output/2.1-2_team_percentages_athletes_with_5_measurements.csv', index=False)
        print(f"Team percentages for athletes with at least 5 measurements:")
        for index, row in response.iterrows():
            print(f"  {row['team']}: {row['percentage']}% ({row['athletes_with_5_plus']}/{row['total_athletes_in_team']})")
    return response
def get_athletes_not_tested_in_last_num_days(days_ago: int,report_prefix: str) -> int:
    """Get the percentage of athletes not tested in the last 6 months.
    Args:
        report_prefix (str): Prefix for the report.
        days_ago (int): Number of days to look back for testing.

    Returns:
        int: The percentage of athletes not tested in the last 6 months.
        csv: A CSV file containing all records.
    """
    ## get mysql date -target_num_days_ago
    target_num_days_ago = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d %H:%M:%S')
    ## get athletes who haven't been tested in the last 6 months (for your selected metrics)
    sql_test_query = "SELECT DISTINCT playername, team " \
                        "FROM (SELECT DISTINCT playername, team FROM research_experiment_refactor_test " \
                        "WHERE REPLACE(team,'\\\'','') NOT IN ('Unknown','Player Not Found','Graduated (No longer enrolled)') " \
                        "AND metric IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total')) AS all_athletes " \
                        "WHERE playername NOT IN (SELECT DISTINCT playername FROM research_experiment_refactor_test " \
                        "WHERE value IS NOT NULL AND value > 0.0 " \
                        "AND metric IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                        "AND (timestamp >= '" + target_num_days_ago + "' OR created_at >= '" + target_num_days_ago + "'));"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        response.to_csv(f'output/{report_prefix}_athletes_not_tested_in_last_{days_ago}_days.csv')
        print(f"The percentage of athletes NOT tested in the last {days_ago} days for selected metrics is {response['playername'].nunique()/get_unique_athletes() * 100:.2f}%.")
 
    return response['playername'].unique()
def get_data_in_wide_format_by_athlete_and_metric(report_prefix: str,input_metric_list: list, input_playername_list: list, format_type: str) -> pd.DataFrame:
    """Get the data in wide format by athlete and metric based on the provides list of metrics and athletes.
    Args:
        report_prefix (str): Prefix for the report.
        input_metric_list (list): List of metrics to filter the data.
        input_playername_list (list): List of player names to filter the data.
        format_type (str): "wide" for wide format, "long" for long format.
    Returns:
        pd.DataFrame: A DataFrame with athletes as rows and metrics as columns.
    """
    ## create a list of metrics and players for the SQL query
    #initnialize empty strings
    metric_list = ""
    playername_list = ""
    response = pd.DataFrame()
    
    # Build the metrics list first (needed for both branches)
    for metric in input_metric_list:
        metric_list = metric_list + "\'" + metric + "',"
    metric_list = metric_list.rstrip(",")
    
    if isinstance(input_playername_list, str) and input_playername_list.upper() == "ALL":

            sql_test_query = (
                f"SELECT timestamp, metric, value, playername, team "
                f"FROM research_experiment_refactor_test "
                f"WHERE metric IN ({metric_list}) "
                f"AND value > 0.0 "
                f"AND REPLACE(team,'\\'','') not in ('Unknown','Player Not Found','Graduated (No longer enrolled)') "
                f"ORDER BY playername, timestamp DESC;"
            )
            response = run_sport_data_query(sql_test_query)
            if not response.empty:
                # create a separate csv file of all players data long format
                response.to_csv(f'output/{report_prefix}_ALL_players_data_in_long_format_by_athlete_and_metric.csv')
                    # only create pivoted wide format if requested
                if format_type == "wide":
                    response_pivot = response.pivot_table(index=['playername', 'timestamp'], columns='metric', values='value').reset_index()
                    response_pivot.to_csv(f'output/{report_prefix}_ALL_players_data_in_wide_format_by_athlete_and_metric_pivoted.csv')
                print(f"Sample raw data for all athletes: {response.head(10)}")
    else:
        #loop through input lists to create single quote comma-separated parameter for playernames
        for playername in input_playername_list:
            playername_list = playername_list + "\'" + playername + "',"
        if playername_list.endswith(","):
            playername_list = playername_list[:-1]
        print(f"metric_list: {metric_list}")
        print(f"playername_list: {playername_list}")
        ## get player metric data in wide format based on the provided list of metrics requested among clean data sets where the team is valid and the metric is not null.
        sql_test_query = (
            f"SELECT timestamp, metric, value, playername, team "
            f"FROM research_experiment_refactor_test "
            f"WHERE metric IN ({metric_list}) "
            f"AND playername IN ({playername_list}) "
            f"AND value > 0.0 "
            f"AND REPLACE(team,'\\'','') not in ('Unknown','Player Not Found','Graduated (No longer enrolled)') "
            f"ORDER BY playername, timestamp DESC;"
        )
        response = run_sport_data_query(sql_test_query)
        
        if not response.empty:
            # for each athlete in the input list, create a separate csv file
            for player in input_playername_list:
                player_data = response[response['playername'] == player]
                player_data.to_csv(f'output/{report_prefix}_{player}_data_in_long_format_by_athlete_and_metric.csv')
                # only create pivoted wide format if requested
                if format_type.upper() == "WIDE":
                    player_pivot = player_data.pivot_table(index=['playername', 'timestamp'], columns='metric', values='value').reset_index()
                    player_pivot.to_csv(f'output/{report_prefix}_{player}_data_in_wide_format_by_athlete_and_metric_pivoted.csv')
                print(f"Sample raw data for athlete {player}")
                for index, row in player_data.iterrows():
                    if index < 10 and row['playername'] == player:
                        print(f"  {row['playername']}:{row['timestamp']}:{row['metric']}:{row['value']}")
                    print(f"  {row['playername']}:{row['timestamp']}:{row['metric']}:{row['value']}")
    return response

def get_mean_value_for_each_team() -> pd.DataFrame:
    """Get the mean value for each metric by team.
    Returns:
        pd.DataFrame: DataFrame with team, metric, and mean values.
        csv: A CSV file containing results per team and metric.
    """
    ## Calculates the mean value for each team (using the team column)
    sql_test_query = "SELECT REPLACE(team, '\\'', '') AS team, " \
                     "metric, " \
                     "ROUND(AVG(value), 2) AS mean_value, " \
                     "COUNT(*) AS measurement_count, " \
                     "ROUND(MIN(value), 2) AS min_value, " \
                     "ROUND(MAX(value), 2) AS max_value, " \
                     "ROUND(STD(value), 2) AS std_dev " \
                     "FROM research_experiment_refactor_test " \
                     "WHERE value IS NOT NULL AND value > 0.0 " \
                     "AND metric IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                     "AND REPLACE(team, '\\'', '') NOT IN ('Unknown', 'Player Not Found', 'Graduated (No longer enrolled)') " \
                     "GROUP BY REPLACE(team, '\\'', ''), metric " \
                     "ORDER BY team, metric;"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        response.to_csv('output/2.3-1&2_mean_value_for_each_team.csv', index=False)
        print(f"Mean values for each metric by team:")
        current_team = None
        for index, row in response.iterrows():
            if current_team != row['team']:
                print(f"\n{row['team']}:")
                current_team = row['team']
            print(f"  {row['metric']}: Mean={row['mean_value']}, Count={row['measurement_count']}, Min={row['min_value']}, Max={row['max_value']}, StdDev={row['std_dev']}")
    return response
def get_all_clean_metrics_records() -> int:
    """Get all records from the database with clean metrics.
    Returns:
        int: The number of records retrieved.
        csv: A CSV file containing all records.
    """
    ## How many unique athlete are in the database?
    sql_test_query = "SELECT  metric,data_source, value,REPLACE(team,'\\'','') as team, playername " \
                        "FROM research_experiment_refactor_test WHERE value is not null AND value > 0.0 " \
                        "AND TRIM(metric) in ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total')" \
                        "AND TRIM(REPLACE(team,'\\'',''))  not in ('Unknown','Player Not Found','Graduated (No longer enrolled)');"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        output_file = 'output/3.2-1_all_clean_metrics_records.csv'
        try:
            response.to_csv(output_file)
            print(f"Successfully saved to {output_file}")
        except PermissionError as e:
            print(f"Permission error writing to {output_file}: {e}")
    return response
def get_all_clean_metrics_records(report_type:str) -> pd.DataFrame:
    """Get all records from the database with clean metrics.
    Returns:
        dataframe: The number of records retrieved.
        csv: A CSV file containing all records.
    """
    ## How many unique athlete are in the database?
    sql_test_query = "SELECT  DATE(timestamp) as test_date,timestamp,created_at,metric,data_source, value,REPLACE(team,'\\'','') as team, playername " \
                        "FROM research_experiment_refactor_test WHERE value is not null AND value > 0.0 " \
                        "AND TRIM(metric) in ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total', 'avg_accel_load_accum','avg_torque_asymmetry','avg_max_force_asymmetry')" \
                        "AND TRIM(REPLACE(team,'\\'',''))  not in ('Unknown','Player Not Found','Graduated (No longer enrolled)');"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        output_file = 'output/3.2-1_all_clean_metrics_records.csv'
        if report_type.upper() == "WIDE":
            response = response.pivot_table(index=['playername', 'timestamp', 'team','data_source'], columns='metric', values='value').reset_index()
            output_file = 'output/3.2-1_all_clean_metrics_records_wide_format.csv'
            
            # data must be pivoted to calculate avg_torque_asymmetry and avg_max_force_asymmetry after pivot - using formula from index 10 in the results analysis on our literature review
            # reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8488821/
            
            # Check if required columns exist before calculating asymmetry
            if 'leftTorque' in response.columns and 'rightTorque' in response.columns:
                response['avg_torque_asymmetry'] = ((response['leftTorque'] - response['rightTorque'])/ (response['leftTorque'] + response['rightTorque']) )*100
            else:
                print(f"Warning: 'leftTorque' and/or 'rightTorque' columns not found. Available columns: {list(response.columns)}")
            
            if 'leftMaxForce' in response.columns and 'rightMaxForce' in response.columns:
                response['avg_max_force_asymmetry'] = ((response['leftMaxForce'] - response['rightMaxForce']) / (response['leftMaxForce'] + response['rightMaxForce']) ) *100
            else:
                print(f"Warning: 'leftMaxForce' and/or 'rightMaxForce' columns not found. Available columns: {list(response.columns)}")
            
            # Calculate z-scores for each metric within each team
            # Z-score = (value - team_mean) / team_std_dev
            metric_columns = ['leftTorque', 'rightTorque', 'leftMaxForce', 'rightMaxForce', 'accel_load_accum', 'distance_total','avg_max_force_asymmetry','avg_torque_asymmetry']
            for metric_col in metric_columns:
                if metric_col in response.columns:
                    zscore_col = f'{metric_col}_zscore'
                    # Group by team and calculate z-score
                    response[zscore_col] = response.groupby('team')[metric_col].transform(
                        lambda x: (x - x.mean()) / x.std() if x.std() != 0 else 0
                    )
                    print(f"Z-score calculated for {metric_col}")
                    
        try:
            response.to_csv(output_file)
            print(f"Successfully saved to {output_file}")
        except PermissionError as e:
            print(f"Permission error writing to {output_file}: {e}")
    return response

def get_top_five_players_per_team() -> pd.DataFrame:
    """Get top 5 players per team relative to their team's mean per metric.
    Uses window functions to calculate team average and player average.
    Returns:
        pd.DataFrame: DataFrame with top 5 players per team/metric.
        csv: A CSV file containing results.
    """
    ## Identifies the top five player relative to their teams mean per metric
    ## Using window function to get individual values with team average
    sql_test_query = "SELECT metric, data_source, REPLACE(team,'\\'','') as team, playername, value, " \
                        "ROUND(AVG(value) OVER (PARTITION BY REPLACE(team,'\\'',''), metric), 2) AS team_avg_value, " \
                        "ROUND(AVG(value) OVER (PARTITION BY REPLACE(team,'\\'',''), metric, playername), 2) AS player_mean_value " \
                        "FROM research_experiment_refactor_test WHERE value is not null AND value > 0.0 " \
                        "AND TRIM(metric) in ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                        "AND TRIM(REPLACE(team,'\\'',''))  not in ('Unknown','Player Not Found','Graduated (No longer enrolled)');"
    response = run_sport_data_query(sql_test_query)
    
    # Check if DataFrame is valid
    if response is None or response.empty:
        print("Warning: response DataFrame is empty or None")
        return None
    
    # Verify required columns exist
    if 'team' not in response.columns or 'metric' not in response.columns:
        print(f"Warning: Missing required columns in response. Columns: {response.columns.tolist()}")
        return None
    
    # Calculate percent difference using team_avg_value from window function
    response['percent_difference_from_team_mean'] = ((response['player_mean_value'] - response['team_avg_value']) / response['team_avg_value']) * 100
    
    # Get unique player averages (remove duplicate rows from window function)
    player_summary = response.drop_duplicates(subset=['team', 'metric', 'playername'])[['team', 'metric', 'playername', 'data_source', 'player_mean_value', 'team_avg_value', 'percent_difference_from_team_mean']]
    
    # Sort descending for top performers and get top 5 per team/metric
    player_summary.sort_values(by=['team', 'metric', 'percent_difference_from_team_mean'], ascending=[True, True, False], inplace=True)
    top_five_df = player_summary.groupby(['team', 'metric']).head(5).reset_index(drop=True)
    
    if not top_five_df.empty:
        output_file = 'output/2.3-3_top_five_players_per_team.csv'
        try:
            top_five_df.to_csv(output_file)
            print(f"Successfully saved to {output_file}")
        except PermissionError as e:
            print(f"Permission error writing to {output_file}: {e}")
    return top_five_df

def get_bottom_five_players_per_team() -> pd.DataFrame:
    """Get bottom 5 players per team relative to their team's mean per metric.
    Uses window functions to calculate team average and player average.
    Returns:
        pd.DataFrame: DataFrame with bottom 5 players per team/metric.
        csv: A CSV file containing results.
    """
    ## Identifies the bottom five player relative to their teams mean per metric
    ## Using window function to get individual values with team average
    sql_test_query = "SELECT metric, data_source, REPLACE(team,'\\'','') as team, playername, value, " \
                        "ROUND(AVG(value) OVER (PARTITION BY REPLACE(team,'\\'',''), metric), 2) AS team_avg_value, " \
                        "ROUND(AVG(value) OVER (PARTITION BY REPLACE(team,'\\'',''), metric, playername), 2) AS player_mean_value " \
                        "FROM research_experiment_refactor_test WHERE value is not null AND value > 0.0 " \
                        "AND TRIM(metric) in ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                        "AND TRIM(REPLACE(team,'\\'',''))  not in ('Unknown','Player Not Found','Graduated (No longer enrolled)');"
    response = run_sport_data_query(sql_test_query)
    
    # Check if DataFrame is valid
    if response is None or response.empty:
        print("Warning: response DataFrame is empty or None")
        return None
    
    # Verify required columns exist
    if 'team' not in response.columns or 'metric' not in response.columns:
        print(f"Warning: Missing required columns in response. Columns: {response.columns.tolist()}")
        return None
    
    # Calculate percent difference using team_avg_value from window function
    response['percent_difference_from_team_mean'] = ((response['player_mean_value'] - response['team_avg_value']) / response['team_avg_value']) * 100
    
    # Get unique player averages (remove duplicate rows from window function)
    player_summary = response.drop_duplicates(subset=['team', 'metric', 'playername'])[['team', 'metric', 'playername', 'data_source', 'player_mean_value', 'team_avg_value', 'percent_difference_from_team_mean']]
    
    # Sort ascending for bottom performers (most negative first) and get bottom 5 per team/metric
    player_summary.sort_values(by=['team', 'metric', 'percent_difference_from_team_mean'], ascending=[True, True, True], inplace=True)
    bottom_five_df = player_summary.groupby(['team', 'metric']).head(5).reset_index(drop=True)
    
    if not bottom_five_df.empty:
        output_file = 'output/2.3-3_bottom_five_players_per_team.csv'
        try:
            bottom_five_df.to_csv(output_file)
            print(f"Successfully saved to {output_file}")
        except PermissionError as e:
            print(f"Permission error writing to {output_file}: {e}")
    return bottom_five_df

# 2.3-2: For each athlete measurement, calculate their percent difference from their team's average
def calculate_percent_difference_from_team_mean() -> pd.DataFrame:
    """Calculate percent difference from team mean for each athlete measurement.
    Returns:
        pd.DataFrame: DataFrame with athlete measurements and their percent difference from team mean.
        csv: A CSV file containing all measurements with percent differences.
    """
    ## Get all individual athlete measurements
    sql_test_query = "SELECT metric, data_source, " \
                     "REPLACE(team,'\\'','') as team, " \
                     "playername, " \
                     "timestamp, " \
                     "value " \
                     "FROM research_experiment_refactor_test " \
                     "WHERE value IS NOT NULL AND value > 0.0 " \
                     "AND TRIM(metric) IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                     "AND TRIM(REPLACE(team,'\\'','')) NOT IN ('Unknown','Player Not Found','Graduated (No longer enrolled)');"
    
    response = run_sport_data_query(sql_test_query)
    
    if response.empty:
        print("No data returned from query")
        return pd.DataFrame()
    
    # Load the team means CSV
    team_means_df = pd.read_csv('output/2.3-1&2_mean_value_for_each_team.csv')
    
    # Merge athlete measurements with team means
    merged_df = pd.merge(response, team_means_df[['team', 'metric', 'mean_value']], on=['team', 'metric'], how='inner')
    
    # Calculate percent difference from team mean
    merged_df['percent_difference_from_team_mean'] = ((merged_df['value'] - merged_df['mean_value']) / merged_df['mean_value']) * 100
    
    if not merged_df.empty:
        output_file = 'output/2.3-2_athlete_measurements_with_percent_difference.csv'
        try:
            merged_df.to_csv(output_file, index=False)
            print(f"Successfully saved to {output_file}")
            print(f"\nTotal measurements with percent difference calculated: {len(merged_df)}")
            print(f"\nSample results:")
            print(merged_df[['playername', 'team', 'metric', 'value', 'mean_value', 'percent_difference_from_team_mean']].head(10))
        except PermissionError as e:
            print(f"Permission error writing to {output_file}: {e}")
    
    return merged_df