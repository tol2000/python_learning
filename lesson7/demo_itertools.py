from itertools import combinations

max_len = 2

nums = [0, 1, 2, 3, 4, 5]

for comb in combinations(nums, max_len):
    print(comb)
