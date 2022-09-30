from common import display, turn_time


def waiting_time(process, wait_time, quantum):
    n = len(process)
    rem_burst_time = [0] * n

    for i in range(n):
        rem_burst_time[i] = process[i][2]

    current_t = 0

    while True:
        flag = True

        for i in range(n):

            if rem_burst_time[i] > 0:
                flag = False
                if rem_burst_time[i] > quantum:
                    current_t += quantum
                    rem_burst_time[i] -= quantum

                else:
                    current_t += rem_burst_time[i]
                    wait_time[i] = current_t - process[i][2]
                    rem_burst_time[i] = 0

        if flag:
            break


def avg_time(process, quantum):
    n = len(process)
    wait_time = [0] * n
    turn_around_time = [0] * n
    total_wait_time = 0
    total_turn_around_time = 0

    waiting_time(process, wait_time, quantum)
    turn_time(process, wait_time, turn_around_time)

    for i in range(n):
        total_wait_time = total_wait_time + wait_time[i]

    for i in range(n):
        total_turn_around_time = total_turn_around_time + turn_around_time[i]

    avg_wait_time = total_wait_time / n
    avg_turn_around_time = total_turn_around_time / n

    display(process, wait_time, turn_around_time, avg_wait_time, avg_turn_around_time)


def main():
    process = [[1, 0, 10], [2, 1, 5], [3, 2, 8]]
    quantum = 2

    avg_time(process, quantum)


if __name__ == '__main__':
    main()
