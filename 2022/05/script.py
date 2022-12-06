import sys
import copy
from typing import Iterable

def parse_initial_stack(lines: list[str]) -> list[list[str]]:
  num_stacks = len(lines[0]) // 4
  stacks = [[] for _ in range(num_stacks)]
  for line in reversed(lines):
    for i in range(len(stacks)):
      idx = 4 * i + 1
      if line[idx] != ' ':
        stacks[i].append(line[idx])
  return stacks

def parse_move_cargo(lines: Iterable[str]) -> list[tuple[int, int, int]]:
  output = []
  for line in lines:
    _, qty, _, src, _, dst = line.split()
    output.append((int(qty), int(src) - 1, int(dst) - 1))
  return output

def parse_input(lines: Iterable[str]) -> tuple[list[list[str]], list[tuple[int, int, int]]]:
  lines = list(lines)
  break_idx = lines.index('\n')
  return parse_initial_stack(lines[:break_idx - 1]), parse_move_cargo(lines[break_idx + 1:])

def solution_a(stacks: list[list[str]], moves: list[tuple[int, int, int]]) -> str:
  for qty, src, dst in moves:
    for _ in range(qty):
      stacks[dst].append(stacks[src].pop())
  return ''.join(stack[-1] for stack in stacks)

def solution_b(stacks: list[list[str]], moves: list[tuple[int, int, int]]) -> str:
  for qty, src, dst in moves:
    stacks[dst].extend(reversed([stacks[src].pop() for _ in range(qty)]))
  return ''.join(stack[-1] for stack in stacks)

stacks, moves = parse_input(sys.stdin)
print(f'a: {solution_a(copy.deepcopy(stacks), moves)}')
print(f'b: {solution_b(copy.deepcopy(stacks), moves)}')