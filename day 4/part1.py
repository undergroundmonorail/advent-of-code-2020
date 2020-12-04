def is_valid(passport):
	return ('byr' in passport
		and 'iyr' in passport
		and 'eyr' in passport
		and 'hgt' in passport
		and 'hcl' in passport
		and 'ecl' in passport
		and 'pid' in passport
		# and 'cid' in passport # don't mind me :)
	)

def passport(raw):
	return dict((field.split(':') for field in raw.split()))

def main():
	with open('input.txt') as f:
		print(sum((is_valid(passport(passport_raw)) for passport_raw in f.read().split('\n\n'))))

if __name__ == '__main__':
	main()