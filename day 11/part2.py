import itertools
import re
import math

class LifeLikeCell:
	rule_pattern = re.compile(r'B(\d*)/S(\d*)')
	
	def __init__(self, board, x, y, rule, state=False):
		self.board = board
		self.x = x
		self.y = y
		
		self.rule = rule
		if not self.rule_pattern.fullmatch(rule):
			raise ValueError('`rule` argument must be in Golly/RLE format')
		self.b, self.s = [(tuple(map(int, b)), tuple(map(int, s))) for b, s in self.rule_pattern.findall(rule)][0]
		
		self.state = state
		self.next = state
	
	def get_neighbours(self):
		def tuple_prod(t, n):
			return map(math.prod, zip(t, itertools.repeat(n)))
	
		coords = (
			(-1, -1),
			(0,  -1),
			(1,  -1),
			(-1, 0),
			(1,  0),
			(-1, 1),
			(0,  1),
			(1,  1),
		)
		
		for coord in coords:
			for n in itertools.count(1):
				dx, dy = tuple_prod(coord, n)
				
				if self.x + dx in (-1, len(self.board[self.y])):
					break
				
				if self.y + dy in (-1, len(self.board)):
					break
				
				if (cell := self.board[self.y+dy][self.x+dx]).rule == self.rule:
					yield cell
					break
	
	def calculate(self):
		if not self.b:
			self.next = False
			return
		
		living_neighbours = sum(self.get_neighbours())
		if living_neighbours in self.b:
			self.next = True
		elif living_neighbours in self.s:
			self.next = self.state
		else:
			self.next = False
	
	def tick(self):
		self.state = self.next
	
	def __str__(self):
		return '[]' if self.state else '  '
	
	def __repr__(self):
		return f'LifeLikeCell(board, {self.x}, {self.y}, {self.rule}, {self.state})'
	
	def __radd__(self, other):
		return self.state + other

board = []

def get_states():
	return [cell.state for row in board for cell in row]

def main():
	with open('input.txt') as f:
		for y, line in enumerate(f):
			board.append([LifeLikeCell(board, x, y, 'B0/S01234' if c == 'L' else 'B/S') for x, c in zip(itertools.count(), line.strip())])
	
	prev = None
	while (state := get_states()) != prev:
		prev = state
		for row in board:
			for cell in row:
				cell.calculate()
		for row in board:
			for cell in row:
				cell.tick()
	
	print(sum(prev))

if __name__ == '__main__':
	main()