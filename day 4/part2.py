import re

def is_valid(passport):
	def safe_int(*args):
		try: return int(*args)
		except: return -1
	
	def validate_height(height):
		if height is None: return False
		
		if (m := re.match(r'(\d+)(\w+)', height)):
			if m[2] == 'in':
				return 59 <= int(m[1]) <= 76
			if m[2] == 'cm':
				return 150 <= int(m[1]) <= 193
		return False
	
	def validate_hair_colour(colour):
		if colour is None: return False
		
		return re.match(r'#[0-9a-f]{6}', colour)
	
	return bool(1920 <= safe_int(passport.get('byr', -1)) <= 2002
		and 2010 <= safe_int(passport.get('iyr', -1)) <= 2020
		and 2020 <= safe_int(passport.get('eyr', -1)) <= 2030
		and validate_height(passport.get('hgt'))
		and validate_hair_colour(passport.get('hcl'))
		and passport.get('ecl') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
		and safe_int(passport.get('pid')) != -1 and len(passport.get('pid')) == 9
	)

def passport(raw):
	return dict((field.split(':') for field in raw.split()))

def main():
	with open('input.txt') as f:
		print(sum((is_valid(passport(passport_raw)) for passport_raw in f.read().split('\n\n'))))

if __name__ == '__main__':
	main()