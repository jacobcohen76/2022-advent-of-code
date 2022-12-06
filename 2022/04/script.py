import itertools
import sys
from typing import Iterable

def encloses(a_lo: int, a_hi: int, b_lo: int, b_hi: int) -> bool:
  return (a_lo <= b_lo and b_hi <= a_hi) \
      or (b_lo <= a_lo and a_hi <= b_hi)

def overlaps(a_lo: int, a_hi: int, b_lo: int, b_hi: int) -> bool:
  return max(a_lo, b_lo) <= min(a_hi, b_hi)

def parse_input(lines: Iterable[str]) -> Iterable[tuple[int, int, int, int]]:
  for line in lines:
    a, b = line.split(',')
    a_lo, a_hi = map(int, a.split('-'))
    b_lo, b_hi = map(int, b.split('-'))
    yield (a_lo, a_hi, b_lo, b_hi)

def solution_a(elf_cleaning_intervals: Iterable[tuple[int, int, int, int]]) -> int:
  return sum(itertools.starmap(encloses, elf_cleaning_intervals))

def solution_b(elf_cleaning_intervals: Iterable[tuple[int, int, int, int]]) -> int:
  return sum(itertools.starmap(overlaps, elf_cleaning_intervals))

elf_cleaning_intervals = list(parse_input(sys.stdin))
print(f'a: {solution_a(elf_cleaning_intervals)}')
print(f'b: {solution_b(elf_cleaning_intervals)}')