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

    if len(results) is 0:
        results = "No files found with that extension in the provided directory."

    return results

print(find_files(".c", "testdir"))
# Should print ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c'], as
# this all of the files ending in '.c' provided by the example directory.

print(find_files(".h", "testdir"))
# Should print ['testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/t1.h', 'testdir/subdir1/a.h'], as
# this all of the files ending in '.h' provided by the example directory.

print(find_files(".x", "testdir"))
# Should print "No files found with that extension in the provided directory." as no files exist with that extension.
