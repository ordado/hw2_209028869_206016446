import sys
import data
import districts
import statistics


def main(argv):
    main_data_q1 = data.Data('dpc-covid19-ita-regioni.csv')
    main_data_q2 = data.Data('dpc-covid19-ita-regioni.csv')

    # Q1:
    print("Question 1:")
    data_q1 = districts.Districts(main_data_q1)
    districts_d = ['L', 'S']
    data_q1.filter_districts(districts_d)
    statistics_features = [statistics.mean, statistics.median]
    feature_list = ["hospitalized_with_symptoms", "intensive_care", "total_hospitalized", "home_insulation"]
    data_q1.print_details(feature_list, statistics_features)

    # Q2:
    print("")
    print("Question 2:")
    data_q2 = districts.Districts(main_data_q2)
    data_q2.determine_day_type()
    districts_class = data_q2.get_districts_class()
    num_of_green_districts = 0
    for key in districts_class.keys():
        if districts_class[key] == "yes":
            num_of_green_districts += 1
    number_of_districts = len(districts_class.keys())
    print("Number of districts:", end=" ")
    print(number_of_districts)
    print("Number of not green districts:", end=" ")
    num_of_red_district = number_of_districts - num_of_green_districts
    print(num_of_red_district)
    print("Will a lockdown be forced on whole of Italy?:", end=" ")
    if num_of_red_district > 10:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main(sys.argv)
