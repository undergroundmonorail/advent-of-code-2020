import re

def is_valid(lower, upper, character, password):
	return (password[int(lower)-1] == character) != (password[int(upper)-1] == character)

def main():
	with open('input.txt') as f:
		print(sum((is_valid(*(re.findall(r'(\d+)-(\d+) (.): (.+)', line)[0])) for line in f)))

if __name__ == '__main__':
	main()