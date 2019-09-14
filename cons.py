import re


def process_dataset():
    fasta_pattern = re.compile(r'Rosalind_\d')

    with open('data/rosalind_cons.txt', 'r') as f1:
        raw_dna = f1.read()
        for dna in raw_dna.split(">"):
            if dna and fasta_pattern.match(dna):
                cleaned_dna = "".join(dna.split("\n")[1:])
                yield cleaned_dna


def generate_profile(dna_bank):
    profile = {x: [0] * len(dna_bank[0]) for x in ("A", "C", "G", "T")}
    for dna in dna_bank:
        for index, x in enumerate(dna):
            profile[x][index] += 1

    return profile


def generate_consensus(profile):
    dna_len = len(list(profile.values())[0])
    consensus = ["-"] * dna_len
    for i in range(dna_len):
        max_value = -1
        for x in profile.keys():
            if profile[x][i] > max_value:
                max_value = profile[x][i]
                consensus[i] = x

    return "".join(consensus)


dna_bank = [x for x in process_dataset()]
profile = generate_profile(dna_bank)
consensus = generate_consensus(profile)

print(consensus)
for k, v in profile.items():
    print(f"{k}: {' '.join(map(str, v))}")

