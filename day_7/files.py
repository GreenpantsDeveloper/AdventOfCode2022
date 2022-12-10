from typing import List

from file_system.directory import Directory
from file_system.file import File
from file_system.file_system import FileSystem

DIR_SIZE_CONSIDERED_SMALL = 100000
MAXIMUM_DISK_SPACE = 70000000
DISK_SPACE_NEEDED = 30000000


def read_files(filename="input.txt") -> FileSystem:
    file_system = FileSystem()  # filesystem-as-a-dict (faad)

    with open(filename, 'r') as fp:
        for line in [line.strip() for line in fp.readlines()[1:]]:  # Skip initial cd into '/'
            if not line or line.startswith("$ ls"):
                # Do nothing for irrelevant lines.
                continue

            if line.startswith("$ cd"):
                # Change directory.
                dir_name = line.split("$ cd ")[1]
                file_system.cd(dir_name)

            elif line.startswith("dir"):
                # Add a new directory to the file system.
                new_dir = Directory(name=line.split(' ')[1])
                file_system.add(new_dir)

            else:
                # Add a new file to the file system.
                file_size, file_name = line.split(' ')
                new_file = File(name=file_name, size=int(file_size))
                file_system.add(new_file)

    return file_system


if __name__ == '__main__':
    file_system = read_files()
    file_system_size = file_system.compute_size()
    print(f"The full file system size is: {file_system_size}")

    # Solve challenge #1.
    sum_small_dir_sizes = 0
    dir_sizes: List[int] = [d.get_size() for d in file_system.all_dirs]
    for dir_size in dir_sizes:
        if dir_size <= DIR_SIZE_CONSIDERED_SMALL:
            sum_small_dir_sizes += dir_size

    print(f"The sum of directory sizes that are at most 100000 is: {sum_small_dir_sizes}.")

    # Solve challenge #2.
    for dir_size in sorted(dir_sizes):
        if MAXIMUM_DISK_SPACE - file_system_size + dir_size >= DISK_SPACE_NEEDED:
            print(f"Directory with size {dir_size} can be deleted to leave just enough space!")
            break
