import platform as platform
import numpy as np
from common_clean_functions import get_athletes_not_tested_in_last_num_days,get_all_clean_metrics_records

##4.1 Identify athletes who haven't been tested in the last 30 days(for your selected metrics)
get_athletes_not_tested_in_last_num_days(30,"4.1")
##4.2 Identify athletes who asymmetrically difference is >= 10% to flag potential injury risk
all_clean_metrics_records = get_all_clean_metrics_records("wide")
# Use bitwise | operator for pandas Series comparison (not 'or')
athletes_at_risk_based_on_asymmetrical_difference=all_clean_metrics_records[(all_clean_metrics_records['avg_max_force_asymmetry'].notnull()) | (all_clean_metrics_records['avg_torque_asymmetry'].notnull())]

# Calculate max asymmetry and categorize into 3 risk levels: Normal or low (<10%), At Risk (10-15%), HIGH risk (15%+)
max_asymmetry = np.maximum(
    abs(athletes_at_risk_based_on_asymmetrical_difference['avg_max_force_asymmetry'].fillna(0)),
    abs(athletes_at_risk_based_on_asymmetrical_difference['avg_torque_asymmetry'].fillna(0))
)
athletes_at_risk_based_on_asymmetrical_difference['Injury_Risk_Level'] = np.select(
    [max_asymmetry < 10, (max_asymmetry >= 10) & (max_asymmetry < 15), max_asymmetry >= 15],
    ['Normal or Low', 'At Risk', 'HIGH Risk'],
    default='Normal or Low'
)
athletes_at_risk_based_on_asymmetrical_difference.to_csv('output/4.1-athletes_at_risk_based_on_asymmetrical_difference.csv')