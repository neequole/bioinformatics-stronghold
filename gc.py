import re

fasta_pattern = re.compile(r'Rosalind_\d{4}')

with open('data/rosalind_gc.txt', 'r') as f1:
    raw_dna = f1.read()
    dna_gc_map = list()

    for dna in raw_dna.split(">"):
        if dna and fasta_pattern.match(dna):
            cleaned_dna = dna[13:].replace('\n', '')
            gc_count = (cleaned_dna.count('G') + cleaned_dna.count('C')) / len(cleaned_dna)
            dna_gc_map.append((dna[:13], gc_count * 100))

    dna_gc_map.sort(key=lambda x: x[1])

    max_dna = dna_gc_map[-1]
    print(max_dna[0])
    print(max_dna[1])



