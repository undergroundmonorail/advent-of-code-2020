def num_yes(answers):
	return len(set(answers.replace('\n', '')))

def main():
	with open('input.txt') as f:
		print(sum(map(num_yes, f.read().split('\n\n'))))

if __name__ == '__main__':
	main()