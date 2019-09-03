homo_d_count, hetero_count, homo_r_count = map(int, input("Enter: ").split())

outcomes = {
    "homo_d": homo_d_count,
    "hetero": hetero_count,
    "homo_r": homo_r_count
}

total_count = sum(outcomes.values())
outcomes_probability = {}

for k, v in outcomes.items():

    probability_x = v / total_count

    for k2, v2 in outcomes.items():

        if k == k2:
            probability_y = (v2 - 1) / (total_count - 1)
        else:
            probability_y = v2 / (total_count - 1)

        outcomes_probability[(k, k2)] = probability_x * probability_y

foo = []

for k, v in outcomes_probability.items():
    if "homo_d" in k:
        foo.append(v)
    elif "hetero" in k:
        if "homo_r" in k:
            foo.append(v * (0.5))
        else:
            foo.append(v * (0.75))

print(sum(foo))
