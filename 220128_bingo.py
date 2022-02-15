import numpy as np
import pandas as pd

def read_input(path):
    f = open(path, "r")
    line_1 = f.readline()
    persons, matrix_size = int(line_1.split()[0]), int(line_1.split()[1])
    matrix_all = []
    matrix_dict = {}
    for i in range(persons):
        ls_n = []
        for j in range(matrix_size):
            line2ls = f.readline().strip('\n').split()
            line2int = list(map(int,line2ls))
            ls_n.append(line2int)
        matrix_all.append(ls_n)
    for i in range(persons):
        matrix_dict[i] = pd.DataFrame(matrix_all[i])
    bingo_ls = list(map(int, f.readline().split()))
    return persons, matrix_size, matrix_dict, bingo_ls

def bingo(matrix_df, matrix_size, bingo_seq):
    bingo_df = pd.DataFrame(columns=range(matrix_size), index=range(matrix_size))
    pass
    for i in range(matrix_size):
        matrix_df.iloc[i,:] # row
        matrix_df.iloc[:,i] # column
        matrix_df.iloc[i,i] # diagonal
    
        

if __name__ == "__main__":
    path = "./in.txt"
    persons, matrix_size, matrix_dict, bingo_ls = read_input(path)
       


########################################3

import numpy as np
import pandas as pd

matrix_size = 3
bingo_ls = [1, 2, 4, 8, 6, 3, 9, 5, 7]
matrix_df = pd.DataFrame([[1 ,2 ,3], [4 ,5 ,6], [7 ,8 ,9]])

def bingo_condition(matrix_size, bingo_df, bingo):
    for i in range(matrix_size): # bingo 條件
        sum_diagonal_1 = 0 # 對角線
        sum_diagonal_2 = 0 # 對角線2
        sum_diagonal_1 += bingo_df.iloc[i,i]
        sum_diagonal_2 += bingo_df.iloc[i,matrix_size-i-1]
        if (bingo_df.iloc[i,:].aggregate(np.sum) == 3) \
        or (bingo_df.iloc[:,i].aggregate(np.sum) == 3) \
        or (sum_diagonal_1 == 3) or (sum_diagonal_2 == 3):
            print('bingo!!')
            return True

def bingo_sequence(matrix_size, matrix_df, bingo_ls):
    bingo_df = pd.DataFrame(columns=range(matrix_size), index=range(matrix_size))
    for i in range(len(bingo_ls)): # 一個個叫號 
        coordinate = np.where(matrix_df[:] == bingo_ls[i]) # 找叫號的坐標
        bingo_df.iloc[int(coordinate[0]), int(coordinate[1])] = 1 # 在該位置設1
        bingo = False
        print('bingo_seq:', bingo_ls[i])
        bingo = bingo_condition(matrix_size, bingo_df, bingo)
        if bingo == True:
            print(bingo_df)
            return bingo_ls[i]

bingo_sequence(matrix_size, matrix_df, bingo_ls)





"""
題目敘述
寫一個程式來玩賓果。一個賓果盤面共有 m 欄及 m 列；每個格子中都會有一個 1 至 m * m 間不重複的數字。
遊戲過程中，1 至 m * m 間的數字會隨機被喊到。
若一個玩家在他賓果盤面中任何一欄、一列、一斜對角中的所有數字都被喊過，該玩家就贏了該場遊戲。
現在給定 n 個玩家以及他們的賓果盤面，計算誰贏了遊戲。

輸入格式
第一行包含數字 n 及 m。
接下來 m 行為編號 0 號玩家的賓果盤面，每行皆有 m 組數字。
接下來的 m 行為編號 1 號玩家的賓果盤面，以此類推。
最後一行將會有 m * m 個數字，代表賓果遊戲進行中數字被喊到的順序。

輸出格式
輸出哪個喊到的數字讓玩家獲勝，並輸出獲勝的玩家編號。
若有多名玩家同時獲勝，從小至大輸出所有獲勝玩家的編號。

輸入限制
n 是一個正整數且不大於 10。
m 是一個正整數且不大於 256。

輸入範例
2 3
1 2 3
4 5 6
7 8 9
1 2 3
4 5 6
7 8 9
1 2 4 8 6 3 9 5 7

輸出範例
3 0 1
"""