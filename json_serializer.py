from serializer import Serializer
from intermediate_format_serializer import IntermediateFormatSerializer
from parser import JsonParser


class JsonSerializer(Serializer):
    def dumps(self, obj) -> str:
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        return JsonParser.serialize_json(form)

    def dump(self, obj, file: str) -> None:
        form = IntermediateFormatSerializer.obj_to_intermediate_format(obj)
        with open(file, 'w') as f:
            f.write(JsonParser.serialize_json(form))

    def loads(self, serialized_obj: str):
        form = JsonParser.deserialize_json(serialized_obj)
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)

    def load(self, file: str):
        with open(file, "r") as f:
            form = JsonParser.deserialize_json(f.readline())
        return IntermediateFormatSerializer.intermediate_format_to_obj(form)
