class StatisticsCounter:
    def __init__(self, text, k=10, n=4):
        self.text = text
        self.K = k
        self.N = n
        self.words = []
        self.average_number_of_words_in_sentence = 0
        self.median_number_of_words_in_sentence = 0
        self.number_of_each_word = dict()
        self.top_ngrams = dict()
        self.calculate_statistics()

    def set_text(self, text):
        self.text = text

    def set_k(self, k):
        self.K = k

    def set_n(self, n):
        self.N = n

    def get_k(self) -> int:
        return self.K

    def get_n(self) -> int:
        return self.N

    def get_num_of_each_word(self) -> dict:
        return self.number_of_each_word

    def get_average_number_of_words_in_sentence(self) -> float:
        return float(self.average_number_of_words_in_sentence)

    def get_median_number_of_words_in_sentence(self) -> float:
        return float(self.median_number_of_words_in_sentence)

    def get_top_ngrams(self) -> dict:
        return self.top_ngrams

    def calculate_statistics(self):
        self.text_refactoring()
        self.split_text_into_words()
        self.calculate_average_number_of_words_in_sentence()
        self.calculate_median_number_of_words_in_sentence()
        self.count_number_of_each_word()
        self.calculate_top_ngrams()

    def text_refactoring(self):
        self.text = self.text.strip()
        self.text = self.text.lower()
        self.punctuation_refactoring()

    def punctuation_refactoring(self):
        self.text = self.text.replace(",", "")
        self.text = self.text.replace(";", "")
        self.text = self.text.replace(":", "")
        self.text = self.text.replace('-', "")
        self.text = self.text.replace("'", "")
        self.text = self.text.replace('"', '')
        self.text = self.text.replace("(", "")
        self.text = self.text.replace(")", "")
        self.text = self.text.replace("[", "")
        self.text = self.text.replace("]", "")
        self.text = self.text.replace("{", "")
        self.text = self.text.replace("}", "")
        self.text = self.text.replace("...", ".")
        self.text = self.text.replace("!", ".")
        self.text = self.text.replace("?", ".")

    def split_text_into_words(self):
        sentences = list(filter(lambda s: len(s) != 0, self.text.split(".")))
        for s in sentences:
            self.words.append(list(filter(lambda x: len(x) != 0, s.split())))

    def calculate_average_number_of_words_in_sentence(self):
        num_of_words = 0
        for s in self.words:
            num_of_words += len(s)
        self.average_number_of_words_in_sentence = num_of_words / len(self.words)

    def calculate_median_number_of_words_in_sentence(self):
        num_of_words_in_sentence = []
        for s in self.words:
            num_of_words_in_sentence.append(len(s))
        num_of_words_in_sentence.sort()
        if len(num_of_words_in_sentence) % 2 == 0:
            mid_index = int(len(num_of_words_in_sentence) / 2)
            self.median_number_of_words_in_sentence = (num_of_words_in_sentence[mid_index - 1] +
                                                       num_of_words_in_sentence[mid_index]) / 2
        else:
            min_index = int((len(num_of_words_in_sentence) - 1) / 2)
            self.median_number_of_words_in_sentence = num_of_words_in_sentence[min_index]

    def count_number_of_each_word(self):
        for s in self.words:
            for w in s:
                self.number_of_each_word[w] = self.number_of_each_word.get(w, 0) + 1

    def calculate_top_ngrams(self):
        ngrams = self.calculate_ngrams()
        sorted_keys = sorted(ngrams, key=ngrams.get, reverse=True)
        top_size = self.K
        if top_size > len(sorted_keys):
            top_size = len(sorted_keys)

        for i in range(0, top_size):
            self.top_ngrams[sorted_keys[i]] = ngrams[sorted_keys[i]]

    def calculate_ngrams(self) -> dict:
        ngrams = dict()
        for s in self.words:
            for w in s:
                self.add_ngrams(w, ngrams)
        return ngrams

    def add_ngrams(self, word, ngrams):
        for i in range(0, len(word) - self.N + 1):
            ngram = word[i: i + self.N]
            ngrams[ngram] = ngrams.get(ngram, 0) + 1
