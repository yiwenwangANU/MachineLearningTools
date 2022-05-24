import zipfile


def unzip_data(filename):
    """
    Unzip filename into the current directory

    :param filename: a file path to a target file that need to be unzipped
    :return: None
    """
    zip_ref = zipfile.ZipFile(filename, "r")
    zip_ref.extractall()
    zip_ref.close()


import os


def walk_through_dir(dir_path):
    """
    Walk though the dir_path and returns its sub-dirs and files

    :param dir_path: a directory path that need to be walk through
    :return: None
    """
    for dirpath, dirnames, filenames in os.walk(dir_path):
        print(f"Current directory: {dirpath}, number of sub-directories: {len(dirnames)}, "
              f"number of files: {len(filenames)}")
