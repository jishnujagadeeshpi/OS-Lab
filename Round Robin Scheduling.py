
'''
    Write a program to implement Round Robin Scheduling with arrival time (quantum 2 ns).
'''

from prettytable import PrettyTable

time = 0
processes = []
ID = 0
quantum =2

table = PrettyTable()
table.field_names = ["Process" , "Arrival Time" , "Burst Time" , "Completion Time" , "Turn-around Time" , "Waiting Time"   ]

class Process:
    def __init__(self,id,arrival,burst):
        self.id = id
        self.ArrivalTime = arrival
        self.BurstTime = burst
        self.RemainingTime = burst
        self.CompletionTime = int()
        self.TurnAroundTime = int()
        self.WaitingTime = int()

    def updateRemainingTime(self,quantum):
        self.RemainingTime -= quantum
        if self.RemainingTime < 0:
            self.RemainingTime = 0

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
    processes.sort(key=(lambda x:[x.ArrivalTime, x.BurstTime]))


def sortProcessesOnId():
    global processes
    processes.sort(key=lambda x: x.id)

def executeProcesses(quantum):
    global processes, time
    completedProcesses = []
    waitingProcesses = [processes[0]]
    
    while len(waitingProcesses) > 0:
        curProcess = waitingProcesses[0]
        if curProcess in processes:
            processes.remove(curProcess)

        if time < curProcess.ArrivalTime:
            time = curProcess.ArrivalTime
        time += (quantum if curProcess.RemainingTime >= quantum else curProcess.RemainingTime)
        curProcess.updateRemainingTime(quantum)

        waitingProcesses = waitingProcesses + [process for process in processes if process.ArrivalTime <= time and process not in waitingProcesses]
        if curProcess.RemainingTime == 0:
            curProcess.SetCompletionTime(time)
            curProcess.SetTurnAroundTime()
            curProcess.SetWaitingTime()
            completedProcesses += [curProcess]
            waitingProcesses.remove(curProcess)
        else:
            waitingProcesses.append(curProcess)
            waitingProcesses.remove(curProcess)

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
    executeProcesses(2)
    sortProcessesOnId()
    print_table()


main()


'''
Sample 1:

    Enter the number of processes: 4

    Process 1
    Enter the arrival time of the process 1 :- 0
    Enter the burst time of the process 1 :- 5

    Process 2
    Enter the arrival time of the process 2 :- 1
    Enter the burst time of the process 2 :- 4

    Process 3
    Enter the arrival time of the process 3 :- 2
    Enter the burst time of the process 3 :- 2

    Process 4
    Enter the arrival time of the process 4 :- 4
    Enter the burst time of the process 4 :- 1

    +---------+--------------+------------+-----------------+------------------+--------------+
    | Process | Arrival Time | Burst Time | Completion Time | Turn-around Time | Waiting Time |
    +---------+--------------+------------+-----------------+------------------+--------------+
    |    1    |      0       |     5      |        12       |        12        |      7       |
    |    2    |      1       |     4      |        11       |        10        |      6       |
    |    3    |      2       |     2      |        6        |        4         |      2       |
    |    4    |      4       |     1      |        9        |        5         |      4       |
    +---------+--------------+------------+-----------------+------------------+--------------+
    Average waiting time: 4.75000
    Average turn-around time: 7.75000

Sample 2:

    Enter the number of processes: 6

    Process 1
    Enter the arrival time of the process 1 :- 0
    Enter the burst time of the process 1 :- 4

    Process 2
    Enter the arrival time of the process 2 :- 1
    Enter the burst time of the process 2 :- 5

    Process 3
    Enter the arrival time of the process 3 :- 2
    Enter the burst time of the process 3 :- 2

    Process 4
    Enter the arrival time of the process 4 :- 3
    Enter the burst time of the process 4 :- 1

    Process 5
    Enter the arrival time of the process 5 :- 4
    Enter the burst time of the process 5 :- 6

    Process 6
    Enter the arrival time of the process 6 :- 6
    Enter the burst time of the process 6 :- 3

    +---------+--------------+------------+-----------------+------------------+--------------+
    | Process | Arrival Time | Burst Time | Completion Time | Turn-around Time | Waiting Time |
    +---------+--------------+------------+-----------------+------------------+--------------+
    |    1    |      0       |     4      |        8        |        8         |      4       |
    |    2    |      1       |     5      |        18       |        17        |      12      |
    |    3    |      2       |     2      |        6        |        4         |      2       |
    |    4    |      3       |     1      |        9        |        6         |      5       |
    |    5    |      4       |     6      |        21       |        17        |      11      |
    |    6    |      6       |     3      |        19       |        13        |      10      |
    +---------+--------------+------------+-----------------+------------------+--------------+
    Average waiting time: 7.33333
    Average turn-around time: 10.83333

'''