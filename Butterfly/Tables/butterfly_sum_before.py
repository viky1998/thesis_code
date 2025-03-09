from butterfly import Butterfly
butterfly = Butterfly()

# Set the ranges for c and N
c_range = range(5, 20)
N_range = range(9, 24)

# Calculate the sum before the first occurrence of c
df_sum_before = butterfly.get_table_sum_before(c_range, N_range)
pivot_sum_before = df_sum_before.pivot(index='c', columns='logn', values='sum_before_first_c')

# Print the pivot table
print(pivot_sum_before)

# # Save the pivot table to a csv file
# pivot_sum_before.to_csv('pivot_sum_before.csv')