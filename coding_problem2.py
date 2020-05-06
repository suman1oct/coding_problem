"""
Problem 2

Write a method to compress all file in a folder with specified extensions and save to output path.
Please write unit test cases using pytest.
Write production level code and project structure


import os
from zipfile import ZipFile

def zip_files(search_directory, selected_extensions, output_path):
	# TODO


if __name__ == '__main__':
    zip_files('.\\my_stuff', ['.jpg','.txt'], 'my_stuff.zip')
"""

import os
from zipfile import ZipFile

def zip_files(search_directory, selected_extensions, output_path):
    zipObj = ZipFile(output_path, 'w')
    # Add multiple files to the zip

    for file_name in os.listdir(search_directory):
        if os.path.splitext(file_name)[1] in selected_extensions:
            zipObj.write(file_name)

    # close the Zip File
    zipObj.close()


if __name__ == '__main__':
    zip_files('/home/suman/Desktop/', ['.jpg','.txt'], 'my_stuff.zip')
