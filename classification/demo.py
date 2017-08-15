#coding:utf-8

#所有操作都基于是列向量
import numpy as np
if __name__ == "__main__":
    features = [[1,2,3,4],[5,6,7,8],[14,11,17,13],[20,4,3,8]]
    labels = [1,0,1]
    fMat = np.array(features)
    fmatT = fMat.T
    # m = np.dot(fMat,fmatT)#求两个矩阵的内积、
    m = fmatT.dot(fMat)
    mv = np.linalg.inv(m)
    print("m.dot(mv)")
    print(m.dot(mv))
    print(np.linalg.det(m.dot(mv)))
    pass