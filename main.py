"""Contain function main().
Import StatisticsCounter from statistics_counter.
Import InputDataScanner from input_data_scanner.
Import StatisticsPrinter from statistics_printer."""

from statistics_counter import StatisticsCounter
from input_data_scanner import InputDataScanner
from statistics_printer import StatisticsPrinter


def main() -> None:
    """"Receives text and two numbers as input,
    calculates text statistics and displays
    statistics on the screen
    """
    scanner = InputDataScanner()
    scanner.scan()
    stat_counter = StatisticsCounter(scanner.text, scanner.k, scanner.n)
    printer = StatisticsPrinter(stat_counter)
    printer.print()


if __name__ == '__main__':
    main()
