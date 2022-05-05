"""
The module that allows you to convert objects to the toml format(return string or write to file) and back.
Contains a class TomlSerializer.
"""
from typing import Any

import tomli
import tomli_w

from serializers.intermediate_format_serializer import IntermediateFormatSerializer
from serializers.serializer import Serializer


class TomlSerializer(Serializer):
    """
    Class that allows to convert objects to toml format and vice versa.
    Provides four main methods: dumps, dump, loads, load.
    """

    @staticmethod
    def dumps(obj: Any) -> str:
        """
        Convert object to toml format string.
        :param obj: Any
        :return: str
        """
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        form = TomlSerializer._prepare_to_serialize(form)
        return tomli_w.dumps(form)

    @staticmethod
    def dump(obj: Any, file_name: str) -> None:
        """
        Conver object to toml format and write result to file with name "file_name".
        :param obj: Any
        :param file_name: str
        :return: None
        """
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        form = TomlSerializer._prepare_to_serialize(form)
        with open(file_name, 'w') as f:
            f.write(tomli_w.dumps(form))

    @staticmethod
    def loads(serialized_obj: str) -> Any:
        """
        Convert toml format string to object.
        :param serialized_obj: str
        :return: Any
        """
        form = tomli.loads(serialized_obj)
        form = TomlSerializer._prepare_to_deserialize(form)
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)

    @staticmethod
    def load(file_name: str) -> Any:
        """
        Read toml format string from file with name "file name". Convert this string to object.
        :param file_name: str
        :return: Any
        """
        ser_obj = ""
        with open(file_name, "r") as f:
            for line in f:
                ser_obj += line
        form = tomli.loads(ser_obj)
        form = TomlSerializer._prepare_to_deserialize(form)
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)

    @staticmethod
    def _prepare_to_serialize(obj: dict) -> dict:
        """
        Prepares an intermediate format for serialization in toml format
        Replace Null to string "__null__".
        :param obj: dict
        :return: dict
        """
        for key, value in obj.items():
            if type(value) == dict:
                TomlSerializer._prepare_to_serialize(value)
            elif type(value) == list:
                for i in range(len(value)):
                    if value[i] is None:
                        obj[key][i] = "__none__"
            elif value is None:
                obj[key] = "__none__"
        return obj

    @staticmethod
    def _prepare_to_deserialize(obj: dict) -> dict:
        """
        Replace string "__null__" to Null.
        :param obj: dict
        :return: dict
        """
        for key, value in obj.items():
            if type(value) == dict:
                obj[key] = TomlSerializer._prepare_to_deserialize(value)
            elif type(value) == list:
                for i in range(len(value)):
                    if value[i] == "__none__":
                        obj[key][i] = None
            elif value == "__none__":
                obj[key] = None
        return obj
