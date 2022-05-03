"""
Module for tools that allow you to convert a dictionary or array to a json format string and vice versa.
Contains a class JsonConverter.
"""

JSON_WHITESPACE = [' ', '\t', '\b', '\n', '\r']


class JsonConverter:
    """
    Class that allows to convert a dictionary or array to a json format string and vice versa.
    Provides two main methods to_json and from_json.
    """
    @staticmethod
    def _parse_list(tokens: list, index: int) -> (list, int) or None:
        """
        Parse tokens into list starting from index.
        :param tokens: list
        :param index: int
        :return: (list, int) or None
        """
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
    def _parse_dict(tokens: list, index: int) -> (dict, int) or None:
        """
        Parse tokens into dict starting from index.
        :param tokens: list
        :param index: int
        :return: (dict, int) or None
        """
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
    def _parse(tokens: list, index: int = 0) -> (dict or list or bool or complex or int or
                                                 str or None or float or bytes, int):
        """
        Parse tokens into objects starting from index.
        :param tokens: list
        :param index: int
        :return: (dict or list or bool or complex or int or str or None or float or bytes, int)
        """
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
    def _token_split_string(string: str, cur_index: int) -> (str or None, int):
        """
        Searching for a string token in string starting at cur_index.
        :param string: str
        :param cur_index: int
        :return: (str or None, int)
        """
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
    def _token_split_number(string: str, cur_index: int) -> (int or float or None, int):
        """
        Searching for a number token in string starting at cur_index.
        :param string: str
        :param cur_index: int
        :return: (int or float or None, int)
        """
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
    def _token_split_bool(string: str, cur_index: int) -> (bool or None, int):
        """
        Searching for a bool token in string starting at cur_index.
        :param string: str
        :param cur_index: int
        :return: (bool or None, int)
        """
        a, b = JsonConverter._token_split_by(string, cur_index, 'true', True)
        if b is not None:
            return a, b

        a, b = JsonConverter._token_split_by(string, cur_index, 'false', False)
        if b is not None:
            return a, b

        return None, cur_index

    @staticmethod
    def _token_split_null(string: str, cur_index: int) -> (bool or None, int):
        """
        Searching for a null token in string starting at cur_index.
        :param string: str
        :param cur_index: int
        :return: (bool or None, int)
        """
        a, b = JsonConverter._token_split_by(string, cur_index, 'null', True)
        if b is not None:
            return a, b

        return None, cur_index

    @staticmethod
    def _token_split_by(string: str, cur_index: int, flag: str, res: bool) -> (bool or None, int):
        """
        Searching for a flag token in string starting at cur_index.
        :param string: str
        :param cur_index: int
        :param flag: str
        :param res: bool
        :return: (bool, int)
        """
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
    def _token_split(string: str) -> list:
        """
        Splits a string into tokens.
        :param string: str
        :return: list
        """
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
    def from_json(string: str) -> dict or list or bool or complex or int or str or None or float or bytes:
        """
        Convert string in json format to object.
        :param string: str
        :return: dict or bool or complex or int or str or None or float or bytes
        """
        tokens = JsonConverter._token_split(string)
        # print(f"Tokens: {tokens}")
        # print(f"open breackets: {tokens.count('{')}")
        # print(f"close: {tokens.count('}')}")
        # print(f"open:{tokens.count('[')}")
        # print(f"close: {tokens.count(']')}")
        result = JsonConverter._parse(tokens)[0]
        return result

    @staticmethod
    def to_json(obj: dict or bool or complex or int or str or None or float or bytes) -> str:
        """
        Convert object to string in json format.
        :param obj: dict or bool or complex or int or str or None or float or bytes
        :return: str
        """
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
