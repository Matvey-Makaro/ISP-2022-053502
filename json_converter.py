JSON_WHITESPACE = [' ', '\t', '\b', '\n', '\r']


class JsonConverter:
    @staticmethod
    def _parse_list(tokens, index):
        json_array = []

        t = tokens[index]
        if t == ']':
            return json_array, index + 1

        while index < len(tokens):
            json, index = JsonConverter._parse(tokens, index)
            json_array.append(json)

            if index >= len(tokens):
                break

            t = tokens[index]
            if t == ']':
                return json_array, index + 1
            else:
                index += 1

    @staticmethod
    def _parse_dict(tokens, index):
        json_object = {}

        while index < len(tokens):
            key = tokens[index]
            if type(key) == str:
                index += 1

            value, index = JsonConverter._parse(tokens, index + 1)

            if index >= len(tokens):
                break

            json_object[key] = value

            t = tokens[index]
            if t == '}':
                return json_object, index + 1

            index += 1

    @staticmethod
    def _parse(tokens, index=0):
        index = index

        t = tokens[index]

        if t == '{':
            if tokens[index + 1] == '}':
                return {}, index + 2
            return JsonConverter._parse_dict(tokens, index + 1)
        if t == '[':
            return JsonConverter._parse_list(tokens, index + 1)

        return t, index + 1

    @staticmethod
    def _token_split_string(string, cur_index):
        if string[cur_index] == '"':
            cur_index += 1
        else:
            return None, cur_index

        result = ''

        i = cur_index

        while i < len(string):
            if i < len(string) - 1 and string[i] == '\\' and string[i + 1] == '"':
                result += string[i + 1]
                i += 1
            elif string[i] == '"':
                return result, i + 1
            else:
                result += string[i]
            i += 1

        raise SyntaxError('Expected end of string quote')

    @staticmethod
    def _token_split_number(string, cur_index):
        result = ''

        i = cur_index

        while i < len(string) and string[i] in [str(digit) for digit in range(0, 10)] + ['-', 'e', '.']:
            result += string[i]
            i += 1

        try:
            if '.' in result:
                return float(result), i

            return int(result), i
        except IndentationError:
            return None, cur_index
        except ValueError:
            return None, cur_index

    @staticmethod
    def _token_split_bool(string, cur_index):
        a, b = JsonConverter._token_split_by(string, cur_index, 'true', True)
        if b is not None:
            return a, b

        a, b = JsonConverter._token_split_by(string, cur_index, 'false', False)
        if b is not None:
            return a, b

        return None, cur_index

    @staticmethod
    def _token_split_null(string, cur_index):
        a, b = JsonConverter._token_split_by(string, cur_index, 'null', True)
        if b is not None:
            return a, b

        return None, cur_index

    @staticmethod
    def _token_split_by(string, cur_index, flag, res):
        if len(string) - cur_index + 1 >= len(flag):
            i = cur_index
            j = 0

            while j < len(flag) and string[i] == flag[j]:
                i += 1
                j += 1

            if j == len(flag):
                return res, i

        return None, None

    @staticmethod
    def _token_split(string):
        tokens = []

        i = 0

        while i < len(string):
            result, i = JsonConverter._token_split_string(string, i)
            if result is not None:
                tokens.append(result)
                continue

            result, i = JsonConverter._token_split_number(string, i)
            if result is not None:
                tokens.append(result)
                continue

            result, i = JsonConverter._token_split_bool(string, i)
            if result is not None:
                tokens.append(result)
                continue

            result, i = JsonConverter._token_split_null(string, i)
            if result is not None:
                tokens.append(None)
                continue

            if string[i] in JSON_WHITESPACE:
                i += 1
                continue
            elif string[i] in (',', ':', '[', ']', '{', '}'):
                tokens.append(string[i])
                i += 1
                continue

        return tokens

    @staticmethod
    def from_json(string):
        tokens = JsonConverter._token_split(string)
        # print(f"Tokens: {tokens}")
        # print(f"open breackets: {tokens.count('{')}")
        # print(f"close: {tokens.count('}')}")
        # print(f"open:{tokens.count('[')}")
        # print(f"close: {tokens.count(']')}")
        result = JsonConverter._parse(tokens)[0]
        return result

    @staticmethod
    def to_json(obj):
        if type(obj) == dict:
            result = '{'

            for i, (key, val) in enumerate(obj.items()):
                key = key.replace('"', '\\"')
                result += f'"{key}": {JsonConverter.to_json(val)}'

                if i < len(obj) - 1:
                    result += ', '
                else:
                    result += '}'
            if result[-1] == '{':
                result += '}'
            return result
        elif type(obj) == list:
            if len(obj) == 0:
                return '[]'

            result = '['

            for i, val in enumerate(obj):
                result += JsonConverter.to_json(val)

                if i < len(obj) - 1:
                    result += ', '
                else:
                    result += ']'

            return result
        elif type(obj) == str:
            obj = obj.replace('"', '\\"')
            return f'"{obj}"'
        elif type(obj) == bool:
            return 'true' if obj else 'false'
        elif obj is None:
            return 'null'
        elif type(obj).__name__ in ('bool', 'complex', 'int', 'str', 'NoneType', 'float', 'bytes'):
            return str(obj)






#
# @staticmethod
#     def _parse_list(tokens, index):
#         json_array = []
#
#         t = tokens[index]
#         if t == ']':
#             return json_array, index + 1
#
#         while index < len(tokens):
#             json, index = _parse(tokens, index)
#             json_array.append(json)
#
#             if index >= len(tokens):
#                 break
#
#             t = tokens[index]
#             if t == ']':
#                 return json_array, index + 1
#             else:
#                 index += 1
#
#     @staticmethod
#     def _parse_dict(tokens, index):
#         json_object = {}
#
#         while index < len(tokens):
#             key = tokens[index]
#             if type(key) == str:
#                 index += 1
#
#             value, index = _parse(tokens, index + 1)
#
#             if index >= len(tokens):
#                 break
#
#             json_object[key] = value
#
#             t = tokens[index]
#             if t == '}':
#                 return json_object, index + 1
#
#             index += 1
#
#     @staticmethod
#     def _parse(tokens, index=0):
#         index = index
#
#         t = tokens[index]
#
#         if t == '{':
#             if tokens[index + 1] == '}':
#                 return {}, index + 2
#             return _parse_dict(tokens, index + 1)
#         if t == '[':
#             return _parse_list(tokens, index + 1)
#
#         return t, index + 1
#
#     @staticmethod
#     def _token_split_string(string, cur_index):
#         if string[cur_index] == '"':
#             cur_index += 1
#         else:
#             return None, cur_index
#
#         result = ''
#
#         i = cur_index
#
#         while i < len(string):
#             if i < len(string) - 1 and string[i] == '\\' and string[i + 1] == '"':
#                 result += string[i + 1]
#                 i += 1
#             elif string[i] == '"':
#                 return result, i + 1
#             else:
#                 result += string[i]
#             i += 1
#
#         raise SyntaxError('Expected end of string quote')
#
#     @staticmethod
#     def _token_split_number(string, cur_index):
#         result = ''
#
#         i = cur_index
#
#         while i < len(string) and string[i] in [str(digit) for digit in range(0, 10)] + ['-', 'e', '.']:
#             result += string[i]
#             i += 1
#
#         try:
#             if '.' in result:
#                 return float(result), i
#
#             return int(result), i
#         except IndentationError:
#             return None, cur_index
#         except ValueError:
#             return None, cur_index
#
#     @staticmethod
#     def _token_split_bool(string, cur_index):
#         a, b = _token_split_by(string, cur_index, 'true', True)
#         if b is not None:
#             return a, b
#
#         a, b = _token_split_by(string, cur_index, 'false', False)
#         if b is not None:
#             return a, b
#
#         return None, cur_index
#
#     @staticmethod
#     def _token_split_null(string, cur_index):
#         a, b = _token_split_by(string, cur_index, 'null', True)
#         if b is not None:
#             return a, b
#
#         return None, cur_index
#
#     @staticmethod
#     def _token_split_by(string, cur_index, flag, res):
#         if len(string) - cur_index + 1 >= len(flag):
#             i = cur_index
#             j = 0
#
#             while j < len(flag) and string[i] == flag[j]:
#                 i += 1
#                 j += 1
#
#             if j == len(flag):
#                 return res, i
#
#         return None, None
#
#     @staticmethod
#     def _token_split(string):
#         tokens = []
#
#         i = 0
#
#         while i < len(string):
#             result, i = _token_split_string(string, i)
#             if result is not None:
#                 tokens.append(result)
#                 continue
#
#             result, i = _token_split_number(string, i)
#             if result is not None:
#                 tokens.append(result)
#                 continue
#
#             result, i = _token_split_bool(string, i)
#             if result is not None:
#                 tokens.append(result)
#                 continue
#
#             result, i = _token_split_null(string, i)
#             if result is not None:
#                 tokens.append(None)
#                 continue
#
#             if string[i] in JSON_WHITESPACE:
#                 i += 1
#                 continue
#             elif string[i] in (',', ':', '[', ']', '{', '}'):
#                 tokens.append(string[i])
#                 i += 1
#                 continue
#
#         return tokens
#
#     @staticmethod
#     def deserialize_json(string):
#         tokens = _token_split(string)
#         print(f"Tokens: {tokens}")
#         print(f"open breackets: {tokens.count('{')}")
#         print(f"close: {tokens.count('}')}")
#         print(f"open:{tokens.count('[')}")
#         print(f"close: {tokens.count(']')}")
#         result = _parse(tokens)[0]
#         return result
#
#     @staticmethod
#     def serialize_json(obj):
#         if type(obj) == dict:
#             result = '{'
#
#             for i, (key, val) in enumerate(obj.items()):
#                 key = key.replace('"', '\\"')
#                 result += f'"{key}": {serialize_json(val)}'
#
#                 if i < len(obj) - 1:
#                     result += ', '
#                 else:
#                     result += '}'
#             if result[-1] == '{':
#                 result += '}'
#             return result
#         elif type(obj) == list:
#             if len(obj) == 0:
#                 return '[]'
#
#             result = '['
#
#             for i, val in enumerate(obj):
#                 result += serialize_json(val)
#
#                 if i < len(obj) - 1:
#                     result += ', '
#                 else:
#                     result += ']'
#
#             return result
#         elif type(obj) == str:
#             obj = obj.replace('"', '\\"')
#             return f'"{obj}"'
#         elif type(obj) == bool:
#             return 'true' if obj else 'false'
#         elif obj is None:
#             return 'null'
#         elif type(obj).__name__ in ('bool', 'complex', 'int', 'str', 'NoneType', 'float', 'bytes'):
#             return str(obj)




# from itertools import chain
# import re
#
#
# def sequence(*funcs):
#     if len(funcs) == 0:
#         def result(src):
#             yield (), src
#
#         return result
#
#     def result(src):
#         for arg1, src in funcs[0](src):
#             for others, src in sequence(*funcs[1:])(src):
#                 yield (arg1,) + others, src
#
#     return result
#
#
# number_regex = re.compile(r"(-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?)\s*(.*)", re.DOTALL)
#
#
# def parse_number(src):
#     match = number_regex.match(src)
#     if match is not None:
#         number, src = match.groups()
#         yield eval(number), src
#
#
# string_regex = re.compile(r"('(?:[^\\']|\\['\\/bfnrt]|\\u[0-9a-fA-F]{4})*?')\s*(.*)", re.DOTALL)
#
#
# def parse_string(src):
#     match = string_regex.match(src)
#     if match is not None:
#         string, src = match.groups()
#         yield eval(string), src
#
#
# def parse_word(word, value=None):
#     l = len(word)
#
#     def result(src):
#         if src.startswith(word):
#             yield value, src[l:].lstrip()
#
#     result.__name__ = "parse_%s" % word
#     return result
#
#
# parse_true = parse_word("true", True)
# parse_false = parse_word("false", False)
# parse_null = parse_word("null", None)
#
#
# def parse_value(src):
#     for match in chain(
#             parse_string(src),
#             parse_number(src),
#             parse_array(src),
#             parse_object(src),
#             parse_true(src),
#             parse_false(src),
#             parse_null(src),
#     ):
#         yield match
#         return
#
#
# parse_left_square_bracket = parse_word("[")
# parse_right_square_bracket = parse_word("]")
# parse_empty_array = sequence(parse_left_square_bracket, parse_right_square_bracket)
#
#
# def parse_array(src):
#     for _, src in parse_empty_array(src):
#         yield [], src
#         return
#
#     for (_, items, _), src in sequence(
#             parse_left_square_bracket,
#             parse_comma_separated_values,
#             parse_right_square_bracket,
#     )(src):
#         yield items, src
#
#
# parse_comma = parse_word(",")
#
#
# def parse_comma_separated_values(src):
#     for (value, _, values), src in sequence(
#             parse_value,
#             parse_comma,
#             parse_comma_separated_values
#     )(src):
#         yield [value] + values, src
#         return
#
#     for value, src in parse_value(src):
#         yield [value], src
#
#
# parse_left_curly_bracket = parse_word("{")
# parse_right_curly_bracket = parse_word("}")
# parse_empty_object = sequence(parse_left_curly_bracket, parse_right_curly_bracket)
#
#
# def parse_object(src):
#     for _, src in parse_empty_object(src):
#         yield {}, src
#         return
#     for (_, items, _), src in sequence(
#             parse_left_curly_bracket,
#             parse_comma_separated_keyvalues,
#             parse_right_curly_bracket,
#     )(src):
#         yield items, src
#
#
# parse_colon = parse_word(":")
#
#
# def parse_keyvalue(src):
#     for (key, _, value), src in sequence(
#             parse_string,
#             parse_colon,
#             parse_value
#     )(src):
#         yield {key: value}, src
#
#
# def parse_comma_separated_keyvalues(src):
#     for (keyvalue, _, keyvalues), src in sequence(
#             parse_keyvalue,
#             parse_comma,
#             parse_comma_separated_keyvalues,
#     )(src):
#         keyvalue.update(keyvalues)
#         yield keyvalue, src
#         return
#
#     for keyvalue, src in parse_keyvalue(src):
#         yield keyvalue, src
#
#
# def parse(s):
#     s = s.strip()
#     match = list(parse_value(s))
#     if len(match) != 1:
#         raise ValueError("not a valid JSON string")
#     result, src = match[0]
#     if src.strip():
#         raise ValueError("not a valid JSON string")
#     return result
