from statistics_counter import StatisticsCounter
from input_data_scanner import InputDataScanner

if __name__ == '__main__':
    scanner = InputDataScanner()
    scanner.scan()
    stat_counter = StatisticsCounter(scanner.get_text(), scanner.get_k(), scanner.get_n())
    print(stat_counter.words)
    print(stat_counter.get_num_of_each_word())
    print(stat_counter.get_average_number_of_words_in_sentence())
    print(stat_counter.get_median_number_of_words_in_sentence())
    print(stat_counter.get_top_ngrams())
