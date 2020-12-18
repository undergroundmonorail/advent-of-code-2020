import re
import math
import functools
import itertools
import collections

def parse_ticket(raw_ticket):
	return tuple(map(int, raw_ticket.split(',')))

def parse_rules(field_rules):
	for rule in field_rules:
		name = rule.split(':')[0]
		a, b, c, d = map(int, re.findall(r'(\d+)-(\d+) or (\d+)-(\d+)', rule)[0])
		
		yield (name, lambda n, a=a, b=b, c=c, d=d: a <= n <= b or c <= n <= d)

def ticket_validator(ticket, rules):
	return all((any((rule(field) for name, rule in rules)) for field in ticket))

def main():
	with open('input.txt') as f:
		field_rules, my_ticket, nearby_tickets = re.split(r'\n\n.+:\n', f.read().strip())
	my_ticket = parse_ticket(my_ticket)
	
	rules = tuple(parse_rules(field_rules.split('\n')))
	is_valid = functools.partial(ticket_validator, rules=rules)
	
	nearby_tickets = [parse_ticket(t) for t in nearby_tickets.split('\n') if is_valid(parse_ticket(t))]
	
	rule_possibilities = collections.defaultdict(list)
	known_rules = {}
	
	for name, rule in rules:
		for n, values in enumerate(zip(*nearby_tickets)):
			if all((rule(value) for value in values)):
				rule_possibilities[name].append(n)
	
	while rule_possibilities and len((m := min(rule_possibilities.items(), key=lambda r: len(r[1])))[1]) == 1:
		n, r = m
		known_rules[n] = r[0]
		del rule_possibilities[n]
		for p in rule_possibilities.values():
			if r[0] in p:
				p.remove(r[0])
	
	if rule_possibilities:
		# i thought i was going to have to write code for this case but i guess i don't
		pass
	
	print(math.prod((my_ticket[v] for k, v in known_rules.items() if k.startswith('departure'))))


if __name__ == '__main__':
	main()