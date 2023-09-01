for n in range(1, 11):
    with open(f'{n}.in') as f:
        raw = f.read()

    with open(f'{n}.in', 'w') as f:
        print(raw.lower(), file=f, end='')

    with open(f'{n}.out') as f:
        raw = f.read()

    with open(f'{n}.out', 'w') as f:
        print(raw.lower(), file=f, end='')
