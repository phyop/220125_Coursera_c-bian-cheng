def what_day():
    pass

if __name__ == "__main__":

    path = "./in.txt"

    f = open(path,"r")
    lines = f.readlines()

    year = lines[0].split()[0]
    yuandan = lines[0].split()[1]
    count = lines[1]



    f.close()