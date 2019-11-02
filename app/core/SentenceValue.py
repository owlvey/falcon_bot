class SentenceValue:

    def __init__(self):
        self.words = list()

    def parse(self, arg: str):
        self.words = arg.split(" ")


