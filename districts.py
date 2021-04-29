import data
import statistics


class Districts:
    def __init__(self, dataset: data.Data):
        self.dataset = dataset

    def filter_districts(self, letters):
        list_districts = self.dataset.get_all_districts()
        list_districts_starts_letters = []
        for run_districts in list_districts:
            for run_letter in letters:
                if run_districts[0] == run_letter:
                    flag = 0
                    for run_list_districts_starts_letters in list_districts_starts_letters:
                        if run_districts == run_list_districts_starts_letters:
                            flag = 1
                            break
                    if flag == 0:
                        list_districts_starts_letters.append(run_districts)
        self.dataset.set_districts_data(list_districts_starts_letters)

    def print_details(self, features, statistic_functions):
        l_feature = len(statistic_functions)
        for run_features in features:
            print(f"{run_features}", end=": ")
            temp_list = self.dataset.get_list_of_specific_feature(run_features)
            for index, run_statistic_function in enumerate(statistic_functions):
                if index == l_feature - 1:
                    print(run_statistic_function(temp_list))
                else:
                    print(run_statistic_function(temp_list), end=", ")
