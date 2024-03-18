""""This module is used to solve problem 2 from Project Euler. The problem"""

def even_fibonacci_numbers (number):
    """Function print the sum of all even numbers in the Fibonacci 
    sequence that are less than the given number."""

    print("The sum of all even numbers in the Fibonacci sequence that are less than", number, "is:")

    if number > 4000001:
        print("Number is too large")

    a, b = 1, 2
    even_sum = 0
    fibonacci_list = []
    while number >= 0:
        if a % 2 == 0:
            even_sum += a
        fibonacci_list.append(a)
        a, b = b, a + b
        if a > number:
            break
        number -= 1

    print(fibonacci_list)
    return even_sum

print("answer:", even_fibonacci_numbers(10))
print("answer:", even_fibonacci_numbers(20))
print("answer:", even_fibonacci_numbers(30))
print("answer:", even_fibonacci_numbers(50))
print("answer:", even_fibonacci_numbers(100))
print("answer:", even_fibonacci_numbers(1000))
print("answer:", even_fibonacci_numbers(10000))
print("answer:", even_fibonacci_numbers(100000))
print("answer:", even_fibonacci_numbers(4000000))
