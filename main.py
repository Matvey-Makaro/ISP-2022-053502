import inspect
from types import *
import Serializer
import parser

import math
c = 42


def f(x):
    a = 123
    return math.sin(x * a * c)




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
    # result = parser.parse(str(tmp))
    result = eval(str(tmp))
    print(type(result))
    print(result)
    new_func = Serializer.intermediate_format_to_obj(result)
    # print(f"Function {new_func(1)}")
    # print(inspect.getmembers(math))
    # print(type(math))
    # print(math)
    # print(math.__dict__)
    # print(math.__name__)
    help(ModuleType)
    modul = ModuleType("math")
    modul.__loader__ = math.__loader__


    print(inspect.getmembers(modul))
    print(inspect.getmembers(math))
    print(math.__dir__())
    print(math.__doc__)
    print(f.__globals__)
    print(f.__code__.co_names)
    # print(f.__globals__('math').)

    print("--------------------------------------------------------")
    # for attr in CODE_ATTRIBUTES:
    #     print(f"Attr: {attr}: Type: {type(main.__code__.__getattribute__(attr))}, value: {main.__code__.__getattribute__(attr)}")

    # for key, value in main.__globals__.items():
    #     print(inspect.ismodule(key))
    #print(inspect.ismodule(main.__globals__["__loader__"]))




if __name__ == '__main__':
    main()
