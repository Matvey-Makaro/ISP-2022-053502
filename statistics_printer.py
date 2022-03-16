"""Contains a class StatisticsPrinter.
From statistics_counter import StatisticsCounter."""
from statistics_counter import StatisticsCounter


class StatisticsPrinter:
    """Receives an object of type StatisticsCounter and prints statistical information of the text.

    Contains methods:
    print(self) -- prints statistical information of the text.
    """
    def __init__(self, statistics_counter: StatisticsCounter) -> None:
        """Receives an object of type StatisticsCounter and
        Return None."""
        self.statistics_counter = statistics_counter

    def print(self) -> None:
        """Prints statistical information of the text.
        Return None."""
        print(f"Number of each word: {self.statistics_counter.number_of_each_word}")
        print(f"Average number of words in sentence: "
              f"{self.statistics_counter.average_number_of_words_in_sentence}")
        print(f"Median number of words in sentence: "
              f"{self.statistics_counter.median_number_of_words_in_sentence}")
        print(f"Top {self.statistics_counter.k} most frequently repeated letter "
              f"{self.statistics_counter.n}-grams: {self.statistics_counter.top_ngrams}")
