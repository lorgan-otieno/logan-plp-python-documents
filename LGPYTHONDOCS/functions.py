def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = []  # Initialize the sequence

    if n <= 0:
        return fibonacci_sequence  # Return an empty sequence if n is zero or negative
    elif n == 1:
        fibonacci_sequence.append(0)  # Add the first term to the sequence
        return fibonacci_sequence
    else:
        a, b = 0, 1  # Initialize the first two terms
        fibonacci_sequence.extend([a, b])  # Add the first two terms to the sequence

        for _ in range(2, n):
            c = a + b
            fibonacci_sequence.append(c)  # Add the next term to the sequence
            a, b = b, c  # Update a and b for the next iteration

        return fibonacci_sequence


# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print("Fibonacci sequence up to term", num_terms, ":", fibonacci_sequence)
