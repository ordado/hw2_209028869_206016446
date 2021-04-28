import data


class Districts:
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        list_districts = self.dataset.get_all_districts
        list_index_need_delete=[]
        for index, run_list in enumerate(list_districts):
            flag=0
            for run_letters in letters:
                if run_list[0]==run_letters:
                    flag=1
            if flag==0:
                list_index_need_delete.append(index)

        for index in reversed(list_index_need_delete):
            for key in self.dataset.keys():
                self.dataset[key].pop(index)
