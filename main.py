import Serializer
from json_converter import JsonConverter
import tomli
import tomli_w

from serializers.intermediate_format_serializer import IntermediateFormatSerializer
from serializers.toml_serializer import TomlSerializer

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

    test_obj = Test(44)
    ser_test_obj = Serializer.obj_to_intermediate_format(test_obj)
    print(f"ser_test_obj: {ser_test_obj}")
    deser_test_obj = Serializer.intermediate_format_to_obj(ser_test_obj)
    print(f"deser_test_obj: {deser_test_obj}")
    print(deser_test_obj.get_value())
    deser_test_obj.print_value()
    tmp = JsonConverter.to_json(ser_test_obj)
    print(f"JsonConverter to json: {tmp}")
    deser_tmp = JsonConverter.from_json(tmp)
    print(f"JsonConverter from json: {deser_tmp}")
    deser_tmp = Serializer.intermediate_format_to_obj(deser_tmp)
    print(deser_tmp)
    deser_tmp.print_value()

    # serializer = JsonSerializer()
    # ser_func = serializer.dumps(f)
    # desr_func = serializer.loads(ser_func)
    # print(desr_func)
    # print(desr_func(5))
    # serializer.dump(f, "file.txt")
    # new_func = serializer.load("file.txt")
    # print(new_func)
    # print(new_func(5))

    # print("List")
    # l = [1, 2, "Hello", 'world', 3.14, {'set1', 'set2'}, ('tuple1', 2), {'item1': 1}]
    # print(l)
    # intermediate_l = IntermediateFormatSerializer.iterable_to_dict(l)
    # print(intermediate_l)
    # deser_l = IntermediateFormatSerializer.intermediate_format_to_obj(intermediate_l)
    # print(deser_l)
    # print(l == deser_l)
    # ser_lst = JsonSerializer.dumps(l)
    # print(ser_lst)
    #
    # print("\nTuple")
    # tpl = (1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {"item1": 1}, ["list", 3.14, 10, 12])
    # print(tpl)
    # intermediate_tpl = IntermediateFormatSerializer.iterable_to_dict(tpl)
    # print(intermediate_tpl)
    # deser_tpl = IntermediateFormatSerializer.intermediate_format_to_obj(intermediate_tpl)
    # print(deser_tpl)
    # print(tpl == deser_tpl)
    #
    # print("\nBytearray")
    # b_arr = bytearray(b'hello world!')
    # print(b_arr)
    # intermediate_b_arr = IntermediateFormatSerializer.iterable_to_dict(b_arr)
    # print(intermediate_b_arr)
    # deser_b_arr = IntermediateFormatSerializer.intermediate_format_to_obj(intermediate_b_arr)
    # print(deser_b_arr)
    # print(b_arr == deser_b_arr)
    #
    # print("\nDictionary")
    # dct = {"lst": [1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {'item1': 1}],
    #        "tpl": (1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {"item1": 1}, ["list", 3.14, 10, 12]),
    #        "one": 1}
    # print(dct)
    # intermediate_dct = IntermediateFormatSerializer.dict_to_dict(dct)
    # print(intermediate_dct)
    # deser_dct = IntermediateFormatSerializer.intermediate_format_to_obj(intermediate_dct)
    # print(deser_dct)
    # print(dct == deser_dct)
    #
    # print("\nCode")
    # code = f.__code__
    # print(code)
    # intermediate_code = IntermediateFormatSerializer.code_to_dict(code)
    # print(intermediate_code)
    # deser_code = IntermediateFormatSerializer.form_to_code(intermediate_code)
    # print(deser_code)
    # print(deser_code == code)
    #
    # print("\nFunction")
    # func = f
    # print(func)
    # intermediate_func = IntermediateFormatSerializer.function_to_dict(func)
    # print(intermediate_func)
    # deser_func = IntermediateFormatSerializer.intermediate_format_to_obj(intermediate_func)
    # print(deser_func)
    # print(func == deser_func)
    #
    # print("\nModule")
    # module = __import__("math")
    # print(module)
    # intermediate_module = IntermediateFormatSerializer.module_to_dict(module)
    # print(intermediate_module)
    # deser_module = IntermediateFormatSerializer.intermediate_format_to_obj(intermediate_module)
    # print(deser_module)
    # print(module == deser_module)
    # print(inspect.getmembers(func))

    toml_string = """
    # This is a TOML document.
    
     title = "TOML Example"
    
     [owner]
     name = "Tom Preston-Werner"
     dob = 1979-05-27T07:32:00-08:00 # First class dates
    
     [database]
     server = "192.168.1.1"
     ports = [ 8001, 8001, 8002 ]
     connection_max = 5000
     enabled = true
    
     [servers]
    
       # Indentation (tabs and/or spaces) is allowed but not required
       [servers.alpha]
       ip = "10.0.0.1"
       dc = "eqdc10"
    
       [servers.beta]
       ip = "10.0.0.2"
       dc = "eqdc10"
    
     [clients]
     data = [ ["gamma", "delta"], [1, 2] ]
    
     # Line breaks are OK when inside arrays
     hosts = [
       "alpha",
       "omega"
     ]
     """
    # parsed_toml = toml.loads(toml_string)
    # print(f"Parsed_toml {parsed_toml}")
    #
    # print(toml.dumps({"People": {'Name': "Matvey", 'Surename': "Makaro", "Surname": None}}))
    # print("List")
    # l = [1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {'item1': 1}]
    # print(l)
    # intermediate_l = IntermediateFormatSerializer.iterable_to_dict(l)
    # print(intermediate_l)
    # tmp = IntermediateFormatSerializer.obj_to_intermediate_format(f)
    # print(tmp)
    # tmp = JsonConverter.to_json(tmp)
    # print(tmp)
    # dumps_f = pytoml.dumps(tmp)
    # print(f"Toml dumps {dumps_f}")
    # loads_f = toml.loads(dumps_f)
    # print(f"Toml loads {loads_f}")
    # print(yaml.dump(intermediate_l))
    #ser_l = toml.dumps(intermediate_l)
    #print(ser_l)
    #deser_l = toml.loads(ser_l)
    #print(deser_l)
    # expected_f = f
    # ser_f = YamlSerializer.dumps(f)
    # print(ser_f)
    # deser_f = YamlSerializer.loads(ser_f)
    # print(deser_f)
    # print(deser_f(3))

    l = [1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {'item1': 1}]
    intermediate_l = IntermediateFormatSerializer.obj_to_intermediate_format(l)
    intermediat_f = IntermediateFormatSerializer.obj_to_intermediate_format(f)
    print(intermediate_l)
    ser_f = tomli_w.dumps(intermediate_l)
    print(ser_f)
    deser_f = tomli.loads(ser_f)
    print(deser_f)
    print("-----------------------------------------------------")
    ser_lst = """list = [
        1,
        2,
        "Hello",
        "world",
        3.14,
        { tuple = [
        "tuple1",
        2,
    ] },
        { item1 = 1 },
    ]
    """
    print(ser_lst.replace("\n\r", "\n"))
    deser_lst = TomlSerializer.loads(ser_lst)
    print(deser_lst)
    expected_lst = [1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {'item1': 1}]





if __name__ == '__main__':
    main()
