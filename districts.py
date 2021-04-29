import data


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

    def determine_day_type(self):
        resigned_healed_i = self.dataset.get_list_of_specific_feature("resigned_healed")
        new_positives_i = self.dataset.get_list_of_specific_feature("new_positives")
        list_type_day = []
        for index, run_resigned_healed in enumerate(resigned_healed_i):
            if (run_resigned_healed - new_positives_i[index]) > 0:
                list_type_day.append(1)
            else:
                list_type_day.append(0)
        self.dataset.add_key_and_values("type_day", list_type_day)

    def get_districts_class(self):
        is_green_districts = {}
        list_type_day = self.dataset.get_list_of_specific_feature("type_day")
        list_districts = self.dataset.get_list_of_specific_feature("denominazione_region")
        for district in self.dataset.get_all_districts():
            counter = 0
            for index, run_list in enumerate(list_type_day):
                if list_districts[index] == district:
                    if list_type_day[index] == 1:
                        counter += 1
            if counter > 340:
                is_green_districts[district] = "yes"
            else:
                is_green_districts[district] = "no"

        return is_green_districts
