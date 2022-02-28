class StatisticsCounter:
    def __init__(self, text, k=10, n=4):
        self.text = text
        self.K = k
        self.N = n

    def set_text(self, text):
        self.text = text

    def set_k(self, k):
        self.K = k

    def set_n(self, n):
        self.N = n

    def calculate_statistics(self):
        self.punctuation_refactoring()

    def punctuation_refactoring(self):
        pass

    def split_text_into_sentences(self):
        pass

    def calculate_average_number_of_words_in_sentence(self):
        pass

    def calculate_median_number_of_words_in_sentence(self):
        pass

    def replace_dots_with_spaces(self):
        pass

    def split_sentences_into_words(self):
        pass

    def count_number_of_each_word(self):
        pass

    def calculate_top_ngram(self):
        pass


if __name__ == '__main__':
    string = input("Enter text: ")
