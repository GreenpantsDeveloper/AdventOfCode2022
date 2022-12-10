from typing import List

from file_system.directory import Directory
from file_system.file_element import FileElement


class FileSystem:
    def __init__(self):
        self.root: Directory = Directory(name='/')
        self.__directory_path: List[Directory] = [self.root]
        self.all_dirs: List[Directory] = []

    def __get_current_dir(self) -> Directory:
        """Get the directory that the file system is currently in."""
        return self.__directory_path[-1]

    def cd(self, dir_name: str):
        """Change directory in the file system."""
        if dir_name == "..":
            self.__directory_path.pop()
        else:
            subdir = self.__get_current_dir().get_subdir(dir_name)
            self.__directory_path.append(subdir)

    def add(self, file_element: FileElement):
        """Add a file element to the current directory."""
        self.__get_current_dir().add(file_element)

        # Helper for tracking all directories.
        if isinstance(file_element, Directory):
            self.all_dirs.append(file_element)

    def compute_size(self) -> int:
        """Compute the size of all subdirectories."""
        return self.root.get_size()
