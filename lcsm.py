import re

def process_dataset():
    fasta_pattern = re.compile(r'Rosalind_\d')

    with open('data/rosalind_lcsm.txt', 'r') as f1:
        raw_dna = f1.read()
        for dna in raw_dna.split(">"):
            if dna and fasta_pattern.match(dna):
                label, *cleaned_dna = dna.split("\n")
                yield label, "".join(cleaned_dna)

dna_bank = [dna for _, dna in process_dataset()]
longest_ss = ""


for x in range(len(dna_bank[0]), 0, -1):
    y = 0
    while x + y <= len(dna_bank[0]):
        ss = dna_bank[0][y: x+y]
        ss_count = 1

        for dna in dna_bank[1:]:
            if ss not in dna:
                break
            ss_count += 1

        if ss_count == len(dna_bank) and len(ss) > len(longest_ss):
            longest_ss = ss

        y += 1


print(longest_ss)
