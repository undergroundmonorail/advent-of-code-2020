import collections

def parse_line(l):
	ingredients, allergens = l.strip()[:-1].split(' (contains ')
	return frozenset(ingredients.split(' ')), frozenset(allergens.split(', '))

def main():
	ingredients = set()
	allergens = set()
	
	labels_with = collections.Counter()
	
	with open('input.txt') as f:
		labels = dict(map(parse_line, f))
	
	for k, v in labels.items():
		ingredients.update(k)
		allergens.update(v)
		
		for i in k:
			labels_with[i] += 1
	
	could_be = {i:allergens.copy() for i in ingredients}
	
	for k, v in labels.items():
		for impossible in ingredients - k:
			could_be[impossible] -= v
	
	print(sum((v for k, v in labels_with.items() if not could_be[k])))

if __name__ == '__main__':
	main()