
'''
    Write a program to implement FCFS scheduling with arrival time.
'''


from prettytable import PrettyTable

time = 0
processes = []
ID = 0

table = PrettyTable()
table.field_names = ["Process" , "Arrival Time" , "Burst Time" , "Completion Time" , "Turn-around Time" , "Waiting Time"   ]

class Process:
    def __init__(self,id,arrival,burst):
        self.id = id
        self.ArrivalTime = arrival
        self.BurstTime = burst
        self.CompletionTime = int()
        self.TurnAroundTime = int()
        self.WaitingTime = int()

    def SetCompletionTime(self,time):
        self.CompletionTime = time
    
    def SetTurnAroundTime(self):
        self.TurnAroundTime = self.CompletionTime - self.ArrivalTime

    def SetWaitingTime(self):
        self.WaitingTime = self.TurnAroundTime - self.BurstTime


def createProcess():
    global ID,processes

    ID += 1
    id =ID

    print(f'Process {ID}')
    arrival = int(input(f'Enter the arrival time of the process {ID} :- '))
    burst = int(input(f'Enter the burst time of the process {ID} :- '))
    
    print()

    p = Process(id,arrival,burst)
    processes.append(p)

def sortProcesses():
    global processes
    processes.sort(key=(lambda x : x.ArrivalTime))

def print_table():
    global processes,table

    avgWaitingTime = sum(process.WaitingTime for process in processes) / len(processes)
    avgTurnAroundTime = sum(process.TurnAroundTime for process in processes) / len(processes)

    for process in processes:
        table.add_row([
            process.id,
            process.ArrivalTime,
            process.BurstTime,
            process.CompletionTime,
            process.TurnAroundTime,
            process.WaitingTime,
        ])

    print(table)
    print("Average waiting time: " + str(format(avgWaitingTime, '.5f')))
    print("Average turn-around time: " + str(format(avgTurnAroundTime, '.5f')))



def sortProcessesOnId():
    global processes
    processes.sort(key=lambda x: x.id)

def executeProcesses():
    global processes, time

    for process in processes:

        if time < process.ArrivalTime:
            time = process.ArrivalTime
        time += process.BurstTime
        process.SetCompletionTime(time)
        process.SetTurnAroundTime()
        process.SetWaitingTime()


def main():

    print("\n Jishnu Jagadeesh P I \n")
    N = int(input("Enter the number of processes: "))
    print()

    for i in range(N):
        createProcess()
    sortProcesses()
    executeProcesses()
    sortProcessesOnId()
    print_table()


main()



'''

Sample 1:

    Enter the number of processes: 3

    Process 1
    Enter the arrival time of the process 1 :- 0
    Enter the burst time of the process 1 :- 5

    Process 2
    Enter the arrival time of the process 2 :- 3
    Enter the burst time of the process 2 :- 9

    Process 3
    Enter the arrival time of the process 3 :- 6
    Enter the burst time of the process 3 :- 6

    +---------+--------------+------------+-----------------+------------------+--------------+
    | Process | Arrival Time | Burst Time | Completion Time | Turn-around Time | Waiting Time |
    +---------+--------------+------------+-----------------+------------------+--------------+
    |    1    |      0       |     5      |        5        |        5         |      0       |
    |    2    |      3       |     9      |        14       |        11        |      2       |
    |    3    |      6       |     6      |        20       |        14        |      8       |
    +---------+--------------+------------+-----------------+------------------+--------------+
    Average waiting time: 3.33333
    Average turn-around time: 10.00000

Sample 2:

    Enter the number of processes: 4

    Process 1
    Enter the arrival time of the process 1 :- 0
    Enter the burst time of the process 1 :- 2

    Process 2
    Enter the arrival time of the process 2 :- 1
    Enter the burst time of the process 2 :- 2

    Process 3
    Enter the arrival time of the process 3 :- 5
    Enter the burst time of the process 3 :- 3

    Process 4
    Enter the arrival time of the process 4 :- 6
    Enter the burst time of the process 4 :- 4

    +---------+--------------+------------+-----------------+------------------+--------------+
    | Process | Arrival Time | Burst Time | Completion Time | Turn-around Time | Waiting Time |
    +---------+--------------+------------+-----------------+------------------+--------------+
    |    1    |      0       |     2      |        2        |        2         |      0       |
    |    2    |      1       |     2      |        4        |        3         |      1       |
    |    3    |      5       |     3      |        8        |        3         |      0       |
    |    4    |      6       |     4      |        12       |        6         |      2       |
    +---------+--------------+------------+-----------------+------------------+--------------+
    Average waiting time: 0.75000
    Average turn-around time: 3.50000

Sample 3:

    Enter the number of processes: 5

    Process 1
    Enter the arrival time of the process 1 :- 2
    Enter the burst time of the process 1 :- 2

    Process 2
    Enter the arrival time of the process 2 :- 0
    Enter the burst time of the process 2 :- 1

    Process 3
    Enter the arrival time of the process 3 :- 2
    Enter the burst time of the process 3 :- 3

    Process 4
    Enter the arrival time of the process 4 :- 3
    Enter the burst time of the process 4 :- 5

    Process 5
    Enter the arrival time of the process 5 :- 4
    Enter the burst time of the process 5 :- 4

    +---------+--------------+------------+-----------------+------------------+--------------+
    | Process | Arrival Time | Burst Time | Completion Time | Turn-around Time | Waiting Time |
    +---------+--------------+------------+-----------------+------------------+--------------+
    |    1    |      2       |     2      |        4        |        2         |      0       |
    |    2    |      0       |     1      |        1        |        1         |      0       |
    |    3    |      2       |     3      |        7        |        5         |      2       |
    |    4    |      3       |     5      |        12       |        9         |      4       |
    |    5    |      4       |     4      |        16       |        12        |      8       |
    +---------+--------------+------------+-----------------+------------------+--------------+
    Average waiting time: 2.80000
    Average turn-around time: 5.80000

'''