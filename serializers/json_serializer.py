"""
The module that allows you to convert objects to the json format(return string or write to file) and back.
Contains a class JsonSerializer.
"""
from typing import Any

from json_converter.json_converter import JsonConverter
from serializers.intermediate_format_serializer import IntermediateFormatSerializer
from serializers.serializer import Serializer


class JsonSerializer(Serializer):
    """
    Class that allows to convert objects to json format and vice versa.
    Provides four main methods: dumps, dump, loads, load.
    """

    @staticmethod
    def dumps(obj: Any) -> str:
        """
        Convert object to json format string.
        :param obj: Any
        :return: str
        """
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        return JsonConverter.to_json(form)

    @staticmethod
    def dump(obj: Any, file_name: str) -> None:
        """
        Conver object to json format and write result to file with name "file_name".
        :param obj: Any
        :param file_name: str
        :return: None
        """
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        with open(file_name, "w") as f:
            f.write(JsonConverter.to_json(form))

    @staticmethod
    def loads(serialized_obj: str) -> Any:
        """
        Convert json format string to object.
        :param serialized_obj: str
        :return: Any
        """
        form = JsonConverter.from_json(serialized_obj)
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)

    @staticmethod
    def load(file_name: str) -> Any:
        """
        Read json format string from file with name "file name". Convert this string to object.
        :param file_name: str
        :return: Any
        """
        with open(file_name, "r") as f:
            form = JsonConverter.from_json(f.readline())
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)
