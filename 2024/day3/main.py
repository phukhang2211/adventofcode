# The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

# It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

# However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

# For example, consider the following section of corrupted memory:

# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

# Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?



example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# Add new code
import re
dont_pattern = r"don't\(\)"
do_pattern = r"do\(\)"
pattern = r"mul\((\d+),(\d+)\)"
# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.

matches = re.finditer(pattern, example)
total = 0
enabled = True  # Start with multiplications enabled

for match in matches:
    # Check if there's a don't() or do() before this match
    text_before = example[:match.start()]
    last_dont = text_before.rfind("don't()")
    last_do = text_before.rfind("do()")
    
    # Update enabled status based on most recent don't() or do()
    if last_dont > last_do:
        enabled = False
    elif last_do > last_dont:
        enabled = True
        
    if enabled:
        x, y = match.groups()
        total += int(x) * int(y)

print(total)  # Should print: 161

import os
with open(os.path.join(os.path.dirname(__file__), 'input3.txt')) as f:
    data = f.read()
    matches = re.finditer(pattern, data)
    total = 0
    enabled = True
    
    for match in matches:
        text_before = data[:match.start()]
        last_dont = text_before.rfind("don't()")
        last_do = text_before.rfind("do()")
        
        if last_dont > last_do:
            enabled = False
        elif last_do > last_dont:
            enabled = True
            
        if enabled:
            x, y = match.groups()
            total += int(x) * int(y)

    print(total)
