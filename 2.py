def main():
    number = get_number()
    
    if is_even(number):
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")


def is_even(number):    
    return number % 2 == 0

def get_number():
    while True:
        number = input("Enter the whole number you want to check: ")

        try:
            return int(number)
        
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")


if __name__ == "__main__":
    main()