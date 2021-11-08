from itertools import combinations_with_replacement, combinations

# nums = []
# max_digits = 3
# max_digit_value = 9
#
# for i in range(1, max_digits+1):
#     nums += list(range(0, max_digit_value+1))

# max_len = 3
#
# nums = [0, 1, 2, 3, 4, 5]
#
# for comb in combinations_with_replacement(nums, max_len):
#     print(comb)
#
# print()
#
# for comb in combinations(nums, max_len):
#     print(comb)
#

alphabet = [0, 1]
min_word_len = 1
max_word_len = 3


def list_all_words(alphabet, min_word_len, max_word_len):
    res = []
    len_alphabet = len(alphabet)
    for i in range(1, max_word_len+1):
        for j in range(0, len_alphabet):
            res.append(alphabet[j])
            if max_word_len > 1:
                for add in list_all_words(alphabet, min_word_len, max_word_len-1):
                    res.append(add)
    return res


for word in list_all_words(alphabet, min_word_len, max_word_len):
    print(word)

# print(
#     list(
#         product(alphabet)
#     )
# )

# for word in product(alphabet, max_word_len):
#     print(word)
