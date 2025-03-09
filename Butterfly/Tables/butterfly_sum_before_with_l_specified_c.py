from butterfly import Butterfly
butterfly = Butterfly()

# Set the range for N and specify c
c = 5
N_range = range(9, 21)

# Calculate the sum before the first occurrence of c with l additional stages
df_sum_before_with_l_specified_c = butterfly.get_table_sum_before_with_l_specified_c(c, N_range)
pivot_sum_before_with_l_specified_c = df_sum_before_with_l_specified_c.pivot(index='l', columns='logn', values='sum_before_first_c')

# Print the pivot table
print(pivot_sum_before_with_l_specified_c)

# # Save the pivot table to a csv file
# pivot_sum_before_with_l_specified_c.to_csv('pivot_sum_before_with_l_specified_c.csv')