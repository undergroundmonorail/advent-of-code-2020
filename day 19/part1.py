import re
import functools

def parse_rule(r):
	def parse_subrule(s):
		if (m := re.search(r'"(.)"', s)):
			return m.group(1)
		
		return tuple(map(int, s.split(' ')))
	
	num, text = r.split(': ')
	subrules = [parse_subrule(s) for s in text.split(' | ')]
	return int(num), subrules

def to_regex(r, rules):
	def handle_subrule(s):
		if isinstance(s, str):
			return s
		
		return ''.join((f'({to_regex(rule_id, rules)})' for rule_id in s))
	
	return '|'.join((handle_subrule(s) for s in rules[r]))

def main():
	with open('input.txt') as f:
		raw_rules, messages = [s.split('\n') for s in f.read().strip().split('\n\n')]
	rules = dict(parse_rule(s) for s in raw_rules)
	
	rule_0 = re.compile(to_regex(0, rules))
	print(sum((bool(rule_0.fullmatch(m)) for m in messages)))

if __name__ == '__main__':
	main()