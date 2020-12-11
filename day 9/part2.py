import itertools

def find_sum(all_nums, target):
	for l in itertools.count(2):
		for chunk in [all_nums[i:i+l] for i in range(len(all_nums) - l)]:
			if sum(chunk) == target:
				return min(chunk) + max(chunk)

def main():
	buffer = []

	with open('input.txt') as f:
		all_nums = [int(line) for line in f]
	
	for num in all_nums:
		if len(buffer) < 25:
			buffer.append(num)
			continue
		
		if not any((sum(t) == num for t in itertools.combinations(buffer, 2))):
			invalid = num
			break
			
		buffer = buffer[1:] + [num]
	
	print(find_sum(all_nums, invalid))

if __name__ == '__main__':
	main()