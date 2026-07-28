# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def calculate_sum(num):
    total = 0
    for n in num:
        total += n
    return total

def calculate_average(num):
    total = calculate_sum(num)
    return total / len(num) if len(num) > 0 else 0

def calculate_maximum(num):
    if not num:
        return None
    max_val = num[0]
    for n in num:
        if n > max_val:
            max_val = n
    return max_val

def calculate_minimum(num):
    if not num:
        return None
    min_val = num[0]
    for n in num:
        if n < min_val:
            min_val = n
    return min_val

number = int(input("How many numbers? "))
numbers = []

if number <= 0:
    print("Error: Please enter a positive integer.")
else:
    for i in range(number):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

print("\nResults:")
print(f"Sum:     {calculate_sum(numbers)}")
print(f"Average: {calculate_average(numbers)}")
print(f"Maximum: {calculate_maximum(numbers)}")
print(f"Minimum: {calculate_minimum(numbers)}")
