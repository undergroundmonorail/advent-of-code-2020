import re

def parse_bags(bags):
	return tuple(map(lambda b: (b[1], int(b[0])), re.findall(r'(\d+) (\w+ \w+) bags?', bags)))

def main():
	bag_tree = {}
	bags = {
		'shiny gold': 1,
	}
	
	def num_gold(bag, num=1):
		if bag not in bags:
			bags[bag] = sum((num_gold(*inner) for inner in bag_tree[bag]))
	
		return bags[bag] * num
	
	with open('input.txt') as f:
		for line in f:
			outer, inner = line.split(' bags contain ')
			bag_tree[outer] = parse_bags(inner)
	
	for bag in bag_tree:
		bags[bag] = num_gold(bag)
	
	del bags['shiny gold']
	print(sum((bool(n) for n in bags.values())))

if __name__ == '__main__':
	main()