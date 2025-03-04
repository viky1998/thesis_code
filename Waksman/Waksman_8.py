import pandas as pd
import itertools

class Waksman_8:
    permutation_length = 8
    total_number_of_switches = 17

    initial_permutation = [i for i in range(8)]
    
    def __init__(self):
        self.switch_combinations = self.get_switch_combinations()
        self.permutations = self.get_all_permutations()

    def get_switch_combinations(self):
        switch_combinations = []
        for i in range(2**self.total_number_of_switches):
            switch_combinations.append([bool(int(x)) for x in bin(i)[2:].zfill(self.total_number_of_switches)])
        return switch_combinations
    
    def get_all_permutations(self):
        permutations = itertools.permutations(self.initial_permutation)
        final_permutations = []
        for permutation in permutations:
            final_permutations.append(list(permutation))
        return final_permutations

    
    def evaluate_switches(self, switches_combinations):
        data_dict = {str(permutation): 0 for permutation in self.permutations}

        for switches in switches_combinations:
            permutation = self.apply_switches(self.initial_permutation, switches)
            # when the permutation in the dataframe data is equal to the permutation we just calculated, we increment the frequency
            data_dict[str(permutation)] += 1
        return pd.DataFrame(data_dict.items(), columns=['Permutation', 'Frequency'])


    
    def apply_switches(self, permutation, switches):
        permutation = self.apply_layer_1_switches(permutation, switches[:4])
        permutation = self.apply_layer_2_switches(permutation, switches[4:8])
        permutation = self.apply_layer_3_switches(permutation, switches[8:12])
        permutation = self.apply_layer_4_switches(permutation, switches[12:14])
        permutation = self.apply_layer_5_switches(permutation, switches[14:17])
        return permutation
    
    def apply_layer_1_switches(self, permutation, switches):
        val0 = permutation[0] if not switches[0] else permutation[1]
        val1 = permutation[1] if not switches[0] else permutation[0]
        val2 = permutation[2] if not switches[1] else permutation[3]
        val3 = permutation[3] if not switches[1] else permutation[2]
        val4 = permutation[4] if not switches[2] else permutation[5]
        val5 = permutation[5] if not switches[2] else permutation[4]
        val6 = permutation[6] if not switches[3] else permutation[7]
        val7 = permutation[7] if not switches[3] else permutation[6]

        return [val0, val1, val2, val3, val4, val5, val6, val7]
    
    def apply_layer_2_switches(self, permutation, switches):
        val0 = permutation[0] if not switches[0] else permutation[4]
        val1 = permutation[4] if not switches[0] else permutation[0]
        val2 = permutation[2] if not switches[1] else permutation[6]
        val3 = permutation[6] if not switches[1] else permutation[2]
        val4 = permutation[1] if not switches[2] else permutation[5]
        val5 = permutation[5] if not switches[2] else permutation[1]
        val6 = permutation[3] if not switches[3] else permutation[7]
        val7 = permutation[7] if not switches[3] else permutation[3]

        return [val0, val1, val2, val3, val4, val5, val6, val7]
    
    def apply_layer_3_switches(self, permutation, switches):
        val0 = permutation[0] if not switches[0] else permutation[2]
        val1 = permutation[2] if not switches[0] else permutation[0]
        val2 = permutation[1] if not switches[1] else permutation[3]
        val3 = permutation[3] if not switches[1] else permutation[1]
        val4 = permutation[4] if not switches[2] else permutation[6]
        val5 = permutation[6] if not switches[2] else permutation[4]
        val6 = permutation[5] if not switches[3] else permutation[7]
        val7 = permutation[7] if not switches[3] else permutation[5]

        return [val0, val1, val2, val3, val4, val5, val6, val7]
    
    def apply_layer_4_switches(self, permutation, switches):
        val0 = permutation[0] if not switches[0] else permutation[2]
        val1 = permutation[2] if not switches[0] else permutation[0]
        val2 = permutation[1]
        val3 = permutation[3]
        val4 = permutation[4] if not switches[1] else permutation[6]
        val5 = permutation[6] if not switches[1] else permutation[4]
        val6 = permutation[5]
        val7 = permutation[7]

        return [val0, val1, val2, val3, val4, val5, val6, val7]
    
    def apply_layer_5_switches(self, permutation, switches):
        val0 = permutation[0] if not switches[0] else permutation[4]
        val1 = permutation[4] if not switches[0] else permutation[0]
        val2 = permutation[2] if not switches[1] else permutation[6]
        val3 = permutation[6] if not switches[1] else permutation[2]
        val4 = permutation[1] if not switches[2] else permutation[5]
        val5 = permutation[5] if not switches[2] else permutation[1]
        val6 = permutation[3]
        val7 = permutation[7]

        return [val0, val1, val2, val3, val4, val5, val6, val7]
