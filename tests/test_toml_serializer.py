from serializers.toml_serializer import TomlSerializer


def test_dumps() -> None:
    lst = [1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {'item1': 1}]
    ser_lst = TomlSerializer.dumps(lst)
    expected_ser_lst = """list = [
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
    assert ser_lst == expected_ser_lst


def test_dump() -> None:
    lst = [1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {'item1': 1}]
    file_name = "tomlfile.txt"
    TomlSerializer.dump(lst, file_name)
    ser_lst = ""
    with open(file_name, "r") as file:
        for line in file:
            ser_lst += line
    expected_ser_lst = """list = [
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
    assert ser_lst == expected_ser_lst


def test_loads() -> None:
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
    deser_lst = TomlSerializer.loads(ser_lst)
    print(deser_lst)
    expected_lst = [1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {'item1': 1}]
    assert deser_lst == expected_lst


def test_load() -> None:
    file_name = "tomlfile.txt"
    deser_lst = TomlSerializer.load(file_name)
    expected_lst = [1, 2, "Hello", 'world', 3.14, ('tuple1', 2), {'item1': 1}]
    assert deser_lst == expected_lst
