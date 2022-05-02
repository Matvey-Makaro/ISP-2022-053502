import pytest
from json_converter import JsonConverter


def test_to_json() -> None:
    location = '/home/matvey/Documents/Projects/Python lab rab/lab rab 2/main.py'
    intermediate_object = {'object':
                               {'class':
                                    {'class':
                                         {'name': 'Test', 'qualname': 'Test',
                                          'bases': {'tuple': []}, 'attrs': {'__module__': '__main__', 'static_value': 3,
                                                                            '__init__': {
                                                                                'function': {'__closure__': None,
                                                                                             '__code__':
                                                                                                 {'co_argcount': 2,
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
                                                                                                             '64005300',
                                                                                                  'co_consts': {
                                                                                                      'tuple': [None,
                                                                                                                10]},
                                                                                                  'co_names': {
                                                                                                      'tuple': ['value',
                                                                                                        'test_value']},
                                                                                                  'co_varnames': {
                                                                                                      'tuple': ['self',
                                                                                                                'value'
                                                                                                                ]},
                                                                                                  'co_filename':
                                                                                                      location,
                                                                                                  'co_name': '__init__',
                                                                                                  'co_firstlineno': 39,
                                                                                                  'co_lnotab': '000106'
                                                                                                               '01',
                                                                                                  'co_freevars': {
                                                                                                      'tuple': []},
                                                                                                  'co_cellvars': {
                                                                                                      'tuple': []}},
                                                                                             '__globals__': {},
                                                                                             '__defaults__': None}},
                                                                            'get_value': {
                                                                                'function': {'__closure__': None,
                                                                                             '__code__': {
                                                                                                 'co_argcount': 1,
                                                                                                 'co_posonlyargcount':
                                                                                                     0,
                                                                                                 'co_kwonlyargcount': 0,
                                                                                                 'co_nlocals': 1,
                                                                                                 'co_stacksize': 2,
                                                                                                 'co_flags': 67,
                                                                                                 'co_code': '7c006a006'
                                                                                                            '401170053'
                                                                                                            '00',
                                                                                                 'co_consts': {
                                                                                                     'tuple': [None,
                                                                                                               1]},
                                                                                                 'co_names': {'tuple': [
                                                                                                     'value']},
                                                                                                 'co_varnames': {
                                                                                                     'tuple': ['self']},
                                                                                                 'co_filename':
                                                                                                     location,
                                                                                                 'co_name': 'get_value',
                                                                                                 'co_firstlineno': 43,
                                                                                                 'co_lnotab': '0001',
                                                                                                 'co_freevars': {
                                                                                                     'tuple': []},
                                                                                                 'co_cellvars': {
                                                                                                     'tuple': []}},
                                                                                             '__globals__': {},
                                                                                             '__defaults__': None}},
                                                                            'print_value': {
                                                                                'function': {'__closure__': None,
                                                                                             '__code__': {
                                                                                                 'co_argcount': 1,
                                                                                                 'co_posonlyargcount': 0,
                                                                                                 'co_kwonlyargcount': 0,
                                                                                                 'co_nlocals': 1,
                                                                                                 'co_stacksize': 2,
                                                                                                 'co_flags': 67,
                                                                                                 'co_code': '74007c006'
                                                                                                            'a01830101'
                                                                                                            '006400530'
                                                                                                            '0',
                                                                                                 'co_consts': {
                                                                                                     'tuple': [None]},
                                                                                                 'co_names': {
                                                                                                     'tuple': ['print',
                                                                                                               'value']
                                                                                                 },
                                                                                                 'co_varnames': {
                                                                                                     'tuple': ['self']},
                                                                                                 'co_filename':
                                                                                                     location,
                                                                                                 'co_name':
                                                                                                     'print_value',
                                                                                                 'co_firstlineno': 46,
                                                                                                 'co_lnotab': '0001',
                                                                                                 'co_freevars': {
                                                                                                     'tuple': []},
                                                                                                 'co_cellvars': {
                                                                                                     'tuple': []}},
                                                                                             '__globals__': {},
                                                                                             '__defaults__': None}},
                                                                            '__doc__': None}}},
                                'attrs': {'value': 44, 'test_value': 10}}}
    json_obj = JsonConverter.to_json(intermediate_object)
    expected_json_obj = '{"object": {"class": {"class": {"name": "Test", "qualname": "Test", "bases": {"tuple": []}, "attrs": {"__module__": "__main__", "static_value": 3, "__init__": {"function": {"__closure__": null, "__code__": {"co_argcount": 2, "co_posonlyargcount": 0, "co_kwonlyargcount": 0, "co_nlocals": 2, "co_stacksize": 2, "co_flags": 67, "co_code": "7c017c005f0064017c005f0164005300", "co_consts": {"tuple": [null, 10]}, "co_names": {"tuple": ["value", "test_value"]}, "co_varnames": {"tuple": ["self", "value"]}, "co_filename": "/home/matvey/Documents/Projects/Python lab rab/lab rab 2/main.py", "co_name": "__init__", "co_firstlineno": 39, "co_lnotab": "00010601", "co_freevars": {"tuple": []}, "co_cellvars": {"tuple": []}}, "__globals__": {}, "__defaults__": null}}, "get_value": {"function": {"__closure__": null, "__code__": {"co_argcount": 1, "co_posonlyargcount": 0, "co_kwonlyargcount": 0, "co_nlocals": 1, "co_stacksize": 2, "co_flags": 67, "co_code": "7c006a00640117005300", "co_consts": {"tuple": [null, 1]}, "co_names": {"tuple": ["value"]}, "co_varnames": {"tuple": ["self"]}, "co_filename": "/home/matvey/Documents/Projects/Python lab rab/lab rab 2/main.py", "co_name": "get_value", "co_firstlineno": 43, "co_lnotab": "0001", "co_freevars": {"tuple": []}, "co_cellvars": {"tuple": []}}, "__globals__": {}, "__defaults__": null}}, "print_value": {"function": {"__closure__": null, "__code__": {"co_argcount": 1, "co_posonlyargcount": 0, "co_kwonlyargcount": 0, "co_nlocals": 1, "co_stacksize": 2, "co_flags": 67, "co_code": "74007c006a018301010064005300", "co_consts": {"tuple": [null]}, "co_names": {"tuple": ["print", "value"]}, "co_varnames": {"tuple": ["self"]}, "co_filename": "/home/matvey/Documents/Projects/Python lab rab/lab rab 2/main.py", "co_name": "print_value", "co_firstlineno": 46, "co_lnotab": "0001", "co_freevars": {"tuple": []}, "co_cellvars": {"tuple": []}}, "__globals__": {}, "__defaults__": null}}, "__doc__": null}}}, "attrs": {"value": 44, "test_value": 10}}}'
    assert json_obj == expected_json_obj


def test_from_json() -> None:
    location = '/home/matvey/Documents/Projects/Python lab rab/lab rab 2/main.py'
    json_obj = '{"object": {"class": {"class": {"name": "Test", "qualname": "Test", "bases": {"tuple": []}, "attrs": {"__module__": "__main__", "static_value": 3, "__init__": {"function": {"__closure__": null, "__code__": {"co_argcount": 2, "co_posonlyargcount": 0, "co_kwonlyargcount": 0, "co_nlocals": 2, "co_stacksize": 2, "co_flags": 67, "co_code": "7c017c005f0064017c005f0164005300", "co_consts": {"tuple": [null, 10]}, "co_names": {"tuple": ["value", "test_value"]}, "co_varnames": {"tuple": ["self", "value"]}, "co_filename": "/home/matvey/Documents/Projects/Python lab rab/lab rab 2/main.py", "co_name": "__init__", "co_firstlineno": 39, "co_lnotab": "00010601", "co_freevars": {"tuple": []}, "co_cellvars": {"tuple": []}}, "__globals__": {}, "__defaults__": null}}, "get_value": {"function": {"__closure__": null, "__code__": {"co_argcount": 1, "co_posonlyargcount": 0, "co_kwonlyargcount": 0, "co_nlocals": 1, "co_stacksize": 2, "co_flags": 67, "co_code": "7c006a00640117005300", "co_consts": {"tuple": [null, 1]}, "co_names": {"tuple": ["value"]}, "co_varnames": {"tuple": ["self"]}, "co_filename": "/home/matvey/Documents/Projects/Python lab rab/lab rab 2/main.py", "co_name": "get_value", "co_firstlineno": 43, "co_lnotab": "0001", "co_freevars": {"tuple": []}, "co_cellvars": {"tuple": []}}, "__globals__": {}, "__defaults__": null}}, "print_value": {"function": {"__closure__": null, "__code__": {"co_argcount": 1, "co_posonlyargcount": 0, "co_kwonlyargcount": 0, "co_nlocals": 1, "co_stacksize": 2, "co_flags": 67, "co_code": "74007c006a018301010064005300", "co_consts": {"tuple": [null]}, "co_names": {"tuple": ["print", "value"]}, "co_varnames": {"tuple": ["self"]}, "co_filename": "/home/matvey/Documents/Projects/Python lab rab/lab rab 2/main.py", "co_name": "print_value", "co_firstlineno": 46, "co_lnotab": "0001", "co_freevars": {"tuple": []}, "co_cellvars": {"tuple": []}}, "__globals__": {}, "__defaults__": null}}, "__doc__": null}}}, "attrs": {"value": 44, "test_value": 10}}}'
    obj = JsonConverter.from_json(json_obj)
    expected_obj = {'object':
                        {'class':
                             {'class':
                                  {'name': 'Test', 'qualname': 'Test',
                                   'bases': {'tuple': []}, 'attrs': {'__module__': '__main__', 'static_value': 3,
                                                                     '__init__': {
                                                                         'function': {'__closure__': None,
                                                                                      '__code__':
                                                                                          {'co_argcount': 2,
                                                                                           'co_posonlyargcount': 0,
                                                                                           'co_kwonlyargcount': 0,
                                                                                           'co_nlocals': 2,
                                                                                           'co_stacksize': 2,
                                                                                           'co_flags': 67,
                                                                                           'co_code': '7c017c00'
                                                                                                      '5f006401'
                                                                                                      '7c005f01'
                                                                                                      '64005300',
                                                                                           'co_consts': {
                                                                                               'tuple': [None,
                                                                                                         10]},
                                                                                           'co_names': {
                                                                                               'tuple': ['value',
                                                                                                         'test_value']},
                                                                                           'co_varnames': {
                                                                                               'tuple': ['self',
                                                                                                         'value']},
                                                                                           'co_filename':
                                                                                               location,
                                                                                           'co_name': '__init__',
                                                                                           'co_firstlineno': 39,
                                                                                           'co_lnotab': '000106'
                                                                                                        '01',
                                                                                           'co_freevars': {
                                                                                               'tuple': []},
                                                                                           'co_cellvars': {
                                                                                               'tuple': []}},
                                                                                      '__globals__': {},
                                                                                      '__defaults__': None}},
                                                                     'get_value': {
                                                                         'function': {'__closure__': None,
                                                                                      '__code__': {
                                                                                          'co_argcount': 1,
                                                                                          'co_posonlyargcount': 0,
                                                                                          'co_kwonlyargcount': 0,
                                                                                          'co_nlocals': 1,
                                                                                          'co_stacksize': 2,
                                                                                          'co_flags': 67,
                                                                                          'co_code': '7c006a006'
                                                                                                     '401170053'
                                                                                                     '00',
                                                                                          'co_consts': {
                                                                                              'tuple': [None,
                                                                                                        1]},
                                                                                          'co_names': {'tuple': [
                                                                                              'value']},
                                                                                          'co_varnames': {
                                                                                              'tuple': ['self']},
                                                                                          'co_filename':
                                                                                              location,
                                                                                          'co_name': 'get_value',
                                                                                          'co_firstlineno': 43,
                                                                                          'co_lnotab': '0001',
                                                                                          'co_freevars': {
                                                                                              'tuple': []},
                                                                                          'co_cellvars': {
                                                                                              'tuple': []}},
                                                                                      '__globals__': {},
                                                                                      '__defaults__': None}},
                                                                     'print_value': {
                                                                         'function': {'__closure__': None,
                                                                                      '__code__': {
                                                                                          'co_argcount': 1,
                                                                                          'co_posonlyargcount': 0,
                                                                                          'co_kwonlyargcount': 0,
                                                                                          'co_nlocals': 1,
                                                                                          'co_stacksize': 2,
                                                                                          'co_flags': 67,
                                                                                          'co_code': '74007c006'
                                                                                                     'a01830101'
                                                                                                     '006400530'
                                                                                                     '0',
                                                                                          'co_consts': {
                                                                                              'tuple': [None]},
                                                                                          'co_names': {
                                                                                              'tuple': ['print',
                                                                                                        'value']
                                                                                          },
                                                                                          'co_varnames': {
                                                                                              'tuple': ['self']},
                                                                                          'co_filename':
                                                                                              location,
                                                                                          'co_name':
                                                                                              'print_value',
                                                                                          'co_firstlineno': 46,
                                                                                          'co_lnotab': '0001',
                                                                                          'co_freevars': {
                                                                                              'tuple': []},
                                                                                          'co_cellvars': {
                                                                                              'tuple': []}},
                                                                                      '__globals__': {},
                                                                                      '__defaults__': None}},
                                                                     '__doc__': None}}},
                         'attrs': {'value': 44, 'test_value': 10}}}
    assert obj == expected_obj
