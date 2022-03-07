class InputDataScanner:
    def __init__(self):
        self.text = ""
        self.K = 0
        self.N = 0

    def scan(self):
        self.scan_text()
        answer = input("Do you want to enter N and K?(Y/n)")
        if answer == "Y" or answer == "y":
            self.scan_k()
            self.scan_n()
        else:
            self.K = 10
            self.N = 4

    def scan_text(self):
        self.text = input("Enter text: ")
        while len(self.text) == 0:
            print("Error! Empty text.")
            self.text = input("Try again: ")

    def scan_k(self):
        try:
            self.K = int(input("Enter K: "))
            if self.K < 0:
                raise ValueError
        except ValueError:
            print("Incorrect input!")
            exit()

    def scan_n(self):
        try:
            self.N = int(input("Enter N: "))
            if self.N < 0:
                raise ValueError
        except ValueError:
            print("Incorrect input!")
            exit()

    def get_text(self) -> str:
        return self.text

    def get_k(self) -> int:
        return self.K

    def get_n(self) -> int:
        return self.N