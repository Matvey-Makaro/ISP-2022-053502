import inspect
import builtins
from types import *
import Serializer
import AnotherSerializer
import parser
import time
import pytest

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

    test_obj = Test(44)
    ser_test_obj = Serializer.obj_to_intermediate_format(test_obj)
    print(f"ser_test_obj: {ser_test_obj}")
    deser_test_obj = Serializer.intermediate_format_to_obj(ser_test_obj)
    print(f"deser_test_obj: {deser_test_obj}")
    print(deser_test_obj.get_value())
    deser_test_obj.print_value()
    tmp = parser.serialize_json(ser_test_obj)
    print(f"tmp: {tmp}")
    deser_tmp = parser.deserialize_json(tmp)
    print(f"Deser_tmp: {deser_tmp}")
    deser_tmp = Serializer.intermediate_format_to_obj(deser_tmp)
    print(deser_tmp)
    deser_tmp.print_value()
    print(deser_tmp.get_value())

    # ser_test_obj = Serializer.obj_to_intermediate_format(test_obj)
    # string = str(ser_test_obj)
    # print(string)
    # print(f"Open: {string.count('{')}")
    # print(f"Close: {string.count('}')}")
    # tmp = parser.serialize_json(ser_test_obj)
    # print(tmp)
    # print(f"Open: {tmp.count('{')}")
    # print(f"Close: {tmp.count('}')}")
    # print(f"deser_json: {parser.deserialize_json(tmp)}")


if __name__ == '__main__':
    main()
