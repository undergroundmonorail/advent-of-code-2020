import itertools

def path_trees():
	with open('input.txt') as f:
		for x, line in zip(itertools.count(start=0, step=3), f):
			yield line[x % len(line.strip())] == '#'

def main():
	print(sum(path_trees()))

if __name__ == '__main__':
	main()