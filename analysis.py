import pandas as pd 
df = pd.read_csv('restaurant_data.csv')
print(df.head(5))
# Clean the data by droppping rows where 'BORO' or "CRITICAL FLAG' is missing
df_cleaned = df.dropna(subset=['BORO', 'CRITICAL FLAG'])
# Group the data by 'BORO' and count the number of critical violations
critical_violations = df_cleaned[df_cleaned['CRITICAL FLAG'] == 'Critical'].groupby('BORO').size()
# Print the number of critical violations for each borough
print("Critical Violations by Borough:")
print(critical_violations)

# Import matplotlib.pyplot and seaborn 
import matplotlib.pyplot as plt
import seaborn as sns
#Set the style of the plot to whitegrid
sns.set_style('whitegrid')
# Create a bar plot of the critical_violations data
plt.figure(figsize=(10, 6))
sns.barplot(x=critical_violations.index, y=critical_violations.values)
plt.title('Critical health violations by NYC Borough')
plt.xlabel('Borough')
plt.ylabel('Number of Critical Violations')
plt.show()
