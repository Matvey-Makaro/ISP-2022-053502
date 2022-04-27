import inspect
import math
from types import *
import Serializer
import parser

import math
c = 42


def f(x):
    a = 123
    return math.sin(x * a * c)


class Test:
    def __init__(self, value):
        self.value = value
    staticValue = 3


def main() -> None:
    global a
    a = 3
    dict = {1: "one", 2: "Two"}
    t = (1, 5, 7, 10)
    l = [1, 2, t, dict, 5]
    print(f"Function {f(1)}")
    dict = {"1": t, "2": l, "3": 3}
    tmp = Serializer.obj_to_intermediate_format(f)
    print(tmp)
    result = eval(str(tmp))
    print(result)
    new_func = Serializer.intermediate_format_to_obj(result)
    print(f"Function {new_func(1)}")


if __name__ == '__main__':
    main()
