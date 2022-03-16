from statistics_counter import StatisticsCounter


class StatisticsPrinter:
    def __init__(self, statistics_counter: StatisticsCounter) -> None:
        self.statistics_counter = statistics_counter

    def print(self) -> None:
        print(f"Number of each word: {self.statistics_counter.number_of_each_word}")
        print(f"Average number of words in sentence: "
              f"{self.statistics_counter.average_number_of_words_in_sentence}")
        print(f"Median number of words in sentence: "
              f"{self.statistics_counter.median_number_of_words_in_sentence}")
        print(f"Top {self.statistics_counter.k} most frequently repeated letter "
              f"{self.statistics_counter.n}-grams: {self.statistics_counter.top_ngrams}")
