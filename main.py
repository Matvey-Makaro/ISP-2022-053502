import inspect
import builtins
from types import *
import Serializer
import AnotherSerializer
import json_converter
import time
import pytest
import json

from intermediate_format_serializer import IntermediateFormatSerializer
from json_serializer import JsonSerializer

import math

# from math import sin

c = 42


def f(x):
    a = 123
    print(a)
    return math.sin(x * a * c)


def gen():
    for i in range(10):
        yield i ** 2


class Sup:
    pass


class Test():
    static_value = 3

    def __init__(self, value):
        self.value = value
        self.test_value = 10

    def get_value(self):
        return self.value + 1

    def print_value(self):
        print(self.value)


def main() -> None:
    global a
    a = 3
    dict = {1: "one", 2: "Two"}
    t = (1, 5, 7, 10)
    l = [1, 2, t, dict, 5]
    dict = {"1": t, "2": l, "3": 3}
    # result = eval(str(tmp))
    # print(result)
    # new_func = Serializer.intermediate_format_to_obj(result)
    # print(f"Function {new_func(1)}")

    # tmp = Serializer.obj_to_intermediate_format(f)
    # deser_tmp = Serializer.intermediate_format_to_obj(tmp)
    # print(f(1))
    # print(deser_tmp(1))
    # print(f"Print_value: {Test.get_value.__dict__}")
    # test_class = Test(15)

    # ser_test_class = Serializer.obj_to_intermediate_format(Test)
    # deser_test_class = Serializer.intermediate_format_to_obj(ser_test_class)
    # tmp = deser_test_class(31)
    # tmp.print_value()

    # print(f(1))
    # ser_func = Serializer.obj_to_intermediate_format(f)
    # json_func = parser.serialize_json(ser_func)
    # print(ser_func)
    # print(json_func)
    # deser_json_fun = parser.deserialize_json(json_func)
    # print(f"Deser func: {deser_json_fun}")
    # new_func = Serializer.intermediate_format_to_obj(deser_json_fun)
    # print(new_func)
    # print(new_func(1))

    # test_obj = Test(44)
    # ser_test_obj = Serializer.obj_to_intermediate_format(test_obj)
    # print(f"ser_test_obj: {ser_test_obj}")
    # deser_test_obj = Serializer.intermediate_format_to_obj(ser_test_obj)
    # print(f"deser_test_obj: {deser_test_obj}")
    # print(deser_test_obj.get_value())
    # deser_test_obj.print_value()
    # tmp = parser.serialize_json(ser_test_obj)
    # print(f"tmp: {tmp}")
    # deser_tmp = parser.deserialize_json(tmp)
    # print(f"Deser_tmp: {deser_tmp}")
    # deser_tmp = Serializer.intermediate_format_to_obj(deser_tmp)
    # print(deser_tmp)
    # deser_tmp.print_value()
    # print(deser_tmp.get_value())
    # with open("file.txt", 'w') as file:
    #     json.dump(l, file)
    # print(Serializer.obj_to_intermediate_format(t))
    # tmp = json.dumps(dict)
    # print(tmp)
    # print(Serializer.obj_to_intermediate_format(dict))
    # print(type(json.loads(tmp)))
    # ser_test_obj = Serializer.obj_to_intermediate_format(test_obj)
    # print(json.dumps(ser_test_obj))

    # serializer = JsonSerializer()
    # ser_func = serializer.dumps(f)
    # desr_func = serializer.loads(ser_func)
    # print(desr_func)
    # print(desr_func(5))
    # serializer.dump(f, "file.txt")
    # new_func = serializer.load("file.txt")
    # print(new_func)
    # print(new_func(5))

    print("List")
    l = [1, 2, "Hello", 'world', 3.14, {'set1', 'set2'}, ('tuple1', 2), {'item1': 1}]
    print(l)
    intermediate_l = IntermediateFormatSerializer.iterable_to_dict(l)
    print(intermediate_l)
    deser_l = IntermediateFormatSerializer.intermediate_format_to_obj(intermediate_l)
    print(deser_l)
    print(l == deser_l)

    print("\nTuple")
    tpl = (1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {"item1": 1}, ["list", 3.14, 10, 12])
    print(tpl)
    intermediate_tpl = IntermediateFormatSerializer.iterable_to_dict(tpl)
    print(intermediate_tpl)
    deser_tpl = IntermediateFormatSerializer.intermediate_format_to_obj(intermediate_tpl)
    print(deser_tpl)
    print(tpl == deser_tpl)

    print("\nBytearray")
    b_arr = bytearray(b'hello world!')
    print(b_arr)
    intermediate_b_arr = IntermediateFormatSerializer.iterable_to_dict(b_arr)
    print(intermediate_b_arr)
    deser_b_arr = IntermediateFormatSerializer.intermediate_format_to_obj(intermediate_b_arr)
    print(deser_b_arr)
    print(b_arr == deser_b_arr)

    print("\nDictionary")
    dct = {"lst": [1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {'item1': 1}],
           "tpl": (1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {"item1": 1}, ["list", 3.14, 10, 12]),
           "one": 1}
    print(dct)
    intermediate_dct = IntermediateFormatSerializer.dict_to_dict(dct)
    print(intermediate_dct)
    deser_dct = IntermediateFormatSerializer.intermediate_format_to_obj(intermediate_dct)
    print(deser_dct)
    print(dct == deser_dct)

    print("\nCode")
    code = f.__code__
    print(code)
    intermediate_code = IntermediateFormatSerializer.code_to_dict(code)
    print(intermediate_code)
    deser_code = IntermediateFormatSerializer.form_to_code(intermediate_code)
    print(deser_code)
    print(deser_code == code)

    print("\nFunction")
    func = f
    print(func)
    intermediate_func = IntermediateFormatSerializer.function_to_dict(func)
    print(intermediate_func)
    deser_func = IntermediateFormatSerializer.intermediate_format_to_obj(intermediate_func)
    print(deser_func)
    print(func == deser_func)

    print("\nModule")
    module = __import__("math")
    print(module)
    intermediate_module = IntermediateFormatSerializer.module_to_dict(module)
    print(intermediate_module)
    deser_module = IntermediateFormatSerializer.intermediate_format_to_obj(intermediate_module)
    print(deser_module)
    print(module == deser_module)
    print(inspect.getmembers(func))


if __name__ == '__main__':
    main()
