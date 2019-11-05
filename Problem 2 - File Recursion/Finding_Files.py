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
    paths = []

    # Get files in current directory
    files = os.listdir(".")

    # Check for file names with suffix
    files_with_suffix = []
    for file in files:

        # If file is a file (not a subdirectory)
        if os.path.isfile(file):

            # If file ends with suffix
            if file.endswith(suffix):
                # Append file to files_with_suffix
                files_with_suffix.append(file)

                # Note path
                paths.append(os.path.split(file)[0] + os.path.split(file)[1])

    print(paths)

    # Go into subdirectories
    for file in files:

        # If file is a subdirectory (not a file)
        if os.path.isdir(file):

            # Append folder name to paths
            paths.extend(os.path.dirname(file))

            # Recursion
            for path in paths:
                find_files(suffix, path)

    return paths


find_files(".py", ".")
find_files(".pdf", ".")
find_files(".c", ".")
