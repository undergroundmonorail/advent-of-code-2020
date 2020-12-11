import itertools

def main():
	buffer = []

	with open('input.txt') as f:
		for line in f:
			target = int(line)
			
			if len(buffer) < 25:
				buffer.append(target)
				continue
		
			if not any((sum(t) == target for t in itertools.combinations(buffer, 2))):
				print(target)
				break
				
			buffer = buffer[1:] + [target]

if __name__ == '__main__':
	main()