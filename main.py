import math

from serializers.serializer_creator import SerializerCreator

c = 42


def f(x):
    a = 123
    print(a)
    return math.sin(x * a * c)


def prepare_toml(obj: dict) -> dict:
    for key, value in obj.items():
        if type(value) == dict:
            prepare_toml(value)
        if type(value) == list:
            for i in range(len(value)):
                if value[i] is None:
                    obj[key][i] = "__none__"
        if value is None:
            obj[key] = "__none__"
    return obj


def deprepare_toml(obj: dict) -> dict:
    for key, value in obj.items():
        if type(value) == dict:
            value = deprepare_toml(value)
        if value == "__none__":
            value = None
    return obj


class Test:
    static_value = 3

    def __init__(self, value):
        self.value = value
        self.test_value = 10

    def get_value(self):
        return self.value + 1

    def print_value(self):
        print(self.value)


def main() -> None:
    # json_serializer = SerializerCreator.create("json")
    # print(f(10))
    # ser_f = json_serializer.dumps(f)
    # print(ser_f)
    # deser_f = json_serializer.loads(ser_f)
    # print(deser_f(10))
    #
    # print("---------------------")
    # yaml_serializer = SerializerCreator.create("yaml")
    # print(Test.static_value)
    # ser_cls = yaml_serializer.dumps(Test)
    # print(ser_cls)
    # desr_cls = yaml_serializer.loads(ser_cls)
    # print(desr_cls.static_value)
    #
    # print("--------------------------------------------------------")
    # toml_serializer = SerializerCreator.create("toml")
    # intermediate_f = IntermediateFormatSerializer.obj_to_intermediate_format(f)
    # intermediate_f = prepare_toml(intermediate_f)
    # print(intermediate_f)
    # ser_f = tomli_w.dumps(intermediate_f)
    #
    # print(ser_f)
    print("--------------------------------------------")
    print(f(7))
    toml_serializer = SerializerCreator.create("toml")
    func_ser = toml_serializer.dumps(f)
    print(func_ser)
    deser_func = toml_serializer.loads(func_ser)
    print(deser_func)
    print(deser_func(7))

    print("--------------------------------------------")
    print(f(7))
    toml_serializer = SerializerCreator.create("toml")
    func_ser = toml_serializer.dumps(Test)
    print(func_ser)
    deser_func = toml_serializer.loads(func_ser)
    print(deser_func)
    print(deser_func(7))


if __name__ == '__main__':
    main()
