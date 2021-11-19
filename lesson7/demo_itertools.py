from itertools import combinations, combinations_with_replacement,\
    count, permutations

max_len = 3

nums = range(10)

print(nums)

# for comb in enumerate(combinations(nums, max_len)):
#     print(f'{comb[0]}:  {comb[1]}')
#
# for comb in combinations_with_replacement(nums, max_len):
#     print(comb)

for comb in enumerate(permutations('ABCD', 2)):
    print(f'{comb[0]}:  {comb[1]}')

odds = count(start=1, step=2)
for _ in range(10):
    print(next(odds))
