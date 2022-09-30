from common import avg_time


def order_process(process):
	process.sort(key= lambda process:process[2])
	return process

def main():

	process=[[1, 0, 3], [2, 0, 4], [3, 0, 5], [4, 0, 1], [5, 0, 2]]

	process= order_process(process)
	avg_time(process)

if __name__=='__main__':
	main()