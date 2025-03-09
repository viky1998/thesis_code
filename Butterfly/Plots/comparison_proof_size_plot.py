import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Set the parameter k 
k = 256

# Define the functions

# Zig-Zag Sort
def f(n):
    return 2 * 2 * 10**4 * n * np.log2(n) * (4*k-2) +n

# Bitonic Sort
def j(n):
    return 2 * (4*k-2) * ((n) / 4) * np.log2(n) * (np.log2(n) + 1) +n 

# Permutation network
def g(n):
    return 3 * (n * np.log2(n) - n + 1) +n

# Butterfly network
def h(n):
    return 3 * ((n) / 2) * np.log2(n)+n


# Generate a range of n values (n starts at 2 to avoid log(0))
n = np.linspace(2, 500000, 1000000)

# Compute the proof size of each function's values
log_g = 2*np.log2(g(n)) +13 
log_h = 2*np.log2(h(n))+13
log_f = 2*np.log2(f(n))+13
log_j = 2*np.log2(j(n))+13

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(n, log_f, label='Zig-Zag Sort')
plt.plot(n, log_j, label='Bitonic Sort')
plt.plot(n, log_g, label='Permutation Network')
plt.plot(n, log_h, label='Butterfly Network')

# Label the axes
plt.xlabel('Number of inputs n')
plt.ylabel('Proof Size')
plt.title('Proof Size Comparison')

# Create a legend box
plt.legend(loc='best')

# Add thousands delimiters to the x-axis
formatter = FuncFormatter(lambda x, pos: f'{int(x):,}'.replace(',', '.'))
plt.gca().xaxis.set_major_formatter(formatter)

plt.grid(True)
# plt.show()

plt.savefig('plot_proof_size_comparison.png', dpi=1200)