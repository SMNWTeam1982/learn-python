from utils import read_input

def transformer(line):
    l, w, h = line.strip().split('x')
    return [int(l), int(w), int(h)]

presents = read_input(2, transformer)

def calculate_paper_need(present):
    l, w, h = present
    areas = [l*w, w*h, h*l]
    
    return sum(2*area for area in areas) + min(areas)

result = sum(calculate_paper_need(present) for present in presents)

print(f'Solution: {result}')
assert result == 1586300

import math

def calculate_ribbon(present):
    smallest_sides = sorted(present)[:2]
        
    ribbon = sum(x*2 for x in smallest_sides)
    bow = math.prod(present)
    
    return ribbon + bow

result = sum(calculate_ribbon(present) for present in presents)
print(f'Solution: {result}')
assert result == 3737498 # For refactoring