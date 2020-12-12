import re

def iter_mul(it, n):
	return map(lambda c: c*n, it)

def iter_add(*args):
	return map(sum, zip(*args))

def turn_left(x, y):
	return (-y, x)

def turn_right(x, y):
	return (y, -x)

def main():
	x, y = 0, 0
	wx, wy = 10, 1
	
	with open('input.txt') as f:
		for line in f:
			action, units = re.findall(r'(\w)(\d+)', line)[0]
			units = int(units)
			
			if action == 'N':
				wy += units
			if action == 'S':
				wy -= units
			if action == 'E':
				wx += units
			if action == 'W':
				wx -= units
			if action == 'L':
				for _ in range(units // 90):
					wx, wy = turn_left(wx, wy)
			if action == 'R':
				for _ in range(units // 90):
					wx, wy = turn_right(wx, wy)
			if action == 'F':
				x, y = iter_add((x, y), iter_mul((wx, wy), units))
	
	print(abs(x) + abs(y))

if __name__ == '__main__':
	main()