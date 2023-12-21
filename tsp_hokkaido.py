import csv
import numpy as np
from scipy.spatial import distance
from ortoolpy import tsp

NewChitose_Airport = [141.6811815, 42.7876057]

# 開始地点を新千歳空港に指定
start_point = NewChitose_Airport
nodes = [start_point]

with open('tsp_Hokkaido.csv') as f:
    reader = csv.reader(f)
    header = next(f)
    for row in reader:
        nodes.append([ row[2], row[1] ])

dist = distance.cdist(nodes, nodes)
print(tsp(nodes, dist))
