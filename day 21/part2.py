def parse_line(l):
	ingredients, allergens = l.strip()[:-1].split(' (contains ')
	return frozenset(ingredients.split(' ')), frozenset(allergens.split(', '))

def main():
	ingredients = set()
	allergens = set()
	
	with open('input.txt') as f:
		labels = dict(map(parse_line, f))
	
	for k, v in labels.items():
		ingredients.update(k)
		allergens.update(v)
	
	could_be = {i:allergens.copy() for i in ingredients}
	
	for k, v in labels.items():
		for impossible in ingredients - k:
			could_be[impossible] -= v
	
	could_be = dict((k,v) for k, v in could_be.items() if v)
	
	certain = {}
	
	while could_be:
		known_ingredient, known_allergen = min(could_be.items(), key=(lambda e:len(e[1])))
		assert(len(known_allergen) == 1)
		
		del could_be[known_ingredient]
		for allergen_set in could_be.values():
			allergen_set -= known_allergen
		
		certain[known_ingredient] = known_allergen.pop()
	
	print(','.join((k for k, v in sorted(certain.items(), key=lambda e:e[1]))))

if __name__ == '__main__':
	main()