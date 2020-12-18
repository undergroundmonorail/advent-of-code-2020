import re
import functools
import itertools

def parse_ticket(raw_ticket):
	return tuple(map(int, raw_ticket.split(',')))

def parse_rules(field_rules):
	for rule in field_rules:
		a, b, c, d = map(int, re.findall(r'(\d+)-(\d+) or (\d+)-(\d+)', rule)[0])
		
		yield lambda n, a=a, b=b, c=c, d=d: a <= n <= b or c <= n <= d

def ticket_validator(ticket, rules):
	return sum(field for field in ticket if not any((rule(field) for rule in rules)))

def main():
	with open('input.txt') as f:
		field_rules, my_ticket, nearby_tickets = re.split(r'\n\n.+:\n', f.read().strip())
	my_ticket = parse_ticket(my_ticket)
	nearby_tickets = [parse_ticket(t) for t in nearby_tickets.split('\n')]
	
	rules = tuple(parse_rules(field_rules.split('\n')))
	
	is_valid = functools.partial(ticket_validator, rules=rules)
	
	print(sum(map(is_valid, nearby_tickets)))

if __name__ == '__main__':
	main()