import re

def get_addresses(addr, mask):
	def expand_floating(pairs):
		if not pairs:
			return [0]
			
		ret = []
		
		m, b = pairs[0]
		
		for a in expand_floating(pairs[1:]):
			if m == '0':
				ret.append(a << 1 | b)
			if m == '1':
				ret.append(a << 1 | 1)
			if m == 'X':
				ret.append(a << 1)
				ret.append(a << 1 | 1)
		
		return ret
	
	return expand_floating([(c, addr >> n & 1) for n, c in enumerate(mask[::-1])])

def main():
	parse = re.compile(r'(?:mem\[)?(\d+|mask)\]? = ([\d|X]+)')
	
	mask = '0'*36
	
	memory = {}
	
	with open('input.txt') as f:
		for addr, value in (parse.findall(line)[0] for line in f):
			if addr == 'mask':
				mask = value
			else:
				for a in get_addresses(int(addr), mask):
					memory[a] = int(value)
	
	print(sum(memory.values()))

if __name__ == '__main__':
	main()