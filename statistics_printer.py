class StatisticsPrinter:
    def __init__(self, statistics_counter):
        self.statistics_counter = statistics_counter

    def print(self):
        print(f"Number of each word: {self.statistics_counter.get_num_of_each_word()}")
        print(f"Average number of words in sentence: "
              f"{self.statistics_counter.get_average_number_of_words_in_sentence()}")
        print(f"Median number of words in sentence: "
              f"{self.statistics_counter.get_median_number_of_words_in_sentence()}")
        print(f"Top {self.statistics_counter.get_k()} most frequently repeated letter "
              f"{self.statistics_counter.get_n()}-grams: {self.statistics_counter.get_top_ngrams()}")
