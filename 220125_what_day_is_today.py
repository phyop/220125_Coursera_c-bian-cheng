#!/usr/bin/python3
# -*- coding: utf-8 -*-

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

def date(year, month):
    """# 若輸入的「月」有誤輸出 -1；若輸入的「日」有誤輸出 -2"""
    month_ls = [i for i in range(1,13)]
    day_ls = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year):
        day_ls[1] = 29
    date_dict = dict(zip(month_ls, day_ls))
    return date_dict

def what_day(year, month, day, whatday_yuandan, date_dict):
    """到4/6所增加的天數d = (date_dict.month[1]+...date_dict.month[4-1])+(6-1)
    假設1/1是禮拜6，而4/6是增加n周又5天(周四)：((d%7+6))%7=(5+6)%7=4,
    假設1/1是禮拜0(周日)，而4/6是增加n周又6天(周六)：((d%7+0))%7=(6+0)%7=6,
    假設1/1是禮拜whatday_yuandan，而month/day是：((d%7+whatday_yuandan))%7"""
    
    # print(today, end=" ")

if __name__ == "__main__":
    path = "./in.txt"
    f = open(path,"r")
    line_1 = f.readline()
    year, whatday_yuandan = line_1.split()[0], line_1.split()[1]
    leap = leap_year(year)
    count = int(f.readline())
    for i in range(count):
        line = f.readline()
        month, day = line.split()[0], line.split()[1]
        what_day(year, whatday_yuandan,month, day)
    f.close()

