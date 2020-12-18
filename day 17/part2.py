import re

class LifeLikeCell:
	rule_pattern = re.compile(r'B(\d*)/S(\d*)')
	
	def __init__(self, board, x, y, z, w, rule, state=False):
		self.board = board
		self.x = x
		self.y = y
		self.z = z
		self.w = w
		
		self.rule = rule
		if not self.rule_pattern.fullmatch(rule):
			raise ValueError('`rule` argument must be in Golly/RLE format')
		self.b, self.s = [(tuple(map(int, b)), tuple(map(int, s))) for b, s in self.rule_pattern.findall(rule)][0]
		
		self.state = state
		self.next = state
	
	def get_neighbours(self):
		coords = [(a, b, c, d) for a in range(-1, 2) for b in range(-1, 2) for c in range(-1, 2) for d in range(-1, 2)]
		
		for dx, dy, dz, dw in coords:
			if self.w + dw in (-1, len(self.board)):
				continue
			
			if self.z + dz in (-1, len(self.board[self.w])):
				continue
			
			if self.y + dy in (-1, len(self.board[self.w][self.z])):
				continue
				
			if self.x + dx in (-1, len(self.board[self.w][self.z][self.y])):
				continue
			
			if dx == dy == dz == dw == 0:
				continue
			
			yield self.board[self.w+dw][self.z+dz][self.y+dy][self.x+dx]
	
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
		return f'LifeLikeCell(board, {self.x}, {self.y}, {self.z}, {self.w}, {self.rule}, {self.state})'
	
	def __radd__(self, other):
		return self.state + other

def pad_cells(cells, n):
	cells = (('.'*len(cells.split('\n')[0]) + '\n')*n + cells + ('.'*len(cells.split('\n')[0]) + '\n')*n).strip()
	cells = ['.'*n + row + '.'*n for row in cells.split()]
	
	empty_plane = ['.'*len(cells[0]) for _ in cells]
	
	empty_cube = [empty_plane]*(n+n+1)
	
	return [empty_cube]*n + [[empty_plane]*n + [cells] + [empty_plane]*n] + [empty_cube]*n

def main():
	with open('input.txt') as f:
		cells = pad_cells(f.read(), 6)
	
	board = [[[[] for row in plane] for plane in cube] for cube in cells]
	
	for w, cube in enumerate(cells):
		for z, plane in enumerate(cube):
			for y, row in enumerate(plane):
				for x, cell in enumerate(row):
					board[w][z][y].append(LifeLikeCell(board, x, y, z, w, 'B3/S23', cell == '#'))
	
	for _ in range(6):
		for cube in board:
			for plane in cube:
				for row in plane:
					for cell in row:
						cell.calculate()
		
		for cube in board:
			for plane in cube:
				for row in plane:
					for cell in row:
						cell.tick()
	
	print(sum((cell for cube in board for plane in cube for row in plane for cell in row)))

if __name__ == '__main__':
	main()