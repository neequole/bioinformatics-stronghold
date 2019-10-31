import re


def process_dataset():
    fasta_pattern = re.compile(r'Rosalind_\d')

    with open('data/rosalind_grph.txt', 'r') as f1:
        raw_dna = f1.read()
        for dna in raw_dna.split(">"):
            if dna and fasta_pattern.match(dna):
                label, *cleaned_dna = dna.split("\n")
                yield label, "".join(cleaned_dna)

k = 3
dna_bank = [(label, dna) for label, dna in process_dataset()]
graph = []

for x in range(len(dna_bank)):
    for y in range(len(dna_bank)):
        if x == y:
            continue

        if dna_bank[x][1][-k:] == dna_bank[y][1][:k]:
            graph.append((dna_bank[x][0], dna_bank[y][0]))

for v, w in graph:
    print(v, w)
