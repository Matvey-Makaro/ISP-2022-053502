import inspect
from types import *
import Serializer

import math
c = 42


def f(x):
    a = 123
    return math.sin(x * a * c)




def main() -> None:
    global a
    a = 3
    t = (1, 5, 7, 10)
    l = [1, 2, t, 4, 5]
    print(Serializer.obj_to_intermediate_format(f))


    print("--------------------------------------------------------")
    # for attr in CODE_ATTRIBUTES:
    #     print(f"Attr: {attr}: Type: {type(main.__code__.__getattribute__(attr))}, value: {main.__code__.__getattribute__(attr)}")

    # for key, value in main.__globals__.items():
    #     print(inspect.ismodule(key))
    #print(inspect.ismodule(main.__globals__["__loader__"]))




if __name__ == '__main__':
    main()
