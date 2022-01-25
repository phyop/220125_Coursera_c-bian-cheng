#!/usr/bin/python3
# -*- coding: utf-8 -*-

def leap_year(year):
    """閏年規則
公元年分非4的倍數，為平年。
公元年分為4的倍數但非100的倍數，为闰年。
公元年分為100的倍數但非400的倍數，为平年。
公元年分為400的倍數為閏年。"""
    if ...:
        leap = True
    else ...:
        leap  = False
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

