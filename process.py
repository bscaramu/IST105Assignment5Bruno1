#!/usr/bin/python3

import sys
import math
import random

print("Content-type: text/html\n")


if len(sys.argv) < 3:
    print("<p>Error: Missing input values.</p>")
    sys.exit()

try:
    number = int(sys.argv[1])
    text = sys.argv[2]
except ValueError:
    print("<p>Error: Invalid input format.</p>")
    sys.exit()


if number % 2 == 0:
    number_result = f"The number {number} is even. Its square root is {math.sqrt(number):.2f}."
else:
    number_result = f"The number {number} is odd. Its cube is {number ** 3}."


binary_text = ' '.join(format(ord(char), '08b') for char in text)
vowel_count = sum(1 for char in text.lower() if char in "aeiou")


secret_number = random.randint(1, 100)
attempts = []
found = False
max_attempts = 5
current_attempt = 1

while not found:
    guess = random.randint(1, 100)
    if guess == secret_number:
        attempts.append(f"Attempt {current_attempt}: {guess} 🎉 (Correct!)")
        found = True
    elif guess < secret_number:
        attempts.append(f"Attempt {current_attempt}: {guess} (Too low!!!)")
    else:
        attempts.append(f"Attempt {current_attempt}: {guess} (Too high!!!)")

    if current_attempt >= max_attempts and not found:
        max_attempts += 1  

    current_attempt += 1


print(f"""
<html><body>
    <h2>Number Puzzle</h2>
    <p>{number_result}</p>

    <h2>Text Puzzle</h2>
    <p>Binary: {binary_text}</p>
    <p>Vowel Count: {vowel_count}</p>

    <h2>Treasure Hunt</h2>
    <p>The secret number was: {secret_number}</p>
    <ul>
""")
for attempt in attempts:
    print(f"<li>{attempt}</li>")
print(f"""
    </ul>
    <p>🎯 You found the treasure in {current_attempt - 1} attempts!</p>
</body></html>
""")
