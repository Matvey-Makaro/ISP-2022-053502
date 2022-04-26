import inspect
from types import *

IMPORTANT_FUNCTION_ATTRIBUTES = [
    "__code__",
    "__globals__",
    "__defaults__",
    "__closure__"
]

CODE_ATTRIBUTES = [
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
]

CODE_FIELD_NAME = "__code__"
GLOBALS_FIELD_NAME = "__globals__"
DEFAULTS_FIELD_NAME = "__defaults__"
CLOSURE_FIELD_NAME = "__closure__"
CODE_NAMES_FIELD_NAME = "co_names"


def sequence_to_dict(sequence: list or tuple) -> dict:
    result_list = []
    for s in sequence:
        result_list.append(obj_to_intermediate_format(s))
    if isinstance(sequence, list):
        return {'list': result_list}
    if isinstance(sequence, tuple):
        return {'tuple': result_list}
    raise ValueError("Value error in sequence_to_dict")


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
                    print(f"Debug: {glob[co_name]}")
                    result[GLOBALS_FIELD_NAME][co_name] = obj_to_intermediate_format(glob[co_name])
    result = {"function": result}
    return result


def class_to_dict(cls) -> dict:
    pass


def obj_to_intermediate_format(obj) -> dict or int or float or complex or bool or str or bytes or None:
    result = {}
    if isinstance(obj, (int, float, complex, bool, str, bytes)) or obj is None:
        return obj
    if isinstance(obj, (list, tuple)):
        return sequence_to_dict(obj)
    if isinstance(obj, dict):
        return dict_to_dict(obj)
    if inspect.isfunction(obj) or inspect.ismethod(obj):
        return function_to_dict(obj)
    if inspect.isclass(obj):
        pass
    # if inspect.ismodule(obj):
    #     return obj
    else:
        pass


def format_to_tuple(form: tuple) -> tuple:
    result = []
    for element in form:
        result.append(intermediate_format_to_obj(element))
    return tuple(result)


def format_to_list(form: list) -> list:
    result = []
    for element in form:
        result.append(intermediate_format_to_obj(element))
    return result


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
    for key, value in form.items():
        if key == CODE_FIELD_NAME:
            code = form_to_code(value)
        elif key == GLOBALS_FIELD_NAME:
            glob = value
        elif key == DEFAULTS_FIELD_NAME:
            default = value
        elif key == CLOSURE_FIELD_NAME:
            closure = value
        else:
            raise ValueError("Incorrect key value in function format")
    return FunctionType(code, glob, None, default, closure)


def intermediate_format_to_obj(form: dict or int or float or complex or bool or str or bytes or None):
    if isinstance(form, dict):
        for key, value in form.items():
            if key == 'tuple':
                return format_to_tuple(value)
            if key == 'list':
                return format_to_list(value)
            if key == 'function':
                return format_to_function(value)
            else:
                return format_to_dict(form)

    if isinstance(form, (int, float, complex, bool, str, bytes)):
        return form


