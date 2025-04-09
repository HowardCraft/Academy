def factorial(n):
    """
    Recursive function to calculate the factorial of n.

    Factorial is defined as:
        n! = n * (n-1) * (n-2) * ... * 1, for n > 0
        and 0! = 1 by definition.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of n.
    """
    # Base case: if n is 0, return 1.
    if n == 0:
        return 1
    # Recursive case: multiply n by factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage:
if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num} is {factorial(num)}")
