import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    results = []

    def do_file_find(suffix, path):
        if os.path.isfile(path) and path.endswith(suffix):
            results.append(path)

        if os.path.isdir(path):
            files_and_dirs = os.listdir(path)
            for item in files_and_dirs:
                new_path = f'{path}/{item}'
                do_file_find(suffix, new_path)

    do_file_find(suffix, path)

    return results

print (find_files(".c", "testdir"))