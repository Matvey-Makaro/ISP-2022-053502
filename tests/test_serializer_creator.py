from serializer_creator import SerializerCreator
from json_serializer import JsonSerializer
from toml_serializer import TomlSerializer
from yaml_serializer import YamlSerializer


def test_create_serializer() -> None:
    json_serializer = SerializerCreator.create("json")
    assert json_serializer == JsonSerializer
    yaml_serializer = SerializerCreator.create("yaml")
    assert yaml_serializer == YamlSerializer
    toml_serializer = SerializerCreator.create("toml")
    assert toml_serializer == TomlSerializer
