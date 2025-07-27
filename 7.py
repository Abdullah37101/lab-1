def main():
    upper_bound = get_upper_bound()
    
    for i in range(2, upper_bound + 1, 2):
        print(i)

def get_upper_bound():
    while True:
        number = input("Enter the upper bound of the even numbers: ")

        if number.isdigit():
            return int(number)
        
        print("Invalid input. Please enter a valid natural number.")


if __name__ == "__main__":
    main()