import pandas


class Data:
    def __init__(self, path):
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")
        feature = ["date", "region_code", "denominazione_region", "hospitalized_with_symptoms", "Intensive_care",
                   "total_hospitalized", "home_insulation", "new_positives", "resigned_healed"]
        for run_feature in feature:
            flag = 0
            for keys in self.data.keys():
                if keys != run_feature:
                    continue
                else:
                    flag = 1
            if flag == 0:
                del self.data[keys]

    def get_all_districts(self):
        list_districts = []
        for district in self.data["denominazione_region"]:
            flag = 0
            for run_list_districts in list_districts:
                if district != run_list_districts:
                    continue
                else:
                    flag = 1
            if flag == 0:
                list_districts.append(district)
        return list_districts

    def set_districts_data(self, districts):
        index_need_delete = []
        list_of_data_district = self.data['denominazione_region']

        for index, element in enumerate(list_of_data_district):
            flag = 0
            for run_districts in districts:
                if run_districts == element:
                    flag = 1
            if flag == 0:
                index_need_delete.append(index)

        for index in reversed(index_need_delete):
            for key in self.data.keys():
                self.data[key].pop(index)
