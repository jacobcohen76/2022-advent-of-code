import sys
from typing import Iterable

def parse_input(lines: Iterable[str]) -> Iterable[str]:
  return map(str.strip, lines)

def priority(code: str) -> int:
  if code.islower():
    return ord(code) - ord('a') + 1
  return ord(code) - ord('A') + 27

def solution_a(rucksacks: Iterable[str]) -> None:
  total = 0
  for rucksack in rucksacks:
    mid = len(rucksack) // 2
    intersection = set(rucksack[:mid]) & set(rucksack[mid:])
    total += sum(priority(code) for code in intersection)
  return total

def solution_b(rucksacks: Iterable[str]) -> None:
  rucksacks = list(rucksacks)
  total     = 0
  for i in range(0, len(rucksacks), 3):
    badge, = set(rucksacks[i]) & set(rucksacks[i + 1]) & set(rucksacks[i + 2])
    total += priority(badge)
  return total

rucksacks = list(parse_input(sys.stdin))
print(f'a: {solution_a(rucksacks)}')
print(f'b: {solution_b(rucksacks)}')