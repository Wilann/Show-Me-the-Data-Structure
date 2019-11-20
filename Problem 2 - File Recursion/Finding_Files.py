import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files = []
    paths = []

    print('\n', "path:", path)
    print("os.listdir(path):", os.listdir(path))

    # For all files in the current directory
    for file in os.listdir(path):
        file_absolute_path = os.path.abspath(file)

        print("file:", file)

        # If file is a file (not a subdirectory)
        if os.path.isfile(file):

            # If file ends with suffix
            if file.endswith(suffix):
                # Save file name
                files.append(file)

                # Save path
                paths.append(file_absolute_path)

        # If file is a subdirectory (not a file)
        if os.path.isdir(file_absolute_path):

            # TODO: Recursion only going into surface folders
            # Recursion - Go into the subdirectory
            new_files, new_paths = find_files(suffix, file_absolute_path)

            # Append new_paths to paths
            files.extend(new_files)
            paths.extend(new_paths)

    return files, paths


def find_files_ver1(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files = []
    paths = []

    # print("os.path.dirname(path):", os.path.dirname(path))
    # print("os.path.abspath(path)):", os.path.abspath(path))
    # print("os.path.basename(path):", os.path.basename(path))
    # print("os.path.realpath(path):", os.path.realpath(path))
    # splittext = os.path.splitext(path)
    # print("os.path.splitext(path):", splittext)
    # print("os.path.splitext(path)[0]:", splittext[0])
    # print("os.path.splitext(path)[1]:", splittext[1])
    # print("os.path.join(os.path.abspath(path), path):", os.path.join(os.path.abspath(path), path))

    # For all files in the current directory
    print("os.listdir(path):", os.listdir(path))
    for file in os.listdir(path):
        print("file:", file)

        # If file is a file (not a subdirectory)
        if os.path.isfile(file):

            # If file ends with suffix
            if file.endswith(suffix):
                # Save file name
                files.append(file)

                # Save path
                paths.append(os.path.join(os.path.abspath(file), file))

    print("----- files:", files)
    print("----- paths:", paths)

    # For all files in the current directory
    print("os.listdir(path):", os.listdir(path))
    for file in os.listdir(path):
        print("file:", file)

        # If file is a subdirectory (not a file)
        if os.path.isdir(file):
            print("os.path.join(path, file):", os.path.join(path, file), '\n')

            # Recursion - Go into the subdirectory
            new_files_and_paths = find_files(suffix, os.path.join(path, file))

            # Append new_paths to paths
            if not file:
                files.append(new_files_and_paths[0])
                paths.append(new_files_and_paths[1])

    return files, paths


output1 = find_files(".py", ".")
print("-----", output1[0])
print("-----", output1[1])

print('\n\n\n\n\n')

output2 = find_files(".pdf", ".")
print("-----", output2[0])
print("-----", output2[1])

print('\n\n\n\n\n')

output3 = find_files(".c", ".")
print("-----", output3[0])
print("-----", output3[1])
