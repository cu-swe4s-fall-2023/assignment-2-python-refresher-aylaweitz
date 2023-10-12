import math
import sys


def get_column(file_name, query_column, query_value, result_column=1):
    """Return array of result_column values for each row
      in file_name has query_value in query_column.

    Parameters
    ----------
    file_name: str
        name of the file to read in

    query_column: int
        the index of the column to check if contains query_value

    query_value: str
        value to check for in query_column

    result_column: int
        index of the column we want values from

    Returns
    -------
    result_array: lst
        values of result_column from rows that contain
          query_value in query_column.
    """
    f = open_file(file_name)

    result_array = []
    for line in f:
        split_line = line.rstrip().split(',')
        if split_line[query_column] == query_value:
            value = split_line[result_column]
            int_value = convert_to_int(value)  # convert to int
            result_array.append(int_value)

    f.close()

    return result_array


def open_file(file_name):
    """Open the file and return it as a readable object.

    Parameters
    ----------
    file_name: str
        name of file

    Returns
    -------
    <class '_io.TextIOWrapper'>
        file that can be read.rup
    """
    try:
        f = open(file_name, 'r')
        return f
    except FileNotFoundError:
        print('Could not find: ' + file_name)
        sys.exit(3)


def convert_to_int(value):
    """Convert given value to an integer.

    Parameters
    ----------
    value: str
        value to convert to integer.

    Returns
    -------
    int_elem: int
        value as a rounded up integer.
    """
    try:
        int_elem = math.ceil(float(value))
        return int_elem

    except ValueError:
        print('Value given could not be converted to an integer.')
        sys.exit(2)


def calc_mean(a_list):
    """Calculate the mean of a list of integers

    Parameters
    ----------
    a_list: list
        list of integers

    Returns
    -------
    mean: float
        mean value of the list provided
    """
    try:
        iter(a_list)
    except TypeError:
        print('Input is not iterable -- cannot calculate mean')
        sys.exit(4)

    # doing this without numpy
    mean = sum(a_list)/len(a_list)
    return mean


def calc_median(a_list):
    """Calculate the median of a list of integers

    Parameters
    ----------
    a_list: lst
        list of integers

    Returns
    -------
    median: float
        median value of the list provided
    """
    try:
        iter(a_list)
    except TypeError:
        print('Input is not iterable -- cannot calculate median')
        sys.exit(4)

    median = a_list[len(a_list)//2]  # will force middle value
    return median


def calc_std(a_list):
    """Calculate the standard deviation of a list of integers

    Parameters
    ----------
    a_list: lst
        list of integers

    Returns
    -------
    std: float
        standard deviation of the list provided
    """
    try:
        iter(a_list)
    except TypeError:
        print('Input is not iterable -- cannot calculate standard deviation')
        sys.exit(4)

    mu = calc_mean(a_list)
    the_sum = 0
    for i in a_list:
        the_sum += (i - mu)**2
    std = (the_sum / len(a_list))**(1/2)
    return std
