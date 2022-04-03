import numpy as np
import pandas as pd

import time

date = time.strftime('%Y%m%d')

# ! Read history
# file_name = ("../project-cs-tu-presure-matress/python/history/history-" + date + ".csv")
file_name = ("../project-cs-tu-presure-matress/python/history/history-20220301.csv")
raw_data = pd.read_csv(file_name, header=None)
# print(raw_data)
raw_pressure = raw_data[1]
raw_class = raw_data[2]
index = raw_pressure.index
number_of_rows = len(index)

# Count each class
# print('Total; ' + str(number_of_rows))
# print(raw_data[raw_data[2] == 1].shape[0])
# print(raw_data[raw_data[2] == 2].shape[0])
# print(raw_data[raw_data[2] == 3].shape[0])

# Choose a class with 15 minute
posture_index = 1 # 1-supine
temp = raw_data[raw_data[2] == posture_index].iloc[-2:]
index2 = temp.index
number_of_rows2 = len(index2)

for i in range(number_of_rows2):
    print("\nRow: " + str(i))
    temp2 = temp.iloc[i]
    temp3 = temp2[1]
    a = np.fromstring(temp3[3:-3], dtype=int, sep=' ')

    if posture_index == 1:
        # head
        head_indices = [
            21,22,23,24,25,26,
            37,38,39,40,41,42,
            53,54,55,56,57,58,
            69,70,71,72,73,74
            ]
        head = a[head_indices]
        head_max = np.max(head)
        print("head: " + str(head_max))

        # shoulder_R
        shoulder_R_indices = [ 
            98, 99,100,
            114,115,116,
            130,131,132
            ]
        shoulder_R = a[shoulder_R_indices]
        shoulder_R_max = np.max(shoulder_R)
        print("shoulder_R: " + str(shoulder_R_max))

        # shoulder_L
        shoulder_L_indices = [
            107,108,109,
            123,124,125,
            139,140,141
            ]
        shoulder_L = a[shoulder_L_indices]
        shoulder_L_max = np.max(shoulder_L)
        print("shoulder_L: " + str(shoulder_L_max))

        # elbow_R
        elbow_R_indices = [
            177,178,179,180,181,
            193,194,195,196,197
            ]
        elbow_R = a[elbow_R_indices]
        elbow_R_max = np.max(elbow_R)
        print("elbow_R: " + str(elbow_R_max))

        # elbow_L
        elbow_L_indices = [
            186,187,188,189,190,
            202,203,204,205,206
            ]
        elbow_L = a[elbow_L_indices]
        elbow_L_max = np.max(elbow_L)
        print("elbow_L: " + str(elbow_L_max))

        # center_hip
        center_hip_indices = [
            213,214,215,216,217,218,219,
            229,230,231,232,233,234,235,
            245,246,247,248,249,250,251,
            261,262,263,264,265,266,267
            ]
        center_hip = a[center_hip_indices]
        center_hip_max = np.max(center_hip)
        print("center_hip: " + str(center_hip_max))

        # heel_R
        heel_R_indices = [
            417,418,419,420,421,422,
            433,434,435,436,437,438,
            449,450,451,452,453,454,
            465,466,467,468,469,470
            ]
        heel_R = a[heel_R_indices]
        heel_R_max = np.max(heel_R)
        print("heel_R: " + str(heel_R_max))

        # heel_L
        heel_L_indices = [
            425,426,427,428,429,430,
            441,442,443,444,445,446,
            457,458,459,460,461,462,
            473,474,475,476,477,478
            ]
        heel_L = a[heel_L_indices]
        heel_L_max = np.max(heel_L)
        print("heel_L: " + str(heel_L_max))

    # elif posture_index == 2:
        

    # else:


