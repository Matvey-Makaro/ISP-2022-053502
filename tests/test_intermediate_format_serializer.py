import math
from serializers.intermediate_format_serializer import IntermediateFormatSerializer

c = 42


def f(x):
    a = 123
    print(a)
    return math.sin(x * a * c)


class ExampleClass:
    static_value = 3

    def __init__(self, value):
        self.value = value
        self.test_value = 10

    def get_value(self) -> int:
        return self.value + 1

    def print_value(self) -> None:
        print(self.value)


def test_iterable_to_dict() -> None:
    # list
    lst = [1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {'item1': 1}]
    intermediate_lst = IntermediateFormatSerializer.iterable_to_dict(lst)
    expected_lst = {
        'list': [1, 2, 'Hello', 'world', 3.14, {'tuple': ['tuple1', 2]}, {'item1': 1}]}
    assert intermediate_lst == expected_lst

    # tuple
    tpl = (1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {"item1": 1}, ["list", 3.14, 10, 12])
    intermediate_tpl = IntermediateFormatSerializer.iterable_to_dict(tpl)
    expected_tpl = {'tuple': [1, 2, 'Hello', 'world', 3.14,
                              {'tuple': ['tuple1', 2]}, {'item1': 1}, {'list': ['list', 3.14, 10, 12]}]}
    assert intermediate_tpl == expected_tpl

    # bytearray
    b_arr = bytearray(b'hello world!')
    intermediate_b_arr = IntermediateFormatSerializer.iterable_to_dict(b_arr)
    expected_b_arr = {'bytearray': [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33]}
    assert intermediate_b_arr == expected_b_arr


def test_dict_to_dict() -> None:
    dct = {"lst": [1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {'item1': 1}],
           "tpl": (1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {"item1": 1}, ["list", 3.14, 10, 12]),
           "one": 1}
    intermediate_dct = IntermediateFormatSerializer.dict_to_dict(dct)
    expected_dct = {'lst': {'list': [1, 2, 'Hello', 'world', 3.14, {'tuple': ['tuple1', 2]}, {'item1': 1}]}, 'tpl': {
        'tuple': [1, 2, 'Hello', 'world', 3.14, {'tuple': ['tuple1', 2]}, {'item1': 1},
                  {'list': ['list', 3.14, 10, 12]}]}, 'one': 1}
    assert intermediate_dct == expected_dct


def test_code_to_dict() -> None:
    code = f.__code__
    intermediate_code = IntermediateFormatSerializer.code_to_dict(code)
    expected_code = {'co_argcount': 1, 'co_posonlyargcount': 0, 'co_kwonlyargcount': 0, 'co_nlocals': 2,
                     'co_stacksize': 4, 'co_flags': 67,
                     'co_code': '64017d0174007c01830101007401a0027c007c01140074031400a1015300',
                     'co_consts': {'tuple': [None, 123]}, 'co_names': {'tuple': ['print', 'math', 'sin', 'c']},
                     'co_varnames': {'tuple': ['x', 'a']},
                     'co_filename': '/home/matvey/Documents/Projects/Python lab rab/lab rab '
                                    '2/tests/test_intermediate_format_serializer.py', 'co_name': 'f',
                     'co_firstlineno': f.__code__.co_firstlineno, 'co_lnotab': '000104010801', 'co_freevars':
                         {'tuple': []}, 'co_cellvars': {'tuple': []}}

    assert intermediate_code == expected_code


def test_function_to_dict() -> None:
    func = f
    intermediate_func = IntermediateFormatSerializer.function_to_dict(func)
    expected_func = {'function': {'__closure__': None,
                                  '__code__': {'co_argcount': 1, 'co_posonlyargcount': 0, 'co_kwonlyargcount': 0,
                                               'co_nlocals': 2, 'co_stacksize': 4,
                                               'co_flags': 67,
                                               'co_code': '64017d0174007c01830101007401a0027c007c01140074031400'
                                                          'a1015300',
                                               'co_consts': {'tuple': [None, 123]},
                                               'co_names': {'tuple': ['print', 'math', 'sin', 'c']},
                                               'co_varnames': {'tuple': ['x', 'a']},
                                               'co_filename': '/home/matvey/Documents/Projects/Python lab rab/'
                                                              'lab rab '
                                                              '2/tests/test_intermediate_format_serializer.py',
                                               'co_name': 'f', 'co_firstlineno': f.__code__.co_firstlineno,
                                               'co_lnotab': '000104010801', 'co_freevars':
                                                   {'tuple': []}, 'co_cellvars': {'tuple': []}},
                                  '__globals__': {'math': {'module': {'name': 'math'}},
                                                  'c': 42}, '__defaults__': None}}
    assert intermediate_func == expected_func


def test_module_to_dict() -> None:
    module = __import__("math")
    intermediate_module = IntermediateFormatSerializer.module_to_dict(module)
    expected_module = {'module': {'name': 'math'}}
    assert intermediate_module == expected_module


def test_class_to_dict() -> None:
    cls = ExampleClass
    intermediate_cls = IntermediateFormatSerializer.class_to_dict(cls)
    init_lno = ExampleClass.__init__.__code__.co_firstlineno
    get_lno = ExampleClass.get_value.__code__.co_firstlineno
    print_lno = ExampleClass.print_value.__code__.co_firstlineno
    expected_cls = {'class': {'name': 'ExampleClass', 'qualname': 'ExampleClass', 'bases': {'tuple': []},
                              'attrs': {'__module__': 'tests.test_intermediate_format_serializer', 'static_value': 3,
                                        '__init__':
                                            {'function': {'__closure__': None,
                                                          '__code__': {'co_argcount': 2, 'co_posonlyargcount': 0,
                                                                       'co_kwonlyargcount': 0, 'co_nlocals': 2,
                                                                       'co_stacksize': 2, 'co_flags': 67,
                                                                       'co_code': '7c017c005f0064017c005f0164005300',
                                                                       'co_consts': {'tuple': [None, 10]},
                                                                       'co_names': {'tuple': ['value', 'test_value']},
                                                                       'co_varnames': {'tuple': ['self', 'value']},
                                                                       'co_filename': '/home/matvey/Documents/Projects/'
                                                                                      'Python lab rab/lab rab 2/tests/'
                                                                                      'test_intermediate_format_'
                                                                                      'serializer.py',
                                                                       'co_name': '__init__', 'co_firstlineno':
                                                                           init_lno,
                                                                       'co_lnotab': '00010601',
                                                                       'co_freevars': {'tuple': []},
                                                                       'co_cellvars': {'tuple': []}}, '__globals__': {},
                                                          '__defaults__': None}}, 'get_value': {
                                      'function': {'__closure__': None,
                                                   '__code__': {'co_argcount': 1, 'co_posonlyargcount': 0,
                                                                'co_kwonlyargcount': 0, 'co_nlocals': 1,
                                                                'co_stacksize': 2, 'co_flags': 67,
                                                                'co_code': '7c006a00640117005300',
                                                                'co_consts': {'tuple': [None, 1]},
                                                                'co_names': {'tuple': ['value']},
                                                                'co_varnames': {'tuple': ['self']},
                                                                'co_filename': '/home/matvey/Documents/Projects/'
                                                                               'Python lab rab/lab rab 2/tests/'
                                                                               'test_intermediate_format_serializer.py',
                                                                'co_name': 'get_value', 'co_firstlineno': get_lno,
                                                                'co_lnotab': '0001', 'co_freevars': {'tuple': []},
                                                                'co_cellvars': {'tuple': []}}, '__globals__': {},
                                                   '__defaults__': None}}, 'print_value': {
                                      'function': {'__closure__': None,
                                                   '__code__': {'co_argcount': 1, 'co_posonlyargcount': 0,
                                                                'co_kwonlyargcount': 0, 'co_nlocals': 1,
                                                                'co_stacksize': 2, 'co_flags': 67,
                                                                'co_code': '74007c006a018301010064005300',
                                                                'co_consts': {'tuple': [None]},
                                                                'co_names': {'tuple': ['print', 'value']},
                                                                'co_varnames': {'tuple': ['self']},
                                                                'co_filename': '/home/matvey/Documents/Projects/'
                                                                               'Python lab rab/lab rab 2/tests/'
                                                                               'test_intermediate_format_serializer.py',
                                                                'co_name': 'print_value', 'co_firstlineno': print_lno,
                                                                'co_lnotab': '0001', 'co_freevars': {'tuple': []},
                                                                'co_cellvars': {'tuple': []}}, '__globals__': {},
                                                   '__defaults__': None}}, '__doc__': None}}}
    assert intermediate_cls == expected_cls


def test_instance_of_class_to_dict() -> None:
    instance = ExampleClass(10)
    intermediate_instance = IntermediateFormatSerializer.instance_of_class_to_dict(instance)
    location = '/home/matvey/Documents/Projects/Python lab rab/lab rab 2/tests/test_intermediate_format_serializer.py'
    init_lno = ExampleClass.__init__.__code__.co_firstlineno
    get_lno = ExampleClass.get_value.__code__.co_firstlineno
    print_lno = ExampleClass.print_value.__code__.co_firstlineno
    expected_instance = \
        {'object': {'class': {'class': {'name': 'ExampleClass', 'qualname': 'ExampleClass', 'bases': {'tuple': []},
                                        'attrs': {'__module__': 'tests.test_intermediate_format_serializer',
                                                  'static_value': 3, '__init__': {'function': {'__closure__': None,
                                                                                               '__code__': {
                                                                                                   'co_argcount': 2,
                                                                                                   'co_posonlyargcount':
                                                                                                       0,
                                                                                                   'co_kwonlyargcount':
                                                                                                       0,
                                                                                                   'co_nlocals': 2,
                                                                                                   'co_stacksize': 2,
                                                                                                   'co_flags': 67,
                                                                                                   'co_code': '7c017c00'
                                                                                                              '5f006401'
                                                                                                              '7c005f01'
                                                                                                              '64005300'
                                                                                                   ,
                                                                                                   'co_consts': {
                                                                                                       'tuple': [None,
                                                                                                                 10]},
                                                                                                   'co_names': {
                                                                                                       'tuple': [
                                                                                                           'value',
                                                                                                           'test_value'
                                                                                                       ]},
                                                                                                   'co_varnames': {
                                                                                                       'tuple': ['self',
                                                                                                                 'value'
                                                                                                                 ]},
                                                                                                   'co_filename':
                                                                                                       location,
                                                                                                   'co_name': '__init__'
                                                                                                   ,
                                                                                                   'co_firstlineno':
                                                                                                       init_lno,
                                                                                                   'co_lnotab': '00010'
                                                                                                                '601',
                                                                                                   'co_freevars': {
                                                                                                       'tuple': []},
                                                                                                   'co_cellvars': {
                                                                                                       'tuple': []}},
                                                                                               '__globals__': {},
                                                                                               '__defaults__': None}},
                                                  'get_value': {'function': {'__closure__': None,
                                                                             '__code__': {'co_argcount': 1,
                                                                                          'co_posonlyargcount': 0,
                                                                                          'co_kwonlyargcount': 0,
                                                                                          'co_nlocals': 1,
                                                                                          'co_stacksize': 2,
                                                                                          'co_flags': 67,
                                                                                          'co_code': '7c006a00640117005'
                                                                                                     '300',
                                                                                          'co_consts': {
                                                                                              'tuple': [None, 1]},
                                                                                          'co_names': {
                                                                                              'tuple': ['value']},
                                                                                          'co_varnames': {
                                                                                              'tuple': ['self']},
                                                                                          'co_filename': location,
                                                                                          'co_name': 'get_value',
                                                                                          'co_firstlineno':
                                                                                              get_lno,
                                                                                          'co_lnotab': '0001',
                                                                                          'co_freevars': {'tuple': []},
                                                                                          'co_cellvars': {'tuple': []}},
                                                                             '__globals__': {}, '__defaults__': None}},
                                                  'print_value': {'function': {'__closure__': None,
                                                                               '__code__': {'co_argcount': 1,
                                                                                            'co_posonlyargcount': 0,
                                                                                            'co_kwonlyargcount': 0,
                                                                                            'co_nlocals': 1,
                                                                                            'co_stacksize': 2,
                                                                                            'co_flags': 67,
                                                                                            'co_code': '74007c006a01830'
                                                                                                       '1010064005300',
                                                                                            'co_consts': {
                                                                                                'tuple': [None]},
                                                                                            'co_names': {
                                                                                                'tuple': ['print',
                                                                                                          'value']},
                                                                                            'co_varnames': {
                                                                                                'tuple': ['self']},
                                                                                            'co_filename': location,
                                                                                            'co_name': 'print_value',
                                                                                            'co_firstlineno':
                                                                                                print_lno,
                                                                                            'co_lnotab': '0001',
                                                                                            'co_freevars': {
                                                                                                'tuple': []},
                                                                                            'co_cellvars': {
                                                                                                'tuple': []}},
                                                                               '__globals__': {},
                                                                               '__defaults__': None}},
                                                  '__doc__': None}}}, 'attrs': {'value': 10, 'test_value': 10}}}
    assert intermediate_instance == expected_instance


def test_format_to_iterable() -> None:
    # list
    intermediate_lst = {'list': [1, 2, 'Hello', 'world', 3.14, {'set': ['set2', 'set1']}, {'tuple': ['tuple1', 2]},
                                 {'item1': 1}]}
    lst = IntermediateFormatSerializer.format_to_iterable(intermediate_lst)
    expected_lst = [1, 2, 'Hello', 'world', 3.14, {'set2', 'set1'}, ('tuple1', 2), {'item1': 1}]
    assert lst == expected_lst

    # tuple

    intermediate_tpl = {'tuple': [1, 2, 'Hello', 'world', 3.14, {'tuple': ['tuple1', 2]}, {'item1': 1},
                                  {'list': ['list', 3.14, 10, 12]}]}
    tpl = IntermediateFormatSerializer.format_to_iterable(intermediate_tpl)
    expected_tpl = (1, 2, 'Hello', 'world', 3.14, ('tuple1', 2), {'item1': 1}, ['list', 3.14, 10, 12])
    assert tpl == expected_tpl

    # bytearray
    intermediate_b_arr = {'bytearray': [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33]}
    b_arr = IntermediateFormatSerializer.format_to_iterable(intermediate_b_arr)
    expected_b_arr = bytearray(b'hello world!')
    assert b_arr == expected_b_arr


def test_format_to_dict() -> None:
    intermediate_dct = {'lst': {'list': [1, 2, 'Hello', 'world', 3.14, {'tuple': ['tuple1', 2]}, {'item1': 1}]},
                        'tpl': {'tuple': [1, 2, 'Hello', 'world', 3.14, {'tuple': ['tuple1', 2]}, {'item1': 1},
                                          {'list': ['list', 3.14, 10, 12]}]}, 'one': 1}
    dct = IntermediateFormatSerializer.format_to_dict(intermediate_dct)
    expected_dct = {'lst': [1, 2, 'Hello', 'world', 3.14, ('tuple1', 2), {'item1': 1}], 'tpl':
        (1, 2, 'Hello', 'world', 3.14, ('tuple1', 2), {'item1': 1}, ['list', 3.14, 10, 12]), 'one': 1}
    assert dct == expected_dct


def test_form_to_code() -> None:
    intermediate_code = {'co_argcount': 1, 'co_posonlyargcount': 0, 'co_kwonlyargcount': 0, 'co_nlocals': 2,
                         'co_stacksize': 4, 'co_flags': 67,
                         'co_code': '64017d0174007c01830101007401a0027c007c01140074031400a1015300',
                         'co_consts': {'tuple': [None, 123]}, 'co_names': {'tuple': ['print', 'math', 'sin', 'c']},
                         'co_varnames': {'tuple': ['x', 'a']},
                         'co_filename': '/home/matvey/Documents/Projects/Python lab rab/lab rab '
                                        '2/tests/test_intermediate_format_serializer.py', 'co_name': 'f',
                         'co_firstlineno': f.__code__.co_firstlineno, 'co_lnotab': '000104010801', 'co_freevars':
                             {'tuple': []}, 'co_cellvars': {'tuple': []}}
    code = IntermediateFormatSerializer.form_to_code(intermediate_code)
    expected_code = f.__code__
    assert code == expected_code


def test_format_to_function() -> None:
    intermediate_func = {'function': {'__closure__': None,
                                      "__code__": {'co_argcount': 1, 'co_posonlyargcount': 0, 'co_kwonlyargcount': 0,
                                                   'co_nlocals': 2, 'co_stacksize': 4,
                                                   'co_flags': 67,
                                                   'co_code': '64017d0174007c01830101007401a0027c007c01140074031400'
                                                              'a1015300',
                                                   'co_consts': {'tuple': [None, 123]},
                                                   'co_names': {'tuple': ['print', 'math', 'sin', 'c']},
                                                   'co_varnames': {'tuple': ['x', 'a']},
                                                   'co_filename': '/home/matvey/Documents/Projects/Python lab rab/'
                                                                  'lab rab '
                                                                  '2/tests/test_intermediate_format_serializer.py',
                                                   'co_name': 'f', 'co_firstlineno': f.__code__.co_firstlineno,
                                                   'co_lnotab': '000104010801', 'co_freevars':
                                                       {'tuple': []}, 'co_cellvars': {'tuple': []}},
                                      '__globals__': {'math': {'module': {'name': 'math'}},
                                                      'c': 42}, '__defaults__': None}}
    func = IntermediateFormatSerializer.format_to_function(intermediate_func["function"])
    expected_func = f
    assert func.__closure__ == expected_func.__closure__
    assert func.__code__ == expected_func.__code__
    assert func.__defaults__ == expected_func.__defaults__


def test_format_to_module() -> None:
    intermediate_module = {'module': {'name': 'math'}}
    module = IntermediateFormatSerializer.format_to_module(intermediate_module['module'])
    expected_module = __import__("math")
    assert module == expected_module


def test_format_to_class() -> None:
    init_lno = ExampleClass.__init__.__code__.co_firstlineno
    get_lno = ExampleClass.get_value.__code__.co_firstlineno
    print_lno = ExampleClass.print_value.__code__.co_firstlineno
    intermediate_cls = {'class': {'name': 'ExampleClass', 'qualname': 'ExampleClass', 'bases': {'tuple': []},
                              'attrs': {'__module__': 'tests.test_intermediate_format_serializer', 'static_value': 3,
                                        '__init__':
                                            {'function': {'__closure__': None,
                                                          '__code__': {'co_argcount': 2, 'co_posonlyargcount': 0,
                                                                       'co_kwonlyargcount': 0, 'co_nlocals': 2,
                                                                       'co_stacksize': 2, 'co_flags': 67,
                                                                       'co_code': '7c017c005f0064017c005f0164005300',
                                                                       'co_consts': {'tuple': [None, 10]},
                                                                       'co_names': {'tuple': ['value', 'test_value']},
                                                                       'co_varnames': {'tuple': ['self', 'value']},
                                                                       'co_filename': '/home/matvey/Documents/Projects/'
                                                                                      'Python lab rab/lab rab 2/tests/'
                                                                                      'test_intermediate_format_'
                                                                                      'serializer.py',
                                                                       'co_name': '__init__', 'co_firstlineno':
                                                                           init_lno,
                                                                       'co_lnotab': '00010601',
                                                                       'co_freevars': {'tuple': []},
                                                                       'co_cellvars': {'tuple': []}}, '__globals__': {},
                                                          '__defaults__': None}}, 'get_value': {
                                      'function': {'__closure__': None,
                                                   '__code__': {'co_argcount': 1, 'co_posonlyargcount': 0,
                                                                'co_kwonlyargcount': 0, 'co_nlocals': 1,
                                                                'co_stacksize': 2, 'co_flags': 67,
                                                                'co_code': '7c006a00640117005300',
                                                                'co_consts': {'tuple': [None, 1]},
                                                                'co_names': {'tuple': ['value']},
                                                                'co_varnames': {'tuple': ['self']},
                                                                'co_filename': '/home/matvey/Documents/Projects/'
                                                                               'Python lab rab/lab rab 2/tests/'
                                                                               'test_intermediate_format_serializer.py',
                                                                'co_name': 'get_value', 'co_firstlineno': get_lno,
                                                                'co_lnotab': '0001', 'co_freevars': {'tuple': []},
                                                                'co_cellvars': {'tuple': []}}, '__globals__': {},
                                                   '__defaults__': None}}, 'print_value': {
                                      'function': {'__closure__': None,
                                                   '__code__': {'co_argcount': 1, 'co_posonlyargcount': 0,
                                                                'co_kwonlyargcount': 0, 'co_nlocals': 1,
                                                                'co_stacksize': 2, 'co_flags': 67,
                                                                'co_code': '74007c006a018301010064005300',
                                                                'co_consts': {'tuple': [None]},
                                                                'co_names': {'tuple': ['print', 'value']},
                                                                'co_varnames': {'tuple': ['self']},
                                                                'co_filename': '/home/matvey/Documents/Projects/'
                                                                               'Python lab rab/lab rab 2/tests/'
                                                                               'test_intermediate_format_serializer.py',
                                                                'co_name': 'print_value', 'co_firstlineno': print_lno,
                                                                'co_lnotab': '0001', 'co_freevars': {'tuple': []},
                                                                'co_cellvars': {'tuple': []}}, '__globals__': {},
                                                   '__defaults__': None}}, '__doc__': None}}}
    cls = IntermediateFormatSerializer.format_to_class(intermediate_cls['class'])
    expected_cls = ExampleClass
    assert cls.__name__ == expected_cls.__name__
    assert cls.__qualname__ == expected_cls.__qualname__
    assert cls.__bases__ == expected_cls.__bases__
    assert cls.static_value == expected_cls.static_value


def test_format_to_instance_of_class() -> None:
    location = '/home/matvey/Documents/Projects/Python lab rab/lab rab 2/tests/test_intermediate_format_serializer.py'
    init_lno = ExampleClass.__init__.__code__.co_firstlineno
    get_lno = ExampleClass.get_value.__code__.co_firstlineno
    print_lno = ExampleClass.print_value.__code__.co_firstlineno
    intermediate_instance = \
        {'object': {'class': {'class': {'name': 'ExampleClass', 'qualname': 'ExampleClass', 'bases': {'tuple': []},
                                        'attrs': {'__module__': 'tests.test_intermediate_format_serializer',
                                                  'static_value': 3, '__init__': {'function': {'__closure__': None,
                                                                                               '__code__': {
                                                                                                   'co_argcount': 2,
                                                                                                   'co_posonlyargcount':
                                                                                                       0,
                                                                                                   'co_kwonlyargcount':
                                                                                                       0,
                                                                                                   'co_nlocals': 2,
                                                                                                   'co_stacksize': 2,
                                                                                                   'co_flags': 67,
                                                                                                   'co_code': '7c017c00'
                                                                                                              '5f006401'
                                                                                                              '7c005f01'
                                                                                                              '64005300'
                                                                                                   ,
                                                                                                   'co_consts': {
                                                                                                       'tuple': [None,
                                                                                                                 10]},
                                                                                                   'co_names': {
                                                                                                       'tuple': [
                                                                                                           'value',
                                                                                                           'test_value'
                                                                                                       ]},
                                                                                                   'co_varnames': {
                                                                                                       'tuple': ['self',
                                                                                                                 'value'
                                                                                                                 ]},
                                                                                                   'co_filename':
                                                                                                       location,
                                                                                                   'co_name': '__init__'
                                                                                                   ,
                                                                                                   'co_firstlineno':
                                                                                                       init_lno,
                                                                                                   'co_lnotab': '00010'
                                                                                                                '601',
                                                                                                   'co_freevars': {
                                                                                                       'tuple': []},
                                                                                                   'co_cellvars': {
                                                                                                       'tuple': []}},
                                                                                               '__globals__': {},
                                                                                               '__defaults__': None}},
                                                  'get_value': {'function': {'__closure__': None,
                                                                             '__code__': {'co_argcount': 1,
                                                                                          'co_posonlyargcount': 0,
                                                                                          'co_kwonlyargcount': 0,
                                                                                          'co_nlocals': 1,
                                                                                          'co_stacksize': 2,
                                                                                          'co_flags': 67,
                                                                                          'co_code': '7c006a00640117005'
                                                                                                     '300',
                                                                                          'co_consts': {
                                                                                              'tuple': [None, 1]},
                                                                                          'co_names': {
                                                                                              'tuple': ['value']},
                                                                                          'co_varnames': {
                                                                                              'tuple': ['self']},
                                                                                          'co_filename': location,
                                                                                          'co_name': 'get_value',
                                                                                          'co_firstlineno':
                                                                                              get_lno,
                                                                                          'co_lnotab': '0001',
                                                                                          'co_freevars': {'tuple': []},
                                                                                          'co_cellvars': {'tuple': []}},
                                                                             '__globals__': {}, '__defaults__': None}},
                                                  'print_value': {'function': {'__closure__': None,
                                                                               '__code__': {'co_argcount': 1,
                                                                                            'co_posonlyargcount': 0,
                                                                                            'co_kwonlyargcount': 0,
                                                                                            'co_nlocals': 1,
                                                                                            'co_stacksize': 2,
                                                                                            'co_flags': 67,
                                                                                            'co_code': '74007c006a01830'
                                                                                                       '1010064005300',
                                                                                            'co_consts': {
                                                                                                'tuple': [None]},
                                                                                            'co_names': {
                                                                                                'tuple': ['print',
                                                                                                          'value']},
                                                                                            'co_varnames': {
                                                                                                'tuple': ['self']},
                                                                                            'co_filename': location,
                                                                                            'co_name': 'print_value',
                                                                                            'co_firstlineno':
                                                                                                print_lno,
                                                                                            'co_lnotab': '0001',
                                                                                            'co_freevars': {
                                                                                                'tuple': []},
                                                                                            'co_cellvars': {
                                                                                                'tuple': []}},
                                                                               '__globals__': {},
                                                                               '__defaults__': None}},
                                                  '__doc__': None}}}, 'attrs': {'value': 10, 'test_value': 10}}}
    instance = IntermediateFormatSerializer.format_to_instance_of_class(intermediate_instance["object"])
    expected_instance = ExampleClass(10)
    assert instance.value == expected_instance.value
    assert instance.__class__.__qualname__ == expected_instance.__class__.__qualname__
