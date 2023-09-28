import math
import sys

def get_column(file_name, query_column, query_value, result_column=1):
    """Return array of result_column values for each row in file_name has query_value in query_column.

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
        values of result_column from rows that contain query_value in query_column.
    """
    f = open_file(file_name)

    result_array = []
    for l in f:
        line = l.rstrip().split(',')
        
        if line[query_column] == query_value:
            value = line[result_column]
            int_value = convert_to_int(value) # convert value read in to integer
            result_array.append(int_value)

    f.close()

    return result_array

def open_file(file_name):
    """Open the file and return it as a readable object.

    Parameters
    ----------
    file_name: str
        name of file
    
    Returns: <class '_io.TextIOWrapper'>
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
        print('Value given could not be converted to an integer. Try a different column.')
        sys.exit(2)

