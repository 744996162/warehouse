#coding=utf-8
from numpy import *

def loadDataSet():
    dataMat=[]
    labelMat=[]
    fr = open("testSet.txt")
    for line in fr.readlines():
        lineArr=line.strip().split()
        #为方便计算，将X0的值设置为1.0
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+exp(-inX))


#梯度上升算法 5.2.2
def gradAscent(dataMatIn,classLabels):
    #转换为NumPy矩阵
    dataMatrix=mat(dataMatIn)
    #transpose()为矩阵转置，转置为列向量
    labelMat=mat(classLabels).transpose()

    m,n=shape(dataMatIn)
    alpha=0.001
    maxCycles=500
    weights=ones((n,1))
    for k in range(maxCycles):
        h=sigmoid(dataMatrix*weights)
        error=(labelMat-h)

        #根据误差的方向调整回归系数
        weights=weights+alpha*dataMatrix.transpose()*error
    return weights


###画图 5.2.3
def plotBestFit(wei):
    import matplotlib.pyplot as plt
    weights=wei.getA()

    dataMat,labelMat=loadDataSet()
    dataArr=array(dataMat)
    n=shape(dataArr)[0]
    xcord1=[]
    ycord1=[]
    xcord2=[]
    ycord2=[]
    for i in range(n):
        if int(labelMat[i])==1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1])
            ycord2.append(dataArr[i,2])
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    x=arange(-3.0,3.0,0.1)
    y=(-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x,y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

###随机梯度上升算法 5.2.4

def stocGradAscent0(dataMatrix,classLabels):
    m,n=shape(dataMatrix)
    alpha=0.01
    weights=ones(n)
    for i in range(m):
        h=sigmoid(sum(dataMatrix[i]*weights))
        error=classLabels[i]-h
        weights=weights+alpha*error*dataMatrix[i]
    return weights


#改进的随机梯度上升算法

def stocGradAscent1(dataMatrix,classLabels,numIter=150):
    m,n=shape(dataMatrix)
    weights=ones(n)
    for j in range(numIter):
        dataIndex=range(m)
        for i in range(m):
            #alpha每次迭代时需要调整
            alpha=4/(1.0+j+i)+0.01

            #随机选取更新
            randIndex=int(random.uniform(0,len(dataIndex)))
            h=sigmoid(sum(dataMatrix[randIndex]*weights))
            error=classLabels[randIndex]=h
            weights=weights+alpha*error*dataMatrix[randIndex]
            del(dataIndex[randIndex])
        return weights

    pass

if __name__=="__main__":
    dataMat, labelMat = loadDataSet()
    # print(dataMat)
    m,n = shape(dataMat)
    wei = gradAscent(dataMat,labelMat)
    print(wei.getA())
    # wei2=stocGradAscent0(array(dataMat),labelMat)
    print(wei)
    # wei2=ones((3,1))
    # wei2=[[1.01702007],[0.85914348],[-0.36579921]]

    # print(wei2.getA())
    plotBestFit(wei)

    pass

