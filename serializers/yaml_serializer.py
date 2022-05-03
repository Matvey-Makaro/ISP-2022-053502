"""
The module that allows you to convert objects to the yaml format(return string or write to file) and back.
Contains a class YamlSerializer.
"""
from typing import Any

from serializers.serializer import Serializer
from serializers.intermediate_format_serializer import IntermediateFormatSerializer
import yaml


class YamlSerializer(Serializer):
    """
    Class that allows to convert objects to yaml format and vice versa.
    Provides four main methods: dumps, dump, loads, load.
    """
    @staticmethod
    def dumps(obj: Any) -> str:
        """
        Convert object to yaml format string.
        :param obj: Any
        :return: str
        """
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        return yaml.dump(form)

    @staticmethod
    def dump(obj: Any, file_name: str) -> None:
        """
        Conver object to yaml format and write result to file with name "file_name".
        :param obj: Any
        :param file_name: str
        :return: None
        """
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        with open(file_name, 'w') as f:
            f.write(yaml.dump(form))

    @staticmethod
    def loads(serialized_obj: str) -> Any:
        """
        Convert yaml format string to object.
        :param serialized_obj: str
        :return: Any
        """
        form = yaml.load(serialized_obj, Loader=yaml.Loader)
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)

    @staticmethod
    def load(file_name: str) -> Any:
        """
        Read yaml format string from file with name "file name". Convert this string to object.
        :param file_name: str
        :return: Any
        """
        ser_obj = ""
        with open(file_name, "r") as f:
            for line in f:
                ser_obj += line
            form = yaml.load(ser_obj, Loader=yaml.Loader)
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)
