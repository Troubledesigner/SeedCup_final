#coding=utf-8
import numpy as np
import GetData
from sklearn import preprocessing
import matplotlib
from sklearn.cross_validation import  train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import roc_auc_score
from keras.models import Sequential
from keras.layers import Dense, Activation
import GetTeamData

data_X = GetData.getData()
data_y = GetData.getTarget()

TrainTime = 300
model = LinearRegression()
model.fit(data_X, data_y)


file = open("./matchDataTestGet.csv")
fileToWrite = open("./output.csv", "w")
line = file.readline()
dataList = []
teamDataList = GetTeamData.TeamData()
scoreList = []
allDataList = []
while line:
    list = line.split(",")
    team = GetData.getTeam(int(list[0]), teamDataList)
    scoreList.append(team.all_importance)
    scoreList.append(team.shootAb)
    scoreList.append(team.threeShootAb)
    scoreList.append(team.bbAb)
    scoreList.append(team.penaltyAb)
    scoreList.append(team.attackAb)
    scoreList.append(team.defendAb)
    scoreList.append(team.sideEffectAb)
    scoreList.append(team.scoreAb)

    scoreList.append(team.hitRate)
    scoreList.append(team.hitTime)
    scoreList.append(team.shootTime)
    scoreList.append(team.threeHitRate)
    scoreList.append(team.threeHitTime)
    scoreList.append(team.threeShootTime)
    scoreList.append(team.penaltyRate)
    scoreList.append(team.penaltyHitTime)
    scoreList.append(team.penaltyTime)
    scoreList.append(team.backboard)
    scoreList.append(team.forwardBB)
    scoreList.append(team.backBB)
    scoreList.append(team.support)
    scoreList.append(team.steal)
    scoreList.append(team.block)
    scoreList.append(team.lose)
    scoreList.append(team.charge)

    team = GetData.getTeam(int(list[1]), teamDataList)
    scoreList.append(team.all_importance)
    scoreList.append(team.shootAb)
    scoreList.append(team.threeShootAb)
    scoreList.append(team.bbAb)
    scoreList.append(team.penaltyAb)
    scoreList.append(team.attackAb)
    scoreList.append(team.defendAb)
    scoreList.append(team.sideEffectAb)
    scoreList.append(team.scoreAb)

    scoreList.append(team.hitRate)
    scoreList.append(team.hitTime)
    scoreList.append(team.shootTime)
    scoreList.append(team.threeHitRate)
    scoreList.append(team.threeHitTime)
    scoreList.append(team.threeShootTime)
    scoreList.append(team.penaltyRate)
    scoreList.append(team.penaltyHitTime)
    scoreList.append(team.penaltyTime)
    scoreList.append(team.backboard)
    scoreList.append(team.forwardBB)
    scoreList.append(team.backBB)
    scoreList.append(team.support)
    scoreList.append(team.steal)
    scoreList.append(team.block)
    scoreList.append(team.lose)
    scoreList.append(team.charge)

    for i in range(2, 6):
        dataList.append(int(list[i]))
    dataList = dataList + scoreList
    allDataList.append(dataList)
    scoreList = []
    dataList = []
    line = file.readline()

data_Test = np.array(allDataList)
data_y_Test = model.predict(data_Test)
for i in data_y_Test:
    fileToWrite.write(str(i) + "\r\n")
file.close()
fileToWrite.close()