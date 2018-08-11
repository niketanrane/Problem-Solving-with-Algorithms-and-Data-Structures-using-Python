__author__ = "niketan"

'''
Problem Description : 
On any average day about 10 students are working in the lab at any given hour. 
These students typically print up to twice during that time, and the length of 
these tasks ranges from 1 to 20 pages. The printer in the lab is older, capable 
of processing 10 pages per minute of draft quality. The printer could be switched 
to give better quality, but then it would produce only five pages per minute. The 
slower printing speed could make students wait too long. What page rate should be used?
Link : https://runestone.academy/runestone/static/pythonds/BasicDS/SimulationPrintingTasks.html
'''

import random

class Queue:


    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        return self.items.pop()

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def busy(self):
        '''
        To check if there is a task running in a printer
        :return:
        '''
        return not (self.currentTask == None)

    def tick(self):
        '''
        What the printer will do each second, f it has a job then it will decrement
        the current job by how much it can process in one sec.
        :return: None
        '''
        if self.currentTask is not None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def startNext(self, newTask):
        '''
        This will take the next waiting task and set it to the printer's current task
        :param newTask:
        :return: None
        '''
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60 / self.pagerate

class Task:
    '''
    A task will note down the current time to check  how muc time it was waiting after it was added to the queue, pages we are generating by random ( page limit is 20 pages)
    '''
    def __init__(self, time):
        self.timeStamp = time
        self.pages = random.randrange(1, 21)

    def getPages(self):
        return self.pages

    def getStamp(self):
        return self.timeStamp

    def getWaitTime(self, currentTime):
        return currentTime - self.timeStamp

def simulation(numSeconds, pagesPerMinute):
    '''
    :param numSeconds: Gor how many seconds you need to run the simulation
    :param pagesPerMinute: How many pager a printer can run in a minute
    :return: Average wait time a task has for all tasks
    '''
    printer = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingTimes = []
    for currentSecond in range(numSeconds):
        '''
        Generate a new random task (real simulation so we check every time if a task has been created or not
        '''
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if not printer.busy() and not printQueue.isEmpty():
            currentTask = printQueue.dequeue()
            printer.startNext(currentTask)
            waitingTimes.append(currentTask.getWaitTime(currentSecond))

        # Every second run printer and decrement the job accordingly.
        printer.tick()

    averageWaitTime = sum(waitingTimes) / len(waitingTimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWaitTime, printQueue.size()))
    return averageWaitTime

def newPrintTask():
    return random.randrange(1, 181) == 180

#print(simulation(3600, 5))
for i in range(20):
    simulation(3600, 10)

