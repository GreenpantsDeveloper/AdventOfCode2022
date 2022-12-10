from abc import ABC, abstractmethod


class FileElement(ABC):
    """Abstract model of an element in the file system."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the element and all of its contents."""
        raise NotImplementedError
