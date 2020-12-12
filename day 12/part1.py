import re
from enum import IntEnum

class Direction(IntEnum):
	NORTH = 0
	EAST = 90
	SOUTH = 180
	WEST = 270

def main():
	x, y = 0, 0
	direction = Direction.EAST
	
	with open('input.txt') as f:
		for line in f:
			action, units = re.findall(r'(\w)(\d+)', line)[0]
			units = int(units)
			
			if action == 'N':
				y += units
			if action == 'S':
				y -= units
			if action == 'E':
				x += units
			if action == 'W':
				x -= units
			if action == 'L':
				direction = Direction((direction - units) % 360)
			if action == 'R':
				direction = Direction((direction + units) % 360)
			if action == 'F':
				if direction == Direction.NORTH:
					y += units
				if direction == Direction.EAST:
					x += units
				if direction == Direction.SOUTH:
					y -= units
				if direction == Direction.WEST:
					x -= units
	
	print(abs(x) + abs(y))

if __name__ == '__main__':
	main()