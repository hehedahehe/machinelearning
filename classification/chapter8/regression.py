#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
#1. 加载数据，返回特征矩阵和标签矩阵
#数据第一列为初始化参数设置为x0=1，
#最终得到的回归系数为w
#训练结果为：
# y = w[0]*x0 + w[1]x1
def loadDataSet(fileName):
    dataMat = []
    labelMat = []
    with open(fileName, "r") as dataSet:
        for line in dataSet:
            temp = line.split("\t")
            feature = []
            feature.append(1)
            feature.extend(temp[:-1])
            dataMat.append(feature)
            labelMat.append(temp[-1])
    features = np.array(dataMat, dtype=float)
    labels = np.array(labelMat, dtype=float).reshape((len(labelMat), 1))
    return features, labels

#2.计算w
def standRegress(xArr, yArr):
    xT = xArr.T
    xTx = xT.dot(xArr)
    if(np.linalg.det(xTx) == 0.0001):
        raise Exception("矩阵不可逆")
    w = np.linalg.inv(xTx).dot(xT.dot(yArr))
    return w

#3. 岭回归
def ridgeRegress(xArr, yArr, lam=0.3):
    xT = xArr.T
    xTx = xT.dot(xArr)
    denom = xTx + np.eye(xTx.shape[0])*lam
    if (np.linalg.det(xTx) == 0.0001):
        raise Exception("矩阵不可逆")
    w = np.linalg.inv(denom).dot(xT.dot(yArr))
    return w


def rssError(yHat, yArray):
    return np.sum((yHat-yArray)**2)

if __name__ == "__main__":
    fileName = "./data/ex0.txt"
    features, labels = loadDataSet(fileName=fileName)
    pass




