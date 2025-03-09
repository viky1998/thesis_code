import pandas as pd 

class Butterfly:
    def __init__(self, sigma = 256):
        # If needed, change the value of the parameter sigma
        self.sigma = sigma
        pass


    def recursive_list(self, n, lst=[0]):
        # Creates the recursive list for the given value of n The ith entry of
        # the list is the number of switches that need to be activated to fix
        # the position of the ith input after i-1 inputs have already been
        # routed in the Butterfly network
        if n == 0:
            return lst
        new_lst = [x + 1 for x in lst] + lst
        return self.recursive_list(n - 1, new_lst)

    def find_first_occurrence(self, lst, c):
        # Returns the index of the first occurrence of the value c in the list
        try:
            index = lst.index(c)
            return index
        except ValueError:
            return -1
        
    def find_first_occurrence_with_condition(self, lst, c):
        # For the case with l extra rounds, the order of the elements is not as
        # simple as the original recursive list. This function finds the first
        # occurrence of the value c in the list, or the first value less than c.
        for index, value in enumerate(lst):
            if value <= c:
                return index
        return -1
        
    def sum_before_first_occurrence(self, lst, c):
        # Calculate the sum of the elements in the list before the first occurrence of the
        # value c in the list
        index = self.find_first_occurrence_with_condition(lst=lst, c=c)
        if index == -1:
            return 0
        return sum(lst[:index])
    
    def check_sum_and_next_element(self, lst, c):
        # Calculate the sum of the elements in the list before the first occurrence of the
        # value c in the list and check at which element it is greater than 256
        # and return the next element

        index = self.find_first_occurrence_with_condition(lst=lst, c=c)
        if index == -1:
            return None
        
        current_sum = 0
        for i in range(index):
            current_sum += lst[i]
            if current_sum > self.sigma:
                return lst[i + 1] if i + 1 < len(lst) else None
        return None
    
    def get_table_sum_before(self, c_range, n_range):
        # for each n in n_range and c in c_range, calculate the sum before the
        # first occurrence of the value c
        results = []
        # Loop through the values of n 
        for n in n_range:
            # Loop through the values of c 
            for c in c_range:
                # Calculate the sum before the first occurrence of c
                current_list = self.recursive_list(n)
                current_sum = self.sum_before_first_occurrence(current_list, c)
                # Append the result to the list
                results.append({'logn': n, 'c': c, 'sum_before_first_c': current_sum})
        return pd.DataFrame(results)
    
    def modified_recursive_list(self, n, l, lst=[0]):
        # Modify the recursive list to include l extra rounds
        lst = self.recursive_list(n, lst)
        if l == 0: return lst
        l_list = self.recursive_list(l)
        for i in range(2**n):
            lst[i] += l_list[i % 2**l]
        return lst
    
    def get_table_necessary_l(self, c_range, n_range):
        # For each n in n_range and c in c_range, calculate the smallest l such
        # that the sum before the first occurrence of c is greater than 256
        results = []
        # Loop through the values of n 
        for n in n_range:
            # Loop through the values of c 
            current_list = self.recursive_list(n)
            
            for c in c_range:
                # Find the smallest l such that the sum before the first
                # occurrence of c is greater than sigma
                c_index = self.find_first_occurrence_with_condition(current_list, c)
                if c_index == -1:
                    continue
                l_value = 0
                current_mod_list = self.modified_recursive_list(n, l_value)
                while sum(current_mod_list[:c_index]) < self.sigma:
                    l_value += 1
                    if n-l_value > 0: current_mod_list = self.modified_recursive_list(n, l_value) 
                    else: break #TODO: check if continue or break
                # Append the result to the list
                if c<=n+l_value : results.append({'logn': n, 'c': c, 'l': l_value})
        return pd.DataFrame(results)
    
    def get_table_sum_before_with_l(self, c_range, n_range):
        # for each n in n_range and c in c_range, calculate the sum before the
        # first occurrence of a given c
        results = []
        # Loop through the values of n 
        for n in n_range:
            normal_list = self.recursive_list(n)
            # Loop through the values of c 
            for c in c_range:
                if c > n:
                    continue
                index_normal = self.find_first_occurrence(normal_list, c)
                for l in range(n):
                    # Calculate the sum before the first occurrence of c
                    modified_list = self.modified_recursive_list(n, l)
                    sum_mod = sum(modified_list[:index_normal])
                    results.append({'logn': n, 'c': c, 'l': l, 'sum_before_first_c': sum_mod})
        return pd.DataFrame(results)
    
    def get_table_sum_before_with_l_specified_c(self, c, n_range):
        # for each n in n_range and additional stages l, calculate the sum before the
        # first occurrence of  c
        results = []
        # Loop through the values of n 
        for n in n_range:
            normal_list = self.recursive_list(n)
            if c > n: return None
            index_normal = self.find_first_occurrence(normal_list, c)
            for l in range(n):
                # Calculate the sum before the first occurrence of c
                modified_list = self.modified_recursive_list(n, l)
                sum_mod = sum(modified_list[:index_normal])
                results.append({'logn': n, 'l': l, 'sum_before_first_c': sum_mod})
        return pd.DataFrame(results)
    
    def calc_sum_formula(self, n, c):
        # Calculate the sum of the elements in the list before the first occurrence of the
        # value c in the list using the formula
        return (n+c)/2 *2**(n-c) - c

    def get_index_and_c(self, lst):
        current_sum = 0
        for i in range(len(lst)):
            current_sum += lst[i]
            if current_sum > self.sigma:
                if i+1 < len(lst):
                    index_for_c = i+1
                    current_c = lst[i+1]
                    return [index_for_c, current_c]
                else: return None
        return None
    
    def get_table_c_anonymity_comparison(self,n_range, l_range):
        results = []
        for n in n_range:
            normal_list = self.recursive_list(n)
            for l in l_range:
                if l >= n:
                    continue
                modified_list = self.modified_recursive_list(n, l)

                index_c_mod = self.get_index_and_c(modified_list)
                if index_c_mod is None:
                    continue
                index_modified = index_c_mod[0]
                c_old = index_c_mod[1]
                c_modified = normal_list[index_modified]

                index_c_norm = self.get_index_and_c(normal_list)
                if index_c_norm is None:
                    continue
                c_normal = index_c_norm[1]

                results.append({'logn': n, 'l': l, 'c_comparison': [c_old, c_modified, c_normal]})
        return pd.DataFrame(results)
    
    