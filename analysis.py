import pandas as pd 
df = pd.read_csv('restaurant_data.csv')
print(df.head(5))
# Cleaning the data by droppping rows where 'BORO' or "CRITICAL FLAG' is missing
df_cleaned = df.dropna(subset=['BORO', 'CRITICAL FLAG'])
# grouping the data by 'BORO' and count the number of critical violations
critical_violations = df_cleaned[df_cleaned['CRITICAL FLAG'] == 'Critical'].groupby('BORO').size()
# Print the number of critical violations for each borough
print("Critical Violations by Borough:")
print(critical_violations)

# Importing matplotlib.pyplot and seaborn 
import matplotlib.pyplot as plt
import seaborn as sns
#Setting the style of the plot to whitegrid
sns.set_style('whitegrid')
# Creating a bar plot of the critical_violations data
plt.figure(figsize=(10, 6))
sns.barplot(x=critical_violations.index, y=critical_violations.values)
plt.title('Critical health violations by NYC Borough')
plt.xlabel('Borough')
plt.ylabel('Number of Critical Violations')
plt.show()

# Finding the top 10 most common violation descriptions in the dataset and print them
top_violations = df_cleaned['VIOLATION DESCRIPTION'].value_counts().head(10)
print("\nTop 10 Most Common Violation Descriptions:")
print(top_violations)

# Creating a new column called 'IS_PEST' that is True if 'VIOLATION DESCRIPTION' contains 'mice', 'files', or 'rat' (case-insensitive), and False otherwise
df_cleaned['IS_PEST'] = df_cleaned['VIOLATION DESCRIPTION'].str.contains('mice|flies|rat', case=False, na=False)
# Printing the total number of pest related violations
pest_violations_count = df_cleaned['IS_PEST'].sum()
print(f"\nTotal Pest-Related Violations in NYC: {pest_violations_count}")

# Grouping by 'BORO' and calculate the percentage of pest-related violations
pest_violations_by_boro = df_cleaned.groupby('BORO')['IS_PEST'].mean() * 100
# Printing the percentage of pest-related violations for each borough
print(f"\nPercentage of Pest-Related Violations by Borough:")
print(pest_violations_by_boro)

# Importing chi2_contingency from scipy.stats
from scipy.stats import chi2_contingency
# Creating a contigency table (crosstab) between 'BORO' and 'IS_PEST'
contingency_table = pd.crosstab(df_cleaned['BORO'], df_cleaned['IS_PEST'])
# Running a chi-squared test on the contiengecy table and pritning the ch2 stat and p-value
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

print("\n--- Statistical test Results ---")
print(f"Chi-squared Statistic: {chi2_stat:.4f}")
print(f"P-Value: {p_value:.4f}")
print(f"Degrees of Freedom: {dof}")

# Interpreting the results of these values 
alpha = 0.05
if p_value < alpha:
    print("Conclusion: Reject the null hypothesis: The relationship between borough and pest-related violations is statistically significant.")
else:    print("Conclusion: Fail to reject the null hypothesis: The relationship between borough and pest-related violations is not statistically significant.")