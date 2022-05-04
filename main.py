from serializers.serializer_creator import SerializerCreator

import math

c = 42


def f(x):
    a = 123
    print(a)
    return math.sin(x * a * c)


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
    json_serializer = SerializerCreator.create("json")
    print(f(10))
    ser_f = json_serializer.dumps(f)
    print(ser_f)
    deser_f = json_serializer.loads(ser_f)
    print(deser_f(10))

    print("---------------------")
    yaml_serializer = SerializerCreator.create("yaml")
    print(Test.static_value)
    ser_cls = yaml_serializer.dumps(Test)
    print(ser_cls)
    desr_cls = yaml_serializer.loads(ser_cls)
    print(desr_cls.static_value)



if __name__ == '__main__':
    main()

