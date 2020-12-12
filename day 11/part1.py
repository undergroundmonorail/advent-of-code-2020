import itertools
import re

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
		
		for dx, dy in coords:
			if self.x + dx in (-1, len(self.board[self.y])):
				continue
			
			if self.y + dy in (-1, len(self.board)):
				continue
			
			yield self.board[self.y+dy][self.x+dx]
	
	def calculate(self):
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
			board.append([LifeLikeCell(board, x, y, 'B0/S0123' if c == 'L' else 'B/S') for x, c in zip(itertools.count(), line.strip())])
	
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