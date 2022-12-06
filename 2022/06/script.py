import collections
import sys

def generic_solution(text: str, k: int) -> int | None:
  counter = collections.Counter(text[:k])
  if len(counter) == k:
    return k
  for i in range(k, len(text)):
    counter[text[i - k]] -= 1
    if counter[text[i - k]] == 0:
      del counter[text[i - k]]
    counter[text[i]] += 1
    if len(counter) == k:
      return i + 1

def find_packet_starter(packet: str) -> int:
  for i in range(len(packet)):
    if len(set(packet[i:i + 4])) == 4:
      return i + 4

def solution_a(packet: str) -> int:
  return find_packet_starter(packet)

def solution_b(packet: str) -> int:
  for i in range(len(packet)):
    if len(set(packet[i:i + 14])) == 14:
      return i + 14

packet, = sys.stdin
packet  = packet.strip()
print(f'a: {solution_a(packet)}')
print(f'b: {solution_b(packet)}')
