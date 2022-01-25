#!/usr/bin/python3
# -*- coding: utf-8 -*-

def what_day(year, month, day, yuandan):
    pass
    # print(today, end=" ")

def open_today(path):
    f = open(path,"r")
    line_1 = f.readline()
    year, yuandan = line_1.split()[0], line_1.split()[1]
    count = int(f.readline())
    for i in range(count):
        line = f.readline()
        month, day = line.split()[0], line.split()[1]
        what_day(year, yuandan,month, day)
    f.close()

if __name__ == "__main__":
    path = "./in.txt"
    open_today(path)
