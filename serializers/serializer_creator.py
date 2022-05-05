"""The module that provides class SerializerCreator to create serializers of different formats."""
from serializers.json_serializer import JsonSerializer
from serializers.serializer import Serializer
from serializers.toml_serializer import TomlSerializer
from serializers.yaml_serializer import YamlSerializer


class SerializerCreator:
    """Class with main method create to create serializers of different formats."""
    @staticmethod
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
