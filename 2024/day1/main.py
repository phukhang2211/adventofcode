import os


def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    # Calculate the total distance
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    
    return total_distance

# Example usage
left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]
total_distance = calculate_total_distance(left_list, right_list)



# Open the file and read both columns into separate lists
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input1.txt')
with open(input_path, 'r') as file:
    left_list = []
    right_list = []
    for line in file:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

total_distance = calculate_total_distance(left_list, right_list)
print("Total distance:", total_distance)


# part 2




def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    # Calculate the total distance
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    
    return total_distance

# Example usage
left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]

def calc_times_appear_left_in_right(left_list, right_list):
    total = 0
    for left in left_list:
        count = right_list.count(left)
        total += left * count
    return total


script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input1.txt')
with open(input_path, 'r') as file:
    left_list = []
    right_list = []
    for line in file:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

print(calc_times_appear_left_in_right(left_list, right_list))