from butterfly import Butterfly
butterfly = Butterfly()

# Set the ranges for c and N
c_range = range(5, 20)
N_range = range(5, 20)

# Calculate the sum before the first occurrence of c with l additional stages
df_sum_before_with_l = butterfly.get_table_sum_before_with_l(c_range, N_range)
pivot_sum_before_with_l = df_sum_before_with_l.pivot(index=['c','l'], columns='logn', values='sum_before_first_c')

# Print the pivot table
print(pivot_sum_before_with_l)

# # Save the pivot table to a csv file
# pivot_sum_before_with_l.to_csv('pivot_sum_before_with_l.csv')