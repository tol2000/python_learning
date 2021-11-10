class ListAllWords:

    def __init__(self, alphabet, min_word_len, max_word_len):
        self.alphabet = alphabet
        self.min_word_len = min_word_len
        self.max_word_len = max_word_len

        self.max_index = len(self.alphabet) - 1
        # increment will be at begin )
        self.num_count = self.min_word_len - 1
        self.word = ''
        self.zero_index = None
        self.num = None
        # for internal cycle within num with concrete length
        self.new_num_len = True
        self.shift_enough = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.num_count <= self.max_word_len:
            if self.new_num_len:
                self.new_num_len = False
                self.num_count += 1
                self.zero_index = self.num_count - 1
                self.num = [0] * self.num_count
                self.word = self.pos_to_symbols(self.num)
            else:
                self.shift_enough = False
                while not self.shift_enough:
                    self.inc_and_shift()
                    if not self.shift_enough:
                        self.word = self.pos_to_symbols(self.num)
                    else:
                        self.new_num_len = True

            return self.word
        else:
            raise StopIteration

    def pos_to_symbols(self, inp_list: list):
        return [self.alphabet[x] for x in inp_list]

    def inc_and_shift(self):
        if self.num[self.zero_index] < self.max_index:
            self.num[self.zero_index] += 1
        else:
            # if we will increment number successfully then we reset enough to False
            self.shift_enough = True
            # instead of enough we will raise StopIteration
            for i in range(self.zero_index - 1, -1, -1):
                self.num[i + 1] = 0
                if self.num[i] < self.max_index:
                    self.num[i] += 1
                    self.shift_enough = False
                    break

# it = ListAllWords(stop=3, start=1)
# for i in list(it):
#     print(i)
