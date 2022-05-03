from serializers.serializer import Serializer
from serializers.intermediate_format_serializer import IntermediateFormatSerializer
import yaml


class YamlSerializer(Serializer):
    @staticmethod
    def dumps(obj) -> str:
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        return yaml.dump(form)

    @staticmethod
    def dump(obj, file: str) -> None:
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        with open(file, 'w') as f:
            f.write(yaml.dump(form))

    @staticmethod
    def loads(serialized_obj: str):
        form = yaml.load(serialized_obj, Loader=yaml.Loader)
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)

    @staticmethod
    def load(file: str):
        ser_obj = ""
        with open(file, "r") as f:
            for line in f:
                ser_obj += line
            form = yaml.load(ser_obj, Loader=yaml.Loader)
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)
