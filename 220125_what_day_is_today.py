#!/usr/bin/python3
# -*- coding: utf-8 -*-

def read_input(path):
    f = open(path,"r")
    line_1 = f.readline()
    year, whatday_yuandan = line_1.split()[0], line_1.split()[1]
    count = int(f.readline())
    month_ls = []
    day_ls = []
    for i in range(count):
        line = f.readline()
        month, day = line.split()[0], line.split()[1]
        month_ls.append(month)
        day_ls.append(day)
    date_dict = dict(zip(month_ls, day_ls))
    f.close()
    return (year, date_dict, whatday_yuandan)

def leap_year(year):
    """非4的倍數（1st多），平年。
    （下面都是對4的倍數值做討論）
    非100的倍數（2nd多），闰年，400的倍數，閏年。
    100的倍數，非400的倍數，平年。"""
    # 資料中，不是4的倍數比較多，所以先判斷這個，大部分的case在這個if就解決了，不用走到elif
    if (year % 4 != 0): # 非4的倍數为平年
        leap = False
    # 剩下的都是4的倍數
    elif (year % 100 != 0) or (year % 400 == 0):
        leap = True
    else:
        leap = False
    return leap

def date_0to12(year, month):
    """# 若輸入的「月」有誤輸出 -1；若輸入的「日」有誤輸出 -2"""
    month_ls = [i for i in range(0,13)] # 包含0月
    day_ls = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 0月爲0天
    if leap_year(year):
        day_ls[1] = 29
    date_dict = dict(zip(month_ls, day_ls))
    return date_dict

def what_day(year, month, day, whatday_yuandan, date_dict):
    """到4/6所增加的天數d = (date_dict.month[1]+...date_dict.month[4-1])+(6-1)
    假設1/1是禮拜6，而4/6是增加n周又5天(周四)：((d%7+6))%7=(5+6)%7=4,
    假設1/1是禮拜0(周日)，而4/6是增加n周又6天(周六)：((d%7+0))%7=(6+0)%7=6,
    假設1/1是禮拜whatday_yuandan，而month/day是：((d%7+whatday_yuandan))%7"""
    d = day-1
    for i in range(1, month):
        d += date_dict.month[i]
    whatday = ((d%7+whatday_yuandan))%7
    return what_day

if __name__ == "__main__":
    path = "./in.txt"
    year, test_date_dict, whatday_yuandan = read_input(path)
    leap = leap_year(year)

    
    date_0to12(year, month)
    # print(whatday, end=" ")

#############################################################333
"""
題目敘述
寫一個程式計算給定日期為星期幾。輸入會先告訴程式某年的 1 月 1 號為星期幾，
例如範例中 2012 年的 1 月 1 號為星期日。
接著程式會收到一些日期，並要計算出給定日期為星期幾，
例如範例中程式將會收到 11 月 13 號，並計算出該日期為星期二。

輸入格式
第一行包含一個西元年以及該年的一月一日為星期幾，如範例中 2012 0。
注意，0 代表星期日，1 代表星期一，以此類推。
第二行會告訴程式接下來將有 n 組日期需要計算。n 的範圍為 1 至 10。
接下來的 n 行，每一行將會有一組需要計算的日期(月、日)，如範例中的 11 月 13 號。

輸出格式
共會輸出 n 個數字。我們用 0 代表星期日，1 代表星期一，以此類推。
若輸入的「月」有誤請輸出 -1；若輸入的 「月」無誤但「日」有誤請輸出 -2。(數字間留一個空白)

輸入範例
2012 0
5
11 13
11 14
11 15
13 1
1 200

輸出範例
(請務必依照範例格式填寫，數字間留一個空白，否則系統將會判定答案錯誤)
2 3 4 -1 -2
"""