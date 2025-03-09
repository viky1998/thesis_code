from butterfly import Butterfly
butterfly = Butterfly()

# Set the ranges for N and l
N_range = range(5, 20)
l_range = range(1, 20)

# Calculate the comparison values of c for each N and l
df_anonymity_comparison = butterfly.get_table_c_anonymity_comparison(N_range, l_range)
pivot_anonymity_comparison = df_anonymity_comparison.pivot(index='l', columns='logn', values='c_comparison')

# Print the pivot table
print(pivot_anonymity_comparison)

# # Save the pivot table to a csv file
# pivot_anonymity_comparison.to_csv('pivot_anonymity_comparison.csv')