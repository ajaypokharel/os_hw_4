from common import avg_time

def main():

	process=[[1, 0, 3], [2, 0, 4], [3, 0, 5], [4, 0, 1], [5, 0, 2]]

	process.sort(key= lambda x:x[1])
	avg_time(process)

if __name__=='__main__':
	main()