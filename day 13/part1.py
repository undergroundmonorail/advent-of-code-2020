import re
import math

def departure_time(start_time, bus):
	return (math.floor(start_time / bus) + bool(start_time % bus)) * bus

def main():
	with open('input.txt') as f:
		start_time, *busses = (int(n) for n in re.split(r',|\n', f.read().strip()) if n != 'x')
	
	print(math.prod(min((((bus, departure_time(start_time, bus) - start_time) for bus in busses)), key=lambda t:t[1])))

if __name__ == '__main__':
	main()