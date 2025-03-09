import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


# Define the functions
def g(n):
    return 3 * (n * np.log2(n) - n + 1) +n

def h(n):
    return 3 * ((n) / 2) * np.log2(n) +n

# the number of additional stages is set to log2(n)/2
def i(n):
    return 3 * ((n) / 2) * (np.log2(n)+np.log2(n)/2) +n

# Generate a range of n values (n starts at 32 to scale the plot)
n = np.linspace(32, 500000, 1000000)

# Compute the proof size of each function's values
log_g = 2*np.log2(g(n)) +13 
log_h = 2*np.log2(h(n))+13
log_i = 2*np.log2(i(n))+13

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(n, log_g, label='Permutation Network', color='green')
plt.plot(n, log_h, label='Butterfly Network', color='red')
plt.plot(n, log_i, label='Extended Butterfly Network', color='m')

# Label the axes
plt.xlabel('Number of inputs n')
plt.ylabel('Proof Size')
# plt.title('Proof Size Comparison')

# Create a legend box
plt.legend(loc='lower right')

# Add thousands delimiters to the x-axis
formatter = FuncFormatter(lambda x, pos: f'{int(x):,}'.replace(',', '.'))
plt.gca().xaxis.set_major_formatter(formatter)

plt.grid(True)
# plt.show()

plt.savefig('plot_proof_size_comparison_extended.png', dpi=1200)