def num_yes(answers):
	first, *rest = answers.split('\n')
	return sum((all((c in a for a in rest)) for c in first))

def main():
	with open('input.txt') as f:
		print(sum(map(num_yes, f.read().strip().split('\n\n'))))

if __name__ == '__main__':
	main()