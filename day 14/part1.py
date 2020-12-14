import re

def main():
	parse = re.compile(r'(?:mem\[)?(\d+|mask)\]? = ([\d|X]+)')
	
	and_mask = (1 << 36) - 1
	or_mask = 0
	
	memory = {}
	
	with open('input.txt') as f:
		for addr, value in (parse.findall(line)[0] for line in f):
			if addr == 'mask':
				or_mask = int(value.replace('X', '0'), 2)
				and_mask = int(value.replace('X', '1'), 2)
			else:
				memory[int(addr)] = int(value) & and_mask | or_mask
	
	print(sum(memory.values()))

if __name__ == '__main__':
	main()