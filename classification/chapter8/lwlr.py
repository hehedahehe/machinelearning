#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import classification.chapter8.regression as reg

areas, prices = reg.loadDataSet("./data/ex0.txt")
areas = np.array(areas, dtype=float).reshape(len(areas), 2)
prices = np.array(prices, dtype=float).reshape(len(prices), 1)

areas_valid = areas[:,1]
# 绘制图形
fig = plt.figure()
#ax2
yHat2 = reg.lwlrTest(areas,areas,prices,0.05)
ax2 = fig.add_subplot(411)
ax2.scatter(areas_valid, prices, s=25, alpha=0.4, marker='o')  # 散点图
sortIndex = areas_valid.argsort(0)
ax2.plot(areas_valid[sortIndex], yHat2[sortIndex],c='red')  # 线图
#ax1
yHat1 = reg.lwlrTest(areas,areas,prices,0.1)
ax = fig.add_subplot(412)
ax.scatter(areas_valid, prices, s=25, alpha=0.4, marker='o')  # 散点图
sortIndex = areas_valid.argsort(0)
ax.plot(areas_valid[sortIndex], yHat1[sortIndex],c='red')  # 线图

#ax3
yHat3 = reg.lwlrTest(areas,areas,prices,0.5)
ax3 = fig.add_subplot(413)
ax3.scatter(areas_valid, prices, s=25, alpha=0.4, marker='o')  # 散点图
sortIndex = areas_valid.argsort(0)
ax3.plot(areas_valid[sortIndex], yHat3[sortIndex],c='red')  # 线图

#ax3
yHat4 = reg.lwlrTest(areas,areas,prices,1)
ax3 = fig.add_subplot(414)
ax3.scatter(areas_valid, prices, s=25, alpha=0.4, marker='o')  # 散点图
sortIndex = areas_valid.argsort(0)
ax3.plot(areas_valid[sortIndex], yHat4[sortIndex],c='red')  # 线图



plt.show()