import itertools
import math

def path_trees(right, down):
	with open('input.txt') as f:
		for x, line in zip(itertools.count(start=0, step=right), itertools.islice(f, None, None, down)):
			yield line[x % len(line.strip())] == '#'

def main():
	slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
	print(math.prod((sum(path_trees(*slope)) for slope in slopes)))

if __name__ == '__main__':
	main()