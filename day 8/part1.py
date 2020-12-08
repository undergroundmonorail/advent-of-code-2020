def execute(op, arg, acc, ip):	
	if op == 'jmp':
		return acc, ip+arg
	
	if op == 'acc':
		return acc+arg, ip+1
	
	if op == 'nop':
		return acc, ip+1

def main():
	with open('input.txt') as f:
		instructions = [(lambda x, y: (x, int(y)))(*line.split()) for line in f]
	
	acc = 0
	ip = 0
	executed = []
	
	while ip not in executed:
		executed.append(ip)
		acc, ip = execute(*instructions[ip], acc, ip)
	
	print(acc)

if __name__ == '__main__':
	main()