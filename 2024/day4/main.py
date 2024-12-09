def find_all_xmas(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # All possible directions: down-right, down-left, up-left, up-right
    directions = [
        (1, 1), (1, -1),
        (-1, -1), (-1, 1)
    ]
    
    def is_valid(x, y):
         return 0 <= x < rows and 0 <= y < cols
    
    def check_direction(x, y, dx, dy):
        # Check for M (one step back)
        word = ""
        prev_x, prev_y = x - dx, y - dy
        if not is_valid(prev_x, prev_y) or grid[prev_x][prev_y] not in ('M','S'):
            return False
        word += grid[prev_x][prev_y]
        # We're on A already (current position)
        if grid[x][y] != 'A':
            return False
        word += grid[x][y]
        # Check for S (one step forward)
        next_x, next_y = x + dx, y + dy
        if not is_valid(next_x, next_y) or grid[next_x][next_y] not in ('M','S'):
            return False
        word += grid[next_x][next_y]
        # print("word",word)
        if word == "MAS" or word == "SAM":
            return True
        return False
    
    # Add a set to track used 'A' positions
    used_positions = set()
    
    # Check each starting position
    for i in range(1, rows -1):
        for j in range(1, cols -1):
            # Only process if this is an 'A' we haven't counted yet
            if grid[i][j] == 'A' and (i, j) not in used_positions:
                found_pattern = False
                # Try all directions from this position
                for dx, dy in directions:
                    if check_direction(i, j, dx, dy):
                        found_pattern = True
                        print(i,j)
                
                # If we found any pattern using this 'A', count it once and mark as used
                if found_pattern:
                    count += 1
                    used_positions.add((i, j))
    print("used_positions",used_positions)
    return count

# Example usage
def solve_puzzle(puzzle_str):
    # Convert input string to grid
    grid = [list(line.strip()) for line in puzzle_str.strip().split('\n')]
    return find_all_xmas(grid)

# Test with the example from the problem
puzzle = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
""".strip()

# 4 directions, so divide by 4
# result = solve_puzzle(puzzle) 
# print(f"Found {result} instances of XMAS")
import os  
# open file input.txt
with open(os.path.join(os.path.dirname(__file__), 'input4.txt'), 'r') as f:
    puzzle = f.read()
    result = solve_puzzle(puzzle) 
    
print(f"Found {result} instances of XMAS")
