from butterfly import Butterfly
butterfly = Butterfly()

# Set the ranges for c and N
c_range = range(5, 20)
N_range = range(9, 28)

# Calculate the necessary values of l for each c and N
df_necessary_l = butterfly.get_table_necessary_l(c_range, N_range)
pivot_necessary_l = df_necessary_l.pivot(index='c', columns='logn', values='l')

# Print the pivot table
print(pivot_necessary_l)

# # Save the pivot table to a csv file
# pivot_necessary_l.to_csv('pivot_necessary_l.csv')