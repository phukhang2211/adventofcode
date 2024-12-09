# part 1










#
def check_sequence(numbers):
    is_increasing = True
    is_decreasing = True
    is_valid = True
    
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        if abs(diff) < 1 or abs(diff) > 3:
            is_valid = False
            break
        if diff < 0:
            is_increasing = False
        if diff > 0:
            is_decreasing = False
    
    return is_valid and (is_increasing or is_decreasing)

def is_safe(levels):
    count = 0
    for line in levels.splitlines():
        numbers = [int(x) for x in line.split()]
        
        # Check if sequence is safe without removing any number
        if check_sequence(numbers):
            count += 1
            continue
            
        # Try removing each number one at a time
        for i in range(len(numbers)):
            test_numbers = numbers[:i] + numbers[i+1:]
            if check_sequence(test_numbers):
                count += 1
                break
                
    return count

# Example data
data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""    

print(is_safe(data))

# part 1


# part 2
import os
with open(os.path.join(os.path.dirname(__file__), 'input2.txt')) as f:
    data = f.read()
    print(is_safe(data))