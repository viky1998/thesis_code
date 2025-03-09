import pandas as pd

class Butterfly:
    def recursive_list(self, n, lst=[0]):
        # Creates the recursive list for the given value of n
        if n == 0:
            return lst
        new_lst = [x + 1 for x in lst] + lst
        return self.recursive_list(n - 1, new_lst)

    def find_first_occurrence(self, lst, c):
        # Find the first occurrence of the value c in the list
        try:
            index = lst.index(c)
            return index
        except ValueError:
            return -1
        
    def find_first_occurrence_with_condition(self, lst, c):
        # For the case with k extra rounds, the order of the elements is not as
        # simple as the original recursive list. This function finds the first
        # occurrence of the value c in the list, or the first value less than c.
        for index, value in enumerate(lst):
            if value < c:
                return index
            if value == c:
                return index
        return -1
        
    def sum_before_first_occurrence(self, lst, c):
        # Calculate the sum of the elements before the first occurrence of the
        # value c in the list
        index = self.find_first_occurrence_with_condition(lst=lst, c=c)
        if index == -1:
            return 0
        return sum(lst[:index])
    
    def check_sum_and_next_element(self, lst, c):
        # Calculate the sum of the elements before the first occurrence of the
        # value c in the list and check at which element it is greater than 256
        # and return the next element

        index = self.find_first_occurrence_with_condition(lst=lst, c=c)
        if index == -1:
            return None
        
        current_sum = 0
        for i in range(index):
            current_sum += lst[i]
            if current_sum > 256:
                return lst[i + 1] if i + 1 < len(lst) else None
        return None
    
    def get_table_sum_before_c(self, c, n_range):
        # for each n in n_range, calculate the sum before the first occurrence
        # of a given c

        results = []
        # Loop through the values of n_range
        for n in n_range:
            # Generate the recursive list for the current value of n
            current_result = self.recursive_list(n)
            # Calculate the sum before the first occurrence of c
            current_sum = self.sum_before_first_occurrence(current_result, c)
            # Append the result to the list
            results.append({'n': n,'c': c, 'sum_before_first_c': current_sum})
        # Create a DataFrame from the results
        return pd.DataFrame(results)
    
    def get_table_sum_before(self, c_range, n_range):
        # for each n in n_range and c in c_range, calculate the sum before the
        # first occurrence of a given c
        results = []
        # Loop through the values of n 
        for n in n_range:
            # Loop through the values of c 
            for c in c_range:
                # Calculate the sum before the first occurrence of c
                current_result = self.recursive_list(n)
                current_sum = self.sum_before_first_occurrence(current_result, c)
                # Append the result to the list
                results.append({'logn': n, 'c': c, 'sum_before_first_c': current_sum})
        return pd.DataFrame(results)
    
    def modified_recursive_list(self, n, k, lst=[0]):
        # Modify the recursive list to include k extra rounds
        lst = self.recursive_list(n, lst)
        if k == 0: return lst
        k_list = self.recursive_list(k)
        for i in range(2**n):
            lst[i] += k_list[i % 2**k]
        return lst
    
    def get_table_necessary_k(self, c_range, n_range):
        # For each n in n_range and c in c_range, calculate the smallest k such
        # that the sum before the first occurrence of c is greater than 256
        results = []
        # Loop through the values of n 
        for n in n_range:
            # Loop through the values of c 
            for c in c_range:
                # Find the smallest k such that the sum before the first
                # occurrence of c is greater than 256
                k_value = 0
                current_result = self.modified_recursive_list(n, k_value)
                while self.sum_before_first_occurrence(current_result, c) < 256:
                    k_value += 1
                    if n-k_value > 0: current_result = self.modified_recursive_list(n, k_value) 
                    else: break
                # Append the result to the list
                if c<=n+k_value : results.append({'logn': n, 'c': c, 'k': k_value})
        return pd.DataFrame(results)
    

    def get_table_k_anonymity(self, c_range, n_range):
        # A different approach to still satisfy 2^c anonymity, but this is
        # probably wrong
        results = []
        # Loop through the values of n 
        for n in n_range:
            # Loop through the values of c 
            for c in c_range:
                # Find the smallest k such that the sum before the first
                # occurrence of c is greater than 256
                k_value = 0
                current_result = self.modified_recursive_list(n, k_value)
                while self.sum_before_first_occurrence(current_result, c) < 256:
                    k_value += 1
                    if n-k_value > 0: current_result = self.modified_recursive_list(n, k_value) 
                    else: break
                c_index = self.find_first_occurrence_with_condition(current_result, c)
                while self.recursive_list(n)[c_index] < c:
                    k_value += 1
                    if n-k_value > 0: current_result = self.modified_recursive_list(n, k_value)
                    else : break
                    c_index = self.find_first_occurrence_with_condition(current_result, c)
                if sum(current_result[:c_index])>=256: results.append({'logn': n, 'c': c, 'k': k_value})
                # Append the result to the list
                if c<=n+k_value : results.append({'logn': n, 'c': c, 'k': k_value})
        return pd.DataFrame(results)
    

    def calc_sum_formula(self, n, c):
        return (n+c)/2 *2**(n-c) - c
    
    
    def get_index_and_c(self, lst):
        current_sum = 0
        for i in range(len(lst)):
            current_sum += lst[i]
            if current_sum > 256:
                if i+1 < len(lst):
                    index_for_c = i+1
                    current_c = lst[i+1]
                    # return [index_for_c, current_c]
                else: return None

                # check if any value in the list before c is smaller than c
                for j in range(index_for_c):
                    if lst[j] < current_c:
                        current_c = lst[j]
                return [index_for_c, current_c]
        return None
    
    def get_index_and_c_2(self, lst):
        current_sum = 0
        for i in range(len(lst)):
            current_sum += lst[i]
            if current_sum > 256:
                if i+1 < len(lst):
                    index_for_c = i+1
                    current_c = lst[i+1]
                    return [index_for_c, current_c]
                else: return None
        return None
    
    def get_smallest_c(self, lst, index):
        current_c = lst[index]
        for i in range(index):
            if lst[i] < current_c:
                current_c = lst[i]
        return current_c
    
    def get_biggest_c(self, lst, index):
        current_c = lst[index]
        for i in range(index, len(lst)):
            if lst[i] > current_c:
                current_c = lst[i]
        return current_c
    
    def get_table_c_anonymity_comparison(self,n_range, k_range):
        results = []
        for n in n_range:
            for k in k_range:
                if k >= n:
                    continue
                normal_list = self.recursive_list(n)
                modified_list = self.modified_recursive_list(n, k)

                index_c_mod = self.get_index_and_c(modified_list)
                if index_c_mod is None:
                    continue
                index_modified = index_c_mod[0]
                c_old = index_c_mod[1]
                c_modified = self.get_smallest_c(normal_list, index_modified)

                index_c_norm = self.get_index_and_c(normal_list)
                if index_c_norm is None:
                    continue
                c_normal = index_c_norm[1]
                c_normal_smallest = self.get_smallest_c(normal_list, index_c_norm[0])

                # results.append({'logn': n, 'k': k, 'min_c_in_mod': c_modified, 'c_normal': c_normal})
                results.append({'logn': n, 'k': k, 'c_comparison': [c_old, c_modified, c_normal, c_normal_smallest]})
        return pd.DataFrame(results)
    
    def get_table_c_anonymity_comparison_2(self,n_range, k_range):
        results = []
        for n in n_range:
            for k in k_range:
                if k >= n:
                    continue
                normal_list = self.recursive_list(n)
                modified_list = self.modified_recursive_list(n, k)

                index_c_mod = self.get_index_and_c_2(modified_list)
                if index_c_mod is None:
                    continue
                index_modified = index_c_mod[0]
                c_old = index_c_mod[1]
                c_modified = normal_list[index_modified]
                # c_mod_biggest = self.get_biggest_c(normal_list, index_modified)

                index_c_norm = self.get_index_and_c_2(normal_list)
                if index_c_norm is None:
                    continue
                c_normal = index_c_norm[1]
                # c_normal_biggest = self.get_biggest_c(normal_list, index_c_norm[0])

                # results.append({'logn': n, 'k': k, 'min_c_in_mod': c_modified, 'c_normal': c_normal})
                results.append({'logn': n, 'k': k, 'c_comparison': [c_old, c_modified, c_normal]})
        return pd.DataFrame(results)
    
    def modified_recursive_list_3(self, n, k, lst=[0]):
        # Modify the recursive list to include k extra rounds
        lst = self.recursive_list(n, lst)
        if k == 0: return lst
        k_list = self.recursive_list(k)
        k_list = [item for item in k_list for _ in range(2**(n-k))]
        if len(lst) != len(k_list):
            raise ValueError("lst and k_list must have the same length")
        lst = [lst[i] + k_list[i] for i in range(len(lst))]
        return lst
    
    def get_table_c_anonymity_comparison_3(self,n_range, k_range):
        results = []
        for n in n_range:
            for k in k_range:
                if k >= n:
                    continue
                normal_list = self.recursive_list(n)
                modified_list = self.modified_recursive_list_3(n, k)

                index_c_mod = self.get_index_and_c_2(modified_list)
                if index_c_mod is None:
                    continue
                index_modified = index_c_mod[0]
                c_old = index_c_mod[1]
                c_modified = normal_list[index_modified]

                index_c_norm = self.get_index_and_c_2(normal_list)
                if index_c_norm is None:
                    continue
                c_normal = index_c_norm[1]

                # results.append({'logn': n, 'k': k, 'min_c_in_mod': c_modified, 'c_normal': c_normal})
                results.append({'logn': n, 'k': k, 'c_comparison': [c_old, c_modified, c_normal]})
        return pd.DataFrame(results)
    
    def get_table_sum_before_2(self, c_range, n_range):
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
                # sums=[]
                for k in range(n):
                    # Calculate the sum before the first occurrence of c
                    modified_list = self.modified_recursive_list(n, k)
                    sum_mod = sum(modified_list[:index_normal])
                    # sums.append(sum_mod)
                    results.append({'logn': n, 'c': c, 'k': k, 'sum_before_first_c': sum_mod})
        return pd.DataFrame(results)