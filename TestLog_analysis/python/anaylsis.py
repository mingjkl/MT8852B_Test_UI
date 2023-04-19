

import pandas as pd
import sys

script_path = sys.path[0]
dir_bttc = script_path + "\\bttc_20230410.csv"
dir_orgin = script_path + "\\orgin_20230410.csv"


bttc = pd.read_csv(dir_bttc, encoding='GB2312', header=0, index_col=0)
orgin = pd.read_csv(dir_orgin, encoding='UTF-8', header=0, index_col=0)

# print(bttc.head())
# print(orgin.head())

bttc_pick = pd.DataFrame(columns=bttc.columns)
orgin_pick = pd.DataFrame(columns=bttc.columns)

for i in range(bttc.shape[0]):
    for j in range(orgin.shape[0]):

        if str(bttc.iloc[i,4]) in str(orgin.iloc[j,4]):
            print(bttc.iloc[i,4])
            print(orgin.iloc[j,4])
            print(i)
            print(j)

            bttc_pick = bttc_pick._append(bttc.iloc[i])
            orgin_pick = orgin_pick._append(orgin.iloc[j])
            break

bttc_pick.to_csv(script_path + "\\bttc_pick.csv", encoding='GB2312')
orgin_pick.to_csv(script_path + "\\orgin_pick.csv", encoding='UTF-8')

