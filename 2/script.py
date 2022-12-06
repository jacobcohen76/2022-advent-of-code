import itertools
import sys
from typing import Iterable

ROCK     = 1
PAPER    = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN  = 6

def score_round_a(opponent: str, you: str) -> int:
  match (opponent, you):
    case ('A', 'X'): return ROCK     + DRAW
    case ('A', 'Y'): return PAPER    + WIN
    case ('A', 'Z'): return SCISSORS + LOSE
    case ('B', 'X'): return ROCK     + LOSE
    case ('B', 'Y'): return PAPER    + DRAW
    case ('B', 'Z'): return SCISSORS + WIN
    case ('C', 'X'): return ROCK     + WIN
    case ('C', 'Y'): return PAPER    + LOSE
    case ('C', 'Z'): return SCISSORS + DRAW

def score_round_b(opponent: str, game_state: str) -> int:
  match (opponent, game_state):
    case ('A', 'X'): return LOSE + SCISSORS
    case ('A', 'Y'): return DRAW + ROCK
    case ('A', 'Z'): return WIN  + PAPER
    case ('B', 'X'): return LOSE + ROCK
    case ('B', 'Y'): return DRAW + PAPER
    case ('B', 'Z'): return WIN  + SCISSORS
    case ('C', 'X'): return LOSE + PAPER
    case ('C', 'Y'): return DRAW + SCISSORS
    case ('C', 'Z'): return WIN  + ROCK

def parse_input(lines: Iterable[str]) -> Iterable[tuple[str, str]]:
  for line in lines:
    opponent, you = line.split()
    yield opponent, you

def solution_a(rps_rounds: Iterable[tuple[str, str]]) -> int:
  return sum(itertools.starmap(score_round_a, rps_rounds))

def solution_b(lines: Iterable[str]) -> int:
  return sum(itertools.starmap(score_round_b, rps_rounds))

rps_rounds = list(parse_input(sys.stdin))
print(f'a: {solution_a(rps_rounds)}')
print(f'b: {solution_b(rps_rounds)}')