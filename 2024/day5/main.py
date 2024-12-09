from collections import defaultdict, deque
import os

def parse_input(input_data):
    rules = []
    updates = []
    is_rules_section = True
    
    for line in input_data.strip().split('\n'):
        if line == '':
            is_rules_section = False
            continue
        if is_rules_section:
            rules.append(line)
        else:
            updates.append(line.split(','))
    
    return rules, updates

def build_graph(rules):
    graph = defaultdict(set)
    for rule in rules:
        before, after = rule.split('|')
        graph[before].add(after)
    
    return graph

def is_ordered(update, graph):
    position = {page: idx for idx, page in enumerate(update)}
    
    for page in update:
        for next_page in graph[page]:
            if next_page in position and position[page] > position[next_page]:
                return False
    return True

def find_middle_page(update):
    mid_index = len(update) // 2
    return int(update[mid_index])

def reorder_update(update, graph):
    position = {page: idx for idx, page in enumerate(update)}
    
    sorted_update = []
    visited = set()
    temp_mark = set()
    
    def visit(node):
        if node in temp_mark:
            return
        if node not in visited:
            temp_mark.add(node)
            for neighbor in graph[node]:
                if neighbor in position:
                    visit(neighbor)
            temp_mark.remove(node)
            visited.add(node)
            sorted_update.append(node)
    
    for page in update:
        visit(page)
    
    sorted_update.reverse()
    
    return [page for page in sorted_update if page in update]

def part1(input_data):
    rules, updates = parse_input(input_data)
    graph = build_graph(rules)
    
    total_middle_sum = 0
    
    for update in updates:
        if is_ordered(update, graph):
            middle_page = find_middle_page(update)
            total_middle_sum += middle_page
    
    return total_middle_sum, updates

def part2(input_data, part1_result, ordered_updates):
    rules, updates = parse_input(input_data)
    graph = build_graph(rules)
    
    middle_pages = []
    
    for update in updates:
        if not is_ordered(update, graph):
            ordered_update = reorder_update(update, graph)
            middle_page = find_middle_page(ordered_update)
            middle_pages.append(middle_page)
    
    return sum(middle_pages)

if __name__ == "__main__":
    input_data = os.path.join(os.path.dirname(__file__), 'input5.txt')
    with open(input_data, 'r') as file:
        input_data = file.read()
    
    result_part1, ordered_updates = part1(input_data)
    print(f"Part 1 Result: {result_part1}")

    result_part2 = part2(input_data, result_part1, ordered_updates)
    print(f"Part 2 Result: {result_part2}")