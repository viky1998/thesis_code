import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define a vector of c values from 0 to 20
c_vals = np.linspace(0, 20, 201)
N_sol = np.zeros_like(c_vals)

# Use an initial guess for N; this guess will be updated at each step
initial_guess = 6.3

# Loop over each c value and solve for N
for i, c in enumerate(c_vals):
    # Define the function whose root we are looking for:
    # f(N) = (N+c)*2^(N-c-1) - c - 256 = 0
    def eqfun(N):
        return (N + c) * 2**(N - c - 1) - c - 256

    # Solve for N using fsolve with the current initial guess
    sol = fsolve(eqfun, initial_guess)
    N_sol[i] = sol[0]
    # Update the initial guess for the next iteration
    initial_guess = sol[0]

# Plot the results: c on the x-axis and N on the y-axis.
plt.figure()
plt.plot(c_vals, N_sol, linewidth=2)
plt.xlabel('c')
plt.ylabel('log(n)')
plt.title('Sum before first occurence of c >= 256 \n Solution of 256 = (log(n)+c)*2^(log(n)-c-1) - c')
plt.grid(True)
plt.show()
