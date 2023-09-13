def get_column(file_name, query_column, query_value, result_column):
    """Return array of reult_column values for each row in file_name has query_value in query_column.

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
    result_array = []

    f = open(file_name, 'r')
    for l in f:
        line = l.rstrip().split(',')
        
        if line[query_column] == query_value:
            result_array.append(line[result_column])

    f.close()

    return result_array
