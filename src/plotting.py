import my_utils
import argparse
import matplotlib.pyplot as plt

saving_path = '../doc/'


def create_fire_hist(file_name='../Agrofood_co2_emission.csv',
                     outfile='fire_hist.jpg'):
    forest_fires = my_utils.get_column(file_name,
                                       query_column=0,
                                       query_value="United States of America",
                                       result_column=3)
    savanna_fires = my_utils.get_column(file_name,
                                        query_column=0,
                                        query_value="United States of America",
                                        result_column=2)  # savanna fires
    fig, ax = plt.subplots()
    ax.hist(forest_fires, label=f'Mean = {my_utils.calc_mean(forest_fires)}')
    ax.hist(savanna_fires, label=f'Mean = {my_utils.calc_mean(savanna_fires)}')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)  # noqa
    ax.set_xlabel('Number of Fires in a Year')
    ax.set_ylabel('Frequency')
    ax.set_title('Fires in the U.S.')
    plt.legend()
    plt.savefig(saving_path+outfile, bbox_inches='tight')


def create_forest_v_savanna_scatter(file_name='../Agrofood_co2_emission.csv',
                                    outfile='forest_v_savanna.jpg'):
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
    plt.savefig(saving_path+outfile, bbox_inches='tight')


def create_fire_v_year_scatter(file_name='../Agrofood_co2_emission.csv',
                               outfile='forest_v_year.jpg'):
    forest_fires = my_utils.get_column(file_name,
                                       query_column=0,
                                       query_value="United States of America",
                                       result_column=3)  # forest fires
    savanna_fires = my_utils.get_column(file_name,
                                        query_column=0,
                                        query_value="United States of America",
                                        result_column=2)  # savanna fires
    years = my_utils.get_column(file_name,
                                query_column=0,
                                query_value="United States of America",
                                result_column=1)  # savanna fires
    fig, ax = plt.subplots()
    ax.scatter(years, forest_fires, label='Forest')
    ax.scatter(years, savanna_fires, label='Savanna')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Forest Fires')
    ax.set_title('Number of Forest Fires over the Years in the U.S.')
    plt.legend()
    plt.savefig(saving_path+outfile, bbox_inches='tight')


def main():
    create_fire_hist()
    create_forest_v_savanna_scatter()
    create_fire_v_year_scatter()


if __name__ == '__main__':
    main()
