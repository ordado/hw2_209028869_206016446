import sys
import data
import districts
import statistics


def main(argv):
    main_data = data.Data('dpc-covid19-ita-regioni_sample.csv')

    # Q1:
    print("Question 1:")
    data_q1 = districts.Districts(main_data)
    districts_d = ['L', 'S']
    data_q1.filter_districts(districts_d)
    statistics_features = [statistics.mean, statistics.median]
    feature_list = ["hospitalized_with_symptoms", "intensive_care", "total_hospitalized", "home_insulation"]
    data_q1.print_details(feature_list, statistics_features)


if __name__ == '__main__':
    main(sys.argv)
