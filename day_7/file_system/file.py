from file_system.file_element import FileElement


class File(FileElement):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.__size = size

    def get_size(self) -> int:
        """Get the file's size."""
        return self.__size
