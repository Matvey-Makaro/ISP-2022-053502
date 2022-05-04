"""
A module that allows you to convert json, yaml or toml file into a json, yaml or toml file.
"""

from argparse import ArgumentParser
from configparser import ConfigParser
from serializers.serializer_creator import SerializerCreator


def convert_file(input_file_name: str, input_format: str, output_format: str) -> None:
    """
    Convert file with "input_file_name" name in format "input format" to file with name "input_file_name.output_format
    in format output_format."
    :param input_file_name: str
    :param input_format: str
    :param output_format: str
    :return: None
    """
    if input_format == output_format:
        return None
    output_file_name = input_file_name + "." + output_format
    try:
        input_serializer = SerializerCreator.create(input_format)
        output_serializer = SerializerCreator.create(output_format)
    except ValueError:
        print("No serializers for " + input_format + " or " + output_format)
        exit(1)
    output_serializer.dump(input_serializer.load(input_file_name), output_file_name)


def get_args():
    """Gets arguments from the command line for further parsin."""
    parser = ArgumentParser(description="JSON/TOML/YAML converter.")
    parser.add_argument("-i", "--input", type=str, help="input file name")
    parser.add_argument("--input-format", type=str, help="input file format")
    parser.add_argument("--output-format", type=str, help="output file format")
    parser.add_argument("-c", "--config-file", type=str, help="config file")
    return parser.parse_args()


def parse_config_file(config_file_name: str) -> (str, str, str):
    """
    Extracts from the configuration file and returns arguments needed to convert files such as input_file_name,
    input_format, output_format.
    :param config_file_name: str
    :return: (str, str, str)
    """
    config_parser = ConfigParser()
    config_parser.read(config_file_name)
    input_file_name = config_parser.get("Config", "input")
    input_format = config_parser.get("Config", "input_format")
    output_format = config_parser.get("Config", "output_format")
    return input_file_name, input_format, output_format


def parse_args(args) -> (str, str, str):
    """
    Extracts from command line arguments and returns arguments needed to convert files such as input_file_name,
    input_format, output_format.
    :param args:
    :return: (str, str, str)
    """
    if args.input is None:
        print("You must specify the input file name.")
        exit(1)
    if args.input_format is None:
        print("You must specify the input format.")
        exit(1)
    if args.output_format is None:
        print("You must specify the output format.")
        exit(1)
    input_file_name = args.input
    input_format = args.input_format
    output_format = args.output_format
    return input_file_name, input_format, output_format


def main() -> None:
    """Main function."""
    args = get_args()

    if args.config_file is not None:
        config_file_name = args.config_file
        input_file_name, input_format, output_format = parse_config_file(config_file_name)
    else:
        input_file_name, input_format, output_format = parse_args(args)
    convert_file(input_file_name, input_format, output_format)


if __name__ == '__main__':
    main()
