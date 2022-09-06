from random import randint, seed

seed(42)

MAX = (1 << 31) - 1


def generate_queries(n, q):
    queries = []
    for _ in range(q):
        x = randint(1, n)
        y = randint(x, n)
        queries.append((x, y))
    return queries


def format(n, q, a, queries):
    shoals = ' '.join(map(str, a))
    ranges = '\n'.join([' '.join(map(str, (x, y))) for x, y in queries])
    return '{} {}\n{}\n{}'.format(n, q, shoals, ranges)


def write(n, contents):
    with open('tests/{}.in'.format(n), 'w+') as f:
        f.write(contents)


def example():
    write(0, format(5, 3, [6, 0, 10, 8, 8], [(1, 3), (4, 4), (3, 5)]))


# min queries, min shoals, min shoal size
def smol():
    write(1, "1 0\n0")


# few queries, max shoals, large shoal sizes
def beeg_yoshi():
    n = 1000000
    q = 10
    a = [randint(MAX - 1000, MAX) for _ in range(n)]
    queries = generate_queries(n, q)
    
    write(2, format(n, q, a, queries))


# max queries, few shoals, large shoal sizes
def beeger_yoshi():
    n = 10
    q = 1000000
    a = [randint(MAX - 1000, MAX) for _ in range(n)]
    queries = generate_queries(n, q)
    
    write(3, format(n, q, a, queries))


# max queries, max shoals, large shoal sizes
def beegest_yoshi():
    n = 1000000
    q = 1000000
    a = [randint(MAX - 1000, MAX) for _ in range(n)]
    queries = generate_queries(n, q)
    
    write(4, format(n, q, a, queries))


def small1():
    n = 10
    q = 5
    a = [randint(1, 20) for _ in range(n)]
    queries = generate_queries(n, q)

    write(5, format(n, q, a, queries))


def small2():
    n = 100
    q = 50
    a = [randint(1, 20000) for _ in range(n)]
    queries = generate_queries(n, q)

    write(6, format(n, q, a, queries))


def small3():
    n = 1000
    q = 500
    a = [randint(1, 200000) for _ in range(n)]
    queries = generate_queries(n, q)

    write(7, format(n, q, a, queries))


def medium1():
    n = 10000
    q = 15000
    a = [randint(1, 10000000) for _ in range(n)]
    queries = generate_queries(n, q)

    write(8, format(n, q, a, queries))


def medium2():
    n = 50000
    q = 100000
    a = [randint(1, 100000000) for _ in range(n)]
    queries = generate_queries(n, q)

    write(9, format(n, q, a, queries))


def medium3():
    n = 100000
    q = 200000
    a = [randint(1, MAX) for _ in range(n)]
    queries = generate_queries(n, q)

    write(10, format(n, q, a, queries))


def large1():
    n = 500000
    q = 750000
    a = [randint(1, MAX) for _ in range(n)]
    queries = generate_queries(n, q)

    write(11, format(n, q, a, queries))


def large2():
    n = 1000000
    q = 750000
    a = [randint(1, MAX) for _ in range(n)]
    queries = generate_queries(n, q)

    write(12, format(n, q, a, queries))


def large3():
    n = 1000000
    q = 1000000
    a = [randint(1, MAX) for _ in range(n)]
    queries = generate_queries(n, q)

    write(13, format(n, q, a, queries))


if __name__ == '__main__':
    # sample
    example()

    # corner cases
    smol()
    beeg_yoshi()
    beeger_yoshi()
    beegest_yoshi()

    # small cases
    small1()
    small2()
    small3()

    # medium cases
    medium1()
    medium2()
    medium3()

    # largest cases
    large1()
    large2()
    large3()
