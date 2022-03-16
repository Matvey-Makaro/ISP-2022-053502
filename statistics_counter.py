class StatisticsCounter:
    def __init__(self, text: str, k: int = 10, n: int = 4) -> None:
        self._text = text
        self._K = k
        self._N = n
        self._words = []
        self._average_number_of_words_in_sentence = 0
        self._median_number_of_words_in_sentence = 0
        self._number_of_each_word = dict()
        self._top_ngrams = dict()
        self.calculate_statistics()

    def _set_text(self, text: str) -> None:
        self._text = text

    text = property(fget=None, fset=_set_text)

    @property
    def k(self, k: int) -> None:
        self._K = k

    @property
    def n(self, n: int) -> None:
        self._N = n

    @k.getter
    def k(self) -> int:
        return self._K

    @n.getter
    def n(self) -> int:
        return self._N

    @property
    def number_of_each_word(self) -> dict:
        return self._number_of_each_word

    @property
    def average_number_of_words_in_sentence(self) -> float:
        return float(self._average_number_of_words_in_sentence)

    @property
    def median_number_of_words_in_sentence(self) -> float:
        return float(self._median_number_of_words_in_sentence)

    @property
    def top_ngrams(self) -> dict:
        return self._top_ngrams

    def calculate_statistics(self) -> None:
        self._text_refactoring()
        self._split_text_into_words()
        self._calculate_average_number_of_words_in_sentence()
        self._calculate_median_number_of_words_in_sentence()
        self._count_number_of_each_word()
        self._calculate_top_ngrams()

    def _text_refactoring(self) -> None:
        self._text = self._text.strip()
        self._text = self._text.lower()
        self._punctuation_refactoring()

    def _punctuation_refactoring(self) -> None:
        self._text = self._text.replace(",", "").replace(";", "").replace(":", "").replace('-', "").replace("'", "").\
            replace('"', '').replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").\
            replace("}", "").replace("...", ".").replace("!", ".").replace("?", ".")

    def _split_text_into_words(self) -> None:
        sentences = list(filter(lambda x: len(x) != 0, self._text.split(".")))
        for s in sentences:
            self._words.append(list(filter(lambda x: len(x) != 0, s.split())))

    def _calculate_average_number_of_words_in_sentence(self) -> None:
        num_of_words = 0
        for s in self._words:
            num_of_words += len(s)
        self._average_number_of_words_in_sentence = num_of_words / len(self._words)

    def _calculate_median_number_of_words_in_sentence(self) -> None:
        num_of_words_in_sentence = []
        for s in self._words:
            num_of_words_in_sentence.append(len(s))
        num_of_words_in_sentence.sort()
        if len(num_of_words_in_sentence) % 2 == 0:
            mid_index = int(len(num_of_words_in_sentence) / 2)
            self._median_number_of_words_in_sentence = (num_of_words_in_sentence[mid_index - 1] +
                                                        num_of_words_in_sentence[mid_index]) / 2
        else:
            min_index = int((len(num_of_words_in_sentence) - 1) / 2)
            self._median_number_of_words_in_sentence = num_of_words_in_sentence[min_index]

    def _count_number_of_each_word(self) -> None:
        for s in self._words:
            for w in s:
                self._number_of_each_word[w] = self._number_of_each_word.get(w, 0) + 1

    def _calculate_top_ngrams(self) -> None:
        ngrams = self._calculate_ngrams()
        sorted_keys = sorted(ngrams, key=ngrams.get, reverse=True)
        top_size = self._K
        if top_size > len(sorted_keys):
            top_size = len(sorted_keys)

        for i in range(0, top_size):
            self._top_ngrams[sorted_keys[i]] = ngrams[sorted_keys[i]]

    def _calculate_ngrams(self) -> dict:
        ngrams = dict()
        for s in self._words:
            for w in s:
                self._add_ngrams(w, ngrams)
        return ngrams

    def _add_ngrams(self, word: str, ngrams: dict) -> None:
        for i in range(0, len(word) - self._N + 1):
            ngram = word[i: i + self._N]
            ngrams[ngram] = ngrams.get(ngram, 0) + 1
