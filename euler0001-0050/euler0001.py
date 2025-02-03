import timeit
import pathlib

def problem0001():
	return sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)

if __name__ == '__main__':
	print(problem0001())
	time = timeit.timeit(problem0001, number=1_000_000)
	with open(str(pathlib.Path(__file__).parent.parent) + '/results.csv', 'a') as file:
		file.write(str(pathlib.Path(__file__).name) + ', ' + str(time / 1_000_000) + '\n')
