from serializers.serializer import Serializer
from serializers.json_serializer import JsonSerializer
from toml_serializer import TomlSerializer
from yaml_serializer import YamlSerializer


class SerializerCreator:
    def create(serializer_name: str) -> Serializer:
        """Returns particular serializer with received serializer name. (Possible : Json, Yaml, Toml)."""
        serializer_name = serializer_name.lower()

        if serializer_name == "json":
            return JsonSerializer

        elif serializer_name == "yaml":
            return YamlSerializer

        elif serializer_name == "toml":
            return TomlSerializer

        else:
            raise ValueError
