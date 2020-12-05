import re
import functools
import collections

def to_decimal(s):
	return functools.reduce(lambda x, y: x*2 + y, (c in 'BR' for c in s))

def seat_id(row, col):
	return row * 8 + col

def main():
	with open('input.txt') as f:
		ids = set((seat_id(*map(to_decimal, re.findall(r'([FB]+)([LR]+)', line)[0])) for line in f))
	
	for seat in ids:
		if (seat + 2) in ids and (seat + 1) not in ids:
			print(seat + 1)
			break

if __name__ == '__main__':
	main()