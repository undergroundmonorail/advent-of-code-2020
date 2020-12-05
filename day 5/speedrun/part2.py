def seat(line):
			row, seat = line[:7], line[7:]
			
			rows = list(range(128))
			
			for c in row:
				if c == 'F': rows = rows[:len(rows) // 2]
				if c == 'B': rows = rows[len(rows) // 2:]
			
			seats = list(range(8))
			for c in seat:
				if c == 'L': seats = seats[:len(seats) // 2]
				if c == 'R': seats = seats[len(seats) // 2:]

			return rows[0] * 8 + seats[0]

def main():
	with open('input.txt') as f:
		ids = (list(seat(line) for line in f))
		
		for i in range(999999):
			if (i-1) in ids and (i+1) in ids and i not in ids:
				print(i)
				break

if __name__ == '__main__':
	main()