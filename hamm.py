s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

diff_count = 0

for x in zip(s, t):
    if x[0] != x[1]:
        diff_count += 1

print(diff_count)


