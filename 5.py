from math import sqrt

def main():
    number = get_number()
    
    if is_prime(number):
        print(f"The number {number} is prime.")
    else:
        print(f"The number {number} is not prime.")


def is_prime(number):
    if number <= 1:
        return False
    
    if number <= 3:
        return True
    
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    for i in range(5, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
        
    return True

def get_number():
    while True:
        number = input("Enter the number you want to check: ")

        if number.isdigit():
            return int(number)
        
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()