from yaml_serializer import YamlSerializer

import math

c = 42


def f(x):
    a = 123
    print(a)
    return math.sin(x * a * c)


def test_dumps() -> None:
    expected_f = f
    ser_f = YamlSerializer.dumps(f)
    expected_ser_f = """function:
  __closure__: null
  __code__:
    co_argcount: 1
    co_cellvars:
      tuple: []
    co_code: 64017d0174007c01830101007401a0027c007c01140074031400a1015300
    co_consts:
      tuple:
      - null
      - 123
    co_filename: /home/matvey/Documents/Projects/Python lab rab/lab rab 2/tests/test_yaml_serializer.py
    co_firstlineno: 8
    co_flags: 67
    co_freevars:
      tuple: []
    co_kwonlyargcount: 0
    co_lnotab: 000104010801
    co_name: f
    co_names:
      tuple:
      - print
      - math
      - sin
      - c
    co_nlocals: 2
    co_posonlyargcount: 0
    co_stacksize: 4
    co_varnames:
      tuple:
      - x
      - a
  __defaults__: null
  __globals__:
    c: 42
    math:
      module:
        name: math
"""
    assert ser_f == expected_ser_f

    # simple test
    lst = [1, 2, 'Hello', 'world', 3.14, ('tuple1', 2), {'item1': 1}]
    ser_lst = YamlSerializer.dumps(lst)
    expected_ser_lst = """list:
- 1
- 2
- Hello
- world
- 3.14
- tuple:
  - tuple1
  - 2
- item1: 1
"""
    assert ser_lst == expected_ser_lst


def test_dump() -> None:
    file_name = "yamlfile.txt"
    YamlSerializer.dump(f, file_name)
    ser_f = ""
    with open(file_name, "r") as file:
        for line in file:
            ser_f += line

    print(f"Ser_f: {ser_f}")
    expected_ser_f = """function:
  __closure__: null
  __code__:
    co_argcount: 1
    co_cellvars:
      tuple: []
    co_code: 64017d0174007c01830101007401a0027c007c01140074031400a1015300
    co_consts:
      tuple:
      - null
      - 123
    co_filename: /home/matvey/Documents/Projects/Python lab rab/lab rab 2/tests/test_yaml_serializer.py
    co_firstlineno: 8
    co_flags: 67
    co_freevars:
      tuple: []
    co_kwonlyargcount: 0
    co_lnotab: 000104010801
    co_name: f
    co_names:
      tuple:
      - print
      - math
      - sin
      - c
    co_nlocals: 2
    co_posonlyargcount: 0
    co_stacksize: 4
    co_varnames:
      tuple:
      - x
      - a
  __defaults__: null
  __globals__:
    c: 42
    math:
      module:
        name: math
"""
    print(f"Expected_ser_f: {expected_ser_f}")
    assert ser_f == expected_ser_f


def test_loads() -> None:
    ser_f = """function:
  __closure__: null
  __code__:
    co_argcount: 1
    co_cellvars:
      tuple: []
    co_code: 64017d0174007c01830101007401a0027c007c01140074031400a1015300
    co_consts:
      tuple:
      - null
      - 123
    co_filename: /home/matvey/Documents/Projects/Python lab rab/lab rab 2/tests/test_yaml_serializer.py
    co_firstlineno: 8
    co_flags: 67
    co_freevars:
      tuple: []
    co_kwonlyargcount: 0
    co_lnotab: 000104010801
    co_name: f
    co_names:
      tuple:
      - print
      - math
      - sin
      - c
    co_nlocals: 2
    co_posonlyargcount: 0
    co_stacksize: 4
    co_varnames:
      tuple:
      - x
      - a
  __defaults__: null
  __globals__:
    c: 42
    math:
      module:
        name: math
"""
    deser_f = YamlSerializer.loads(ser_f)
    expected_f = f
    assert deser_f.__closure__ == expected_f.__closure__
    assert deser_f.__code__ == expected_f.__code__
    assert deser_f.__defaults__ == expected_f.__defaults__


def test_load() -> None:
    file_name = "yamlfile.txt"
    deser_f = YamlSerializer.load(file_name)
    expected_f = f
    assert deser_f.__closure__ == expected_f.__closure__
    assert deser_f.__code__ == expected_f.__code__
    assert deser_f.__defaults__ == expected_f.__defaults__