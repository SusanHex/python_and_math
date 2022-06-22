from sys import argv


def is_factor(number: int, potential_factor: int) -> bool:
    """Determines if potential_factor is a factor of number

    Args:
        number (int): the number to test for factor
        potential_factor (int): number that may be a factor of number

    Returns:
        bool: returns the result
    """    
    if number % potential_factor == 0:
        return True
    else:
        return False

def main():
    # Grabs cli arg, if provided
    if len(argv) > 1:
        number = argv[1]
    # else, will attempt to get a valid integer
    else:
        while True:
            try:
                number = int(input("Number?: "))
                break
            except ValueError:
                continue
    # Will loop from 1 to number - 1 and test if they are a factor
    print(f"Finding the factors of {number}...")
    for num in range(1, number):
        if is_factor(number, num):
            print(f"{num}, ", end="")
    print()
    

# if this file is run directly 

if __name__ == "__main__":
    main()