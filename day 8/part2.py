def execute(op, arg, acc, ip):	
	if op == 'jmp':
		return acc, ip+arg
	
	if op == 'acc':
		return acc+arg, ip+1
	
	if op == 'nop':
		return acc, ip+1

def execute_all(instructions):
	acc = 0
	ip = 0
	executed = []
	
	while ip not in executed and ip < len(instructions):
		executed.append(ip)
		acc, ip = execute(*instructions[ip], acc, ip)
	
	return acc * (ip == len(instructions))

def each_mutation(instructions):
	for n, i in enumerate(instructions):
		op, arg = i
		
		if op == 'acc':
			continue
		
		new = instructions.copy()
		new[n] = ('nop' if op == 'jmp' else 'jmp', arg)
		yield new

def first_true(it):
	for e in it:
		if e:
			return e

def main():
	with open('input.txt') as f:
		instructions = [(lambda x, y: (x, int(y)))(*line.split()) for line in f]
	
	print(first_true((execute_all(i) for i in each_mutation(instructions))))

if __name__ == '__main__':
	main()