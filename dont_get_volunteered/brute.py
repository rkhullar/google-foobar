from collections import defaultdict
from solution import answer
import itertools as it

position_codes = list(range(0, 64))

results = dict()

for src, dest in it.product(position_codes, position_codes):
    n = answer(src, dest)
    results[(src, dest)] = n

counts = defaultdict(int)
counts_detail = defaultdict(set)

for key, val in results.items():
    src, dest = key
    counts[val] += 1
    counts_detail[val].add((src, dest))

for n, mode in counts.items():
    print(n, mode)

print()

for src, dest in counts_detail[6]:
    print(src, dest)
