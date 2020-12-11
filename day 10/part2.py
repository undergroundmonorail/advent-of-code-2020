import functools

@functools.cache
def num_chains(jolts, adapters, device):
	if jolts == device:
		return 1
	if jolts not in adapters:
		return 0
	
	return sum((num_chains(jolts+i, adapters, device) for i in range(1, 4)))

def main():
	with open('input.txt') as f:
		adapters = tuple([0] + [int(n) for n in f])
	
	device = max(adapters) + 3
	print(num_chains(0, adapters, device))

if __name__ == '__main__':
	main()