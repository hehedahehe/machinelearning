#coding:utf-8
import matplotlib.pyplot as plt

def simpleDraw(x, y):
    fig = plt.figure()
    ax = fig.subplot(211)
    ax.plot(x,y)