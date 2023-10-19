import my_utils
import argparse
import matplotlib.pyplot as plt


def create_fire_hist(file_name='../Agrofood_co2_emission.csv',
                     outfile='../doc/fire_hist.jpg'):
    forest_fires = my_utils.get_column(file_name,
                                       query_column=0,
                                       query_value="United States of America",
                                       result_column=3)
    fig, ax = plt.subplots()
    ax.hist(forest_fires)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)  # noqa
    ax.set_xlabel('Number of Forest Fires in a Year')
    ax.set_ylabel('Frequency')
    ax.set_title('Forest fires in the U.S.')
    plt.savefig(outfile, bbox_inches='tight')


def create_forest_v_savanna_scatter(file_name='../Agrofood_co2_emission.csv',
                                    outfile='../doc/forest_v_savanna.jpg'):
    forest_fires = my_utils.get_column(file_name,
                                       query_column=0,
                                       query_value="United States of America",
                                       result_column=3)  # forest fires

    savanna_fires = my_utils.get_column(file_name,
                                        query_column=0,
                                        query_value="United States of America",
                                        result_column=2)  # savanna fires
    fig, ax = plt.subplots()
    ax.scatter(savanna_fires, forest_fires)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel('Number of Savanna Fires')
    ax.set_ylabel('Number of Forest Fires')
    ax.set_title('Forest fires vs. Savanna Fires in the U.S.')
    plt.savefig(outfile, bbox_inches='tight')


def create_fire_v_year_scatter(file_name='../Agrofood_co2_emission.csv',
                               outfile='../doc/forest_v_year.jpg'):
    forest_fires = my_utils.get_column(file_name,
                                       query_column=0,
                                       query_value="United States of America",
                                       result_column=3)  # forest fires
    years = my_utils.get_column(file_name,
                                query_column=0,
                                query_value="United States of America",
                                result_column=1)  # savanna fires
    fig, ax = plt.subplots()
    ax.scatter(years, forest_fires)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Forest Fires')
    ax.set_title('Number of Forest Fires over the Years in the U.S.')
    plt.savefig(outfile, bbox_inches='tight')


def main():
    create_fire_hist()
    create_forest_v_savanna_scatter()
    create_fire_v_year_scatter()


if __name__ == '__main__':
    main()
