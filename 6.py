def main():
    UPPER_BOUND = 16
    print_powers_of_two(UPPER_BOUND)


def print_powers_of_two(upper_bound):
    for i in range(upper_bound + 1):
        print(f"2^{i} = {2 ** i}")

if __name__ == "__main__":
    main()