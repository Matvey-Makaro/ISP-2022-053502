from serializer import Serializer
from intermediate_format_serializer import IntermediateFormatSerializer
from json_converter import JsonConverter


class JsonSerializer(Serializer):
    @staticmethod
    def dumps(obj) -> str:
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        return JsonConverter.to_json(form)

    @staticmethod
    def dump(obj, file: str) -> None:
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        with open(file, 'w') as f:
            f.write(JsonConverter.to_json(form))

    @staticmethod
    def loads(serialized_obj: str):
        form = JsonConverter.from_json(serialized_obj)
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)

    @staticmethod
    def load(file: str):
        with open(file, "r") as f:
            form = JsonConverter.from_json(f.readline())
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)
