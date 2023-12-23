import csv
import numpy as np
from scipy.spatial import distance
from ortoolpy import tsp

# 新千歳空港の経度と緯度を指定
NewChitose_Airport = [141.6884719, 42.78066411]

# 新千歳空港を開始地点に指定
start_point = NewChitose_Airport
nodes = [start_point]

with open('tsp_data.csv', encoding="Shift-JIS") as f:
    reader = csv.reader(f)
    header = next(f)
    
    for row in reader:
        nodes.append([ row[2], row[1] ])# Bの2列目から開始

# データを浮動小数点数に変換する
nodes = np.array(nodes).astype(float)
dist = distance.cdist(nodes, nodes)

# 巡回セールスマン問題を計算
print(tsp(nodes, dist))
