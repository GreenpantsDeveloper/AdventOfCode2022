from typing import List, Optional, Dict

from file_system.file import File
from file_system.file_element import FileElement


class Directory(FileElement):
    def __init__(self, name):
        super().__init__(name)
        self.__size = None
        self.contents: Dict[str, FileElement] = {}

    def get_size(self) -> int:
        """Get the directory's size; compute if necessary."""
        if not self.__size:
            self.__size = sum([element.get_size() for element in self.contents.values()])

        return self.__size

    def add(self, file_element: FileElement):
        self.contents[file_element.name] = file_element

    def get_subdir(self, dir_name: str) -> Optional['Directory']:
        """Get the specified subdirectory."""
        subdir = self.contents[dir_name]
        return subdir if isinstance(subdir, Directory) else None

