"""
The module that allows you to convert objects to the intermediate format(dict or primitives) and back.
Contains a class IntermediateFormatSerializer.
"""
import builtins
import inspect
from types import *
from typing import Any

from serializers.serialization_cfg import (
    CODE_ATTRIBUTES,
    ITERABLES,
    PRIMITIVES,
    CODE_FIELD_NAME,
    GLOBALS_FIELD_NAME,
    DEFAULTS_FIELD_NAME,
    CLOSURE_FIELD_NAME,
    CODE_NAMES_FIELD_NAME,
)


class IntermediateFormatSerializer:
    """
    Class that allows to convert objects to the intermediate format and vice versa.
    Provides two main methods obj_to_intermediate_format and intermediate_format_to_obj.
    """

    @staticmethod
    def obj_to_intermediate_format(obj: Any) -> dict or PRIMITIVES:
        """
        Convert objects to the intermediate format(dict or primitives).
        :param obj: Any
        :return: dict or PRIMITIVES
        """
        result = {}
        tp_name = type(obj).__name__
        if tp_name in PRIMITIVES:
            return obj
        if tp_name in ITERABLES:
            return IntermediateFormatSerializer.iterable_to_dict(obj)
        if isinstance(obj, dict):
            return IntermediateFormatSerializer.dict_to_dict(obj)
        if inspect.isroutine(obj):
            return IntermediateFormatSerializer.function_to_dict(obj)
        if inspect.isclass(obj):
            return IntermediateFormatSerializer.class_to_dict(obj)
        if inspect.ismodule(obj):
            return IntermediateFormatSerializer.module_to_dict(obj)

        return IntermediateFormatSerializer.instance_of_class_to_dict(obj)

    @staticmethod
    def intermediate_format_to_obj(form: dict or PRIMITIVES) -> Any:
        """
        Convert intermediate format to the object.
        :param form: dict or PRIMITIVES
        :return: Any
        """
        if type(form) == dict:
            for key, value in form.items():
                if key in ITERABLES:
                    return IntermediateFormatSerializer.format_to_iterable(form)
                if key == "function":
                    return IntermediateFormatSerializer.format_to_function(value)
                if key == "module":
                    return IntermediateFormatSerializer.format_to_module(value)
                if key == "class":
                    return IntermediateFormatSerializer.format_to_class(value)
                if key == "object":
                    return IntermediateFormatSerializer.format_to_instance_of_class(
                        value
                    )
                else:
                    return IntermediateFormatSerializer.format_to_dict(form)
            else:
                return IntermediateFormatSerializer.format_to_dict(form)
            # Поменять сверху два else, которые делают одно и тоже, и цикл который проходит всего один раз
        if type(form).__name__ in PRIMITIVES:
            return form
        raise ValueError(f"Unknown type in intermediate_format_to_obj {type(form)}")

    @staticmethod
    def iterable_to_dict(iterable: ITERABLES) -> dict:
        """
        Convert ITERABLES(list, tuple, set, frozenset or bytearray to dictionary).
        :param iterable: ITERABLES
        :return: dict
        """
        return {
            type(iterable).__name__: [
                IntermediateFormatSerializer.obj_to_intermediate_format(i)
                for i in iterable
            ]
        }

    @staticmethod
    def dict_to_dict(dictionary: dict) -> dict:
        """
        Convert dictionary to dictionary.
        :param dictionary: dict
        :return: dict
        """
        return {
            key: IntermediateFormatSerializer.obj_to_intermediate_format(value)
            for key, value in dictionary.items()
        }

    @staticmethod
    def code_to_dict(code: CodeType) -> dict:
        """
        Convert code to dicitonary.
        :param code: CodeType
        :return: dict
        """
        result = {}
        for attr in CODE_ATTRIBUTES:
            # result[attr] = obj_to_intermediate_format(code.__getattribute__(attr))
            if attr == "co_code" or attr == "co_lnotab":
                result[attr] = IntermediateFormatSerializer.obj_to_intermediate_format(
                    code.__getattribute__(attr).hex()
                )
            else:
                result[attr] = IntermediateFormatSerializer.obj_to_intermediate_format(
                    code.__getattribute__(attr)
                )
        return result

    @staticmethod
    def function_to_dict(function: FunctionType) -> dict:
        """
        Convert function to dictionary.
        :param function: FunctionType
        :return: dict
        """
        result = {}
        for name, value in inspect.getmembers(function):
            if name == DEFAULTS_FIELD_NAME or name == CLOSURE_FIELD_NAME:
                result[name] = IntermediateFormatSerializer.obj_to_intermediate_format(
                    value
                )
                continue
            if name == CODE_FIELD_NAME:
                code = value
                result[CODE_FIELD_NAME] = IntermediateFormatSerializer.code_to_dict(
                    code
                )
                result[GLOBALS_FIELD_NAME] = {}
                glob = function.__getattribute__(GLOBALS_FIELD_NAME)
                for co_name in code.__getattribute__(CODE_NAMES_FIELD_NAME):
                    if co_name == function.__name__:
                        result[GLOBALS_FIELD_NAME][co_name] = function.__name__
                        continue
                        # and not inspect.ismodule(glob[co_name]) and not inspect.isbuiltin(glob[co_name])
                    if co_name in glob:
                        result[GLOBALS_FIELD_NAME][
                            co_name
                        ] = IntermediateFormatSerializer.obj_to_intermediate_format(
                            glob[co_name]
                        )
        result = {"function": result}
        return result

    @staticmethod
    def class_to_dict(cls: type) -> dict:
        """
        Convert class to dictionary.
        :param cls: type
        :return: dict
        """
        bases = tuple(
            filter(
                lambda base: not getattr(builtins, base.__name__, None)
                and not getattr(builtins, base.__qualname__, None),
                cls.__bases__,
            )
        )
        attrs = {
            key: value
            for key, value in cls.__dict__.items()
            if key != "__dict__" and key != "__weakref__"
        }
        result = {
            "name": cls.__name__,
            "qualname": cls.__qualname__,
            "bases": IntermediateFormatSerializer.obj_to_intermediate_format(bases),
            "attrs": IntermediateFormatSerializer.obj_to_intermediate_format(attrs),
        }
        return {"class": result}

    @staticmethod
    def instance_of_class_to_dict(obj) -> dict:
        """
        Convert instance of class to dictionary.
        :param obj:
        :return: dict
        """
        result = {
            "class": IntermediateFormatSerializer.obj_to_intermediate_format(
                obj.__class__
            ),
            "attrs": IntermediateFormatSerializer.obj_to_intermediate_format(
                obj.__dict__
            ),
        }
        return {"object": result}

    @staticmethod
    def module_to_dict(module: ModuleType) -> dict:
        """
        Convert module to dictionary.
        :param module: ModuleType
        :return: dict
        """
        result = {"name": module.__name__}
        return {"module": result}

    @staticmethod
    def format_to_tuple(form: list) -> tuple:
        """
        Convert intermediate format to tuple.
        :param form: list
        :return: tuple.
        """
        return tuple(
            IntermediateFormatSerializer.intermediate_format_to_obj(i) for i in form
        )

    @staticmethod
    def format_to_list(form: list) -> list:
        """
        Convert intermediate format to list.
        :param form: list
        :return: list
        """
        return [
            IntermediateFormatSerializer.intermediate_format_to_obj(i) for i in form
        ]

    @staticmethod
    def format_to_set(form: list) -> set:
        """
        Convert intermediate format to set.
        :param form: list
        :return: set
        """
        return {
            IntermediateFormatSerializer.intermediate_format_to_obj(i) for i in form
        }

    @staticmethod
    def format_to_frozenset(form: list) -> frozenset:
        """
        Convert intermediate format to
        :param form: list
        :return: frozenset
        """
        return frozenset(
            [IntermediateFormatSerializer.intermediate_format_to_obj(i) for i in form]
        )

    @staticmethod
    def format_to_bytearray(form: list) -> bytearray:
        """
        Convert intermediate format to bytearray.
        :param form: list
        :return: bytearray
        """
        return bytearray(
            [IntermediateFormatSerializer.intermediate_format_to_obj(i) for i in form]
        )

    @staticmethod
    def format_to_iterable(form: dict) -> ITERABLES:
        """
        Convert intermediate format to ITERABLES(list, tuple, set, frozenset or bytearray to dictionary).
        :param form: dict
        :return: ITERABLES
        """
        for key, value in form.items():
            if key == ITERABLES[0]:
                return IntermediateFormatSerializer.format_to_list(value)
            if key == ITERABLES[1]:
                return IntermediateFormatSerializer.format_to_tuple(value)
            if key == ITERABLES[2]:
                return IntermediateFormatSerializer.format_to_set(value)
            if key == ITERABLES[3]:
                return IntermediateFormatSerializer.format_to_frozenset(value)
            if key == ITERABLES[4]:
                return IntermediateFormatSerializer.format_to_bytearray(value)

    @staticmethod
    def format_to_dict(form: dict) -> dict:
        """
        Convert intermediate format to dictionary.
        :param form: dict
        :return: dict
        """
        result = {}
        for key, value in form.items():
            result[key] = IntermediateFormatSerializer.intermediate_format_to_obj(value)
        return result

    @staticmethod
    def form_to_code(form: dict) -> CodeType:
        """
        Convert intermediate format to code.
        :param form: dict
        :return: CodeType
        """
        return CodeType(
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[0]]
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[1]]
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[2]]
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[3]]
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[4]]
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[5]]
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                bytes.fromhex(form[CODE_ATTRIBUTES[6]])
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[7]]
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[8]]
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[9]]
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[10]]
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[11]]
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[12]]
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                bytes.fromhex(form[CODE_ATTRIBUTES[13]])
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[14]]
            ),
            IntermediateFormatSerializer.intermediate_format_to_obj(
                form[CODE_ATTRIBUTES[15]]
            ),
        )

    @staticmethod
    def format_to_function(form: dict) -> FunctionType:
        """
        Convert intermediate format to function.
        :param form: dict
        :return: FunctionType
        """
        code = IntermediateFormatSerializer.form_to_code(form[CODE_FIELD_NAME])
        default = form[DEFAULTS_FIELD_NAME]
        glob = IntermediateFormatSerializer.intermediate_format_to_obj(
            form[GLOBALS_FIELD_NAME]
        )
        for key, value in globals().items():
            glob[key] = value

        # Добавить сериализацию для closure
        closure = form[CLOSURE_FIELD_NAME]
        return FunctionType(code, glob, None, default, closure)

    @staticmethod
    def format_to_module(form: dict) -> ModuleType:
        """
        Convert intermediate format to module.
        :param form: dict
        :return: ModuleType
        """
        return __import__(form["name"])

    @staticmethod
    def format_to_class(cls: dict) -> type:
        """
        Convert intermediate format to class.
        :param cls: dict
        :return: type
        """
        bases = IntermediateFormatSerializer.intermediate_format_to_obj(cls["bases"])
        attrs = IntermediateFormatSerializer.intermediate_format_to_obj(cls["attrs"])

        result = type(cls["name"], bases, attrs)
        result.__qualname__ = cls["qualname"]
        return result

    @staticmethod
    def format_to_instance_of_class(form: dict):
        """
        Convert intermediate format to instance of class.
        :param form: dict
        :return:
        """
        cls = IntermediateFormatSerializer.intermediate_format_to_obj(form["class"])
        attrs = IntermediateFormatSerializer.intermediate_format_to_obj(form["attrs"])
        tmp_init = getattr(cls, "__init__", None)

        def __init__(self):
            pass

        cls.__init__ = __init__
        result = cls()
        cls.__init__ = tmp_init
        result.__class__ = cls
        for key, value in attrs.items():
            setattr(result, key, value)
        return result
