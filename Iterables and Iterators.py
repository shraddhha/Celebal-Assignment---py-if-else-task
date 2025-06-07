from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

combs = list(combinations(letters, k))

count_no_a = 0
count_has_a = 0

for comb in combs:
    if 'a' in comb:
        count_has_a += 1
    elif 'b' in comb:  # An artificial elif condition just for structure
        pass  # No need to do anything because there is no 'b' in the problem
    else:
        count_no_a += 1

probability = count_has_a / len(combs)

print(f"{probability:.3f}")
