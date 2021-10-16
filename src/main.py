import time
from datetime import timedelta
import os
import subprocess
import matplotlib.pyplot as plt


class Timer:
    def __init__(self):
        self.diff = 0
    
    def start(self):
        self.start_time = time.monotonic()
    
    def stop(self):
        self.end_time = time.monotonic()
    
    def get_diff(self):
        self.diff = timedelta(seconds=self.end_time - self.start_time)
        return self.diff.total_seconds()

    def reset(self):
        self.diff = 0
        self.start_time = 0
        self.end_time = 0



def executor(binaryName, n):
    dirPath = os.path.dirname(os.path.realpath(__file__))
    argPath = dirPath + "\\" + binaryName
    args = (argPath, str(n))
    # excecute the binary
    subprocess.run(args)

def start():
    # print("Starting...")
    timer = Timer()
# --------------------Linear
    inputSize = []
    timeForExec = []

    starti = 1
    endi = 100000000
    stepi = 700000
    for i in range(starti, endi, stepi):
        timer.start()
        executor("linear.exe", i)
        timer.stop()
        timeForExec.append(timer.get_diff())
        inputSize.append(i)
        timer.reset()
        if(i % (endi/50 ) < 100):
            print("progress:", str(round((i/endi)*100, 1)) + "%")
    

    plt.scatter(inputSize, timeForExec, marker='.')
    plt.show()
#   ------------------Quadratic
    inputSize = []
    timeForExec = []

    starti = 1
    endi = 10000
    stepi = 100
    for i in range(starti, endi, stepi):
        timer.start()
        executor("quadratic.exe", i)
        timer.stop()
        timeForExec.append(timer.get_diff())
        inputSize.append(i)
        timer.reset()
        if(i % (endi/50 ) < 100):
            print("progress:", str(round((i/endi)*100, 1)) + "%")
    

    plt.scatter(inputSize, timeForExec, marker='.')
    plt.show()


    print("Done.")


if __name__ == '__main__':
    start()