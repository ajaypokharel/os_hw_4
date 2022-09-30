
def waiting_time(process, wait_time):
	n = len(process)
	wait_time[0] = 0
	for i in range(1, n):
		wait_time[i] = process[i-1][2] + wait_time[i-1]

def turn_time(process, wait_time, turn_around_time):
	for i in range(len(process)):
		turn_around_time[i] = process[i][2] + wait_time[i]

def avg_time(process):
	n = len(process)
	wait_time = [0] * n
	turn_around_time = [0] * n
	total_wait_time = 0
	total_turn_around_time = 0

	waiting_time(process, wait_time)
	turn_time(process, wait_time, turn_around_time)

	for i in range(n):
		total_wait_time = total_wait_time + wait_time[i]

	for i in range(n):
		total_turn_around_time = total_turn_around_time + turn_around_time[i]

	average_wait_time = total_wait_time/n
	avg_turn_around_time = total_turn_around_time/n

	display(process, wait_time, turn_around_time, average_wait_time, avg_turn_around_time)


# for visual representation of the result and input
def display(process, wait_time, turn_around_time, average_wait_time, avg_turn_around_time):
	print('Process\t Arrival Time\t Burst Time\t Waiting Time\t Turn Around Time')

	for i in range(len(process)):
		print('{}\t {}\t\t {}\t\t {}\t\t {}'
        .format(process[i][0], process[i][1], process[i][2], wait_time[i], turn_around_time[i]))

	print('\nAverage Waiting Time: ', average_wait_time)
	print('Average Turn Around: ', avg_turn_around_time)

