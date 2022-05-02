from abc import ABC, abstractmethod


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def dumps(obj) -> str:
        pass

    @staticmethod
    @abstractmethod
    def dump(obj, file: str) -> None:
        pass

    @staticmethod
    @abstractmethod
    def loads(serialized_obj: str):
        pass

    @staticmethod
    @abstractmethod
    def load(file: str):
        pass
