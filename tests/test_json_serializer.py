from serializers.json_serializer import JsonSerializer

import math

c = 42


def f(x: int or float) -> float:
    a = 123
    print(a)
    return math.sin(x * a * c)


def test_dumps() -> None:
    ser_f = JsonSerializer.dumps(f)
    expected_ser_f = '{"function": {"__closure__": null, "__code__": {"co_argcount": 1, "co_posonlyargcount": 0, ' \
                     '"co_kwonlyargcount": 0, "co_nlocals": 2, "co_stacksize": 4, "co_flags": 67, "co_code": ' \
                     '"64017d0174007c01830101007401a0027c007c01140074031400a1015300", ' \
                     '"co_consts": {"tuple": [null, 123]}, "co_names": ' \
                     '{"tuple": ["print", "math", "sin", "c"]}, "co_varnames": {"tuple": ["x", "a"]}, "co_filename": ' \
                     '"/home/matvey/Documents/Projects/Python lab rab/lab rab 2/tests/test_json_serializer.py", ' \
                     '"co_name": "f", "co_firstlineno": 8, "co_lnotab": "000104010801", "co_freevars": {"tuple": []}, '\
                     '"co_cellvars": {"tuple": []}}, "__globals__": {"math": {"module": {"name": "math"}}, "c": 42}, ' \
                     '"__defaults__": null}}'
    assert ser_f == expected_ser_f

    # simple test
    lst = [1, 2, 'Hello', 'world', 3.14, ('tuple1', 2), {'item1': 1}]
    ser_lst = JsonSerializer.dumps(lst)
    expected_ser_lst = '{"list": [1, 2, "Hello", "world", 3.14, {"tuple": ["tuple1", 2]}, ' \
                       '{"item1": 1}]}'
    assert ser_lst == expected_ser_lst


def test_dump() -> None:
    file_name = "jsonfile.txt"
    JsonSerializer.dump(f, file_name)
    with open(file_name, "r") as file:
        ser_f = file.readline()
    expected_ser_f = '{"function": {"__closure__": null, "__code__": {"co_argcount": 1, "co_posonlyargcount": 0, ' \
                     '"co_kwonlyargcount": 0, "co_nlocals": 2, "co_stacksize": 4, "co_flags": 67, "co_code": ' \
                     '"64017d0174007c01830101007401a0027c007c01140074031400a1015300", ' \
                     '"co_consts": {"tuple": [null, 123]}, "co_names": ' \
                     '{"tuple": ["print", "math", "sin", "c"]}, "co_varnames": {"tuple": ["x", "a"]}, "co_filename": ' \
                     '"/home/matvey/Documents/Projects/Python lab rab/lab rab 2/tests/test_json_serializer.py", ' \
                     '"co_name": "f", "co_firstlineno": 8, "co_lnotab": "000104010801", "co_freevars": {"tuple": []}, ' \
                     '"co_cellvars": {"tuple": []}}, "__globals__": {"math": {"module": {"name": "math"}}, "c": 42}, ' \
                     '"__defaults__": null}}'
    assert ser_f == expected_ser_f


def test_loads() -> None:
    ser_f = '{"function": {"__closure__": null, "__code__": {"co_argcount": 1, "co_posonlyargcount": 0, ' \
                     '"co_kwonlyargcount": 0, "co_nlocals": 2, "co_stacksize": 4, "co_flags": 67, "co_code": ' \
                     '"64017d0174007c01830101007401a0027c007c01140074031400a1015300", ' \
                     '"co_consts": {"tuple": [null, 123]}, "co_names": ' \
                     '{"tuple": ["print", "math", "sin", "c"]}, "co_varnames": {"tuple": ["x", "a"]}, "co_filename": ' \
                     '"/home/matvey/Documents/Projects/Python lab rab/lab rab 2/tests/test_json_serializer.py", ' \
                     '"co_name": "f", "co_firstlineno": 8, "co_lnotab": "000104010801", "co_freevars": {"tuple": []}, ' \
                     '"co_cellvars": {"tuple": []}}, "__globals__": {"math": {"module": {"name": "math"}}, "c": 42}, ' \
                     '"__defaults__": null}}'
    deser_f = JsonSerializer.loads(ser_f)
    expected_f = f
    assert deser_f.__closure__ == expected_f.__closure__
    assert deser_f.__code__ == expected_f.__code__
    assert deser_f.__defaults__ == expected_f.__defaults__

    # simple test
    ser_lst = '{"list": [1, 2, "Hello", "world", 3.14, {"tuple": ["tuple1", 2]}, ' \
              '{"item1": 1}]}'
    deser_lst = JsonSerializer.loads(ser_lst)
    expected_lst = [1, 2, 'Hello', 'world', 3.14, ('tuple1', 2), {'item1': 1}]
    assert deser_lst == expected_lst


def test_load() -> None:
    file_name = "jsonfile.txt"
    deser_f = JsonSerializer.load(file_name)
    expected_f = f
    assert deser_f.__closure__ == expected_f.__closure__
    assert deser_f.__code__ == expected_f.__code__
    assert deser_f.__defaults__ == expected_f.__defaults__
