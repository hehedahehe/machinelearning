#coding:utf-8
import classification.chapter8.regression as reg
import matplotlib.pyplot as plt
import numpy as np
from utils.functiontools import timer

def getW(features,label):
    w = reg.standRegress(features,label)
    return w

def getRSS(yHat,y):
    return reg.rssError(yHat,y)


#测试数据量的大小对于Ein的影响，可以看到
#随着数据量的增大，Ein是逐渐减小的
@timer
def testWithLR():
    #总共4177条数据，以step=1000的数据量进行递增
    features, label = reg.loadDataSet("../data/abalone.txt")
    #测试数据
    f_test = features[-1000:]
    l_test = label[-1000:]

    fig = plt.figure()
    count = features.shape[0]//1000

    for i in range(count):
        if i==count-1:
            f = features[:1000*(i+1)]
            l = label[:1000*(i+1)]
        else:
            continue

        w = getW(f, l)

        yHatout = f_test.dot(w)#使用f_test进行测试
        yHatIn = f.dot(w)
        rssErrorIn = getRSS(yHatIn,l)
        rssErrorout = getRSS(yHatout,l_test)
        print("【数据量大小为"+str(f.shape[0])+"内部误差Ein】===>"+str(rssErrorIn))
        print("【数据量大小为"+str(f.shape[0])+"外部误差Eout】===>"+str(rssErrorout))

        ax1 = fig.add_subplot(211)
        ax1.plot(l[:100,:],c='red',label="实际值")  # 内部测试结果
        ax1.plot(yHatIn[:100,:],label="预测值")  # 预测的结果
        ax1.set_title("rssErrorIn" + str(rssErrorIn))

        legend1 = ax1.legend(loc='upper right', shadow=True, fontsize='x-large')
        #
        # # Put a nicer background color on the legend.
        # legend1.get_frame().set_facecolor('#00FFCC')

        # ax = fig.add_subplot(int(str(count)+"1"+str(i+1)))
        ax = fig.add_subplot(212)
        ax.plot(l_test[:100,:],c='red',label="实际值")#外部测试的结果
        ax.plot(yHatout[:100,:],label="预测值")#预测的结果
        ax.set_title("rssErrorout"+str(rssErrorout))
        ax.legend(loc='upper right', shadow=True, fontsize='x-large')
    # plt.show()


@timer
def testWithRidge(lam,plt,picIndex,picMaxNum):
    #总共4177条数据，以step=1000的数据量进行递增
    features, label = reg.loadDataSet("../data/abalone.txt")
    #测试数据
    f_test = features[-100:]
    l_test = label[-100:]

    f = features[:4000]
    l = label[:4000]
    w = reg.ridgeRegress(f, l, lam)
    yHatout = f_test.dot(w)#使用f_test进行测试
    yHatIn = f.dot(w)
    rssErrorout = getRSS(yHatout,l_test)

    ax = fig.add_subplot(int(str(picMaxNum)+"1"+str(picIndex)))
    ax.plot(l_test[:100,:],c='red',label="实际值")#外部测试的结果
    ax.plot(yHatout[:100,:],label="预测值-lam:"+str(lam))#预测的结果
    ax.set_title("Eout"+str(rssErrorout))
    ax.legend(loc='upper right', shadow=True, fontsize='x-large')

if __name__ == '__main__':
    fig = plt.figure()
    #lam from 0-2, step 0.2
    lams = np.arange(0,0.3,0.05)
    nums = len(lams)
    for index,lam in enumerate(lams):
        index += 1
        testWithRidge(lam,plt,index,nums)
    plt.show()


