#coding=utf-8

from numpy import *

def loadDataSet(fileName):
    numFeat=len(open(fileName).readline().split('\t'))

    dataMat=[]
    labelMat=[]
    fr=open(fileName)

    for line in fr.readlines():
        lineArr=[]
        curLine=line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat


def standRegres(xArr,yArr):
    xMat=mat(xArr)
    yMat=mat(yArr)
    xTx=xMat.T*xMat
    if linalg.det(xTx)==0.0:
        print "This matrix is singular,cannot do inverse"
        return
    ws=xTx.I*(xMat.T*yMat)
    return ws



####局部加权线性回归
def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat=mat(xArr)
    yMat=mat(yArr).T
    m=shape(xMat)[0]
    weights=mat(eye(m))
    for j in range(m):
        diffMat = testPoint-xMat[j,:]
        #权重值大小以指数级衰减
        weights[j,j]=exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx=xMat.T*(weights*xMat)
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular,cannot do inverse"
        return

    ws=xTx.T*(xMat.T*(weights*yMat))
    return testPoint*ws

def lwlrTest(testArr, xArr, yArr, k=1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat


if __name__=="__main__":
    fileName = "ex0.txt"
    data, label = loadDataSet(fileName)
    print data
    pass




















