""" http://rosalind.info/problems/rna/ """

with open('data/rosalind_rna.txt', 'r') as f1:
    dna = f1.read()
    rna = dna.replace("T", "U")
    print(rna)
