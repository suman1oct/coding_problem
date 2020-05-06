"""
Problem 1

Write method to merge 2 csv files with different column header and write the output to another csv with headers from all the csv's files.


import csv

def csv_merge(list_of_csv_file, output_path):
    # build list with all fieldnames
	# TODO

    # write data to output file based on field names
    # TODO

if __name__ == '__main__':
    csv_merge(['class1.csv', 'class2.csv'], 'all_students.csv')

"""

# third-party imports
import pandas as pd

def csv_merge(list_of_csv_file, output_path):
    # build list with all fieldnames
    df_list = []
    for file_name in list_of_csv_file:
        df_list.append(pd.read_csv(file_name))
        # Concatenate all data into one DataFrame
    output_df = pd.concat(df_list, ignore_index=True)

    # write data to output file based on field names
    output_df.to_csv(output_path, index=False)


if __name__ == '__main__':
    csv_merge(['class1.csv', 'class2.csv'], 'all_students.csv')
