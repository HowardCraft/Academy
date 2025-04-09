def fibonacci(n):
    """
    Generates the Fibonacci series up to n elements.

    The Fibonacci sequence starts with 0 and 1. Each subsequent number is the sum of the
    previous two numbers.

    Parameters:
        n (int): The number of elements in the Fibonacci series to generate.

    Returns:
        list: A list containing the Fibonacci series.
    """
    # Handle cases where n is less than or equal to 0
    if n <= 0:
        return []
    # For n = 1, return just the first element.
    elif n == 1:
        return [0]
    
    # Start the series with the first two Fibonacci numbers.
    fib_series = [0, 1]
    
    # Generate the Fibonacci series up to n elements.
    while len(fib_series) < n:
        # The next Fibonacci number is the sum of the last two numbers.
        next_value = fib_series[-1] + fib_series[-2]
        fib_series.append(next_value)
    
    return fib_series

# Example usage:
if __name__ == "__main__":
    num_elements = 10
    print(f"Fibonacci series with {num_elements} elements:")
    print(fibonacci(num_elements))
