import re

def parse_bags(bags):
	return tuple(map(lambda b: (b[1], int(b[0])), re.findall(r'(\d+) (\w+ \w+) bags?', bags)))

def main():
	bag_tree = {}
	bags = {}
	
	def num_bags(bag, num=1):
		if bag not in bags:
			# add 1 to count the bag we're currently looking at
			bags[bag] = sum((num_bags(*inner) for inner in bag_tree[bag])) + 1
	
		return bags[bag] * num
	
	with open('input.txt') as f:
		for line in f:
			outer, inner = line.split(' bags contain ')
			bag_tree[outer] = parse_bags(inner)
	
	# subtract 1 to not count the outer bag
	print(num_bags('shiny gold') - 1)

if __name__ == '__main__':
	main()