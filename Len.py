class RealString:

    def __init__(self, word_1, word_2):
        self.word_1 = word_1
        self.word_2 = word_2

    def compare (self, word_1, word_2):
        if len(word_1) > len(word_2):
            print(f"{word_1} > {word_2}")
        elif len(word_1) == len(word_2):
            print(f'{word_2} = {word_1}')
        else:
            print(f"{word_2} > {word_1}")
my_word = RealString("Word", "Chingacbjnsfij")

my_word.compare("Word", "Word")