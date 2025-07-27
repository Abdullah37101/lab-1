def main():
    upper_bound = get_upper_bound()
    print_pattern(upper_bound)    


def print_pattern(upper_bound):
    for i in range(1, upper_bound +1):
        print(" + ".join(str(j) for j in range(1, i + 1)))

def get_upper_bound():
    while True:
        number = input("Enter the upper bound of the natural numbers summation pattern: ")

        if number.isdigit():
            return int(number)
        
        print("Invalid input. Please enter a valid natural number.")


if __name__ == "__main__":
    main()