import numpy as np
import pandas as pd
import copy

def read_input(path):
    f = open(path, "r")
    line_1 = f.readline()
    players, matrix_size = int(line_1.split()[0]), int(line_1.split()[1])
    matrix_all = [] 
    matrix_dict = {}
    for i in range(players):
        ls_n = []
        for j in range(matrix_size):
            line2ls = f.readline().strip('\n').split()
            line2int = list(map(int,line2ls))
            ls_n.append(line2int)
        matrix_all.append(ls_n)
    for i in range(players):
        matrix_dict[i] = pd.DataFrame(matrix_all[i])
    bingo_ls = list(map(int, f.readline().split()))
    return players, matrix_size, matrix_dict, bingo_ls

def bingo_condition(matrix_size, bingo_df): # 加起來是matrix_size就代表連線了
    sum_diagonal_1 = 0 # 對角線1
    sum_diagonal_2 = 0 # 對角線2
    for i in range(matrix_size):
        sum_diagonal_1 += bingo_df.iloc[i,i]
        sum_diagonal_2 += bingo_df.iloc[i,matrix_size-i-1]
        if (bingo_df.iloc[i,:].aggregate(np.sum) == matrix_size) \
        or (bingo_df.iloc[:,i].aggregate(np.sum) == matrix_size) \
        or (sum_diagonal_1 == matrix_size) or (sum_diagonal_2 == matrix_size):
            return True

def bingo_game(players, matrix_size, matrix_dict, bingo_ls):
    player_ls = range(players) # 建立玩家list
    df = pd.DataFrame(columns=range(matrix_size), index=range(matrix_size)) # 空賓果盤是用來記錄叫號位置
    condition_plate_ls = [copy.deepcopy(df) for i in range(players)] # 每個玩家都要有1個空盤做記錄
    winner_ls = []
    bingo = False # 發到有人bingo的數字，並且所有人都對過號之後，就可以結束迴圈了
    for i in range(len(bingo_ls)): # 開始一個個叫號
        bingo_num = bingo_ls[i] # 這回中了的話，這就是bingo數字
        # print('bingo_ls[i]',bingo_num)
        # 剩下玩家如果要繼續玩，可以在這行做player_ls的更新
        for n in player_ls: # 剩winner_ls.append(n)下的玩家220 4 5 6
            winner = False # 初始化，會拿到號碼的玩家，就代表還沒有嬴
            # print('player', n)
            condition_df = condition_plate_ls[n]
            data_df = pd.DataFrame(matrix_dict[n])
            coordinate = np.where(data_df[:] == bingo_num) # 在玩家賓果盤找對應坐標
            condition_df.iloc[int(coordinate[0]), int(coordinate[1])] = 1 # 在空賓果盤的該位置設標記1    
            # print('condition_df: ',condition_df) 
            # print('condition_plate_ls: ',condition_plate_ls)
            winner = bingo_condition(matrix_size, condition_df)
            if winner == True: 
                bingo = True # 如果有winner出現，就代表bingo遊戲可以停止發號了
                winner_ls.append(n)
                # print('bingo!')
                # print(condition_df)
        if bingo == True:
            winner_ls.insert(0, bingo_num)
            for n in winner_ls:
                print(n, end=' ') 
            break

if __name__ == "__main__":
    path = "./in.txt"
    players, matrix_size, matrix_dict, bingo_ls = read_input(path)
    bingo_game(players, matrix_size, matrix_dict, bingo_ls)



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

"""
1 0 1 3
1 1 4 5 6 8
28 2 3
33 0
200 2
"""

"""
#include <stdio.h>

int main ()
{
   int n, m;
   int num;
   int w_flag = 0;
   scanf ( "%d%d", &n, &m );

   int board[n][m][m];
   int bingo[n][2][m+1];

   for ( int p = 0; p < n; p++ ) {
      for ( int i = 0; i < m; i++ ) {
         bingo[p][0][i] = bingo[p][1][i] = 0;
         for ( int j = 0; j < m; j++ )
            scanf ( "%d", &board[p][i][j] );
      }
      bingo[p][0][m] = bingo[p][1][m] = 0;
   }

   while ( !w_flag ) {
      // read number
      scanf ( "%d", &num );

      // for each player find number in their board
      for ( int p = 0; p < n; p++ ) {
         int f_flag = 0;
         for ( int i = 0; !f_flag && i < m; i++ )
            for ( int j = 0; !f_flag && j < m; j++ )
               // mark if find
               if ( board[p][i][j] == num ) {
                  f_flag = 1;
                  // row and column
                  bingo[p][0][i]++;
                  bingo[p][1][j]++;
                  // diagnal
                  if ( i == j ) bingo[p][0][m]++;
                  if ( i + j == m-1 ) bingo[p][1][m]++;
                  // win
                  if ( bingo[p][0][i] == m || bingo[p][1][j] == m ||
                       bingo[p][0][m] == m || bingo[p][1][m] == m ) {
                     if ( !w_flag ) {
                        printf ( "%d", num );
                        w_flag = 1;
                     }
                     printf ( " %d", p );
                  }
               }
      }

   }

   return 0;
}
"""