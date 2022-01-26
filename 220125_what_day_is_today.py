#!/usr/bin/python3
# -*- coding: utf-8 -*-

def leap_year(year):
    """非4的倍數（1st多），平年。
    （剩下的都是4的倍數）
    非100的倍數（2nd多），闰年，400的倍數，閏年。
    100的倍數，非400的倍數，平年。
    """
    # 資料中，不是4的倍數比較多，所以先判斷這個，大部分的case在這個if就解決了，不用走到elif
    if (year % 4 != 0): # 非4的倍數为平年
        leap = False
    # 剩下的都是4的倍數
    elif (year % 100 != 0) or (year % 400 == 0):
        leap = True
    else:
        leap = False
    return leap

def what_day(year, month, day, yuandan):
    """；若輸入的「日」有誤輸出 -2"""
    if month not in range(1,13): # 若輸入的「月」有誤輸出 -1
        today =  -1
    # print(today, end=" ")

if __name__ == "__main__":
    path = "./in.txt"
    f = open(path,"r")
    line_1 = f.readline()
    year, yuandan = line_1.split()[0], line_1.split()[1]
    leap = leap_year(year)
    count = int(f.readline())
    for i in range(count):
        line = f.readline()
        month, day = line.split()[0], line.split()[1]
        what_day(year, yuandan,month, day)
    f.close()

