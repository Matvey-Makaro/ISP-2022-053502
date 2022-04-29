import inspect
import builtins
from types import *
import Serializer
import parser

import math

c = 42


def f(x):
    a = 123
    return math.sin(x * a * c)


class Sup:
    pass


class Test():
    static_value = 3

    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)


def main() -> None:
    global a
    a = 3
    dict = {1: "one", 2: "Two"}
    t = (1, 5, 7, 10)
    l = [1, 2, t, dict, 5]
    dict = {"1": t, "2": l, "3": 3}
    # print(f"Function {f(1)}")
    # tmp = Serializer.obj_to_intermediate_format(f)
    # print(tmp)
    # result = eval(str(tmp))
    # print(result)
    # new_func = Serializer.intermediate_format_to_obj(result)
    # print(f"Function {new_func(1)}")

    print(f"Print_value: {Test.print_value.__globals__}")
    test_class = Test(15)
    test_class.print_value()
    dict_test_class = Serializer.obj_to_intermediate_format(Test)
    deser_test_class = Serializer.intermediate_format_to_obj(dict_test_class)
    print(deser_test_class)
    deser_test_obj = deser_test_class(231)
    # deser_test_obj.print_value()
    print(test_class)
    print(deser_test_obj)





if __name__ == '__main__':
    main()
