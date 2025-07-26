def main():
    number = get_number()
    
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

def get_number():
    while True:
        number = input("Enter the number you want to check: ")

        if number.isdigit():
            return int(number)
        
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()