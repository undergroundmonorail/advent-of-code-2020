import re

def is_valid(lower, upper, character, password):
	return int(lower) <= password.count(character) <= int(upper)

def main():
	with open('input.txt') as f:
		print(sum((is_valid(*(re.findall(r'(\d+)-(\d+) (.): (.+)', line)[0])) for line in f)))

if __name__ == '__main__':
	main()