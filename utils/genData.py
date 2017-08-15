from utils.functiontools import timer
import random

@timer
def genRandomIntNums(filePath):
    with open(filePath,"w"):
        for i in range(10000000):
            print(random.randint(1, 1000000))

if __name__ == "__main__":
    filePath = ""
