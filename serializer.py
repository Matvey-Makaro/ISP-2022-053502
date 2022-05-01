from abc import ABC, abstractmethod


class Serializer(ABC):
    @abstractmethod
    def dumps(self, obj) -> str:
        pass

    @abstractmethod
    def dump(self, obj, file: str) -> None:
        pass

    @abstractmethod
    def loads(self, serialized_obj: str):
        pass

    @abstractmethod
    def load(self, file: str):
        pass
