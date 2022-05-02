import builtins
import inspect
from types import *
from serialization_cfg import CODE_ATTRIBUTES, ITERABLES, PRIMITIVES, CODE_FIELD_NAME, GLOBALS_FIELD_NAME, \
    DEFAULTS_FIELD_NAME, CLOSURE_FIELD_NAME, CODE_NAMES_FIELD_NAME


class IntermediateFormatSerializer:
    @staticmethod
    def obj_to_intermediate_format(obj) -> dict or PRIMITIVES:
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
    def intermediate_format_to_obj(form: dict or PRIMITIVES):
        if type(form) == dict:
            for key, value in form.items():
                if key in ITERABLES:
                    return IntermediateFormatSerializer.format_to_iterable(form)
                if key == 'function':
                    return IntermediateFormatSerializer.format_to_function(value)
                if key == 'module':
                    return IntermediateFormatSerializer.format_to_module(value)
                if key == 'class':
                    return IntermediateFormatSerializer.format_to_class(value)
                if key == 'object':
                    return IntermediateFormatSerializer.format_to_instance_of_class(value)
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
        return {type(iterable).__name__: [IntermediateFormatSerializer.obj_to_intermediate_format(i) for i in iterable]}

    @staticmethod
    def dict_to_dict(dictionary: dict) -> dict:
        return {key: IntermediateFormatSerializer.obj_to_intermediate_format(value) for
                key, value in dictionary.items()}

    @staticmethod
    def code_to_dict(code) -> dict:
        result = {}
        for attr in CODE_ATTRIBUTES:
            # result[attr] = obj_to_intermediate_format(code.__getattribute__(attr))
            if attr == "co_code" or attr == 'co_lnotab':
                result[attr] = IntermediateFormatSerializer.obj_to_intermediate_format(
                    code.__getattribute__(attr).hex())
            else:
                result[attr] = IntermediateFormatSerializer.obj_to_intermediate_format(code.__getattribute__(attr))
        return result

    @staticmethod
    def function_to_dict(function) -> dict:
        result = {}
        for name, value in inspect.getmembers(function):
            if name == DEFAULTS_FIELD_NAME or name == CLOSURE_FIELD_NAME:
                result[name] = IntermediateFormatSerializer.obj_to_intermediate_format(value)
                continue
            if name == CODE_FIELD_NAME:
                code = value
                result[CODE_FIELD_NAME] = IntermediateFormatSerializer.code_to_dict(code)
                result[GLOBALS_FIELD_NAME] = {}
                glob = function.__getattribute__(GLOBALS_FIELD_NAME)
                for co_name in code.__getattribute__(CODE_NAMES_FIELD_NAME):
                    if co_name == function.__name__:
                        result[GLOBALS_FIELD_NAME][co_name] = function.__name__
                        continue
                        # and not inspect.ismodule(glob[co_name]) and not inspect.isbuiltin(glob[co_name])
                    if co_name in glob:
                        result[GLOBALS_FIELD_NAME][co_name] = \
                            IntermediateFormatSerializer.obj_to_intermediate_format(glob[co_name])
        result = {"function": result}
        return result

    @staticmethod
    def class_to_dict(cls) -> dict:
        bases = tuple(filter(
            lambda base: not getattr(builtins, base.__name__, None) and not getattr(builtins, base.__qualname__, None),
            cls.__bases__))
        attrs = {key: value for key, value in cls.__dict__.items() if key != "__dict__" and key != "__weakref__"}
        result = {"name": cls.__name__, "qualname": cls.__qualname__,
                  "bases": IntermediateFormatSerializer.obj_to_intermediate_format(bases),
                  "attrs": IntermediateFormatSerializer.obj_to_intermediate_format(attrs)}
        return {"class": result}

    @staticmethod
    def instance_of_class_to_dict(obj) -> dict:
        result = {"class": IntermediateFormatSerializer.obj_to_intermediate_format(obj.__class__),
                  "attrs": IntermediateFormatSerializer.obj_to_intermediate_format(obj.__dict__)}
        return {"object": result}

    @staticmethod
    def module_to_dict(module) -> dict:
        result = {"name": module.__name__}
        return {"module": result}

    @staticmethod
    def format_to_tuple(form: list) -> tuple:
        return tuple(IntermediateFormatSerializer.intermediate_format_to_obj(i) for i in form)

    @staticmethod
    def format_to_list(form: list) -> list:
        return [IntermediateFormatSerializer.intermediate_format_to_obj(i) for i in form]

    @staticmethod
    def format_to_set(form: list) -> set:
        return {IntermediateFormatSerializer.intermediate_format_to_obj(i) for i in form}

    @staticmethod
    def format_to_frozenset(form: list) -> frozenset:
        return frozenset([IntermediateFormatSerializer.intermediate_format_to_obj(i) for i in form])

    @staticmethod
    def format_to_bytearray(form: list) -> bytearray:
        return bytearray([IntermediateFormatSerializer.intermediate_format_to_obj(i) for i in form])

    @staticmethod
    def format_to_iterable(form: dict) -> ITERABLES:
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
        result = {}
        for key, value in form.items():
            result[key] = IntermediateFormatSerializer.intermediate_format_to_obj(value)
        return result

    @staticmethod
    def form_to_code(form):
        return CodeType(
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[0]]),
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[1]]),
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[2]]),
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[3]]),
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[4]]),
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[5]]),
            IntermediateFormatSerializer.intermediate_format_to_obj(bytes.fromhex(form[CODE_ATTRIBUTES[6]])),
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[7]]),
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[8]]),
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[9]]),
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[10]]),
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[11]]),
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[12]]),
            IntermediateFormatSerializer.intermediate_format_to_obj(bytes.fromhex(form[CODE_ATTRIBUTES[13]])),
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[14]]),
            IntermediateFormatSerializer.intermediate_format_to_obj(form[CODE_ATTRIBUTES[15]]))

    @staticmethod
    def format_to_function(form):
        code = IntermediateFormatSerializer.form_to_code(form[CODE_FIELD_NAME])
        default = form[DEFAULTS_FIELD_NAME]
        glob = IntermediateFormatSerializer.intermediate_format_to_obj(form[GLOBALS_FIELD_NAME])
        for key, value in globals().items():
            glob[key] = value

        # Добавить сериализацию для closure
        closure = form[CLOSURE_FIELD_NAME]
        return FunctionType(code, glob, None, default, closure)

    @staticmethod
    def format_to_module(form):
        return __import__(form["name"])

    @staticmethod
    def format_to_class(cls: dict):
        bases = IntermediateFormatSerializer.intermediate_format_to_obj(cls["bases"])
        attrs = IntermediateFormatSerializer.intermediate_format_to_obj(cls["attrs"])

        result = type(cls["name"], bases, attrs)
        result.__qualname__ = cls["qualname"]
        return result

    @staticmethod
    def format_to_instance_of_class(form: dict):
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
