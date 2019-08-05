def fib(n, k):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return (k * fib(n-2, k)) + fib(n-1, k)


n = input("Enter month (n): ")
k = input("Enter offspring pair (k): ")

print(fib(int(n), int(k)))
