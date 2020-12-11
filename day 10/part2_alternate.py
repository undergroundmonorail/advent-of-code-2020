# this is probably what was intended, but memoization is powerful enough that i didn't need to do it
# whoops

import math

def num_chains(jolts, adapters, target):
	if jolts == target:
		return 1
	if jolts not in adapters:
		return 0
	
	return sum((num_chains(jolts+i, adapters, target) for i in range(1, 4)))

def main():
	adapters = [[0]]
	with open('input.txt') as f:
		jolts = [int(line) for line in f]
		for adapter in sorted(jolts) + [max(jolts) + 3]:
			adapters[-1].append(adapter)
			if adapters[-1][-1] - adapters[-1][-2] == 3:
				adapters[-1] = (adapters[-1][0], adapters[-1][:-1], adapters[-1][-1])
				adapters.append([adapter])
	
	print(math.prod((num_chains(*sub_list) for sub_list in adapters[:-1])))

if __name__ == '__main__':
	main()