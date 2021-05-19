# -*- coding: utf-8 -*-
import numpy as np
import re
import math

def readfile():
    with open("snow.slope", 'r',encoding='utf-8')as file:
        datas = file.readlines()
    list = []
    strs = ""
    row = 300
    col = 300
    npdata = np.zeros((row, col), dtype=np.int16)
    for data in datas:
        data = data.strip()
        strs = strs + "   " + data
        list.append(strs)
        strs = ""

    for i, sitem in enumerate(list):
        item = str(sitem).strip()
        item = re.findall(r'\d+', item)
        for j, one in enumerate(item):
            npdata[i][j] = int(one)
    return (npdata)

def AddRound(npgrid):
    nx, ny = npgrid.shape[0], npgrid.shape[1]
    zbc=np.zeros((ny+2,nx+2))
    zbc[1:-1,1:-1]=npgrid

    zbc[0,1:-1]=npgrid[0,:]
    zbc[-1,1:-1]=npgrid[-1,:]
    zbc[1:-1,0]=npgrid[:,0]
    zbc[1:-1,-1]=npgrid[:,-1]

    zbc[0,0]=npgrid[0,0]
    zbc[0,-1]=npgrid[0,-1]
    zbc[-1,0]=npgrid[-1,0]
    zbc[-1,-1]=npgrid[-1,0]
    return zbc

def CacSlopAsp(npgrid):
    slope = np.zeros((300, 300), dtype=np.int16)
    for i in range(len(npgrid[1:-1,1:-1])):
        for j in range(len(npgrid[1:-1,1:-1])):
            E = npgrid[i,j] - npgrid[i,j+1]
            W = npgrid[i,j] - npgrid[i,j-1]
            N = npgrid[i,j] - npgrid[i-1,j]
            S = npgrid[i,j] - npgrid[i+1,j]
            SE = (npgrid[i,j] - npgrid[i+1,j+1])/math.sqrt(2)
            SW = (npgrid[i,j] - npgrid[i+1,j-1])/math.sqrt(2)
            NW = (npgrid[i,j] - npgrid[i-1,j-1])/math.sqrt(2)
            NE = (npgrid[i,j] - npgrid[i-1,j+1])/math.sqrt(2)
            if max(E,W,N,S,SE,SW,NW,NE) == E :
                slope[i,j] = 1
            elif max(E,W,N,S,SE,SW,NW,NE) == SE:
                slope[i,j] = 2
            elif max(E, W, N, S, SE, SW, NW, NE) == S:
                slope[i,j] = 4
            elif max(E, W, N, S, SE, SW, NW, NE) == SW:
                slope[i,j] = 8
            elif max(E, W, N, S, SE, SW, NW, NE) == W:
                slope[i,j] = 16
            elif max(E, W, N, S, SE, SW, NW, NE) == NW:
                slope[i,j] = 32
            elif max(E, W, N, S, SE, SW, NW, NE) == N:
                slope[i,j] = 64
            elif max(E, W, N, S, SE, SW, NW, NE) == NE:
                slope[i,j] = 128
    return slope