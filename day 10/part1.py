import math

def iter_add(*args):
	return map(sum, zip(*args))

def main():
	with open('input.txt') as f:
		chain = sorted((int(n) for n in f))
	
	chain = [0] + chain + [max(chain) + 3]
	
	print(math.prod(iter_add(*(((b-a==1), (b-a==3)) for a, b in zip(chain[:-1], chain[1:])))))
	

if __name__ == '__main__':
	main()