import numpy as np
import pandas as pd

def read_input(path):
    f = open(path, "r")
    line_1 = f.readline()
    persons, matrixes = int(line_1.split()[0]), int(line_1.split()[1])
    ls_all = []
    for i in range(persons):
        ls_n = []
        for j in range(matrixes):
            ls_n.append(f.readline().strip('\n'))
        ls_all.append(ls_n)
    bingo_seq = list(map(int, f.readline().split()))
    return persons, matrixes, ls_all, bingo_seq

if __name__ == "__main__":
    path = "./in.txt"
    persons, matrixes, ls_all, bingo_seq = read_input(path)
    
    





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