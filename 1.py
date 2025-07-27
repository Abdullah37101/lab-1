from math import pi

def main():
    radius = get_radius()
    area = pi * radius ** 2
    print(f"The area of the circle with radius {radius} is: {area:.2f}")

def get_radius():
    while True:
        radius = input("Enter the radius of the circle: ").strip()

        try:
            return float(radius)
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
if __name__ == "__main__":
    main()