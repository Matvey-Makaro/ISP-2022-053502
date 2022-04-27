import inspect
from types import *

IMPORTANT_FUNCTION_ATTRIBUTES = (
    "__code__",
    "__globals__",
    "__defaults__",
    "__closure__"
)

CODE_ATTRIBUTES = (
    "co_argcount",
    "co_posonlyargcount",
    "co_kwonlyargcount",
    "co_nlocals",
    "co_stacksize",
    "co_flags",
    "co_code",
    "co_consts",
    "co_names",
    "co_varnames",
    "co_filename",
    "co_name",
    "co_firstlineno",
    "co_lnotab",
    "co_freevars",
    "co_cellvars"
)

ITERABLES = (
    'list',
    'tuple',
    'set',
    'dict',
    'frozenset',
    'bytearray',
)

PRIMITIVES = (
    'int',
    'float',
    'complex',
    'bool',
    'str',
    'bytes',
    'NoneType',
)


CODE_FIELD_NAME = "__code__"
GLOBALS_FIELD_NAME = "__globals__"
DEFAULTS_FIELD_NAME = "__defaults__"
CLOSURE_FIELD_NAME = "__closure__"
CODE_NAMES_FIELD_NAME = "co_names"


def iterable_to_dict(iterable: ITERABLES) -> dict:
    return {type(iterable).__name__: [obj_to_intermediate_format(i) for i in iterable]}


def dict_to_dict(dictionary: dict) -> dict:
    result = {}
    for key, value in dictionary.items():
        result[key] = obj_to_intermediate_format(value)
    # return {'dict': result}
    return result


def code_to_dict(code) -> dict:
    result = {}
    for attr in CODE_ATTRIBUTES:
        result[attr] = obj_to_intermediate_format(code.__getattribute__(attr))
    return result


def function_to_dict(function) -> dict:
    result = {}
    for name, value in inspect.getmembers(function):
        if name == DEFAULTS_FIELD_NAME or name == CLOSURE_FIELD_NAME:
            result[name] = obj_to_intermediate_format(value)
            continue
        if name == CODE_FIELD_NAME:
            code = value
            result[CODE_FIELD_NAME] = code_to_dict(code)
            result[GLOBALS_FIELD_NAME] = {}
            glob = function.__getattribute__(GLOBALS_FIELD_NAME)
            for co_name in code.__getattribute__(CODE_NAMES_FIELD_NAME):
                if co_name == function.__name__:
                    result[GLOBALS_FIELD_NAME][co_name] = function.__name__
                    continue
                if co_name in glob:  # and not inspect.ismodule(glob[co_name]) and not inspect.isbuiltin(glob[co_name])
                    result[GLOBALS_FIELD_NAME][co_name] = obj_to_intermediate_format(glob[co_name])
    result = {"function": result}
    return result


def class_to_dict(cls) -> dict:
    result = {"__name__": cls.__name__}
    for attr in dir(cls):
        if attr == "__init__":
            result[attr] = obj_to_intermediate_format(getattr(cls, attr))
        if not attr.startswith("__"):
            result[attr] = obj_to_intermediate_format(getattr(cls, attr))
    return {"class": result}


def module_to_dict(module) -> dict:
    result = {"name": module.__name__}
    return {"module": result}


# dict or int or float or complex or bool or str or bytes or None
# isinstance(obj, (int, float, complex, bool, str, bytes)) or obj is None
# isinstance(obj, (list, tuple))
# Исправить метод iterables_to_dict для всех типов!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def obj_to_intermediate_format(obj) -> dict or PRIMITIVES:
    result = {}
    tp_name = type(obj).__name__
    if tp_name in PRIMITIVES:
        return obj
    if tp_name in ITERABLES:
        return iterable_to_dict(obj)
    if isinstance(obj, dict):
        return dict_to_dict(obj)
    if inspect.isroutine(obj):
        return function_to_dict(obj)
    if inspect.isclass(obj):
        return class_to_dict(obj)
    if inspect.ismodule(obj):
        return module_to_dict(obj)
    else:
        pass


def format_to_tuple(form: list) -> tuple:
    return tuple(intermediate_format_to_obj(i) for i in form)


def format_to_list(form: list) -> list:
    return [intermediate_format_to_obj(i) for i in form]


def format_to_set(form: list) -> set:
    return set([intermediate_format_to_obj(i) for i in form])


def format_to_frozenset(form: list) -> frozenset:
    return frozenset([intermediate_format_to_obj(i) for i in form])


def format_to_bytearray(form: list) -> bytearray:
    return bytearray([intermediate_format_to_obj(i) for i in form])


def format_to_dict(form: dict) -> dict:
    result = {}
    for key, value in form.items():
        result[key] = intermediate_format_to_obj(value)
    return result


def form_to_code(form):
    return CodeType(
        intermediate_format_to_obj(form[CODE_ATTRIBUTES[0]]), intermediate_format_to_obj(form[CODE_ATTRIBUTES[1]]),
        intermediate_format_to_obj(form[CODE_ATTRIBUTES[2]]), intermediate_format_to_obj(form[CODE_ATTRIBUTES[3]]),
        intermediate_format_to_obj(form[CODE_ATTRIBUTES[4]]), intermediate_format_to_obj(form[CODE_ATTRIBUTES[5]]),
        intermediate_format_to_obj(form[CODE_ATTRIBUTES[6]]), intermediate_format_to_obj(form[CODE_ATTRIBUTES[7]]),
        intermediate_format_to_obj(form[CODE_ATTRIBUTES[8]]), intermediate_format_to_obj(form[CODE_ATTRIBUTES[9]]),
        intermediate_format_to_obj(form[CODE_ATTRIBUTES[10]]), intermediate_format_to_obj(form[CODE_ATTRIBUTES[11]]),
        intermediate_format_to_obj(form[CODE_ATTRIBUTES[12]]), intermediate_format_to_obj(form[CODE_ATTRIBUTES[13]]),
        intermediate_format_to_obj(form[CODE_ATTRIBUTES[14]]), intermediate_format_to_obj(form[CODE_ATTRIBUTES[15]]))


def format_to_function(form):
    code = form_to_code(form[CODE_FIELD_NAME])
    glob = intermediate_format_to_obj(form[GLOBALS_FIELD_NAME])
    default = form[DEFAULTS_FIELD_NAME]

    # Добавить сериализацию для closure
    closure = form[CLOSURE_FIELD_NAME]
    return FunctionType(code, glob, None, default, closure)


def format_to_module(form):
    return __import__(form["name"])


def format_to_iterable(form: dict) -> ITERABLES:
    for key, value in form.items():
        if key == ITERABLES[0]:
            return format_to_list(value)
        if key == ITERABLES[1]:
            return format_to_tuple(value)
        if key == ITERABLES[2]:
            return format_to_set(value)
        if key == ITERABLES[3]:
            return format_to_frozenset(value)
        if key == ITERABLES[4]:
            return format_to_bytearray(value)


def intermediate_format_to_obj(form: PRIMITIVES):
    if isinstance(form, dict):
        for key, value in form.items():
            if key in ITERABLES:
                return format_to_iterable(form)
            if key == 'function':
                return format_to_function(value)
            if key == 'module':
                return format_to_module(value)
            else:
                return format_to_dict(form)
    if type(form).__name__ in PRIMITIVES:
        return form
