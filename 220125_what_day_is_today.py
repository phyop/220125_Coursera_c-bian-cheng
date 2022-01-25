def what_day(year, month, day, yuandan):
    pass

if __name__ == "__main__":
    path = "./in.txt"
    f = open(path,"r")
    line_1 = f.readline()
    year, yuandan = line_1[0].split()[0], line_1[0].split()[1]
    count = f.readline()
    for i in range(count):
        line = f.readline()
        month, day = line.split()[0], line[0].split()[1]
        # what_day(year, month, day, yuandan)
        print("year, month, day, yuandan = ", year, month, day, yuandan)
    f.close()    
