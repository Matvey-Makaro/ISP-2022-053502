from statistics_counter import StatisticsCounter
if __name__ == '__main__':
    text = input("Enter text: ")
    stat_counter = StatisticsCounter(text, 5, 2)
    print(stat_counter.words)
    print(stat_counter.get_num_of_each_word())
    print(stat_counter.get_average_number_of_words_in_sentence())
    print(stat_counter.get_median_number_of_words_in_sentence())
    print(stat_counter.get_top_ngrams())
