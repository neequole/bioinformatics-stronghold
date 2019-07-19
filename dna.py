""" http://rosalind.info/problems/dna/ """
from collections import Counter

nucleobases = {
    "A": 0,
    "C": 0,
    "G": 0,
    "T": 0,
}

with open('data/rosalind_dna.txt', 'r') as f1:
    dna = f1.read()
    # Using dictionary
    for l in dna:
        if l in nucleobases.keys():
            nucleobases[l] += 1

    print(" ".join(map(str, nucleobases.values())))

    # Using built in count method
    count_result = [dna.count(l) for l in nucleobases.keys()]
    print(" ".join(map(str, count_result)))

    # Using collections Counter
    c = Counter(dna)
    counter_result = [c[l] for l in nucleobases.keys()]
    print(" ".join(map(str, counter_result)))
