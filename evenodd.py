import sys

numbers = [13, 14, 5, 8, 9, 16, 30]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

sys.stdout.write(f"Count of even numbers: {even_count}\n")
sys.stdout.write(f"Count of odd numbers: {odd_count}\n")
