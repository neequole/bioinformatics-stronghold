with open('data/rosalind_subs.txt', 'r') as f1:
    s, t, *_ = f1.readlines()
    s = s.strip()
    t = t.strip()
    i = 0
    last_index = len(s)-len(t)+1
    while i <= last_index:
        loc = s.find(t, i)
        if loc > 0:
            i = loc + 1
            print(i, end=" ")
        else:
            i += 1
