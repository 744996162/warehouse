#!/usr/bin/env python
#coding=utf-8
from numpy import *
import operator
from os import listdir
import matplotlib
import matplotlib.pyplot as plt


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

#knn算法实现
def classify(inX, dataSet, labels, k):
    '''
    inX为待分类样本
    dataSet为样本集(属性值)
    labels为标签向量(类别)
    k为最近邻数目k
    '''
    dataSetSize = dataSet.shape[0]
    #带分类值与矩阵的每条记录相减，得到差
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    #计算差的平方
    sqDiffMat = diffMat**2
    #计算平方和并开根，得到距离
    #axis=1表明每一行的总和，axis=0为每一列的总和
    distance = sqDiffMat.sum(axis=1)**0.5
    #argsort为对数组进行升序排列
    sortedDistIndicies = distance.argsort()
    classCount = {}
    for i in range(k):
        labelName=labels[sortedDistIndicies[i]]
        classCount[labelName]=classCount.get(labelName, 0)+1
    sortedClassCount=sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


    # return distance
    # sortedDistIndicies=distance.argsort()

#将读取文本文件数据到矩阵
def file2matrix(filename,parammterNumber):
    fr=open(filename)
    lines=fr.readlines()
    #获取数据数量(行数)
    lineNums=len(lines)
    #创建返回的矩阵
    returnMat=zeros((lineNums,parammterNumber))
    classLabelVector=[]
    for i in range(lineNums):
        #strip去掉空白字符
        line=lines[i].strip()
        itemMat=line.split('\t')
        returnMat[i,:]=itemMat[0:parammterNumber]
        classLabelVector.append(itemMat[-1])
    fr.close()
    return returnMat,classLabelVector


#数据归一化

def autoNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    normMat=zeros(shape(dataSet))
    size=normMat.shape[0]
    normMat=dataSet-tile(minVals,(size,1))
    normMat=normMat/tile(ranges,(size,1))
    return normMat,minVals,ranges


    pass


def test_file2matrix():
    filename="datingTestSet2.txt"
    parammterNumber=3
    returnMat,returnLabel=file2matrix(filename,parammterNumber)
    # print returnMat
    # print returnLabel


    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(returnMat[:,1],returnMat[:,2])
    plt.show()
    pass

if __name__ == '__main__':
    # group,labels=createDataSet()
    # print(group)
    a=array([3, 3])
    b=array([[2,2],[1,1]])
    # t=classify(a,b,"","")
    # print t

    test_file2matrix()


