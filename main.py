from statistics_counter import StatisticsCounter
from input_data_scanner import InputDataScanner
from statistics_printer import StatisticsPrinter


if __name__ == '__main__':
    scanner = InputDataScanner()
    scanner.scan()
    stat_counter = StatisticsCounter(scanner.get_text(), scanner.get_k(), scanner.get_n())
    printer = StatisticsPrinter(stat_counter)
    printer.print()
