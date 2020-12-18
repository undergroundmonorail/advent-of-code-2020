def next(spoken):
	before, recent = spoken[:-1], spoken[-1]
	
	if recent not in before:
		return 0
	
	return before[::-1].index(recent) + 1

def main():
	with open('input.txt') as f:
		spoken = [int(n) for n in f.read().strip().split(',')]
	
	while len(spoken) < 2020:
		spoken.append(next(spoken))
	
	print(spoken[-1])

if __name__ == '__main__':
	main()