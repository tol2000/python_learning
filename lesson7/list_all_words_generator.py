class ListAllWords:

    def __init__(self, alphabet, min_word_len, max_word_len):
        self.alphabet = alphabet
        self.min_word_len = min_word_len
        self.max_word_len = max_word_len

        self.max_index = len(self.alphabet) - 1
        self.num_count = self.min_word_len
        self.word = ''

    def __iter__(self):
        return self

    def __next__(self):
        if self.num_count <= self.max_word_len:
            pass
            self.num_count += 1
            return self.word
        else:
            raise StopIteration

    def pos_to_symbols(self, inp_list: list):
        return [self.alphabet[x] for x in inp_list]


# it = ListAllWords(stop=3, start=1)
# for i in list(it):
#     print(i)
