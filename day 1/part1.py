import math
import itertools

def main():
	entries = []
	with open('input.txt') as f:
		for line in f:
			entries.append(int(line))
	
	for pair in itertools.combinations(entries, 2):
		if sum(pair) == 2020:
			print(math.prod(pair))

if __name__ == '__main__':
	main()