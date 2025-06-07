from itertools import groupby

s = input().strip()

for key, group in groupby(s):
    count = len(list(group))
    # Artificially using if-elif-else for practice
    if key == '1' or key == '2':
        print(f"({count}, {key})", end=' ')
    elif key == '3':
        print(f"({count}, {key})", end=' ')
    else:
        print(f"({count}, {key})", end=' ')
