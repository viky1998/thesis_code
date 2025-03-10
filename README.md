# Switching Networks Analysis

This repository contains the code for the master's thesis titled "More Efficient
Zero-Knowledge Arguments for the Correctness of a Shuffle" by Viktoria Chiara
Hablas.

## Installation Instructions

To execute the code within this repository, ensure that Python 3.8.12 is
installed on your system.

### Virtual Environment Setup

It is advisable to utilize a virtual environment for dependency management. You
can create and activate a virtual environment with the following commands:

```bash
python3.8 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Dependency Installation

After activating the virtual environment, install the necessary dependencies
using pip:

```bash
pip install -r requirements.txt
```

## Code Execution

To execute the code, run the specific Python files as required.

## Repository Structure

The repository is organized into two primary tasks:

- Analysis of the Butterfly Network
- Analysis of the Waksman Network

### Butterfly Network

This section contains code for analyzing the Butterfly network. Each Python file provides detailed information on generating various analyses by selecting different parameters.

#### Tables

- **butterfly.py**: Defines the `Butterfly` class with methods for analyzing the Butterfly network, including generating recursive lists, finding the first occurrence of a value, calculating sums, and modifying lists. It also generates tables for different analyses.

- **butterfly_sum_before.py**: Calculates the sum before the first occurrence of the parameter `c` for different values of `c` and `N`. Generates a pivot table with `c` as the index and `logn` as the columns.

- **butterfly_sum_before_with_l.py**: Calculates the sum before the first occurrence of `c` with `l` additional stages for different values of `c` and `N`. Generates a pivot table with `c` and `l` as the index and `logn` as the columns.

- **butterfly_sum_before_with_l_specified_c.py**: Calculates the sum before the first occurrence of `c` with `l` additional stages for different values of `N`. Generates a pivot table with `l` as the index and `logn` as the columns.

- **butterfly_necessary_l.py**: Calculates the necessary values of `l` for different values of `c` and `N`. Generates a pivot table with `c` as the index and `logn` as the columns.

- **butterfly_c_anonymity_comparison.py**: Compares the values of `c` for different values of `N` and `l`. Generates a pivot table with `l` as the index and `logn` as the columns. Compares three values for `c`: the value in the list \(A_{N,l}\), the worst-case value for \(A_{N,l}\), and the value from \(A_N\).

#### Plots

- **comparison_proof_size_plot.py**: Generates a comparative plot of proof sizes for different verifiable shuffle approaches, including Zig-Zag Sort, Bitonic Sort, Permutation Network, and Butterfly Network. Saves the plot as `plot_proof_size_comparison.png`.

- **comparison_proof_size_plot_extended.py**: Generates a comparative plot of proof sizes for different verifiable shuffle approaches, including the Permutation Network, Butterfly Network, and an Extended Butterfly Network. Saves the plot as `plot_proof_size_comparison_extended.png`.

- **necessaryN_plot.py**: Generates a plot to determine the relationship between `c` and `N` required to satisfy the equation \((N + c) \cdot 2^{(N - c - 1)} - c = 256\). Displays the plot with integer-only axis labels.

#### CSVs

The tables generated are saved in CSV format within this folder.

### Waksman Network

This section includes code from the exploratory phase of the thesis, where the Waksman network was examined. Although this approach was ultimately deemed impractical and excluded from the final thesis, a basic implementation for 8 inputs is provided to illustrate the impact of faulty switches in a switching network.

- **Waksman_8.py**: Implements the Waksman network for 8 inputs. Includes methods to generate all possible switch combinations and permutations of the input sequence, evaluate the effect of different switch configurations, and calculate the frequency of each resulting permutation. Results are stored in a pandas DataFrame.

- **waksman.ipynb**: A Jupyter Notebook for exploring and analyzing the Waksman network for 8 inputs. Focuses on the behavior of output permutations when switches are faulty. Designed for experimentation and understanding of network theory and faulty switches.
