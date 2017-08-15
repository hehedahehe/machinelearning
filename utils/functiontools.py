#coding:utf-8
import time

def timer(func):
    def wrapper(*args,**kwargs):
        startTime = time.time()
        func(*args,**kwargs)
        endTime = time.time()
        print(func.__name__ + "耗时==>"+str(endTime-startTime))
    return wrapper