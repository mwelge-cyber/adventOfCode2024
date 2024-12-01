

lines = []
def readFile(fname):
    print("Reading file: ", fname)
    f = open(fname, "r")
    for x in f:
        lines.append(x.strip())

    f.close()
    return lines