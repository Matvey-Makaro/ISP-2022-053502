"""
The module that provides an absract class Serializer.
"""
from abc import ABC, abstractmethod
from typing import Any


class Serializer(ABC):
    """
    Abstract class which provides interface for other serializers.
    """
    @staticmethod
    @abstractmethod
    def dumps(obj: Any) -> str:
        """Convert object to string of some format."""
        pass

    @staticmethod
    @abstractmethod
    def dump(obj: Any, file_name: str) -> None:
        """Convert object to string of some format and write this string to file with name "file_name". """""
        pass

    @staticmethod
    @abstractmethod
    def loads(serialized_obj: str) -> Any:
        """Convert string of some format to object."""
        pass

    @staticmethod
    @abstractmethod
    def load(file_name: str) -> Any:
        """Read string of some format from file with name "file_name" and convert this string to object."""
        pass
