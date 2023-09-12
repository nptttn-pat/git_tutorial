def generate_fibonacci(n):
    fib_sequence = [1, 1]
    
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Get input from the user
try:
    n = int(input("Number of digits: "))
    
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        # Generate and print the Fibonacci sequence
        fibonacci_sequence = generate_fibonacci(n)
        for number in fibonacci_sequence:
            print(number)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
  
