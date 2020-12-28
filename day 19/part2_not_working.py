# this doesn't work for some reason
# i think there's a bug in my rule 8 code because i already fixed a problem in my rule 11
# code and it seems too simple to have another

import regex
import functools

def parse_rule(r):
	def parse_subrule(s):
		if (m := regex.search(r'"(.)"', s)):
			return m.group(1)
		
		return tuple(map(int, s.split(' ')))
	
	num, text = r.split(': ')
	subrules = [parse_subrule(s) for s in text.split(' | ')]
	return int(num), subrules

def to_regex(r, rules):
	def handle_subrule(s):
		if isinstance(s, str):
			return s
		
		return ''.join((f'(?:{to_regex(rule_id, rules)})' for rule_id in s))
	
	# the part 2 instructions basically give you permission to hardcode a little bit
	#
	# "Remember, you only need to handle the rules you have; building a solution that
	# could handle any hypothetical combination of rules would be [significantly more
	# difficult](https://en.wikipedia.org/wiki/Formal_grammar)."
	#
	# maybe i'll look at formal grammar later. not today
	
	if r == 8:
		return f'(?P<rule8>{handle_subrule((42,))}(?&rule8)?)'
	
	if r == 11:
		return f'(?P<rule11>{to_regex(42, rules)}(?&rule11)?{to_regex(31, rules)})'
	
	return '|'.join((handle_subrule(s) for s in rules[r]))

def main():
	with open('input.txt') as f:
		raw_rules, messages = [s.split('\n') for s in f.read().strip().split('\n\n')]
	rules = dict(parse_rule(s) for s in raw_rules)
	
	# as dictated by part 2 instructions
	rules |= dict(parse_rule(s) for s in ('8: 42 | 42 8', '11: 42 31 | 42 11 31'))
	
	rule_0 = regex.compile(to_regex(0, rules))
	print(sum((bool(rule_0.fullmatch(m)) for m in messages)))

if __name__ == '__main__':
	main()