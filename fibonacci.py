import time


def fibo(n):
    if n == 1:
        return 0
    if n <= 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

start_time = time.time()
print(fibo(30))
print("--- %s seconds ---" % round(time.time() - start_time, 4))


def db_fibo(n):
    res = {}

    def fb(n):
        if n in res:
            return res[n]
        if n == 1:
            f = 0
        elif n <= 2:
            f = 1
        else:
            f = fb(n - 1) + fb(n - 2)

        res[n] = f

        return f

    return fb(n)


start_time = time.time()
print(db_fibo(30))
print("--- %s seconds ---" % (time.time() - start_time))
