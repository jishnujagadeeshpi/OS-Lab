
'''
    Write a program to implement SJF scheduling with arrival time(Non pre-emptive).
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
    processes.sort(key=(lambda x : [ x.ArrivalTime , x.BurstTime ]))

def sortProcessesOnId():
    global processes
    processes.sort(key=lambda x: x.id)

def sortProcessesOnBurst(processes):
    processes.sort(key=lambda x: x.BurstTime)
    return processes

def executeProcesses():
    global processes, time
    completedProcesses = []
    availableProcesses = []
    availableProcesses += [processes[0]]
    curProcess = availableProcesses[0]
    time = curProcess.ArrivalTime
    
    while len(availableProcesses) > 0:
        curProcess = availableProcesses[0]
        processes.remove(curProcess)

        if time < curProcess.ArrivalTime:
            time = curProcess.ArrivalTime
    
        time += curProcess.BurstTime
        curProcess.SetCompletionTime(time)
        curProcess.SetTurnAroundTime()
        curProcess.SetWaitingTime()
        completedProcesses += [curProcess]

        availableProcesses = [process for process in processes if process.ArrivalTime <= time]
        availableProcesses = sortProcessesOnBurst(availableProcesses)    

    processes = completedProcesses


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

    Enter the number of processes: 5

    Process 1
    Enter the arrival time of the process 1 :- 3
    Enter the burst time of the process 1 :- 1

    Process 2
    Enter the arrival time of the process 2 :- 1
    Enter the burst time of the process 2 :- 4

    Process 3
    Enter the arrival time of the process 3 :- 4
    Enter the burst time of the process 3 :- 2

    Process 4
    Enter the arrival time of the process 4 :- 0
    Enter the burst time of the process 4 :- 6

    Process 5
    Enter the arrival time of the process 5 :- 2
    Enter the burst time of the process 5 :- 3
    +---------+--------------+------------+-----------------+------------------+--------------+
    | Process | Arrival Time | Burst Time | Completion Time | Turn-around Time | Waiting Time |
    +---------+--------------+------------+-----------------+------------------+--------------+
    |    1    |      3       |     1      |        7        |        4         |      3       |
    |    2    |      1       |     4      |        16       |        15        |      11      |
    |    3    |      4       |     2      |        9        |        5         |      3       |
    |    4    |      0       |     6      |        6        |        6         |      0       |
    |    5    |      2       |     3      |        12       |        10        |      7       |
    +---------+--------------+------------+-----------------+------------------+--------------+
    Average waiting time: 4.80000
    Average turn-around time: 8.00000

Sample 2:

    Enter the number of processes: 4

    Process 1
    Enter the arrival time of the process 1 :- 1
    Enter the burst time of the process 1 :- 3

    Process 2
    Enter the arrival time of the process 2 :- 2
    Enter the burst time of the process 2 :- 4

    Process 3
    Enter the arrival time of the process 3 :- 1
    Enter the burst time of the process 3 :- 2

    Process 4
    Enter the arrival time of the process 4 :- 4
    Enter the burst time of the process 4 :- 4

    +---------+--------------+------------+-----------------+------------------+--------------+
    | Process | Arrival Time | Burst Time | Completion Time | Turn-around Time | Waiting Time |
    +---------+--------------+------------+-----------------+------------------+--------------+
    |    1    |      1       |     3      |        6        |        5         |      2       |
    |    2    |      2       |     4      |        10       |        8         |      4       |
    |    3    |      1       |     2      |        3        |        2         |      0       |
    |    4    |      4       |     4      |        14       |        10        |      6       |
    +---------+--------------+------------+-----------------+------------------+--------------+
    Average waiting time: 3.00000
    Average turn-around time: 6.25000

Sample 3:

    Enter the number of processes: 5

    Process 1
    Enter the arrival time of the process 1 :- 2
    Enter the burst time of the process 1 :- 1

    Process 2
    Enter the arrival time of the process 2 :- 1
    Enter the burst time of the process 2 :- 5

    Process 3
    Enter the arrival time of the process 3 :- 4
    Enter the burst time of the process 3 :- 1

    Process 4
    Enter the arrival time of the process 4 :- 0
    Enter the burst time of the process 4 :- 6

    Process 5
    Enter the arrival time of the process 5 :- 2
    Enter the burst time of the process 5 :- 3

    +---------+--------------+------------+-----------------+------------------+--------------+
    | Process | Arrival Time | Burst Time | Completion Time | Turn-around Time | Waiting Time |
    +---------+--------------+------------+-----------------+------------------+--------------+
    |    1    |      2       |     1      |        7        |        5         |      4       |
    |    2    |      1       |     5      |        16       |        15        |      10      |
    |    3    |      4       |     1      |        8        |        4         |      3       |
    |    4    |      0       |     6      |        6        |        6         |      0       |
    |    5    |      2       |     3      |        11       |        9         |      6       |
    +---------+--------------+------------+-----------------+------------------+--------------+
    Average waiting time: 4.60000
    Average turn-around time: 7.80000

'''