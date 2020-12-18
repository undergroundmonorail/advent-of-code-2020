def main():
	most_recent = {}
	
	last = -1
	
	with open('input.txt') as f:
		for turn, n in enumerate(f.read().strip().split(','), start=1):
			most_recent[last] = turn-1
			last = int(n)
		
	del most_recent[-1]
	
	for turn in range(turn, 30000000):
		if last in most_recent:
			n = turn - most_recent[last]
		else:
			n = 0
		
		most_recent[last] = turn
		last = n
	
	print(last)

if __name__ == '__main__':
	main()