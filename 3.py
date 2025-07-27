def main():
    NUMBERS_COUNT = 3

    numbers = get_numbers(NUMBERS_COUNT)

    if check_equality_of_two(numbers):
        the_sum = 0
    else:
        the_sum = sum(numbers)

    print(f"The sum of the numbers is: {the_sum}")


def check_equality_of_two(numbers):
    if len(numbers) < 2:
        return False

    if numbers[0] == numbers[1]:
        return True
    
    check_equality_of_two(numbers[1:])
    
def get_numbers(count):
    numbers = []
    for _ in range(count):
        number = get_number()
        numbers.append(number)

    return numbers

def get_number():
    while True:
        number = input("Enter a number you want to add to the sum: ")

        try:
            return float(number)
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()