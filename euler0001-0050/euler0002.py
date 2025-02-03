import timeit
import pathlib

def problem0002():
	x: int = 1
	y: int = 2
	even_sum = 0
	while y < 4_000_000:
		if y % 2 == 0:
			even_sum += y
		x, y = y, x + y
	return even_sum


if __name__ == '__main__':
	print(problem0002())
	time = timeit.timeit(problem0002, number=1_000_000)
	with open(str(pathlib.Path(__file__).parent.parent) + '/results.csv', 'a') as file:
		file.write('\n' + str(pathlib.Path(__file__).name) + ', ' + str(time / 1_000_000) + '\n')
