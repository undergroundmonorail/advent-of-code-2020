import math
import itertools

def main():
	entries = []
	with open('input.txt') as f:
		for line in f:
			entries.append(int(line))
	
	for group in itertools.combinations(entries, 3):
		if sum(group) == 2020:
			print(math.prod(group))

if __name__ == '__main__':
	main()