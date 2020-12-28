# my first attempt, kept for posterity because i think it works despite being ridiculously slow

import re
import functools

rules = {}

def parse_rule(r):
	def parse_subrule(s):
		if (m := re.search(r'"(.)"', s)):
			return m.group(1)
		
		return tuple(map(int, s.split(' ')))
	
	num, text = r.split(': ')
	subrules = [parse_subrule(s) for s in text.split(' | ')]
	return int(num), subrules

@functools.cache
def partial_match(message, rule):
	"""Return list of possible suffixes after removing a prefix from message that matches rule"""
	
	ret = []
	
	subrules = rules[rule]
	for s in subrules:
		if isinstance(s, str):
			if message.startswith(s):
				ret.append(message[len(s):])
		else:
			curr = [message]
			next = []
			for r in s:
				next.extend([partial_match(m, r) for m in curr])
				# flatten list
				curr = sum(next, [])
			ret.extend(curr)
	
	return ret

def full_match(message, rule):
	return '' in partial_match(message, rule)

def main():
	with open('input.txt') as f:
		raw_rules, messages = [s.split('\n') for s in f.read().strip().split('\n\n')]
	global rules
	rules = dict(parse_rule(s) for s in raw_rules)
	
	print(sum((full_match(message, 0) for message in messages)))

if __name__ == '__main__':
	main()