"""Contains a class InputDataScanner"""


class InputDataScanner:
    """Can scan text and two numbers N and K, and provide access to this data.

    Contains methods:
    scan(self) -- scan text and two numbers N and K
    scan_text(self) -- scan text
    scan_k -- scan K
    scan_n -- scan N.

    Contains properties: text, K, N.
    """
    def __init__(self) -> None:
        """Initializes text N and K with default values."""
        self._text = ""
        self._K = 0
        self._N = 0

    def scan(self) -> None:
        """Scan text and two numbers n and k.
        May call exit() if non-integer numbers are entered for N or K, or if the number is non-positive.
        Return None."""
        self.scan_text()
        answer = input("Do you want to enter N and K?(Y/n)")
        if answer == "Y" or answer == "y":
            self.scan_k()
            self.scan_n()
        else:
            self._K = 10
            self._N = 4

    def scan_text(self) -> None:
        """Scan text from standard input.
        Return None."""
        self._text = input("Enter text: ")
        while len(self._text) == 0:
            print("Error! Empty text.")
            self._text = input("Try again: ")

    def scan_k(self) -> None:
        """Scan integer k.
        May call exit() if non-integer number is entered or if the number is non-positive.
        Return None."""
        try:
            self._K = int(input("Enter K: "))
            if self._K <= 0:
                raise ValueError
        except ValueError:
            print("Incorrect input!")
            exit()

    def scan_n(self) -> None:
        """Scan integer n.
        May call exit() if non-integer number is entered or if the number is non-positive.
        Return None."""
        try:
            self._N = int(input("Enter N: "))
            if self._N <= 0:
                raise ValueError
        except ValueError:
            print("Incorrect input!")
            exit()

    @property
    def text(self) -> str:
        """Return text."""
        return self._text

    @property
    def k(self) -> int:
        """Return K."""
        return self._K

    @property
    def n(self) -> int:
        """Return N."""
        return self._N
