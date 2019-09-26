def fibd_to_n(n):
    fibs = [0, 1]

    for x in range(2, n + 1):
        if x > k:
            foo = [fibs[-2 - i] for i in range(k-1)]
            fibs.append(sum(foo))
        else:
            fibs.append(fibs[-1] + fibs[-2])

    return fibs[n]


n = 86
k = 16

print(fibd_to_n(int(n)))
