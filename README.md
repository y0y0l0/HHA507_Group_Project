# HHA507_Group_Project

Group SBU Sports data Project
Goal of this project is to analyze sports performance data from multiple sources (Kinexon and Vald), whether bilateral asymmetry metric differences affect performance metrics (accumulated acceleration load and total distance) that can help improve athlete performance and reduce injury risk.
# Team Roles:
- `Nina & Yatza`: Data Engineer - Responsible for data extraction, transformation.
- `Nina, Katiana, Blanca & Yatza`: Data Analyst - Focuses on data exploration, visualization, and statistical analysis.
- `Blanca, Katiana, Esquilaure, & Luke`: Researcher - Conducts literature review and synthesizes research findings related to sports performance metrics.
- `Nina, & Yatza`: Visualization Specialist - Designs and implements visualizations to effectively communicate data insights.
- `Blanca, Nina & Yatza`: Project Manager - Oversees project timelines, coordinates team efforts, and ensures deliverables are met.
- `Blanca, Nina, Katiana, Esquilaure, Yatza & Luke`: Presenter - Prepares and delivers the final presentation of the project findings.
- `Blanca, Nina, Yatza`: Documentation Specialist - Responsible for maintaining project documentation, including the README file and code comments.

# Team Data Setup:
link to team database setup screenshots: https://drive.google.com/drive/folders/1bX1Yk2YJH1KX1Z3o1F6gD3fQXK5Jt5vP?usp=sharing

# Team presentation slides:
link to team presendation slides: https://docs.google.com/presentation/d/1IiI5CwbIHg4V8L8NR5JBr0AiKxmIxBGMQci9IVsK6oo/edit?usp=sharing

# Team literature review:
link to team literature review: https://docs.google.com/document/d/1hs3RljvobFhrrgEVS4Ev2E5Cl8YE0w7z1t3h8Qo_D-A/edit?tab=t.es53pvsqyhzj#heading=h.owyzndpwo8a8

# Team Notebooks:
### Part 3. Visualizations and Analysis
link to team part3_viz_comparison notebook: https://colab.research.google.com/drive/1pl6wRVZaPeZ0Pbktx6SGiONwlCW_hQ-0?usp=sharing
### 3.3
    - https://colab.research.google.com/drive/1jJDtOS29TCApR4HsrWrxdsDtnwxfeMhS?usp=sharing
### Player 755
    - Part 1:https://colab.research.google.com/drive/1hVXnwQCo98i74oTtsnyllh1HDIaoZXDD?usp=drive_link
    - Part 2: https://colab.research.google.com/drive/1gMds29rwsUNJNJfpWdRJaMjEoiTARa6T?usp=drive_link
### Player 1128
    - Part 1: https://colab.research.google.com/drive/1gMds29rwsUNJNJfpWdRJaMjEoiTARa6T?usp=drive_link
    - Part 2: https://colab.research.google.com/drive/12RbkLah6NVb0m_d2NEfvQ1URxCP6Oq7O?usp=drive_link 

## Project Structure
    HHA507_Group_Project/                  # Root directory
    ├── 1.1 Team Database Setup Screenshots/  # Directory for team database setup screenshots from each team member
    ├── notebooks/                       # Jupyter notebooks
    ├── output/                          # Output data files
    ├── reports/                         # Literature review, Researach Synthesis & Recommendations and presentation slides
    ├── scripts/                         # Main scripts
    │   ├── common_clean_function.py     # Common data cleaning and preprocessing functions
    │   ├── common_functions.py          # Common data analysis functions
    │   ├── part_exploration.py          # Initial data analysis scripts
    │   └── part2_cleaning.py            # Data cleaning scripts
    ├── README.md                        # Readme file
    ├── requirements.txt                 # Project dependencies
    ├── GROUP_ASSIGNMENT.pdf             # Group assignment details    
    └── .gitignore                       # Git ignore file
# 1 Database Connection & Data Exploration
- Establish database connection
- Understand data structure and quality
- Generate summary statistics
### Data Setup (Individual)
Individual team members set up their local database connections using the provided scripts and screenshots are found in the `1.1 Team Database Setup Screenshots/` directory.
- The `common_functions.py` script in the `scripts/` directory contains functions to establish
- The `part_exploration.py` script in the `scripts/` directory contains functions for initial data exploration, including loading datasets, summarizing data, and visualizing key metrics.

### 1.2 Data Quality Assessment
- `1.2` Data Understanding Recap (Group)
    1. Answers to the following questions:
        1. How many unique athletes are in the database?
            * Identify the total number of unique athletes across all datasets.*
            'There are 1287 unique athletes in the database.'
        2. How many different sports/teams are represented?
            * Determine the number of sports teams included in the data (this data is sanitized).*
            'There are Unique sports/teams 89 in the database after removing duplicates and invalid entries ie: 'Unknown','Player Not Found','Graduated (No longer enrolled)'.'
        3. What is the date range of available data?
            * Identify the earliest and latest dates of data collection (this data includes invalid entries).*
            'The creation date range of a data is from 2025-10-21 16:46:54 to 2025-10-21 17:03:12.'
            'The timestamp date range of a data is from 2018-10-15 19:27:41 to 2025-10-21 12:24:21'
        4. Which data source (Hawkins/Kinexon/Vald) has the most records?
            * Compare the number of records from each data source (this data includes invalid entries).*
            'The data source hawkins has 2492372 records.'
            'The data source kinexon has 4073754 records.'
            'The data source vald has 51300 records.'
        5. Are there any athletes with missing or invalid names (this data includes invalid entries)?
            * Identify athletes with missing or improperly formatted names (this data includes invalid entries).*
            -There are no invalid athlete names in the database.
        6. How many athletes have data from multiple sources (2 or 3 systems) (this data is sanitized)?
            * Determine the number of athletes with data from more than one source (this data includes invalid entries).*
            -There are 541 athletes with data from multiple sources.
- `1.3` Metric Discovery & Selection (Group)
    1. Identify and list the top 10 most common metrics for each data source (Hawkins, Kinexon, Vald)
        1. Lists the top 10 most common metrics for Hawkins data (filter by data_source = 'Hawkins')
            * Identify the most frequently recorded metrics in the Hawkins dataset (this data includes invalid entries).
            The top 10 most common metrics for Hawkins data are:
            ```
                _________________________________________________________________________ 
                |         | metric                                     |  metric_count  |
                |---------|--------------------------------------------|----------------|
                |0        |                     System Weight(N)       |31467           |
                |1        |         Propulsive Net Impulse(N.s)        |31295           |
                |2        |           Peak Propulsive Force(N)         |31295           |
                |3        |           Avg. Propulsive Power(W)         |31295           |
                |4        |                     Jump Height(m)         |31295           |
                |5        |                 Peak Velocity(m/s)         |31295           |
                |6        |                Propulsive Phase(s)         |31295           |
                |7        |           Peak Propulsive Power(W)         |31295           |
                |8        |  Avg. Relative Propulsive Force(%)         |31295           |
                |9        |           Avg. Propulsive Force(N)         |31295           |
            ```
    2. Lists the top 10 most common metrics for Kinexon data (filter by data_source = 'Kinexon')
        * Identify the most frequently recorded metrics in the Kinexon dataset (this data includes invalid entries).
                -The top 10 most common metrics for Kinexon data are:
            ```
             ________________________________________________________________________ 
                |         | metric                                     |  metric_count  |
                |---------|--------------------------------------------|----------------|
                |0        | track_outside_field                        |40803           |
                |1        | track_heart_rate_always                    |40803           |
                |2        | accel_load_accum                           |40703           |
                |3        | time_total                                 |40585           |
                |4        | accel_load_accum_avg_per_minute            |40485           |
                |5        | distance_total                             |40317           |
                |6        | speed_distance_per_time                    |40316           |
                |7        | distance_total_avg_per_minute              |40315           |
                |8        | speed_max                                  |40312           |
                |9        | speed_avg                                  |40298           |
            ```
    4. Lists the top 10 most common metrics for Vald data (filter by data_source = 'Vald')
        * Identify the most frequently recorded metrics in the Vald dataset (this data includes invalid entries).*
                -The top 10 most common metrics for Vald data are:
            ```
                _________________________________________________________________________
                |         | metric                                     |  metric_count  |
                |---------|--------------------------------------------|----------------|
                |0        | leftAvgForce                               |3517            |
                |1        | leftMaxForce                               |3517            |
                |2        | leftImpulse                                |3514            |
                |3        | rightAvgForce                              |3514            |
                |4        | rightMaxForce                              |3514            |
                |5        | rightImpulse                               |3509            |
                |6        | leftTorque                                 |3475            |
                |7        | rightTorque                                |3472            |
                |8        | rightRepetitions                           |3460            |
                |9        | leftRepetitions                            |3452            |
            ```    
    6. Identifies how many unique metrics exist across all data sources
        * Identify the total number of distinct metrics recorded across all datasets.*
            -There are 548 unique metrics across all data sources.
    7. For each data source, show the date range and record count for the top metrics
        * Identify the date range and number of records for the most common metrics in each dataset.*
            - Hawkins Top Metrics Date Range and Record Count:
            -Date min_timestamp 2018-10-15 19:27:41 and max_timestamp 2025-10-14 12:50:32 for top metrics by data source Hawkins.
            ```
                ________________________________________________________________________________________________________
                |         | metric                             |  record_count  |   min_timestamp   |   max_timestamp   |
                |---------|------------------------------------|----------------|-------------------|-------------------|
                |0        |          System Weight(N)          |           31467|2018-10-15 19:27:41|2025-10-14 12:50:32|
                |1        | Propulsive Net Impulse(N.s)        |           31295|2018-10-15 19:27:41|2025-10-14 12:50:32|
                |2        | Peak Propulsive Force(N)           |          31295 |2018-10-15 19:27:41|2025-10-14 12:50:32|
                |3        | Avg. Propulsive Power(W)           |          31295 |2018-10-15 19:27:41|2025-10-14 12:50:32|
                |4        |          Jump Height(m)            |          31295 |2018-10-15 19:27:41|2025-10-14 12:50:32|
                |5        |      Peak Velocity(m/s)            |          31295 |2018-10-15 19:27:41|2025-10-14 12:50:32|
                |6        | Avg. Relative Propulsive Force(%)  |          31295 |2018-10-15 19:27:41|2025-10-14 12:50:32|
                |7        | Avg. Propulsive Force(N)           |          31295 |2018-10-15 19:27:41|2025-10-14 12:50:32|
            ```
                    - Kinexon Top Metrics Date Range and Record Count:
                    -Date min_timestamp 2021-06-17 21:49:39 and max_timestamp 2025-10-21 12:24:21 for top metrics by data source Kinexon.
            ```
                ______________________________________________________________________________________________________
                |         | metric                          |  record_count  |   min_timestamp   |   max_timestamp   |
                |---------|---------------------------------|----------------|-------------------|-------------------|
                |0         | track_outside_field            |          40803 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |1         | track_heart_rate_always        |          40803 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |2         | accel_load_accum               |          40703 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |3         | time_total                     |          40585 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |4         | accel_load_accum_avg_per_minute|          40485 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |5         | distance_total                 |          40317 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |6         | speed_distance_per_time        |          40316 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |7         | distance_total_avg_per_minute  |          40315 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |8         | speed_max                      |          40312 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |9         | speed_avg                      |          40298 |2021-06-17 21:49:39|2025-10-21 12:24:21|
            ```
                Vald Top Metrics Date Range and Record Count:
                Date min_timestamp 2020-12-14 12:56:23 and max_timestamp 2025-10-01 15:11:46 for top metrics by data source Vald.
            ```
                ______________________________________________________________________________________________________
                |         | metric                          |  record_count  |   min_timestamp   |   max_timestamp   |
                |---------|---------------------------------|----------------|-------------------|-------------------|
                |0        |leftAvgForce                     |           3517 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |1        |leftMaxForce                     |           3517 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |2        |leftImpulse                      |           3514 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |3        |rightAvgForce                    |           3514 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |4        |rightMaxForce                    |           3514 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |7        |rightTorque                      |           3472 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |8        |rightRepetitions                 |           3460 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |9        |leftRepetitions                  |           3452 |2020-12-14 12:56:23|2025-10-01 15:11:46|
            ```
    - `1.4` Brief Review Of Literature & Metric Selection (Group)
     - Based on your metric discovery, conduct a very brief literature review (does not need to follow and
abide by PRISMA framework due to limited time allowed):
     - Identify 3-5 key papers that discuss the relevance of your selected metrics to athlete performance and injury risk.
        - We selected the following metrics based on their prevalence in the datasets and their relevance to athlete performance and injury risk as discussed in the literature:
            - Bilateral Asymmetry Metrics (e.g., leftMaxForce, rightMaxForce, leftTorque, rightTorque)
            - Performance Metrics (e.g., accel_load_accum, distance_total)
     - Summarize the main findings of these papers in relation to your research question.
     - Justify your selection of metrics based on the literature review.
     - Document your findings in a shared document for team reference. 
     Our literature review document is found here:  https://docs.google.com/document/d/1hs3RljvobFhrrgEVS4Ev2E5Cl8YE0w7z1t3h8Qo_D-A/edit?tab=t.es53pvsqyhzj#heading=h.owyzndpwo8a8 and a final report is found in the `reports/` folder as `part4_research_synthesis.pdf`.
### 2. Data Cleaning and Preprocessing
The `part2_cleaning.py` script in the `scripts/` directory contains functions to clean and preprocess the data. It identifies metrics with missing records, calculates athlete measurement percentages, and flags athletes not tested in the last 6 months.
- `2.2` Missing Data Analysis (Group)
- 1. Identify which of our selected metrics have the most NULL or zero values
 - We analyzed the selected metrics (leftMaxForce, rightMaxForce, leftTorque, rightTorque, accel_load_accum, distance_total) for missing or zero values. The results showed that leftTorque and rightTorque had the highest number of NULL or zero values among the selected metrics.
- 2. For each sport/team, calculate what percentage of athletes have at least 5 measurements for selceted metrics (leftMaxForce, rightMaxForce, leftTorque, rightTorque, accel_load_accum, distance_total)
- We calculated the percentage of athletes with at least 5 measurements for each selected metric across different sports/teams. The results varied significantly, with some teams having over 100% coverage to as low as 5.26%.
- 3. Identify athletes who haven't been tested in the last 6 months (leftMaxForce, rightMaxForce, leftTorque, rightTorque, accel_load_accum, distance_total)
- We identified athletes who had not been tested in the last 6 months (180 days) for the selected metrics. 2 players (Baseball PLAYER 484 and Mens Lax PLAYER 726) were found to be missing tests, particularly for the the selected metrics (leftMaxForce, rightMaxForce, leftTorque, rightTorque, accel_load_accum, distance_total).
- 4. Determine if you have sufficient data to answer your research question
- After conducting the missing data analysis, we found that:
    - The metrics with the most NULL or zero values are leftTorque and rightTorque.
    - The percentage of athletes with at least 5 measurements for the selected metrics varies by sport/team, with some teams having over 100% coverage to as low as 5.26%.
    - Two athletes have not been tested in the last 6 months, particularly for the selected metrics (leftMaxForce, rightMaxForce, leftTorque, rightTorque, accel_load_accum, distance_total).
    - Based on this analysis, we determined that we have sufficient data to proceed with our research question, although we will need to account for missing values in our analyses. 
2.2 Data Transformation Challenge (Group)
- 1. Takes a player name (e.g., "PLAYER_001") and your selected metrics (e.g., "leftMaxForce", "rightMaxForce") as input
    - Returns a pandas DataFrame with:
        - Columns: timestamp, [your selected metrics]
        - One row per test session
        - Properly handles missing values
            - only include records where the team is not in ('Unknown','Player Not Found','Graduated (No longer enrolled)')
            - Concolidate team names by removing any single quotes
            -Saves the resulting DataFrame to a CSV file with the naming convention: `2.2_[first playername in list]_data_in_wide_format_by_athlete_and_metric.csv`
- `2.3` Create a Derived Metric (Group)
- 1. Calculates the mean value for each team (using the team column)
    - Saves the resulting DataFrame to a CSV file named `2.3-1&2_mean_value_for_each_team.csv`
- 2. For each athlete measurement, calculates their percent difference from their team's average
    - Saves the resulting DataFrame to a CSV file named `2.3-1&2_mean_value_for_each_team.csv`
- 3. Identifies the top 5 and bottom 5 performers relative to their team mean
    - Saves the top 5 players per team resulting DataFrame to a CSV file named `2.3-3_top_five_players_per_team.csv`
    - Saves the bottom 5 players per team resulting DataFrame to a CSV file named `2.3-3_bottom_five_players_per_team.csv`
- 4. Optional: Create z-scores as part of 3.2.1 as exported cleaned data
    - Z-scores or percentile rankings for each athlete within their team
# 3 Longitudinal Analysis & Visualization (Group)
- `3.1` Individual Athlete Timeline
  - Select 2 athletes from a team of your choice and use your selected metrics:
  - Create line plots showing their metric values over time (recommended: last 6-12 months)
  - Identify their best and worst performance dates
  - Calculate if they show improvement or decline trend (simple linear regression acceptable)
  - Relate your findings to your literature review - are the trends expected? Surprising?
  Results of Jupyter notebook by player 755 and 1128 in the team SBU Sports data Project are found below:
  ### Player 755
    - Part 1:https://colab.research.google.com/drive/1hVXnwQCo98i74oTtsnyllh1HDIaoZXDD?usp=drive_link
    - Part 2: https://colab.research.google.com/drive/1gMds29rwsUNJNJfpWdRJaMjEoiTARa6T?usp=drive_link
  ### Player 1128
    - Part 1: https://colab.research.google.com/drive/1gMds29rwsUNJNJfpWdRJaMjEoiTARa6T?usp=drive_link
    - Part 2: https://colab.research.google.com/drive/12RbkLah6NVb0m_d2NEfvQ1URxCP6Oq7O?usp=drive_link 

- `3.2` Team Comparison Analysis (Pair Work)
  - Compare two different teams/sports using the team column and your selected metrics:
  - Create box plots or violin plots comparing your selected metric(s) between teams
  - Calculate statistical significance (t-test or ANOVA as appropriate)
  - Create a visualization showing testing frequency by team over time
  - Interpret results in context of your literature review:
    Do differences make sense given sport demands?
    How do values compare to published norms (if available)?
    What might explain the differences or similarities?
    Results of Jupyter notebook part3_viz_comparison in the team SBU Sports data Project are found below:
    link to team part3_viz_comparison notebook: https://colab.research.google.com/drive/1pl6wRVZaPeZ0Pbktx6SGiONwlCW_hQ-0?usp=sharing

- `3.3` Dashboard Metric (Full Group)
   - Create a summary visualization that shows:
   - Total number of tests per month (all systems combined)
   - Breakdown by data source (stacked bar chart recommended)
   - Identify any gaps or unusual patterns in data collection
    link to team part3_viz_comparison notebook: https://colab.research.google.com/drive/1pl6wRVZaPeZ0Pbktx6SGiONwlCW_hQ-0?usp=sharing
    with additional analysis in: https://colab.research.google.com/drive/1jJDtOS29TCApR4HsrWrxdsDtnwxfeMhS?usp=sharing
# 4 Research Synthesis & Application
- `4.1` Performance Monitoring Flag System (Group)
    - Design a flagging system based on your selected metrics and literature review:
    - Based on your literature review, define thresold of asymmetricality of >10%- 15% in bilateral metrics as a risk factor for injury
    - Identify athletes who meet any of the following criteria:
    - Identify Athlete hasn't been tested in >30 days Left/right asymmetry if using bilateral metrics
- Deviation from team norms
- Justify your thresholds using evidence from your literature review
- Create a script that identifies athletes meeting your flag criteria
- Output a CSV with: playername, team, flag reason, metric value, last test date `4.1_part4_flagged_athletes.csv`
- `4.2` Research Synthesis & Recommendations (Group)
 Synthesize your findings into a research report (3-4 pages) that includes:
 - `Introduction:` Your research question and why it matters (based on literature gaps)
  - We selected our research question to investigate the relationship between bilateral asymmetry metrics and performance metrics in athletes, with the goal of improving athlete performance and reducing injury risk. This question is important because existing literature suggests that asymmetries greater than 10-15% may be linked to increased injury risk and decreased performance, yet there is a lack of comprehensive analysis using real-world sports performance data from multiple sources.
  - Our selected metrics include bilateral asymmetry metrics (leftMaxForce, rightMaxForce, leftTorque, rightTorque) and performance metrics (accel_load_accum, distance_total). These metrics were chosen based on their prevalence in the datasets and their relevance to athlete performance and injury risk as highlighted in our literature review.
- `Methods`:
    - We reviewed the data provided from three soruces: Hawkins, Kinexon, and Vald. We focused on bilateral asymmetry metrics (leftMaxForce, rightMaxForce, leftTorque, rightTorque) and performance metrics (accel_load_accum, distance_total) due to their relevance to athlete performance and injury risk as highlighted in our literature review.
    - Initial data exploration was conducted to understand the structure and quality of the data, including summary statistics and missing data analysis. We identified metrics with the most NULL or zero values and calculated the percentage of athletes with sufficient measurements and teams with duplication or invalid entries ie: 'Unknown','Player Not Found','Graduated (No longer enrolled)' crosswalked teams ie: 'Women's Basketball' and 'Womens Basketball' 
    - Data cleaning and preprocessing steps were implemented to handle missing values and prepare the data for analysis. We created derived metrics, such as percent difference from team averages, to contextualize athlete performance.
    - Longitudinal analyses were performed on selected athletes to assess performance trends over time, while team comparisons were made to identify differences in selected metrics between sports/teams.
    - Statistical methods included descriptive statistics, linear regression for trend analysis, and t-tests/ANOVA for team comparisons.
    - Our initial literature review identified key studies discussing the relevance of asymmetry of 10-15% to athlete performance and injury risk. This resulted in our hypothesis that athletes with greater asymmetry would exhibit lower performance metrics and higher injury risk.
    With this foundation, we utilized 10% as our threshold for flagging asymmetry in bilateral metrics as a risk factor for injury.
    Athletes who had asymmetric measurements greater than 10% a higher risk threshold , and less than 10% being a lower risk threshold.
    - Our inital data exploration and cleaning steps ensured that we had sufficient data quality to proceed with our analyses.
    However, we encountered challenges with matching athletes bilateral metrics measurements with corresponding performance metrics due to inconsistancies in data recording across sources and time stamps. This required careful data wrangling and validation to ensure accurate analyses. 
- `Results:`
    - It would be difficult to prove correlation between asymmetry and performance without robust data matching. This key insight deminished our available data to less than 1% from 44,314 to 383 records. Having measurements from multiple sources for the same athlete on the same date would have strengthened our anlaysis and statistical reliability. With more accurate data matching, we could have conducted more robust statistical analyses to assess the relationship between asymmetry and performance metrics. Due to these data challenges, our findings should be interpreted with caution. And we had to adjust our research question to focus more on data quality and flagging rather than definitive conclusions about asymmetry and performance because of the limited data we could not perform T-test designating our performance metrics as our independent variable and asymmetry as our dependent variable.
    With these considerations, we proceeded with our analyses to address our research question by with our performance metrics as our independent variable and asymmetry as our dependent variable. These results did not yield any statistical significance so we calculated the mean values for each category of asymmetry (low risk <10% and high risk >10%) and compared these values. This comparison showed little difference between the two groups.
    ![T-Test Performance vs Asymmetry](.\images\T-test_Asymmetry_Performance.png)
    We furthred our analysis by preforming a linear regression to determine wheter there are any coorrelations that could be identified between asymmetry and performance metrics. Again, these results did not yield any statistical significance yielding low R-squared values.
    ![Linear Regression Asymmetry vs Performance](.\images\Linear_Regression_Asymmetry_Performance.png)
    Despite these challenges, we were able to identify athletes who met our flag criteria based on asymmetry thresholds and testing frequency. This flagging system can serve as a useful tool for coaches and trainers to monitor athlete performance and identify potential injury risks.

- `Discussion:`
    - Unfortunately, due to data limitations and matching challenges, we were unable to determine a definitive relationship between bilateral asymmetry and performance metrics. However, our analysis highlighted the importance of data quality and consistency in sports performance research.
    To address these gaps, we developed a flagging system based on asymmetry thresholds and testing frequency that can aid coaches and trainers in monitoring athlete performance and identifying potential injury risks.
    Additionally, we recommend athletes and coaches perform at least one bilateral test with a performance measurement to better understand the relationship between asymmetry and performance.
    We believe with the improved data colletion and matching, future research could benefit from more robust analyese to help anthletes promote performance and reduce injury risk. Our findings emphasize the need for standardized data collection protocoles across different data sources and teams to ensure accureate and reliable analyses. While we could not draw definitive conclusions about asymmetry and preformance, we hope our flagging system and recommendations will contribute to improving athlete monitoring practices in the field.
- `Limitations & Future Directions:`
    - Our study faced several limitations, primarily related to data quality and matching challenges. The inconsistencies in data recording across sources and time stamps hindered our ability to accurately link bilateral asymmetry measurements with corresponding performance metrics. This limitation significantly reduced our analyzable dataset, impacting the statistical power of our findings.
    - Additionally, the lack of standardized data collection protocols across different teams and data sources introduced variability that may have influenced our results. Future research should focus on establishing uniform data collection practices to enhance data reliability and comparability.
    - To build upon our work, future studies should aim to collect more comprehensive datasets with consistent measurements across multiple time points. Implementing a standardized testing protocol that includes both bilateral asymmetry assessments and performance metrics would facilitate more robust analyses.
    - Furthermore, exploring additional factors such as training load, injury history, and biomechanical assessments could provide a more holistic understanding of the relationship between asymmetry and performance. Advanced statistical techniques, such as multivariate analyses or machine learning approaches, may also yield deeper insights into complex interactions between variables.
    - Overall, while our study was constrained by data limitations, it highlights the critical need for standardized data in sports performance research. By addressing these challenges, future investigations in the study of bilateral asymmetry on athlete performance and injury risk.
- `References:` 
1. Ashworth, B., Hank, M., Khaiyat, O., Coyles, G., Fallon Verbruggen, F., Zemkova, E., Zahalka, F., & Maly, T. (2025). Early Rate of Force Development and Maximal Strength at Different Positions of the Athletic Shoulder Test in Baseball Players. Sports, 13(9), 300.
2. García, F., Schelling, X., Castellano, J., Martín-García, A., Pla, F., & Vázquez-Guerrero, J. (2022). Comparison of the most demanding scenarios during different in-season training sessions and official matches in professional basketball players. Biology of Sport, 39(2), 237–244.
3. Junior, M. N. S. d. O., Veneroso, C. E., Ramos, G. P., Johnson, K. E., Guilkey, J. P., Sena, A. F. d. C., Cabido, C. E. T., & Cholewa, J. M. (2021). Distance and intensity profiles in Division I women's soccer matches across a competitive season. Sports, 9(5), 63.
4. Koyama, T., Nishikawa, J., Yaguchi, K., Irino, T., & Rikukawa, A. (2024). A comparison of the physical demands generated by playing different opponents in basketball friendly matches. Biology of Sport, 41(2), 527–533.
5. Nakatani, M., Murata, K., Kanehisa, H., & Takai, Y. (2021). Force-velocity relationship profile of elbow flexors in male gymnasts. PeerJ, 9, e10907.
6. Prudholme, D. C., Coburn, J. W., Lynn, S. K., & Lockie, R. G. (2022). Relationships between sprint, acceleration, and deceleration metrics with training load in Division I collegiate women's soccer players. Journal of Human Kinetics, 85(1), 53–62.
7. Ruiz-Rios, M., Setuain, I., Cadore, E. L., Izquierdo, M., & Garcia-Tabar, I. (2024). Physical conditioning and functional injury-screening profile of elite female soccer players: a systematic review. International Journal of Sports Physiology and Performance, 19(11), 1355–1366.
8. Şahbat, Y., Kütük, E., Çat, G., Ünsalan, O., Kart, H., Topkar, O. M., Baysal, Ö., & Erol, B. (2022). An unusual injury pattern: arm wrestling injury, treatment modalities, clinical outcomes, and return to sport. Acta Orthopaedica et Traumatologica Turcica, 56(1), 1–6.
9. Schaefer, L. V., Carnarius, F., Dech, S., & Bittmann, F. N. (2023). Repeated measurements of Adaptive Force: Maximal holding capacity differs from other maximal strength parameters and preliminary characteristics for non-professional strength vs. endurance athletes. Frontiers in Physiology, 14, 1020954.
10. Spiering, B. A., Clark, B. C., Schoenfeld, B. J., Foulis, S. A., & Pasiakos, S. M. (2023). Maximizing Strength: The Stimuli and Mediators of Strength Gains and Their Application
to Training and Rehabilitation. Journal of Strength and Conditioning Research, 37(4), 919–929.
11. Tavares, N., Vilas-Boas, J. P., & Castro, M. A. (2025). Effect of Preventive Exercise Programs for Swimmer's Shoulder Injury on Rotator Cuff Torque and Balance in Competitive Swimmers: A Randomized Controlled Trial. Healthcare, 13(5), 538.
12. Xiao, M., Nguyen, J. N., Hwang, C. E., & Abrams, G. D. (2021). Increased lower extremity injury risk associated with player load and distance in collegiate women's soccer. The Orthopaedic Journal of Sports Medicine, 9(10), 23259671211048248.

Report saved in `part4_research_synthesis.pdf` in the `reports` folder
- `4.3` Final Presentation (Group)
-`Introduction (2 min):`
    - Your research question/hypothesis
    - Why it matters (the gap you're addressing)
    - Your selected metrics and why
-`Methods (2 min):`
    - Data overview and quality assessment
    - Analysis approach
-`Key Findings (4 min):`
    - Main results with visualizations
    - Statistical findings
    - Comparison to literature
-`Practical Applications (2 min):`
    - Your performance monitoring flag system
    - Recommendations for coaches/trainers
    - How your findings fill the identified gap
-`Limitations & Future Work (1 min):`
    - Data challenges you encountered
    - What additional research is needed
-`Q&A (1-2 min)`
    - Presentation slides are found in saved at:  https://docs.google.com/presentation/d/1IiI5CwbIHg4V8L8NR5JBr0AiKxmIxBGMQci9IVsK6oo/edit?usp=sharing and a copy of the slides are stored as `AHI 507_ Sports Data.pptx` in the `reports` folder
