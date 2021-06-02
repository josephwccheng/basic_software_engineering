def generator(start, stop):
    while (start <= stop):
        yield start
        print(f'start={start}')
        start += 1


for counter in generator(3, 4):
    print(f'counter={counter}')
