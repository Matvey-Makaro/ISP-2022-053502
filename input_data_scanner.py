class InputDataScanner:
    def __init__(self) -> None:
        self._text = ""
        self._K = 0
        self._N = 0

    def scan(self) -> None:
        self.scan_text()
        answer = input("Do you want to enter N and K?(Y/n)")
        if answer == "Y" or answer == "y":
            self.scan_k()
            self.scan_n()
        else:
            self._K = 10
            self._N = 4

    def scan_text(self) -> None:
        self._text = input("Enter text: ")
        while len(self._text) == 0:
            print("Error! Empty text.")
            self._text = input("Try again: ")

    def scan_k(self) -> None:
        try:
            self._K = int(input("Enter K: "))
            if self._K <= 0:
                raise ValueError
        except ValueError:
            print("Incorrect input!")
            exit()

    def scan_n(self) -> None:
        try:
            self._N = int(input("Enter N: "))
            if self._N <= 0:
                raise ValueError
        except ValueError:
            print("Incorrect input!")
            exit()

    @property
    def text(self) -> str:
        return self._text

    @property
    def k(self) -> int:
        return self._K

    @property
    def n(self) -> int:
        return self._N
