import sys
import data


def main(argv):
    main_data = data.Data('dpc-covid19-ita-regioni_sample.csv')
    feature = ["date", "region_code", "denominazione_region", "hospitalized_with_symptoms", "Intensive_care",
               "total_hospitalized", "home_insulation", "new_positives", "resigned_healed"]
    print(main_data.data)
    print(main_data.get_all_districts())
    feature = ["Sardegna"]
    main_data.set_districts_data(feature)
    print(main_data.data)


if __name__ == '__main__':
    main(sys.argv)
