from common import avg_time


def main():

	process=[[1, 0, 3, 4], [2, 0, 4, 2], [3, 0, 5, 3], [4, 0, 1, 1], [5, 0, 2, 5]]

	process.sort(key= lambda x:x[3])
	avg_time(process)

if __name__=='__main__':
	main()