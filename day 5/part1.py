import re
import functools

def to_decimal(s):
	return functools.reduce(lambda x, y: x*2 + y, (c in 'BR' for c in s))

def seat_id(row, col):
	return row * 8 + col

def main():
	with open('input.txt') as f:
		print(max((seat_id(*map(to_decimal, re.findall(r'([FB]+)([LR]+)', line)[0])) for line in f)))

if __name__ == '__main__':
	main()