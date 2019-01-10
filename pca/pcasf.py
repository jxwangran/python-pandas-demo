import numpy as np

arr = np.array(np.arange(10)).reshape(2,5)
print(arr)
print(arr[:,0])
print(arr[0][1])
print(arr[:][1])

def loadData():
    file = open('secom.data')
    stringArr = [line.strip().split(' ') for line in file.readlines()]
    datArr = [list(map(float,line)) for line in stringArr]
    file.close()
    return np.mat(datArr)


def replaceNanWithMean():
    data = loadData()
    numFeat = np.shape(data)[1]
    for i in range(numFeat):
        meanVal = np.mean(data[np.nonzero(~np.isnan(data[:,i].A))[0],i])
        data[np.nonzero(np.isnan(data[:,i].A))[0],i] = meanVal
    return data


def pca(dataMat, topNfeat=99999):
    meanVals = np.mean(dataMat, axis=0)
    print(dataMat.shape)
    print(meanVals.shape)
    #去平均值
    meanRemoved = dataMat - meanVals
    #计算协方差
    covMat = np.cov(meanRemoved, rowvar=0)
    print(covMat.shape)
    # 第一个是特征值，第二个是特征向量
    eigVals, eigVects = np.linalg.eig(np.mat(covMat))
    print(eigVals.shape)
    #print(eigVals)
    eigValInd = np.argsort(eigVals)
    print(eigValInd.shape)
    print(eigValInd[:-10:-1])
    eigValInd = eigValInd[:-(topNfeat + 1) : -1]
    print(eigValInd[0:10])
    redEigVects = eigVects[:,eigValInd]
    lowDDataMat = meanRemoved * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat






data = replaceNanWithMean()
numFeat = np.shape(data)[1]
print(data.shape)
lowDDataMat, reconMat = pca(data)
print(lowDDataMat.shape)
print(reconMat.shape)
listA = []
for i in range(numFeat):
    listA.append(np.var(lowDDataMat[:, i]))

listASum = np.sum(np.array(listA))
varList = []
for i in range(numFeat):
    varList.append(round(listA[i]/listASum, 4))

print(listA)
np.argsort(np.array(listA))
print(varList)
#print(data[:,1])
#print(data[np.nonzero(data[0:1].A)])
#print(np.nonzero(~np.isnan(data[:,1].A)))
#print(data[np.nonzero(~np.isnan(data[:,1].A))[0],1])
#print(replaceNanWithMean()[0:5])









