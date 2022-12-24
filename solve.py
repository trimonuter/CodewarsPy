# url: https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
# problem: 1_findOdd.py

def find_it(seq):
  for i in set(seq):
    if seq.count(i) % 2 != 0:
      return i