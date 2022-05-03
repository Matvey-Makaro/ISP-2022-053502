from serializers.serializer import Serializer
from serializers.intermediate_format_serializer import IntermediateFormatSerializer
import tomli
import tomli_w


class TomlSerializer(Serializer):
    @staticmethod
    def dumps(obj) -> str:
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        return tomli_w.dumps(form)

    @staticmethod
    def dump(obj, file: str) -> None:
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        with open(file, 'w') as f:
            f.write(tomli_w.dumps(form))

    @staticmethod
    def loads(serialized_obj: str):
        form = tomli.loads(serialized_obj)
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)

    @staticmethod
    def load(file: str):
        ser_obj = ""
        with open(file, "r") as f:
            for line in f:
                ser_obj += line
            form = tomli.loads(ser_obj)
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)
