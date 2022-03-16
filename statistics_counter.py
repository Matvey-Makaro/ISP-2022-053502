"""Contains a class StatisticsCounter"""


class StatisticsCounter:
    """Gets the text, positive numbers N and K.
    Counts the average number of words in a sentence,
    the median number of words in a sentence.
    Counts the number of each word.
    Counts the top K letter N-grams.

    Contains methods:
    calculate_statistics(self) -- сalculate all statistics by text.

    Contains properties:
    text - can set text
    k -- set and get K.
    n -- set and get N.
    number_of_each_word -- get number of each word in the text.
    average_number_of_words_in_sentence -- get average number of words in sentence.
    median_number_of_words_in_sentence -- get median number of words in sentence.
    top_ngrams -- get top K N-grams.
    """
    def __init__(self, text: str, k: int = 10, n: int = 4) -> None:
        """Gets text, K and N. Default: k = 10, n = 4.
        Declares variables: self._text, self._K, self._N, self._words,
        self._average_number_of_words_in_sentence, self._median_number_of_words_in_sentence,
        self._number_of_each_word, self._top_ngrams.
        Return None.
        """
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
        """Gets text. Return None."""
        self._text = text

    text = property(fget=None, fset=_set_text)

    @property
    def k(self, k: int) -> None:
        """Gets K. Return None."""
        self._K = k

    @property
    def n(self, n: int) -> None:
        """Gets N. Return None."""
        self._N = n

    @k.getter
    def k(self) -> int:
        """Return K."""
        return self._K

    @n.getter
    def n(self) -> int:
        """Return N."""
        return self._N

    @property
    def number_of_each_word(self) -> dict:
        """Return number of each word."""
        return self._number_of_each_word

    @property
    def average_number_of_words_in_sentence(self) -> float:
        """Return average number of words in sentence."""
        return float(self._average_number_of_words_in_sentence)

    @property
    def median_number_of_words_in_sentence(self) -> float:
        """Return median number of words in sentence."""
        return float(self._median_number_of_words_in_sentence)

    @property
    def top_ngrams(self) -> dict:
        """Return top K N-grams."""
        return self._top_ngrams

    def calculate_statistics(self) -> None:
        """Calculate all statistics by text. Return None."""
        self._text_refactoring()
        self._split_text_into_words()
        self._calculate_average_number_of_words_in_sentence()
        self._calculate_median_number_of_words_in_sentence()
        self._count_number_of_each_word()
        self._calculate_top_ngrams()

    def _text_refactoring(self) -> None:
        """Removes spaces from the beginning and end of a string. Converts all text to lower case.
        Replaces characters that end sentences with a dot.
        Removes all punctuation marks except for the dot.
        Return None.
        """
        self._text = self._text.strip()
        self._text = self._text.lower()
        self._punctuation_refactoring()

    def _punctuation_refactoring(self) -> None:
        """Replaces characters that end sentences with a dot.
        Removes all punctuation marks except for the dot.
        Return None.
        """
        self._text = self._text.replace(",", "").replace(";", "").replace(":", "").replace('-', "").replace("'", "").\
            replace('"', '').replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").\
            replace("}", "").replace("...", ".").replace("!", ".").replace("?", ".")

    def _split_text_into_words(self) -> None:
        """Separates text into words. Return None."""
        sentences = list(filter(lambda x: len(x) != 0, self._text.split(".")))
        for s in sentences:
            self._words.append(list(filter(lambda x: len(x) != 0, s.split())))

    def _calculate_average_number_of_words_in_sentence(self) -> None:
        """Calculate average number of words in sentence. Return None."""
        num_of_words = 0
        for s in self._words:
            num_of_words += len(s)
        self._average_number_of_words_in_sentence = num_of_words / len(self._words)

    def _calculate_median_number_of_words_in_sentence(self) -> None:
        """Calculate median number of words in sentence. Return None."""
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
        """Count number of each word. Return None."""
        for s in self._words:
            for w in s:
                self._number_of_each_word[w] = self._number_of_each_word.get(w, 0) + 1

    def _calculate_top_ngrams(self) -> None:
        """Calculate top K N-grams. Return None"""
        ngrams = self._calculate_ngrams()
        sorted_keys = sorted(ngrams, key=ngrams.get, reverse=True)
        top_size = self._K
        if top_size > len(sorted_keys):
            top_size = len(sorted_keys)

        for i in range(0, top_size):
            self._top_ngrams[sorted_keys[i]] = ngrams[sorted_keys[i]]

    def _calculate_ngrams(self) -> dict:
        """Calculate all N-grams.
        Return dict -- N-grams
        """
        ngrams = dict()
        for s in self._words:
            for w in s:
                self._add_ngrams(w, ngrams)
        return ngrams

    def _add_ngrams(self, word: str, ngrams: dict) -> None:
        """Add ngram to dict ngrams. Return None."""
        for i in range(0, len(word) - self._N + 1):
            ngram = word[i: i + self._N]
            ngrams[ngram] = ngrams.get(ngram, 0) + 1
