import sys

# If user provides a list of numbers as command-line arguments
if len(sys.argv) > 1:
    print("user provided input values:")
    # Convert command-line arguments (strings) to integers
    numbers = list(map(int, sys.argv[1:]))
else:
    print("no input given - using default list:")
    numbers = [10, 21, 4, 45, 66, 93, 1]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Numbers list:", numbers)
print("Count of even numbers:", even_count)
print("Count of odd numbers:", odd_count)
