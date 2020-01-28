
def fib(n):
    # 1, 1, 2, 3, 5, 8, 13
    f_l = [1]
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
        f_l.append(b)
    return f_l


if __name__ == "__main__":
    list_of_fib = fib(10)
    print(list_of_fib)


