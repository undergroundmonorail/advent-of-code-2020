import operator

def solve(problem):
	parens = []
	paren_depth = 0
	
	for n, e in enumerate(problem):
		if e == '(':
			if paren_depth == 0:
				paren_start = n
			
			paren_depth += 1
		
		if e == ')':
			paren_depth -= 1
			
			if paren_depth == 0:
				parens.append((paren_start, n))
	
	for start, stop in parens[::-1]:
		problem[start:stop+1] = [solve(problem[start+1:stop])]
	
	while '+' in problem:
		i = problem.index('+')
		a, _, b = problem[i-1:i+2]
		problem[i-1:i+2] = [a + b]
	
	while '*' in problem:
		i = problem.index('*')
		a, _, b = problem[i-1:i+2]
		problem[i-1:i+2] = [a * b]
	
	return problem[0]

def main():
	with open('input.txt') as f:
		print(sum((solve([int(c) if c.isdigit() else c for c in line if c not in ' \n']) for line in f)))

if __name__ == '__main__':
	main()