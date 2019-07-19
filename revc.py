""" http://rosalind.info/problems/revc/ """

COMPLEMENTS = ("AGTC", "TCAG")

table = str.maketrans(COMPLEMENTS[0], COMPLEMENTS[1])

with open('data/rosalind_revc.txt', 'r') as f1:
    raw_dna = f1.read()
    reverse_dna = raw_dna.translate(table)[::-1]
    print(reverse_dna)
