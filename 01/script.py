import heapq
import sys
from typing import Iterable

def parse_input(lines: Iterable[str]) -> Iterable[list[int]]:
  numbers = []
  for line in map(str.strip, lines):
    if line == '':
      yield numbers
      numbers = []
    else:
      numbers.append(int(line))
  if numbers:
    yield numbers

def solution_a(elf_fruit_calories: Iterable[list[int]]) -> int:
  return max(sum(calories) for calories in elf_fruit_calories)

def solution_b(elf_fruit_calories: Iterable[list[int]]) -> int:
  fruit_calorie_sums = [-sum(calories) for calories in elf_fruit_calories]
  heapq.heapify(fruit_calorie_sums)
  total = 0
  for _ in range(3):
    total += -heapq.heappop(fruit_calorie_sums)
  return total

elf_fruit_calories = list(parse_input(sys.stdin))
print(f'a: {solution_a(elf_fruit_calories)}')
print(f'b: {solution_b(elf_fruit_calories)}')