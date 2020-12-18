import re
import math

def find_working_time(busses):
	# Chinese Remainder Theorem guarantees that one exists, so we use an algorithm based on it to find it
	# this video was a huge help for me: https://www.youtube.com/watch?v=zIFehsBHB8o
	
	N = math.prod((bus_id for offset, bus_id in busses))
	
	def get_intermediary(offset, bus_id):
		# offsets
		bi = -offset % bus_id
		
		# product of all other bus ids
		Ni = N // bus_id
		
		# invert of Ni (mod bus id)
		xi = pow(Ni, -1, bus_id)
		
		return bi * Ni * xi
	
	return sum((get_intermediary(*bus) for bus in busses)) % N

def parse_busses(s):
	return tuple((n, int(bus)) for n, bus in enumerate(s.split(',')) if bus not in 'x\n')

def main():
	with open('input.txt') as f:
		busses = parse_busses(f.readlines()[1])
	
	print(find_working_time(busses))

if __name__ == '__main__':
	main()