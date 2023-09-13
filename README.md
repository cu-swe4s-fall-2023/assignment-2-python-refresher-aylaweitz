[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

Running print_fires.py prints the number of fires in United States of America

In my_utils.py,
get_column(file_name, query_column, query_value, result_column=1)
    Return array of result_column values for each row in file_name has query_value in query_column.

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