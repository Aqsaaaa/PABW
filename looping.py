def print_odd_numbers():
    for i in range(1, 101):
        if i % 2 == 0:
            continue
        else:
            print(i)

print_odd_numbers()