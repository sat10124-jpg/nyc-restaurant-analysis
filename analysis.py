import pandas as pd 
df = pd.read_csv('restaurant_data.csv')
print(df.head(5))
# Clean the data by dropping rows where 'BORO' or 'CRITICAL FLAG' is missing
# Group by 'BORO' and count the number of 'Critical' violations
# Filter the DataFrame to include only rows where 'CRITICAL FLAG' is 'Critical'
critical_violations = df[df['CRITICAL FLAG'] == 'Critical'].groupby('BORO').size().reset_index(name='Critical Violations')
# Sort the DataFrame by 'Critical Violations' in descending order
critical_violations = critical_violations.sort_values('Critical Violations', ascending=False)